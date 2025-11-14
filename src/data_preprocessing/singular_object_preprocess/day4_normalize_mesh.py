# -------------------------------
# Day 4 – Normalize Full Mesh (Chair 331)
# -------------------------------
# Load all mesh segments (.obj), merge them,
# reorient to Z-up, normalize to unit sphere,
# recompute vertex normals, and save.
# -------------------------------

import os
import numpy as np
import open3d as o3d

# Paths
mesh_dir = "/Volumes/T7/data_v0/331/objs"
out_dir = "processed_outputs"
os.makedirs(out_dir, exist_ok=True)

# Load all .obj segments
obj_files = sorted([
    os.path.join(mesh_dir, f)
    for f in os.listdir(mesh_dir)
    if f.endswith(".obj") and ("original" in f or "new" in f)
])

meshes = []
for path in obj_files:
    mesh = o3d.io.read_triangle_mesh(path)
    if not mesh.is_empty():
        meshes.append(mesh)

print(f"Loaded {len(meshes)} mesh segments.")

# Merge all meshes
full_mesh = meshes[0]
for m in meshes[1:]:
    full_mesh += m

# Reorient to Z-up
verts = np.asarray(full_mesh.vertices)
verts = verts[:, [0, 2, 1]]
verts[:, 2] *= -1
full_mesh.vertices = o3d.utility.Vector3dVector(verts)

# Normalize to unit sphere
centroid = verts.mean(axis=0)
verts -= centroid
scale = np.max(np.linalg.norm(verts, axis=1))
verts /= scale
full_mesh.vertices = o3d.utility.Vector3dVector(verts)

# Recompute normals
full_mesh.compute_vertex_normals()

# Save
out_path = os.path.join(out_dir, "chair331_full_normalized.ply")
o3d.io.write_triangle_mesh(out_path, full_mesh)
print(f"Saved normalized mesh to: {out_path}")

# Preview
o3d.visualization.draw_geometries([full_mesh], window_name="Chair 331 – Normalized Mesh")
