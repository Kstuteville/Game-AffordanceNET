# -------------------------------
# Day 1 – Load & Normalize (Chair 331)
# -------------------------------
# Loads point cloud and labels for a PartNet chair,
# reorients from Y-up to Z-up, normalizes to unit sphere,
# and saves outputs to disk for downstream use.
# -------------------------------

import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

# config
base_dir = "/Volumes/T7/data_v0/331/point_sample"
points_file = os.path.join(base_dir, "sample-points-all-pts-nor-rgba-10000.txt")
labels_file = os.path.join(base_dir, "sample-points-all-label-10000.txt")

# load
pointdata = np.loadtxt(points_file)
points = pointdata[:, :3]
normals = pointdata[:, 3:6]
labels = np.loadtxt(labels_file, dtype=int)

# reorient: Y-up → Z-up
points = points[:, [0, 2, 1]]
points[:, 2] *= -1
normals = normals[:, [0, 2, 1]]
normals[:, 2] *= -1

# normalize
centroid = points.mean(axis=0)
points -= centroid
scale = np.max(np.linalg.norm(points, axis=1))
points /= scale

# Save
os.makedirs("processed_outputs", exist_ok=True)
np.save("processed_outputs/chair331_norm.npy", {
    "points": points,
    "normals": normals,
    "labels": labels,
    "scale": scale,
    "centroid": centroid
})

# Preview (Matplotlib)
sample = np.random.choice(len(points), 3000, replace=False)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(points[sample, 0], points[sample, 1], points[sample, 2],
           c=labels[sample], cmap="tab10", s=5, alpha=0.8)
# --- Universal axis fixing for 3D objects of ANY shape ---
x_limits = [points[:,0].min(), points[:,0].max()]
y_limits = [points[:,1].min(), points[:,1].max()]
z_limits = [points[:,2].min(), points[:,2].max()]

x_range = x_limits[1] - x_limits[0]
y_range = y_limits[1] - y_limits[0]
z_range = z_limits[1] - z_limits[0]

max_range = max(x_range, y_range, z_range) / 2.0

mid_x = np.mean(x_limits)
mid_y = np.mean(y_limits)
mid_z = np.mean(z_limits)

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.set_proj_type('ortho')  # ensures no perspective distortion

ax.set_title("Chair 331 - Normalized (Z-up)")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, 1])
plt.tight_layout(); plt.show()

# Preview (Open3D)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(normals * 0.5 + 0.5)
o3d.visualization.draw_geometries([pcd], window_name="Chair 335 - Point Cloud")
