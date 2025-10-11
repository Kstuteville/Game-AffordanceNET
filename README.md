Game Affordance Net --> Mesh-Based Part Segmentation + Geometry Priors for Gameplay Roles

This project trains a mesh-native segmentation network (MeshCNN / DGNet) on a small subset of PartNet v0 object categories to infer gameplay-relevant roles

Fine-grained PartNet part labels (e.g., chair_leg_back_left) are collapsed into a concise gameplay vocabulary, and the model’s predictions are refined with geometry-based plausibility checks to ensure they make physical sense for in-engine use. For example, a “seat” must be mostly horizontal, not two meters above ground, and a “handle” should protrude and be grasp-sized.

Goal: Produce engine-agnostic affordance representations—clean, topology-consistent face-level masks plus compact geometric parameters (planes, axes, bounds) per affordance island, that can be consumed by thin adapters for Unreal and Unity to auto-instantiate interaction mechanics.


Why this matters:
Designers need high-level, reusable roles—like seat, backrest, handle, or flat_surface. Instead of dozens of dataset-specific labels. These coarse roles make 3D assets immediately usable for gameplay, interaction design, and level prototyping.
Geometry priors bring physical common sense to neural predictions. By enforcing constraints on orientation, height, curvature, and scale, the system filters out implausible results (e.g., a “seat” facing upward two meters high) and outputs regions that align with how objects actually afford use.
