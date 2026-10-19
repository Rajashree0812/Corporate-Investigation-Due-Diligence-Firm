import os
import glob
from PIL import Image

brain_root = r"C:\Users\thand\.gemini\antigravity\brain"

all_imgs = []
for root, dirs, files in os.walk(brain_root):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            all_imgs.append(os.path.join(root, f))

print(f"Total images found in brain directories: {len(all_imgs)}")
for img in sorted(all_imgs):
    sz = "unknown"
    try:
        with Image.open(img) as im:
            sz = im.size
    except:
        pass
    print(f"{os.path.basename(img)}: {sz} -> {img}")
