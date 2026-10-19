import os
import glob
from PIL import Image

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

jpgs = glob.glob(os.path.join(brain_dir, "*.jpg")) + glob.glob(os.path.join(brain_dir, "*.png"))

print(f"Total image artifacts found: {len(jpgs)}")
for img in sorted(jpgs):
    fname = os.path.basename(img)
    try:
        with Image.open(img) as im:
            print(f"{fname}: {im.size}")
    except Exception as e:
        print(f"{fname}: error {e}")
