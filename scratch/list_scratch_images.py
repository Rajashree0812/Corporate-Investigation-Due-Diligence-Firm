import os
from PIL import Image

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

for f in sorted(os.listdir(scratch)):
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        p = os.path.join(scratch, f)
        try:
            im = Image.open(p)
            print(f"{f}: {im.size}, {im.format}")
        except:
            pass
