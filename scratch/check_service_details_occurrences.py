import glob

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8", errors="ignore").read()
    if 'href="service-details.html"' in content:
        count = content.count('href="service-details.html"')
        print(f"{f}: {count} occurrences of service-details.html")
