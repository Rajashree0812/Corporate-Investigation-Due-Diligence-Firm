import os
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"
p1 = os.path.join(workspace, "assets", "images", "hero", "hero-ma-due-diligence.jpg")
print(f"hero-ma-due-diligence.jpg exists: {os.path.exists(p1)}")
if os.path.exists(p1):
    with Image.open(p1) as im:
        print(f"size: {im.size}")
