import os
from PIL import Image
import numpy as np

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

artifacts = {
    "corp_inv": os.path.join(brain_dir, "corporate_investigations_1791883501360.jpg"),
    "exec_screen": os.path.join(brain_dir, "executive_screening_1791883533720.jpg"),
    "ma_due": os.path.join(brain_dir, "ma_due_diligence_1791883574148.jpg"),
    "fraud": os.path.join(brain_dir, "financial_fraud_1791883611509.jpg"),
}

project_imgs = {}
for root, dirs, files in os.walk(os.path.join(workspace, "assets", "images")):
    for f in files:
        if f.endswith((".jpg", ".png")):
            p = os.path.join(root, f)
            try:
                project_imgs[f] = Image.open(p).convert("RGB").resize((100, 100))
            except:
                pass

for k, art_path in artifacts.items():
    art_im = Image.open(art_path).convert("RGB").resize((100, 100))
    art_arr = np.array(art_im)
    closest = None
    min_diff = 999999
    for name, p_im in project_imgs.items():
        diff = np.mean(np.abs(art_arr - np.array(p_im)))
        if diff < min_diff:
            min_diff = diff
            closest = name
    print(f"Artifact {k} ({os.path.basename(art_path)}): closest is {closest} with diff {min_diff:.2f}")
