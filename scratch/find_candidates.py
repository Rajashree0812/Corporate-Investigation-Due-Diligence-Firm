import os, glob, re
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"
artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

# Find all images used in html files
used_images = set()
img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

for root, dirs, files in os.walk(workspace):
    if "veritas-intelligence-template" in root or ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            with open(os.path.join(root, f), "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
                matches = img_regex.findall(txt)
                for m in matches:
                    used_images.add(os.path.basename(m))

print(f"Total used image filenames: {len(used_images)}")

# Find candidate images in artifacts
candidates = []
for f in os.listdir(artifacts_dir):
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) and not f.startswith("media_"):
        full_p = os.path.join(artifacts_dir, f)
        try:
            with Image.open(full_p) as im:
                candidates.append((f, full_p, im.size, f in used_images))
        except:
            pass

# Also check assets/images
for root, dirs, files in os.walk(os.path.join(workspace, "assets", "images")):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            full_p = os.path.join(root, f)
            try:
                with Image.open(full_p) as im:
                    candidates.append((f, full_p, im.size, f in used_images))
            except:
                pass

print(f"Found {len(candidates)} total image files.")
print("=== Unused Candidate Images ===")
unused = [c for c in candidates if not c[3]]
for name, p, sz, is_used in sorted(unused, key=lambda x: x[0]):
    print(f"Size: {str(sz):<15} | File: {name:<45} | Path: {p}")
