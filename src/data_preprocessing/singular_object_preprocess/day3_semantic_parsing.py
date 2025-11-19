"""
Day 3 — Map PartNet Part Labels to Human-Readable Names (Chair 331)

- Load raw point cloud + per-point labels
- Parse the PartNet JSON hierarchy
- Build a label → name lookup table
- Visualize parts with consistent colors
- Save mappings for training and debugging
"""


import os, json, numpy as np, open3d as o3d
import matplotlib.pyplot as plt, matplotlib.patches as mpatches

base_dir = "/Volumes/T7/data_v0/49513"
points_file = os.path.join(base_dir, "point_sample", "sample-points-all-pts-nor-rgba-10000.txt")
labels_file = os.path.join(base_dir, "point_sample", "sample-points-all-label-10000.txt")
json_file = os.path.join(base_dir, "result_after_merging.json")

points = np.loadtxt(points_file)[:, :3]
labels = np.loadtxt(labels_file, dtype=int)
print(f"Loaded {len(points)} points")

def walk_tree(node, out):
    name = node.get("name", "unknown_part")
    if "ori_id" in node:
        out[int(node["ori_id"])] = name
    for child in node.get("children", []):
        walk_tree(child, out)

with open(json_file) as f:
    data = json.load(f)
root = data[0] if isinstance(data, list) else data
ori_to_part = {}
walk_tree(root, ori_to_part)

unique_labels = np.unique(labels)
label_to_name = {lbl: ori_to_part.get(lbl, "unknown_part") for lbl in unique_labels}
mapped = sum(1 for v in label_to_name.values() if v != "unknown_part")
print(f"Mapped {mapped}/{len(unique_labels)} labels")

viz_points = points[:, [0, 2, 1]]
viz_points[:, 2] *= -1

palette = plt.colormaps.get_cmap("nipy_spectral")
colors = np.zeros((len(points), 3))
for i, lbl in enumerate(unique_labels):
    colors[labels == lbl] = palette(i / max(1, len(unique_labels) - 1))[:3]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(viz_points)
pcd.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([pcd], window_name="Chair 331 Parts")

sample = np.random.choice(len(points), 3000, replace=False)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(viz_points[sample, 0], viz_points[sample, 1], viz_points[sample, 2],
           c=colors[sample], s=5, alpha=0.8)
# ---- UNIVERSAL MATPLOTLIB FIX (prevents distortion for knives, doors, chairs, everything) ----
x_limits = [viz_points[:,0].min(), viz_points[:,0].max()]
y_limits = [viz_points[:,1].min(), viz_points[:,1].max()]
z_limits = [viz_points[:,2].min(), viz_points[:,2].max()]

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

ax.set_proj_type('ortho')   # no perspective distortion
# ----------------------------------------------------------------

ax.set_title("Chair 331 Part Labels")
ax.set_box_aspect([1, 1, 1])
legend = []
for i, lbl in enumerate(unique_labels):
    name = label_to_name[lbl]
    color = palette(i / max(1, len(unique_labels) - 1))[:3]
    legend.append(mpatches.Patch(color=color, label=f"{lbl}: {name}"))
ax.legend(handles=legend, loc="center left", bbox_to_anchor=(1.05, 0.5), fontsize=8)
plt.tight_layout()
plt.show()

os.makedirs("processed_outputs", exist_ok=True)
with open("processed_outputs/chair331_label_to_name.json", "w") as f:
    json.dump({str(k): v for k, v in label_to_name.items()}, f, indent=4)
np.savetxt("processed_outputs/chair331_labels.txt", labels, fmt="%d")

for u, c in zip(*np.unique(labels, return_counts=True)):
    print(f"{u:2d}: {c:5d} → {label_to_name.get(u)}")
