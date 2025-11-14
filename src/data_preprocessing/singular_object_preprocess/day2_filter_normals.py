# -------------------------------
# Day 2 – Recompute Normals (Chair 331)
# -------------------------------
# Loads normalized point cloud,
# recomputes normals using local neighborhoods,
# and saves updated version.
# -------------------------------

import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

# load
in_path = "processed_outputs/chair331_norm.npy"
data = np.load(in_path, allow_pickle=True).item()
points = data["points"]
labels = data["labels"]
scale = data["scale"]
centroid = data["centroid"]

# open3D cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# recompute normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
    radius=0.08, max_nn=30))
pcd.normalize_normals()

# preview – Open3D
o3d.visualization.draw_geometries([pcd], window_name="Chair 331 - Recomputed Normals")

# preview – Matplotlib
sample = np.random.choice(len(points), 2000, replace=False)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(points[sample, 0], points[sample, 1], points[sample, 2],
           c=labels[sample], cmap="tab10", s=3, alpha=0.8)

ax.set_title("Chair 331 - Recomputed Normals")
ax.set_box_aspect([1, 1, 1])
plt.tight_layout(); plt.show()

# save
out_dir = "processed_outputs"
os.makedirs(out_dir, exist_ok=True)
np.save(os.path.join(out_dir, "chair331_clean.npy"), {
    "points": np.asarray(pcd.points),
    "normals": np.asarray(pcd.normals),
    "labels": labels,
    "scale": scale,
    "centroid": centroid
})
print("saved cleaned dataset with updated normals.")
