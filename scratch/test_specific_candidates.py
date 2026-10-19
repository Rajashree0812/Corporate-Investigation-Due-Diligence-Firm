import os, glob
from PIL import Image

ws = r"c:\Users\thand\Desktop\Website"
scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# All site images
all_site_images = glob.glob(os.path.join(ws, "assets", "images", "**", "*.*"), recursive=True)
all_site_images = [f for f in all_site_images if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

targets = {
    "hero-blog-details-ma.jpg",
    "blog-detail-featured-ma.jpg",
    "banner-blog-details-ma.jpg",
    "hero-blog-details-whistleblower.jpg",
    "blog-detail-featured-whistleblower.jpg",
    "banner-blog-details-whistleblower.jpg"
}
base_site_images = [f for f in all_site_images if os.path.basename(f) not in targets]

def get_dhash(img_path_or_obj, hash_size=8):
    if isinstance(img_path_or_obj, str):
        im = Image.open(img_path_or_obj)
    else:
        im = img_path_or_obj
    im = im.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
    pixels = list(im.getdata())
    diff = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = pixels[row * (hash_size + 1) + col]
            pixel_right = pixels[row * (hash_size + 1) + col + 1]
            diff.append(pixel_left > pixel_right)
    return diff

def hamming_dist(h1, h2):
    return sum(b1 != b2 for b1, b2 in zip(h1, h2))

site_hashes = {sf: get_dhash(sf) for sf in base_site_images}

candidates = [
    'wm_cand_12.jpg',
    'wm_cand_18.jpg',
    'financial_dashboard.jpg',
    'towers_reflection.jpg',
    'executive_conference_3.jpg',
    'confidential_conference.jpg',
    'candlestick_screen.jpg',
    'first_national_bank.jpg',
    'crop_opt1_bottom.jpg',
    'safe_deposit_vault.jpg'
]

print("Checking specific candidates against ALL site images:")
for c in candidates:
    cp = os.path.join(scratch, c)
    if not os.path.exists(cp):
        continue
    c_hash = get_dhash(cp)
    min_dist = 999
    closest = ""
    for sf, sh in site_hashes.items():
        d = hamming_dist(c_hash, sh)
        if d < min_dist:
            min_dist = d
            closest = os.path.basename(sf)
    print(f"  {c:30s} -> Min Dist = {min_dist:2d} (Closest: {closest})")
