import os, re, filecmp
from collections import defaultdict
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"

print("--- 1. File Synchronization Verification ---")
diff_index = filecmp.cmp(
    os.path.join(workspace, "index.html"),
    os.path.join(workspace, "veritas-intelligence-template", "index.html"),
    shallow=False
)
diff_css = filecmp.cmp(
    os.path.join(workspace, "assets", "css", "style.css"),
    os.path.join(workspace, "veritas-intelligence-template", "assets", "css", "style.css"),
    shallow=False
)
print(f"index.html synced: {diff_index}")
print(f"style.css synced: {diff_css}")

print("\n--- 2. Image Dimensions Verification ---")
process_images = [
    "assets/images/process/process-step-consult.jpg",
    "assets/images/process/process-step-assess.jpg",
    "assets/images/process/process-step-investigate.jpg",
    "assets/images/process/process-step-report.jpg"
]
for p in process_images:
    full_p = os.path.join(workspace, p)
    if os.path.exists(full_p):
        with Image.open(full_p) as im:
            print(f"{p}: {im.size} (4K UHD: {im.size == (3840, 2160)})")
    else:
        print(f"MISSING: {p}")

print("\n--- 3. Global Duplicate Check in HTML Pages ---")
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

print("\n--- 4. Verify Phase Badges Removed ---")
with open(os.path.join(workspace, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()
if "process-step-badge" in idx_content:
    print("WARNING: process-step-badge still present in index.html!")
else:
    print("SUCCESS: process-step-badge completely removed from index.html.")
