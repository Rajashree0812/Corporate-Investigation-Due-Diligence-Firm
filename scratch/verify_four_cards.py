import os
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"
cards = [
    "home-service-investigations.jpg",
    "home-service-screening.jpg",
    "home-service-ma.jpg",
    "home-service-fraud.jpg"
]

for c in cards:
    p1 = os.path.join(workspace, "assets", "images", "services", c)
    p2 = os.path.join(workspace, "veritas-intelligence-template", "assets", "images", "services", c)
    im1 = Image.open(p1)
    im2 = Image.open(p2)
    print(f"Root {c}: format={im1.format}, size={im1.size}, bytes={os.path.getsize(p1)}")
    print(f"Template {c}: format={im2.format}, size={im2.size}, bytes={os.path.getsize(p2)}")
