import os
from PIL import Image

found = []
for root, dirs, files in os.walk('.'):
    # skip .git or node_modules if any
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            fp = os.path.join(root, f)
            try:
                sz = os.path.getsize(fp)
                im = Image.open(fp)
                found.append((fp, im.size, sz))
            except:
                pass

print(f"Total images found in workspace: {len(found)}")
for fp, dims, sz in sorted(found):
    if not fp.startswith('./assets') and not fp.startswith('.\\assets'):
        print(f"{fp:60} {dims} ({sz/1024:.1f} KB)")
