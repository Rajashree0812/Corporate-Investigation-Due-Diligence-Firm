import os
import re
from collections import defaultdict

workspace = r"c:\Users\thand\Desktop\Website"

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
    # Only test root html files to avoid counting template mirror as duplicate
    if "veritas-intelligence-template" in rel_hf:
        continue
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    matches = img_regex.findall(content)
    for m in matches:
        if m.startswith("data:") or "logo" in m:
            continue
        usage[m].append(rel_hf)

print("=== Image Usage in Root HTML Pages ===")
duplicates = {k: v for k, v in usage.items() if len(v) > 1}
if duplicates:
    print(f"Found {len(duplicates)} images used in more than one place:")
    for k, v in duplicates.items():
        print(f"  {k} -> used {len(v)} times in: {', '.join(v)}")
else:
    print("Zero duplicates found! Every single image is unique across all pages.")
