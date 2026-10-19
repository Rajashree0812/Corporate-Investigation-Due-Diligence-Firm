import os
import glob

workspace = r"c:\Users\thand\Desktop\Website"
images_in_project = {}
for root, dirs, files in os.walk(os.path.join(workspace, "assets", "images")):
    for f in files:
        if f.endswith((".jpg", ".png")):
            p = os.path.join(root, f)
            images_in_project[f] = p

print(f"Total image files in assets/images: {len(images_in_project)}")
for name, p in sorted(images_in_project.items()):
    print(f"  {name}")
