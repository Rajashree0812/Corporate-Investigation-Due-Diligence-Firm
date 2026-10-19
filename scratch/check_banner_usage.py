import glob

banners = [
    "banner-cta.jpg",
    "banner-case-scoping.jpg",
    "banner-scoping-proposal.jpg",
    "banner-confidential-consult.jpg",
    "banner-transaction-feasibility.jpg"
]

for b in banners:
    found = []
    for f in sorted(glob.glob("*.html")):
        c = open(f, "r", encoding="utf-8", errors="ignore").read()
        if b in c:
            found.append(f)
    print(f"{b} used in: {', '.join(found) if found else 'NOWHERE'}")
