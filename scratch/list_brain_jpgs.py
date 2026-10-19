import os
import glob
from PIL import Image

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

for f in sorted(os.listdir(brain_dir)):
    if f.endswith(".jpg") and not f.startswith("."):
        fp = os.path.join(brain_dir, f)
        print(f"{f}")
