import os

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Let's inspect the files in scratch:
# 1. legal_contract_signature.jpg
# 2. social_network_analysis.png
# 3. blog_legal_documents.jpg
# 4. blog_cyber_intel.jpg
# 5. financial_dashboard.jpg
# 6. safe_deposit_vault.jpg
# 7. law_library_books.jpg
# 8. test_vault.jpg

for f in ["legal_contract_signature.jpg", "social_network_analysis.png", "blog_legal_documents.jpg", "blog_cyber_intel.jpg", "financial_dashboard.jpg", "safe_deposit_vault.jpg", "law_library_books.jpg", "test_vault.jpg"]:
    p = os.path.join(scratch_dir, f)
    if os.path.exists(p):
        print(f"Exists: {f} ({os.path.getsize(p)} bytes)")
