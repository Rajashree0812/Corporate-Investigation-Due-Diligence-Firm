import os
from PIL import Image

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

for f in ["team_consultation.jpg", "confidential_conference.jpg", "legal_contract_signature.jpg"]:
    p = os.path.join(scratch, f)
    im = Image.open(p)
    # Check middle crop
    w, h = im.size
    print(f"{f}: size={w}x{h}")
