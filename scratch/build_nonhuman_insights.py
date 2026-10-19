import os
from PIL import Image, ImageFilter

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
workspace = r"c:\Users\thand\Desktop\Website"

# The 3 curated aesthetic, zero-human intelligence assets for Strategic Risk Insights:
# 1. Sanctions Risk: Modern aerial container ship navigating international waters (sanctions_cargo_vessel.jpg)
# 2. OSINT & Litigation Support: Global digital network telemetry & interconnected intelligence nodes (osint_data_network.jpg)
# 3. Asset Tracing: Modern reinforced steel bank vault door with heavy chrome locking bolts (asset_tracing_vault_door.jpg)

sources = {
    "home2-briefing-sanctions.jpg": os.path.join(scratch_dir, "sanctions_cargo_vessel.jpg"),
    "home2-briefing-osint.jpg": os.path.join(scratch_dir, "osint_data_network.jpg"),
    "home2-briefing-asset-recovery.jpg": os.path.join(scratch_dir, "asset_tracing_vault_door.jpg")
}

target_w = 3840
target_h = 2160
target_aspect = target_w / target_h

dest_dirs = [
    os.path.join(workspace, "assets", "images", "blog"),
    os.path.join(workspace, "veritas-intelligence-template", "assets", "images", "blog")
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

for fname, src_p in sources.items():
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
        im_sharp = im_4k.filter(ImageFilter.UnsharpMask(radius=1.2, percent=105, threshold=3))
        
        for d in dest_dirs:
            out_path = os.path.join(d, fname)
            im_sharp.save(out_path, format="JPEG", quality=95, optimize=True)
            print(f"  -> Saved {out_path} ({target_w}x{target_h})")

print("All 3 Strategic Risk Insights 4K images processed and saved successfully!")
