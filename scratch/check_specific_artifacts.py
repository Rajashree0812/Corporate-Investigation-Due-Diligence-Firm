import os
import glob
from PIL import Image

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

# Check ma_due_diligence_1791883574148.jpg
for f in ["ma_due_diligence_1791883574148.jpg", "cross_border_ma_1791905904638.jpg", "transaction_feasibility_1791957393659.jpg"]:
    p = os.path.join(brain_dir, f)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"{f}: size={im.size}")
