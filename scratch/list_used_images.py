import os, re

workspace = r"c:\Users\thand\Desktop\Website"
img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

used = {}
for root, dirs, files in os.walk(workspace):
    if "veritas-intelligence-template" in root or ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, workspace)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
                for m in img_regex.findall(txt):
                    base = os.path.basename(m)
                    if base not in used:
                        used[base] = []
                    used[base].append(rel)

print(f"Total distinct image basenames referenced: {len(used)}")
for k, v in sorted(used.items()):
    print(f"{k} -> {', '.join(v)}")
