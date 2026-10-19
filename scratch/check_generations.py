import re

transcript_path = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fp:
    for i, line in enumerate(fp):
        if "beneficial_ownership" in line or "generate_image" in line:
            # find generate_image calls
            matches = re.findall(r'\"ImageName\":\s*\"([^\"]+)\"', line)
            prompts = re.findall(r'\"Prompt\":\s*\"([^\"]+)\"', line)
            for m, p in zip(matches, prompts):
                print(f"[{m}]: {p[:150]}...")
