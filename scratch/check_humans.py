import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Check if there are any people or hands in legal_contract_signature.jpg or 4k_consult_fountain_pen.jpg
# We can check description or inspect center/edges
with open(os.path.join(scratch_dir, "check_desc.txt"), "w") as fp:
    fp.write("Checking...")

print("Both are available. Let's inspect 4k_consult_fountain_pen.jpg:")
with Image.open(os.path.join(scratch_dir, "consult_fountain_pen.jpg")) as im:
    print(f"consult_fountain_pen: {im.size}")

with Image.open(os.path.join(scratch_dir, "legal_contract_signature.jpg")) as im:
    print(f"legal_contract_signature: {im.size}")
