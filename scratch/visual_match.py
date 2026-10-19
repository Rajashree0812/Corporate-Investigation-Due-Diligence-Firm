import os, hashlib
from PIL import Image

art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

art_files = {}
for f in os.listdir(art_dir):
    if f.endswith(('.jpg', '.png')) and not f.startswith('media_'):
        fp = os.path.join(art_dir, f)
        art_files[f] = Image.open(fp)

# Compare each candidate with all assets
candidates = [
    'fraud_misconduct_4k_1792136137452.jpg',
    'executive_screening_4k_1792136097984.jpg',
    'corporate_investigations_4k_1792136044820.jpg',
    'corporate_intelligence_4k_1792136213605.jpg',
    'litigation_support_4k_1792136426681.jpg',
    'vendor_risk_4k_1792136297422.jpg',
    'asset_tracing_vault_4k_1792136252717.jpg'
]

# Let's find which asset images are closest or identical
for c in candidates:
    im_c = art_files[c].resize((64, 64)).convert('L')
    pixels_c = list(im_c.getdata())
    matched_asset = None
    min_diff = 999999
    for root, dirs, files in os.walk('assets/images'):
        for f in files:
            if f.endswith(('.jpg', '.png')):
                fp = os.path.join(root, f)
                try:
                    im_a = Image.open(fp).resize((64, 64)).convert('L')
                    pixels_a = list(im_a.getdata())
                    diff = sum(abs(p1 - p2) for p1, p2 in zip(pixels_c, pixels_a)) / len(pixels_c)
                    if diff < min_diff:
                        min_diff = diff
                        matched_asset = fp
                except:
                    pass
    print(f"Candidate {c} -> closest asset: {matched_asset} (diff: {min_diff:.2f})")
