import os
from PIL import Image

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
p = os.path.join(brain_dir, "blog_mandate_cta_1791957823858.jpg")
with Image.open(p) as im:
    print(f"blog_mandate_cta: size={im.size}")
