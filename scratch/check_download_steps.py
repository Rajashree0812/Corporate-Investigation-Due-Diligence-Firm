import json
import os

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
transcript = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")

for line in open(transcript, "r", encoding="utf-8", errors="ignore"):
    data = json.loads(line)
    if data.get("step_index") in [3622, 3623, 3624, 3625, 3649, 3650]:
        print(f"Step {data.get('step_index')}: {data.get('tool_calls') or data.get('content')[:300]}")
