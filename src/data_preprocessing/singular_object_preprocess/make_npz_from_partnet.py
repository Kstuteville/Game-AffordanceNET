#!/usr/bin/env python3
# Minimal NPZ packer (points + normals + labels only)

import os, json, numpy as np

# --- Change these if your paths differ ---
BASE_DIR    = "/Volumes/T7/data_v0/331"
LABELS_FILE = os.path.join(BASE_DIR, "point_sample", "sample-points-all-label-10000.txt")
CLEAN_SNAP  = "processed_outputs/chair331_clean.npy"  # from Day 2
OUT_NPZ     = "data/processed_raw/chair/Chair_331.simple.npz"

def main():
    os.makedirs(os.path.dirname(OUT_NPZ), exist_ok=True)

    # Load Day 2 snapshot (already normalized)
    snap = np.load(CLEAN_SNAP, allow_pickle=True).item()
    points  = snap["points"].astype(np.float32)     # (N,3)
    normals = snap["normals"].astype(np.float32)    # (N,3)
    scale   = np.array([snap["scale"], *snap["centroid"]], dtype=np.float32)  # [radius, cx, cy, cz]

    # Per-point labels (PartNet object IDs like 17,22,40,...)
    labels = np.loadtxt(LABELS_FILE, dtype=int).astype(np.int64)  # (N,)

    # Tiny meta
    meta = {
        "category": "chair",
        "model_id": "Chair_331",
        "units_to_cm": 1.0,
        "afford_vocab": None,
        "afford_vocab_version": "unassigned",
        "schema": "simple-v1"  # indicates no mesh/bary fields yet
    }

    # Save minimal NPZ
    np.savez_compressed(
        OUT_NPZ,
        points=points,          # (N,3)
        normals=normals,        # (N,3)
        labels=labels,          # (N,)
        part_id=labels,         # duplicate for future affordance mapping
        scale_center=scale,     # (4,)
        meta=json.dumps(meta)   # str
    )

    print(f"✅ Wrote {OUT_NPZ}")
    print(f"N points: {points.shape[0]} | labels unique: {np.unique(labels).size}")

if __name__ == "__main__":
    main()
