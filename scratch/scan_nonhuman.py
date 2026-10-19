import os
from PIL import Image

artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

# Check all images in artifacts and assets
candidate_paths = []
for root, dirs, files in os.walk(artifacts_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) and not f.startswith('media_'):
            candidate_paths.append(os.path.join(root, f))

for root, dirs, files in os.walk(workspace):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            candidate_paths.append(os.path.join(root, f))

print(f"Total images found: {len(candidate_paths)}")
for p in candidate_paths:
    name = os.path.basename(p)
    if any(k in name.lower() for k in ["vault", "map", "dossier", "desk", "cyber", "network", "matrix", "seal", "data", "tech", "screen", "boardroom", "doc", "archive"]):
        print(f"Candidate: {name} | {p}")
