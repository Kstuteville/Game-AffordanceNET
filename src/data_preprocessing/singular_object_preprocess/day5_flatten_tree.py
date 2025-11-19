#!/usr/bin/env python3
"""
Day 5 — Step A: Flatten the PartNet tree to a simple table.

Outputs:
  processed_outputs/part_tree_flat.json
  processed_outputs/part_tree_flat.csv
"""
import json, csv, os
from collections import deque

RESULT_FILE = "/Volumes/T7/data_v0/331/result_after_merging.json"
OUT_JSON = "processed_outputs/part_tree_flat.json"
OUT_CSV  = "processed_outputs/part_tree_flat.csv"

def is_leaf(n): return not n.get("children")
def nm(n): return n.get("name") or n.get("text") or "unnamed"

def main():
    os.makedirs("processed_outputs", exist_ok=True)
    with open(RESULT_FILE, "r") as f:
        tree = json.load(f)
    root = tree[0] if isinstance(tree, list) else tree

    flat = []
    q = deque([(root, None)])
    while q:
        node, parent = q.popleft()
        row = {
            "node_id": node.get("id", None),     # hierarchy node id
            "parent_id": parent,                 # parent node id
            "name": nm(node),                    # human-readable part name
            "is_leaf": bool(is_leaf(node)),      # leaves are actual parts
            "obj_ids": node.get("objs", []),     # e.g. ["original-22","new-3"]
        }
        flat.append(row)
        for ch in node.get("children", []):
            q.append((ch, node.get("id", None)))

    with open(OUT_JSON, "w") as f: json.dump(flat, f, indent=2)
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(flat[0].keys()))
        w.writeheader(); w.writerows(flat)

    print(f" Wrote {OUT_JSON} and {OUT_CSV} with {len(flat)} rows")

if __name__ == "__main__":
    main()
