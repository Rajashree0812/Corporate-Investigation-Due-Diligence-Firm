import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

files_to_check = [
    "legal_contract_signature.jpg",
    "social_network_analysis.png",
    "financial_dashboard.jpg",
    "forensic_accounting_ledger.jpg",
    "financial_statements_audit.jpg",
    "blog_legal_documents.jpg",
    "blog_cyber_intel.jpg",
    "safe_deposit_vault.jpg",
    "law_library_books.jpg",
    "test_vault.jpg"
]

# Let's inspect where these files originated from or check their EXIF/headers/metadata or generate small previews
for f in files_to_check:
    p = os.path.join(scratch_dir, f)
    with Image.open(p) as im:
        print(f"{f}: size={im.size}, mode={im.mode}")
