import os

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
transcript = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")

if os.path.exists(transcript):
    for line in open(transcript, "r", encoding="utf-8", errors="ignore"):
        if "blog_mandate_cta" in line:
            print(line[:300])
