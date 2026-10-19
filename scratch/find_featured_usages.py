import os, glob, re

for hf in glob.glob("*.html"):
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+\.(?:jpg|png|webp|svg|jpeg)', content)
    for m in matches:
        if "featured" in m or "diagram" in m or "matrix" in m or "blog-detail" in m:
            print(f"{hf:35s}: {m}")
