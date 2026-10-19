import os, re
from PIL import Image

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Collect all image files in assets/images and artifacts
all_images = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith(('.jpg', '.png')):
            fp = os.path.join(root, f)
            all_images[fp] = {'type': 'asset', 'name': f}

art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'
for f in os.listdir(art_dir):
    if f.endswith(('.jpg', '.png')) and not f.startswith('media_'):
        fp = os.path.join(art_dir, f)
        all_images[fp] = {'type': 'artifact', 'name': f}

# Read all HTML contents
html_contents = {}
for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        html_contents[h] = f.read()

# For each image, check if its filename appears in any HTML file
unused_images = []
used_images = {}

for fp, info in all_images.items():
    fn = info['name']
    used_in = [h for h, c in html_contents.items() if fn in c]
    if used_in:
        used_images[fp] = used_in
    else:
        unused_images.append(fp)

print(f"Total images checked: {len(all_images)}")
print(f"Total unused image files: {len(unused_images)}")
for p in unused_images:
    try:
        im = Image.open(p)
        print(f"  {p} {im.size}")
    except Exception as e:
        print(f"  {p} error: {e}")
