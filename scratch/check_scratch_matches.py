import os
from PIL import Image
import numpy as np

workspace = r"c:\Users\thand\Desktop\Website"
scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

project_images = {}
for root, dirs, files in os.walk(os.path.join(workspace, "assets", "images")):
    for f in files:
        if f.lower().endswith((".jpg", ".png")):
            fp = os.path.join(root, f)
            try:
                project_images[f] = Image.open(fp).convert("RGB").resize((64, 64))
            except:
                pass

candidates = [
    "confidential_conference.jpg",
    "legal_contract_signature.jpg",
    "contract_deal_review.jpg",
    "case_files_audit.jpg",
    "financial_dashboard.jpg",
    "forensic_accounting_ledger.jpg",
    "operations_center_screens.jpg",
    "social_network_analysis.png",
    "boardroom_strategy.jpg",
    "executive_conference_1.jpg",
    "executive_conference_2.jpg",
    "executive_conference_3.jpg",
    "team_consultation.jpg"
]

for cand in candidates:
    cp = os.path.join(scratch, cand)
    if os.path.exists(cp):
        im = Image.open(cp).convert("RGB").resize((64, 64))
        arr = np.array(im)
        min_diff = 9999
        closest = None
        for name, pim in project_images.items():
            diff = np.mean(np.abs(arr - np.array(pim)))
            if diff < min_diff:
                min_diff = diff
                closest = name
        print(f"{cand}: closest in project is {closest} (diff={min_diff:.2f})")
