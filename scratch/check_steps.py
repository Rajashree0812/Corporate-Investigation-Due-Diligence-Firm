import json
import os

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
transcript = os.path.join(brain_dir, ".system_generated", "logs", "transcript.jsonl")

for line in open(transcript, "r", encoding="utf-8", errors="ignore"):
    data = json.loads(line)
    step = data.get("step_index")
    if step in [1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243]:
        tc = data.get("tool_calls", [])
        if tc:
            print(f"Step {step}: {tc}")
