Game Affordance Net --> 3D Part Segmentation + Geometry Priors for Gameplay Roles

We train a point-cloud part-segmentation model (PointNet++/DGCNN) on ~5 PartNet categories, collapse fine-grained labels → gameplay roles (e.g., chair_leg_* → leg), and add geometry plausibility checks to make predictions game-usable (e.g., “seat must be roughly horizontal and not 2m tall”). This repo is a semester prototype toward a larger “Game Affordance Net.”

Why this matters:
Designers need course, reliable roles (seats, backrest, leg, handle, flat_surface) instead of dozens of tiny labels.
Geometry priors reduce black box weirdness and improve downstream use with colliders, triggers, placement in Games.