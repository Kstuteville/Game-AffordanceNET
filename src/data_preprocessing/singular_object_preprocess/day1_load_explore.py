"""
Day 1 — Load + Normalize a PartNet figure (Chair ID: 331) but you
can you for any object
#try 42
#try 49513

- Load raw point samples + normals + labels
- Convert PartNet's Y-up coordinates to Z-up
- Normalize object to a unit sphere
- Save a clean .npy bundle for training
- Preview point cloud for sanity checking
"""

import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt



# Paths to data
DATA_ROOT = "/Volumes/T7/data_v0/49513/point_sample"
points_path = os.path.join(DATA_ROOT, "sample-points-all-pts-nor-rgba-10000.txt")
labels_path = os.path.join(DATA_ROOT, "sample-points-all-label-10000.txt")

OUT_DIR = "processed_outputs"
os.makedirs(OUT_DIR, exist_ok=True)



# Load point cloud + labels
print("Loading PartNet chair...")
raw = np.loadtxt(points_path)

points = raw[:, :3]
normals = raw[:, 3:6]
labels = np.loadtxt(labels_path, dtype=int)

print(f"Loaded {len(points)} points.")


# Reorient from Y-up → Z-up
# PartNet uses Y as "up"; games/ML pipelines prefer Z-up.
def y_up_to_z_up(arr):
    out = arr[:, [0, 2, 1]].copy()
    out[:, 2] *= -1
    return out

points = y_up_to_z_up(points)
normals = y_up_to_z_up(normals)


# Normalize into unit sphere
centroid = points.mean(axis=0)
points -= centroid

max_dist = np.max(np.linalg.norm(points, axis=1))
points /= max_dist

print("Normalized to unit sphere.")



# Save preprocessed object
save_path = os.path.join(OUT_DIR, "chair331_norm.npy")

np.save(save_path, {
    "points": points,
    "normals": normals,
    "labels": labels,
    "centroid": centroid,
    "scale": max_dist
})

print(f"Saved preprocessed chair to {save_path}")



# Matplotlib preview (QC)
sample_idx = np.random.choice(len(points), 3000, replace=False)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    points[sample_idx, 0],
    points[sample_idx, 1],
    points[sample_idx, 2],
    c=labels[sample_idx],
    cmap="tab10",
    s=5, alpha=0.85
)

#Force axes to same scale
mins = points.min(axis=0)
maxs = points.max(axis=0)
ranges = maxs - mins
half = np.max(ranges) / 2
mid = (maxs + mins) / 2

ax.set_xlim(mid[0] - half, mid[0] + half)
ax.set_ylim(mid[1] - half, mid[1] + half)
ax.set_zlim(mid[2] - half, mid[2] + half)

ax.set_proj_type("ortho")
ax.set_title("Chair 331 — Normalized (Z-up)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.tight_layout()
plt.show()


# Open3D preview (nicer vis)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(normals * 0.5 + 0.5)

o3d.visualization.draw_geometries(
    [pcd],
    window_name="Chair 331 — Point Cloud"
)
