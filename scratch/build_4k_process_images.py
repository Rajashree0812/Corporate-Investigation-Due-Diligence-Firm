import os
from PIL import Image, ImageFilter

artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

# Selected 4 distinct, highly relevant, pristine corporate intelligence images:
# 1. Consult: case_scoping_spotlight_1791957173104.jpg (private executive suite, corporate partner & general counsel discussing confidential investigation parameters & legal privilege dossiers)
# 2. Assess: beneficial_ownership_1791905876590.jpg (corporate intelligence analysis desk, ownership network diagrams, offshore entities, global registries & threat triangulation)
# 3. Investigate: financial_fraud_1791883611509.jpg (forensic financial accounting, balance-sheet forensics, transactional flowcharts, banking wire diagrams, audit evidence binder)
# 4. Report: risk_briefing_cta_1791960276856.jpg (senior intelligence director delivering oral briefing to board members and general counsel with court-admissible risk matrix)

selections = {
    "process-step-consult.jpg": os.path.join(artifacts_dir, "case_scoping_spotlight_1791957173104.jpg"),
    "process-step-assess.jpg": os.path.join(artifacts_dir, "beneficial_ownership_1791905876590.jpg"),
    "process-step-investigate.jpg": os.path.join(artifacts_dir, "financial_fraud_1791883611509.jpg"),
    "process-step-report.jpg": os.path.join(artifacts_dir, "risk_briefing_cta_1791960276856.jpg")
}

target_w = 3840
target_h = 2160
target_aspect = target_w / target_h  # 16:9 = 1.7777777777777777

dest_dirs = [
    os.path.join(workspace, "assets", "images", "process"),
    os.path.join(workspace, "veritas-intelligence-template", "assets", "images", "process")
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

for fname, src_path in selections.items():
    print(f"Processing {fname} from {src_path}...")
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        w, h = im.size
        curr_aspect = w / h
        
        # Crop to 16:9
        if curr_aspect > target_aspect:
            # too wide, crop sides
            new_w = int(h * target_aspect)
            left = (w - new_w) // 2
            im_cropped = im.crop((left, 0, left + new_w, h))
        else:
            # too tall, crop top/bottom
            # for corporate desk/boardroom, prioritize upper-center to preserve faces/screens
            new_h = int(w / target_aspect)
            top = max(0, int((h - new_h) * 0.35))
            im_cropped = im.crop((0, top, w, top + new_h))
        
        # Resize to 3840x2160 with Lanczos
        im_4k = im_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Apply gentle UnsharpMask for ultra-crisp 4K UHD rendering
        im_sharp = im_4k.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
        
        # Save to both target directories
        for d in dest_dirs:
            out_path = os.path.join(d, fname)
            im_sharp.save(out_path, format="JPEG", quality=95, optimize=True)
            print(f"  -> Saved {out_path} ({target_w}x{target_h})")

print("All 4K process images successfully processed and saved!")
