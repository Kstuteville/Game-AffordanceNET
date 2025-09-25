#  Open3D Affordance Prototype
--------------------------------
This repository contains the **first prototype** for my affordance research project.  
The goal is to build a minimal pipeline that takes a 3D object, decomposes its geometry,  
and predicts simple affordances (possible interactions) such as **sit, place, lean, and contain**.  

---

##  Overview
-------------------
Game developers usually have to manually program every way players can interact with objects  
(e.g., sitting on a chair, placing items on a table).  

This project explores how AI systems can automatically map:  


---

## 📂 Repo Structure

```text
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





-------------------------------------


📊 Deliverables
-----------------------
Modular Open3D codebase

Tiny labeled dataset (4–5 furniture models)

Rule-based affordance predictions

Documentation & notes for next iterations