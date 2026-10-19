import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
for f in os.listdir(scratch_dir):
    if f.lower().endswith(('.jpg', '.png', '.jpeg')):
        p = os.path.join(scratch_dir, f)
        try:
            with Image.open(p) as im:
                print(f"{f}: size={im.size}")
        except:
            pass
