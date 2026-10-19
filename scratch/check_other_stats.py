import os
from PIL import Image, ImageStat

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

for f in ["legal_contract_signature.jpg", "social_network_analysis.png", "blog_legal_documents.jpg", "blog_cyber_intel.jpg", "safe_deposit_vault.jpg"]:
    p = os.path.join(scratch_dir, f)
    if os.path.exists(p):
        with Image.open(p) as im:
            stat = ImageStat.Stat(im)
            print(f"{f:<30} | size: {str(im.size):<15} | mean RGB: {[round(x,1) for x in stat.mean]}")
