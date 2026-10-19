import os

workspace = r"c:\Users\thand\Desktop\Website"
for root, dirs, files in os.walk(workspace):
    if "veritas-intelligence-template" in root or ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                for num, line in enumerate(fp, 1):
                    if "btn-outline-white" in line or "btn-white" in line:
                        print(f"{f}:{num} -> {line.strip()}")
