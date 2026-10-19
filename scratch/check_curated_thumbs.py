import os
from PIL import Image

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

to_check = [
    "investigate_audit_ledger.jpg",
    "investigate_magnifier_docs.jpg",
    "assess_data_charts.jpg",
    "assess_cyber_telemetry.jpg",
    "consult_fountain_pen.jpg",
    "executive_conference_1.jpg",
    "executive_conference_2.jpg"
]

for name in to_check:
    p = os.path.join(scratch, name)
    if os.path.exists(p):
        with Image.open(p) as im:
            thumb = im.copy()
            thumb.thumbnail((800, 450), Image.Resampling.LANCZOS)
            out_p = os.path.join(brain_dir, f"preview_{name}")
            thumb.save(out_p, "JPEG", quality=85)
            print(f"{name:30s}: size={im.size}")
    else:
        print(f"{name:30s}: NOT FOUND")
