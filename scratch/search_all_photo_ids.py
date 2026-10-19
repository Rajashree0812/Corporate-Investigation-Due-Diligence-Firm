import re, os

transcript_path = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript_full.jsonl"

all_pids = set()
with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fp:
    for line in fp:
        matches = re.findall(r'photo-[0-9]{10,}-[a-zA-Z0-9]+', line)
        for m in matches:
            all_pids.add(m)

print(f"Total unique photo IDs found in transcript: {len(all_pids)}")
for pid in sorted(all_pids):
    print(pid)
