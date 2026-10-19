import glob

for f in sorted(glob.glob("*.html")):
    c = open(f, "r", encoding="utf-8", errors="ignore").read()
    for name in ["home-service-investigations", "home-service-screening", "home-service-ma", "home-service-fraud"]:
        if name in c:
            print(f"{name} referenced in {f}")
