"""
Day 2 — Recompute Surface Normals (Chair 331)

Loads the normalized point cloud from Day 1,
recomputes surface normals using local neighborhoods
for smoother, more consistent geometry, and saves
the updated dataset.
"""

import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt


# Load preprocessed Day 1 object

INPUT_PATH = "processed_outputs/chair331_norm.npy"
data = np.load(INPUT_PATH, allow_pickle=True).item()

points = data["points"]
labels = data["labels"]
centroid = data["centroid"]
scale = data["scale"]

print(f"Loaded normalized chair from {INPUT_PATH}")


# Build Open3D point cloud

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)



# Recompute surface normals
print("Recomputing normals.")

pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=0.08,     # neighborhood search radius in normalized space
        max_nn=30        # max number of neighbors to consider
    )
)

pcd.normalize_normals()



# Preview normals (Open3D)

o3d.visualization.draw_geometries(
    [pcd],
    window_name="Chair 331 — Recomputed Normals"
)



# Preview point cloud (Matplotlib)

sample = np.random.choice(len(points), 2000, replace=False)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    points[sample, 0],
    points[sample, 1],
    points[sample, 2],
    c=labels[sample],
    cmap="tab10",
    s=3,
    alpha=0.8
)

ax.set_title("Chair 331 — Recomputed Normals")
ax.set_box_aspect([1, 1, 1])
plt.tight_layout()
plt.show()



# Save updated dataset
OUT_PATH = "processed_outputs/chair331_clean.npy"
os.makedirs("processed_outputs", exist_ok=True)

np.save(OUT_PATH, {
    "points": np.asarray(pcd.points),
    "normals": np.asarray(pcd.normals),
    "labels": labels,
    "centroid": centroid,
    "scale": scale
})

print(f"Saved cleaned dataset with updated normals to {OUT_PATH}")
