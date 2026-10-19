import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

candidates = [
    ("consult_pen_contract", os.path.join(scratch_dir, "consult_pen_contract.jpg")),
    ("consult_fountain_pen", os.path.join(scratch_dir, "consult_fountain_pen.jpg")),
    ("assess_data_charts", os.path.join(scratch_dir, "assess_data_charts.jpg")),
    ("assess_cyber_telemetry", os.path.join(scratch_dir, "assess_cyber_telemetry.jpg")),
    ("investigate_audit_ledger", os.path.join(scratch_dir, "investigate_audit_ledger.jpg")),
    ("investigate_magnifier_docs", os.path.join(scratch_dir, "investigate_magnifier_docs.jpg")),
    ("report_gavel_brief", os.path.join(scratch_dir, "report_gavel_brief.jpg")),
    ("report_boardroom_luxury", os.path.join(scratch_dir, "report_boardroom_luxury.jpg"))
]

for label, p in candidates:
    with Image.open(p) as im:
        print(f"{label}: size={im.size}, aspect={im.width/im.height:.2f}")
