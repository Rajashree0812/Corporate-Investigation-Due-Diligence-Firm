import os, re
from PIL import Image

workspace = r"c:\Users\thand\Desktop\Website"
scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Get all images referenced in html
used = set()
img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
for root, dirs, files in os.walk(workspace):
    if "veritas-intelligence-template" in root or ".git" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            with open(os.path.join(root, f), "r", encoding="utf-8", errors="ignore") as fp:
                for m in img_regex.findall(fp.read()):
                    used.add(os.path.basename(m))

candidates = [
    "legal_contract_signature.jpg",
    "social_network_analysis.png",
    "financial_dashboard.jpg",
    "forensic_accounting_ledger.jpg",
    "financial_statements_audit.jpg",
    "blog_legal_documents.jpg",
    "blog_cyber_intel.jpg",
    "safe_deposit_vault.jpg",
    "law_library_books.jpg",
    "test_vault.jpg",
    "towers_reflection.jpg",
    "blog_city_towers.jpg"
]

print("=== Scratch Candidate Files Usage & Info ===")
for c in candidates:
    p = os.path.join(scratch_dir, c)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"{c:<30} | size: {str(im.size):<15} | Used in HTML: {c in used}")
