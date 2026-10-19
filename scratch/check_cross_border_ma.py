import glob

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8", errors="ignore").read()
    if 'cross_border_ma' in content or 'home-service-ma' in content:
        print(f"found in {f}")
