import os
from PIL import Image, ImageStat

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

files = [
    "4k_consult_pen_contract.jpg",
    "4k_consult_fountain_pen.jpg",
    "4k_assess_data_charts.jpg",
    "4k_assess_cyber_telemetry.jpg",
    "4k_investigate_magnifier_docs.jpg",
    "4k_investigate_audit_ledger.jpg",
    "4k_report_gavel_brief.jpg",
    "4k_report_boardroom_luxury.jpg"
]

for f in files:
    p = os.path.join(scratch_dir, f)
    with Image.open(p) as im:
        stat = ImageStat.Stat(im)
        print(f"{f:<30} | mean RGB: {[round(x,1) for x in stat.mean]}")
