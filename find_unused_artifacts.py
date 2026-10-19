import os, glob
from PIL import Image
import numpy as np

artifact_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

def get_thumb(p):
    try:
        with Image.open(p) as img:
            im = img.convert('RGB').resize((32, 18), Image.Resampling.BILINEAR)
            return np.array(im, dtype=np.float32)
    except:
        return None

# Collect all assets thumbs
assets_thumbs = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith(('.jpg', '.png')):
            full = os.path.join(root, f)
            t = get_thumb(full)
            if t is not None:
                assets_thumbs[full] = t

# Compare each artifact
print('=== Artifact comparison with assets/images ===')
for f in sorted(os.listdir(artifact_dir)):
    if f.endswith('.jpg'):
        ap = os.path.join(artifact_dir, f)
        at = get_thumb(ap)
        if at is None:
            continue
        best_match = None
        best_diff = float('inf')
        for asset_path, asset_t in assets_thumbs.items():
            diff = np.mean(np.abs(at - asset_t))
            if diff < best_diff:
                best_diff = diff
                best_match = asset_path
        if best_diff < 15.0:
            print(f'{f} MATCHES {best_match} (diff={best_diff:.2f})')
        else:
            print(f'*** UNUSED ARTIFACT: {f} (closest: {best_match}, diff={best_diff:.2f})')
