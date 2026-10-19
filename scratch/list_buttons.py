import os, re

workspace = r"c:\Users\thand\Desktop\Website"
buttons = set()

for root, dirs, files in os.walk(workspace):
    if "veritas-intelligence-template" in root or ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            with open(os.path.join(root, f), "r", encoding="utf-8", errors="ignore") as fp:
                for line in fp:
                    if "btn" in line:
                        for m in re.findall(r'class=["\']([^"\']*btn[^"\']*)["\']', line):
                            buttons.add(m.strip())

for b in sorted(buttons):
    print(b)
