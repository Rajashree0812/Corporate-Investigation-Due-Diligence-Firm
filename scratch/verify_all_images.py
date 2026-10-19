import os
import re
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"

html_files = []
for root, dirs, files in os.walk(workspace):
    # Skip .git or cache if any
    if ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files.")

image_refs = []
img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

for hf in sorted(html_files):
    rel_hf = os.path.relpath(hf, workspace)
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    matches = img_regex.findall(content)
    for m in matches:
        if m.startswith("data:") or m.startswith("http://") or m.startswith("https://"):
            continue
        # resolve path relative to html file directory
        h_dir = os.path.dirname(hf)
        img_full_path = os.path.normpath(os.path.join(h_dir, m))
        image_refs.append({
            "html": rel_hf,
            "src": m,
            "full_path": img_full_path
        })

print(f"Total local image references in HTML: {len(image_refs)}")

# Check missing and dimensions
missing = []
dims_by_path = {}
for item in image_refs:
    p = item["full_path"]
    if not os.path.exists(p):
        missing.append(item)
    else:
        if p not in dims_by_path:
            try:
                with Image.open(p) as im:
                    dims_by_path[p] = im.size
            except Exception as e:
                dims_by_path[p] = f"Error: {e}"

if missing:
    print(f"WARNING: {len(missing)} missing image references:")
    for m in missing:
        print(f"  In {m['html']}: {m['src']} -> {m['full_path']}")
else:
    print("SUCCESS: All image references exist on disk!")

print("\n--- Image Dimensions Summary ---")
for p, sz in sorted(dims_by_path.items()):
    rel_p = os.path.relpath(p, workspace)
    print(f"{rel_p}: {sz}")
