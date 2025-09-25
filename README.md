Open3D Affordance Prototype
-------------------------------

This repository contains the first prototype for my affordance research project. The goal is to build a minimal pipeline that takes a 3D object, decomposes its geometry, and predicts simple affordances (possible interactions) such as sit, place, lean, and contain. 

---------------------------------------------- 

OVERVIEW

Game developers usually have to manually program every way players can interact with objects (e.g., sitting on a chair, placing items on a table). This project explores how AI systems can automatically map 3D geometry--> structural parts --> affordances, reducing manual work and opening the door to richer game interactions.

------------------------------------------

🚀 Getting Started
Requirements

Install dependencies:

pip install -r requirements.txt


Main libraries:

Open3D
 – mesh/point cloud processing

NumPy, SciPy – math utilities

scikit-learn – clustering support

trimesh – mesh I/O helpers

Running the demo
python demos/run_one.py data/chair_01/mesh.glb


This will:

Load the chair mesh

Decompose it into sub-regions

Extract features

Classify affordances

Save outputs:

annotations/chair_01_pred.json (predicted labels)

out/chair_01_overlay.png (visualized regions)


-----------------------------------------
REPO STRUCTURE

Open3D-Project/
│
├── src/              # core modules
│   ├── io.py         # mesh/point cloud loading
│   ├── decompose.py  # segmentation (planes, clusters)
│   ├── features.py   # compute geometric descriptors
│   └── rules.py      # affordance mapping
│
├── data/             # sample furniture meshes
├── annotations/      # labeled datasets + predictions
├── notebooks/        # experimental Jupyter notebooks
├── results/          # visualizations, metrics
├── notes/            # research notes, readings
├── demos/            # runnable scripts
├── README.md
├── requirements.txt
└── main.py









📊 Deliverables

Modular Open3D codebase

Tiny labeled dataset (4–5 furniture models)

Rule-based affordance predictions

Documentation & notes for next iterations