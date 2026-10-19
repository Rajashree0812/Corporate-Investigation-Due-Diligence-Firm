import os
from PIL import Image, ImageEnhance

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
workspace = r"c:\Users\thand\Desktop\Website"
template = os.path.join(workspace, "veritas-intelligence-template")

dir1 = os.path.join(workspace, "assets", "images", "process")
dir2 = os.path.join(template, "assets", "images", "process")
os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)

steps = [
    {
        "src": os.path.join(scratch, "team_consultation.jpg"),
        "dest": "process-step-consult.jpg",
        "crop_top": 0.15 # slight center-top focus
    },
    {
        "src": os.path.join(scratch, "operations_center_screens.jpg"),
        "dest": "process-step-assess.jpg",
        "crop_top": 0.2
    },
    {
        "src": os.path.join(scratch, "case_files_audit.jpg"),
        "dest": "process-step-investigate.jpg",
        "crop_top": 0.1
    },
    {
        "src": os.path.join(scratch, "boardroom_strategy.jpg"),
        "dest": "process-step-report.jpg",
        "crop_top": 0.0
    }
]

target_w, target_h = 3840, 2160
target_aspect = target_w / target_h

for s in steps:
    im = Image.open(s["src"]).convert("RGB")
    w, h = im.size
    aspect = w / h
    
    # Crop to 16:9
    if aspect > target_aspect:
        # Image is wider than 16:9
        new_w = int(h * target_aspect)
        left = (w - new_w) // 2
        im_cropped = im.crop((left, 0, left + new_w, h))
    else:
        # Image is taller than 16:9
        new_h = int(w / target_aspect)
        top = int((h - new_h) * s["crop_top"])
        top = max(0, min(top, h - new_h))
        im_cropped = im.crop((0, top, w, top + new_h))
        
    # Resize to exact 4K
    im_4k = im_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Sharpness(im_4k)
    im_4k = enhancer.enhance(1.15)
    
    p1 = os.path.join(dir1, s["dest"])
    p2 = os.path.join(dir2, s["dest"])
    im_4k.save(p1, "JPEG", quality=95, optimize=True)
    im_4k.save(p2, "JPEG", quality=95, optimize=True)
    print(f"Saved {s['dest']}: size={im_4k.size}, bytes={os.path.getsize(p1)}")

print("All 4 process lifecycle images successfully processed to true 4K!")
