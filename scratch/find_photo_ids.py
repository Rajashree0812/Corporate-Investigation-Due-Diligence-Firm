import re

transcript_path = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript_full.jsonl"

targets = ["financial_dashboard", "forensic_accounting_ledger", "blog_legal_documents", "blog_cyber_intel", "case_files_audit"]

with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fp:
    for line in fp:
        for t in targets:
            if t in line and "photo-" in line:
                m = re.findall(r'photo-[a-zA-Z0-9\-]+', line)
                if m:
                    print(f"{t}: {set(m)}")
