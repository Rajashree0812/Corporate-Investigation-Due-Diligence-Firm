import json
import os

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
transcript = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")

files = [
    "confidential_conference",
    "case_files_audit",
    "operations_center_screens",
    "boardroom_strategy",
    "team_consultation"
]

for line in open(transcript, "r", encoding="utf-8", errors="ignore"):
    for f in files:
        if f in line and "generate_image" in line:
            print(f"=== {f} ===")
            print(line[:350])
            break
