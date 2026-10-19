import os
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"
p = os.path.join(workspace, "assets", "images", "banners", "banner-cta.jpg")
with Image.open(p) as im:
    print(f"banner-cta.jpg: format={im.format}, size={im.size}")
