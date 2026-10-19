import glob

for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, 1):
        if "service-details.html" in line:
            print(f"{f}:{i}: {line.strip()}")
