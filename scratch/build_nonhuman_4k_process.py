import os
from PIL import Image, ImageFilter

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
workspace = r"c:\Users\thand\Desktop\Website"

# The 4 curated aesthetic, zero-human intelligence assets:
# 1. Consult: Black & gold luxury fountain pen resting on confidential agreement paper (photo-1455390582262-044cdead277a)
# 2. Assess: Dark corporate intelligence risk & financial data triangulation charts on monitor (photo-1551288049-bebda4e38f71)
# 3. Investigate: Forensic magnifying glass on evidentiary case files and audit ledgers (photo-1586281380349-632531db7ed4)
# 4. Report: Luxury executive boardroom conference suite overlooking panoramic skyline (photo-1497366811353-6870744d04b2)

selected_sources = {
    "process-step-consult.jpg": os.path.join(scratch_dir, "consult_fountain_pen.jpg"),
    "process-step-assess.jpg": os.path.join(scratch_dir, "assess_data_charts.jpg"),
    "process-step-investigate.jpg": os.path.join(scratch_dir, "investigate_magnifier_docs.jpg"),
    "process-step-report.jpg": os.path.join(scratch_dir, "report_boardroom_luxury.jpg")
}

target_w = 3840
target_h = 2160
target_aspect = target_w / target_h  # 16:9

dest_dirs = [
    os.path.join(workspace, "assets", "images", "process"),
    os.path.join(workspace, "veritas-intelligence-template", "assets", "images", "process")
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

for fname, src_p in selected_sources.items():
    print(f"Processing 4K {fname} from {src_p}...")
    with Image.open(src_p) as im:
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
            
        im_4k = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
        # Apply gentle unsharp mask for crystal clear 4K UHD definition
        im_sharp = im_4k.filter(ImageFilter.UnsharpMask(radius=1.2, percent=105, threshold=3))
        
        for d in dest_dirs:
            out_path = os.path.join(d, fname)
            im_sharp.save(out_path, format="JPEG", quality=95, optimize=True)
            print(f"  -> Saved {out_path} ({target_w}x{target_h})")

print("All 4 zero-human 4K process images successfully saved!")
