import os

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
transcript = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")

targets = [
    "internal_investigation",
    "corporate_investigations",
    "executive_screening",
    "cross_border_ma",
    "ma_due_diligence",
    "financial_fraud"
]

if os.path.exists(transcript):
    for line in open(transcript, "r", encoding="utf-8", errors="ignore"):
        for t in targets:
            if t in line and "generate_image" in line:
                print(f"=== {t} ===")
                print(line[:400])
