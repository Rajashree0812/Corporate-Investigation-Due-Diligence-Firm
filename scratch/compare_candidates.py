import os
from PIL import Image

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

im1 = Image.open(os.path.join(scratch, "confidential_conference.jpg"))
im2 = Image.open(os.path.join(scratch, "team_consultation.jpg"))
im3 = Image.open(os.path.join(scratch, "legal_contract_signature.jpg"))

print("im1 (confidential_conference):", im1.size)
print("im2 (team_consultation):", im2.size)
print("im3 (legal_contract_signature):", im3.size)
