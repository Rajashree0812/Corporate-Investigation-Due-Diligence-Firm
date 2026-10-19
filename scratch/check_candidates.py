import os, glob
from PIL import Image

scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"
brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

candidates = [
    'contract_deal_review.jpg',
    'blog_legal_documents.jpg',
    'towers_reflection.jpg',
    'first_national_bank.jpg',
    'case_files_audit.jpg',
    'confidential_conference.jpg'
]

# Check if used anywhere in Website/assets/images
assets_images = glob.glob(r"c:\Users\thand\Desktop\Website\assets\images\**\*.*", recursive=True)
asset_basenames = {os.path.basename(f) for f in assets_images}

print("Checking candidate files:")
for c in candidates:
    src_p = os.path.join(scratch, c)
    im = Image.open(src_p)
    # create preview in brain_dir
    prev_path = os.path.join(brain_dir, f"preview_{c}")
    im_thumb = im.copy()
    im_thumb.thumbnail((800, 450), Image.Resampling.LANCZOS)
    im_thumb.save(prev_path, "JPEG", quality=85)
    in_assets = c in asset_basenames
    print(f"  {c}: size={im.size}, saved preview to {prev_path}, in_assets={in_assets}")
