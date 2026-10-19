import os
from PIL import Image, ImageFilter

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
target_w = 3840
target_h = 2160
target_aspect = target_w / target_h

options = [
    ("consult_fountain_pen", os.path.join(scratch_dir, "consult_fountain_pen.jpg")),
    ("consult_pen_contract", os.path.join(scratch_dir, "consult_pen_contract.jpg")),
    ("assess_data_charts", os.path.join(scratch_dir, "assess_data_charts.jpg")),
    ("assess_cyber_telemetry", os.path.join(scratch_dir, "assess_cyber_telemetry.jpg")),
    ("investigate_magnifier_docs", os.path.join(scratch_dir, "investigate_magnifier_docs.jpg")),
    ("investigate_audit_ledger", os.path.join(scratch_dir, "investigate_audit_ledger.jpg")),
    ("report_gavel_brief", os.path.join(scratch_dir, "report_gavel_brief.jpg")),
    ("report_boardroom_luxury", os.path.join(scratch_dir, "report_boardroom_luxury.jpg"))
]

for name, src in options:
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        curr_aspect = w / h
        if curr_aspect > target_aspect:
            new_w = int(h * target_aspect)
            left = (w - new_w) // 2
            cropped = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_aspect)
            top = (h - new_h) // 2
            cropped = im.crop((0, top, w, top + new_h))
        
        resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
        out_p = os.path.join(scratch_dir, f"4k_{name}.jpg")
        resized.save(out_p, format="JPEG", quality=95)
        print(f"Processed 4K: {out_p}")
