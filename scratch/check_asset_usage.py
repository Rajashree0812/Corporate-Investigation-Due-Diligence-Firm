import glob

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8", errors="ignore").read()
    if 'hero-intelligence-risk' in content:
        print(f"hero-intelligence-risk used in {f}")
    if 'banner-risk-briefing' in content:
        print(f"banner-risk-briefing used in {f}")
