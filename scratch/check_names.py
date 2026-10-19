import glob

artifacts_to_check = [
    "blog_mandate_cta",
    "internal_investigation",
    "ma_due_diligence",
    "investigative_history_archive",
    "banner-cta"
]

for name in artifacts_to_check:
    found = []
    for f in glob.glob("*.html"):
        c = open(f, "r", encoding="utf-8", errors="ignore").read()
        if name in c:
            found.append(f)
    print(f"{name} -> {found}")
