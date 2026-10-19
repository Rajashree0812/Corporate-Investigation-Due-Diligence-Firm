import os
from PIL import Image, ImageStat

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

files = [
    "sanctions_cargo_vessel.jpg",
    "sanctions_port_terminal.jpg",
    "osint_data_network.jpg",
    "osint_cyber_matrix.jpg",
    "asset_tracing_vault_door.jpg",
    "asset_tracing_gold_bars.jpg",
    "asset_tracing_deposit_boxes.jpg"
]

for f in files:
    p = os.path.join(scratch_dir, f)
    if os.path.exists(p):
        with Image.open(p) as im:
            stat = ImageStat.Stat(im)
            print(f"{f:<30} | size: {str(im.size):<15} | mean RGB: {[round(x,1) for x in stat.mean]}")
