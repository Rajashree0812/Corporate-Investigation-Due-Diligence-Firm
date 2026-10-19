import os
from PIL import Image, ImageStat

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

imgs = [
    "confidential_conference.jpg",
    "operations_center_screens.jpg",
    "case_files_audit.jpg",
    "boardroom_strategy.jpg",
    "team_consultation.jpg",
    "legal_contract_signature.jpg"
]

for name in imgs:
    p = os.path.join(scratch, name)
    im = Image.open(p)
    stat = ImageStat.Stat(im)
    print(f"{name}: size={im.size}, mean_rgb={[round(x, 1) for x in stat.mean]}")
