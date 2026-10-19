import os, hashlib, re
from PIL import Image

# 1. Map all images in assets/images with MD5 hash
asset_images = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith(('.jpg', '.png', '.svg')):
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, '.').replace('\\', '/')
            with open(fp, 'rb') as b:
                h = hashlib.md5(b.read()).hexdigest()
            asset_images[rel] = {'hash': h, 'name': f, 'size': Image.open(fp).size if not f.endswith('.svg') else None}

# 2. Map all images in artifacts with MD5 hash
art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'
art_images = {}
for f in os.listdir(art_dir):
    if f.endswith(('.jpg', '.png')) and not f.startswith('media_'):
        fp = os.path.join(art_dir, f)
        with open(fp, 'rb') as b:
            h = hashlib.md5(b.read()).hexdigest()
        art_images[f] = {'hash': h, 'size': Image.open(fp).size}

# 3. Check HTML references
html_refs = {}
for h in os.listdir('.'):
    if h.endswith('.html'):
        with open(h, 'r', encoding='utf-8') as hf:
            content = hf.read()
            for m in re.findall(r'assets/images/[^\s"\'\)>]+', content):
                html_refs.setdefault(m, set()).add(h)

print("=== IMAGES IN blog-details-ma-diligence.html ===")
for ref, pages in html_refs.items():
    if 'blog-details-ma-diligence.html' in pages:
        print(f"  {ref} -> also used in: {pages - {'blog-details-ma-diligence.html'}}")

print("\n=== IMAGES IN blog-details-whistleblower.html ===")
for ref, pages in html_refs.items():
    if 'blog-details-whistleblower.html' in pages:
        print(f"  {ref} -> also used in: {pages - {'blog-details-whistleblower.html'}}")

print("\n=== IMAGES IN blog-details.html ===")
for ref, pages in html_refs.items():
    if 'blog-details.html' in pages:
        print(f"  {ref} -> also used in: {pages - {'blog-details.html'}}")

print("\n=== DUPLICATE CONTENT CHECK ===")
# Find which asset images share hashes or were created from the same base
for a1, d1 in asset_images.items():
    for a2, d2 in asset_images.items():
        if a1 < a2 and d1['hash'] == d2['hash']:
            print(f"Duplicate hash: {a1} == {a2}")
