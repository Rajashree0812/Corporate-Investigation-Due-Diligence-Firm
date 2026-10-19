import os, re, filecmp
from collections import defaultdict
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"

print("--- 1. File Sync Check: index-2.html ---")
diff_index2 = filecmp.cmp(
    os.path.join(workspace, "index-2.html"),
    os.path.join(workspace, "veritas-intelligence-template", "index-2.html"),
    shallow=False
)
print(f"index-2.html 100% in sync: {diff_index2}")

print("\n--- 2. Dimensions Check: Strategic Risk Insights Images ---")
images = [
    "assets/images/blog/home2-briefing-sanctions.jpg",
    "assets/images/blog/home2-briefing-osint.jpg",
    "assets/images/blog/home2-briefing-asset-recovery.jpg"
]

for img in images:
    p = os.path.join(workspace, img)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"{img}: {im.size} (4K UHD: {im.size == (3840, 2160)})")
    else:
        print(f"MISSING: {img}")

print("\n--- 3. Global Duplicate Check ---")
html_files = []
for root, dirs, files in os.walk(workspace):
    if ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
usage = defaultdict(list)

for hf in sorted(html_files):
    rel_hf = os.path.relpath(hf, workspace)
    if "veritas-intelligence-template" in rel_hf:
        continue
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    matches = img_regex.findall(content)
    for m in matches:
        if m.startswith("data:") or "logo" in m:
            continue
        usage[m].append(rel_hf)

duplicates = {k: v for k, v in usage.items() if len(v) > 1}
if duplicates:
    print(f"FAILED: Found {len(duplicates)} duplicate image usages:")
    for k, v in duplicates.items():
        print(f"  {k} used in: {v}")
else:
    print("SUCCESS: Zero duplicate images found across all website pages!")
