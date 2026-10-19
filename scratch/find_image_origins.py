import json, re

transcript_path = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript_full.jsonl"

targets = [
    "legal_contract_signature",
    "social_network_analysis",
    "financial_dashboard",
    "forensic_accounting_ledger",
    "financial_statements_audit",
    "blog_legal_documents",
    "blog_cyber_intel",
    "safe_deposit_vault",
    "law_library_books",
    "case_files_audit"
]

found = {}
with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fp:
    for line in fp:
        for t in targets:
            if t in line:
                # Find context around it (like URL or description)
                urls = re.findall(r'https?://[^\s\"\'\\]+', line)
                if t not in found:
                    found[t] = []
                found[t].extend(urls[:3])

for k, v in found.items():
    print(f"{k}: {set(v)}")
