# Project Overview

This first prototype explores affordance detection on simple 3D furniture models using Open3D. The goal is to build a minimal end-to-end pipeline that can take a raw 3D object, break it into geometric parts, and map those parts to basic affordances (possible interactions).

# Objectives

- Set up a clean reproducible codebase for affordance research.
- Work with 4-5 simple objects (chair, table, bed, sofa, stool).
-Decompose each mesh into meaningful sub-regions (planes, clusters, cavaties)
- Label structural roles (eg. support, container, backrest).
- Map structural roles to affordances:
    - Seat -> sit
    - Tabletop -> place
    - Backrest -> Lean
    - Hollow/cavity -> contain

- Prototype a rule based classifier that predicts affordances from geometry features



# Pipeline
3D Model → Geometric Decomposition → Region Features → Affordance Mapping

Input (io.py) – Load 3D mesh, sample to point cloud.

Decomposition (decompose.py) – Segment planes & clusters.

Feature Extraction (features.py) – Compute descriptors (planarity, normal, area, height, concavity).

Mapping (rules.py) – Apply rules to assign affordances.



# Deliverables
A GitHub repo with modular code (src/io.py, decompose.py, features.py, rules.py).

A tiny labeled dataset of 4–5 furniture models with region-affordance annotations.

A baseline rule-based affordance detector with JSON output + visualization.

Documentation (README + notes) explaining methods, limitations, and next steps.
