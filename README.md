# Game Affordance Net  
**Learning Gameplay-Relevant Affordances from 3D Geometry**

##  Overview
Game Affordance Net is a machine learning framework that teaches 3D models to understand their own *functional geometry* — answering the question:  
> “What can I do with this shape?”  

The system bridges **3D geometry**, **design cognition**, and **AI perception** by automatically predicting how objects in a game world can be used (sit, grasp, support, contain).  
Instead of manually setting up colliders, triggers, and interaction tags, designers can import assets that are already *affordance-aware.*

---

## Motivation: Why This Matters
In current game pipelines, developers and artists spend hours manually tagging every interactive region:
- Seats must be hand-marked as “sit zones.”  
- Handles and levers must be given custom collision volumes.  
- Containers need coded triggers for “open” or “hold.”

This manual affordance tagging is:
- **Slow** — every object must be manually processed.  
- **Inconsistent** — two similar chairs might have different setups.  
- **Error-prone** — gameplay logic can easily break between assets.

Game Affordance Net aims to automate this process through geometry-aware learning, allowing assets to “know” what functions their shapes afford.

---

##  Framework Overview

### **Goal**
Automatically map **structure → function → interaction** from 3D geometry,  
so a mesh can be imported into Unreal Engine already tagged with gameplay metadata.

### **Pipeline Summary**
1. **Input:** 3D mesh from the PartNet dataset.  
2. **Dense Point Sampling:** Convert mesh into a 20–50k point cloud preserving surface detail.  
3. **Supervised Labeling:** Each point inherits affordance labels via a `part → affordance` mapping (e.g., seat → sit, handle → grasp).  
4. **Model Training (DGCNN):**  
   - Learns local geometric patterns that correspond to affordances.  
   - Dynamically builds neighborhood graphs each batch to capture curvature, flatness, and spatial structure.  
5. **Projection to Mesh:** Predicted per-point affordances are projected back to mesh faces via nearest-neighbor or barycentric interpolation.  
6. **Unreal Integration:**  
   - The labeled mesh is imported with metadata.  
   - An Unreal Editor Utility Blueprint reads affordance labels and automatically assigns gameplay tags, colliders, or interaction triggers.

### **Technical Summary**
- **Training Domain:** Point-space (for scalability and GPU efficiency).  
- **Output Domain:** Mesh-space (for engine usability).  
- **Architecture:** Dynamic Graph CNN (DGCNN).  
- **Dataset:** [PartNet](https://cs.stanford.edu/~kaichun/partnet/).  
- **Affordance Labels:** sit, grasp, support, contain, place, pull.

---

##  Why a Hybrid Pipeline?
Mesh-native GNNs (like MeshCNN or DGNet) are topology-faithful but heavy and brittle for production.  
DGCNN, by contrast, learns dynamically in point-space, which makes it:
- **Topology-agnostic** — works across scanned and stylized assets.  
- **Scalable** — handles 50k+ points with mini-batching.  
- **Geometrically precise** — edge features capture the shape cues affordances depend on.

By training in point-space and projecting results back to mesh-space, we preserve geometric fidelity *and* maintain engine compatibility.

---


---

## Future Directions

### **Short Term**
- Extend beyond furniture to props, tools, and environmental assets.  
- Improve projection alignment and region smoothing.  
- Integrate Unreal-side visualization of affordance zones (via vertex colors or masks).  

### **Long Term**
- Train on **multi-dataset pipelines.  
- Introduce **transformer-based or mesh-hybrid architectures** for richer context reasoning.  
- Explore **self-supervised or CLIP-guided affordance discovery** from text–geometry pairs.  
- Enable **bi-directional design workflows** — AI suggests affordance-driven edits to geometry.

---

##  Why This Matters for Game Design
By letting models *understand their own geometry*, Game Affordance Net:
- Reduces friction in level design and environment setup.  
- Encourages emergent, consistent interactivity across worlds.  
- Opens the door to **AI-assisted worldbuilding** — where designers sketch shapes and the system infers what those shapes can do.  
- Lays the groundwork for **living, responsive worlds** where every object has meaning and function.  

This is not just about saving time — it’s about reimagining how digital worlds are built.  
When geometry becomes self-descriptive, **game engines evolve from static scene builders into affordance-aware ecosystems.**

---

##  Citation & References (ongoing adds)
If you use this work, please cite:
- Wang et al. (2019). *Dynamic Graph CNN for Learning on Point Clouds (DGCNN)*.  
- Mo et al. (2019). *PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding.*  
- Xu et al. (2022). *PartAfford: Part-Level Affordance Discovery from 3D Objects.*  

---

##  Team
Kaylie Stuteville
M.S. Integrated Design & Media, NYU Tandon  
Research: Geometry-Aware AI, Affordance Detection, Emotion-Aware NPC Systems  
Advisor: Prof. Ahmed Ansari  

---

*Game Affordance Net is an ongoing research prototype exploring the intersection of AI perception, geometry understanding, and interactive design.*
