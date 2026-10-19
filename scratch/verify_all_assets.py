import os, glob, re, hashlib
from PIL import Image

ws = r"c:\Users\thand\Desktop\Website"
tmpl = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"

target_assets = [
    ("hero", "hero-blog-details-ma.jpg"),
    ("blog", "blog-detail-featured-ma.jpg"),
    ("banners", "banner-blog-details-ma.jpg"),
    ("hero", "hero-blog-details-whistleblower.jpg"),
    ("blog", "blog-detail-featured-whistleblower.jpg"),
    ("banners", "banner-blog-details-whistleblower.jpg")
]

print("==================================================================")
print("1. VERIFYING TARGET ASSET DIMENSIONS & EXISTENCE (TRUE 4K: 3840x2160)")
print("==================================================================")
all_dimensions_valid = True
for folder, fname in target_assets:
    p_root = os.path.join(ws, "assets", "images", folder, fname)
    p_tmpl = os.path.join(tmpl, "assets", "images", folder, fname)
    
    if not os.path.exists(p_root) or not os.path.exists(p_tmpl):
        print(f"FAILED: Missing file {fname}")
        all_dimensions_valid = False
        continue
    
    im_r = Image.open(p_root)
    im_t = Image.open(p_tmpl)
    
    match = (im_r.size == (3840, 2160)) and (im_t.size == (3840, 2160))
    if not match:
        all_dimensions_valid = False
        print(f"FAILED {fname}: Root size {im_r.size}, Template size {im_t.size}")
    else:
        print(f"PASS [4K 3840x2160]: {fname} (Size: {im_r.size}, Format: {im_r.format}, Mode: {im_r.mode})")

print("Dimensions Check Result:", "ALL VALID" if all_dimensions_valid else "FAILED")

print("\n==================================================================")
print("2. VERIFYING BYTE-FOR-BYTE ROOT <-> TEMPLATE SYNCHRONIZATION")
print("==================================================================")
sync_valid = True
files_to_sync_check = [
    os.path.join("assets", "images", folder, fname) for folder, fname in target_assets
] + ["blog-details-ma-diligence.html", "blog-details-whistleblower.html"]

for rel_path in files_to_sync_check:
    f_root = os.path.join(ws, rel_path)
    f_tmpl = os.path.join(tmpl, rel_path)
    
    with open(f_root, 'rb') as fp:
        md5_r = hashlib.md5(fp.read()).hexdigest()
    with open(f_tmpl, 'rb') as fp:
        md5_t = hashlib.md5(fp.read()).hexdigest()
        
    if md5_r == md5_t:
        print(f"SYNC PASS: {os.path.basename(rel_path)} -> MD5: {md5_r}")
    else:
        print(f"SYNC FAILED: {rel_path} MISMATCH!")
        sync_valid = False

print("\n==================================================================")
print("3. VERIFYING IMAGE UNIQUENESS ACROSS ALL HTML PAGES IN SITE")
print("==================================================================")
html_files = glob.glob(os.path.join(ws, "*.html"))
image_usage = {}

for hf in html_files:
    page_name = os.path.basename(hf)
    with open(hf, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        matches = re.findall(r'assets/images/([a-zA-Z0-9_\-\./]+\.(?:jpg|png|webp|svg|jpeg))', content)
        for m in matches:
            bname = os.path.basename(m)
            # Skip global site brand assets (logos, favicon)
            if bname in ['logo.svg', 'logo-light.svg', 'favicon.svg']:
                continue
            if bname not in image_usage:
                image_usage[bname] = set()
            image_usage[bname].add(page_name)

# Check specifically the 6 target assets
target_basenames = [fname for _, fname in target_assets]
uniqueness_valid = True
for tb in target_basenames:
    pages = image_usage.get(tb, set())
    if len(pages) == 1:
        print(f"UNIQUE PASS: {tb} is used EXCLUSIVELY on page: {list(pages)[0]}")
    elif len(pages) == 0:
        print(f"WARNING: {tb} is not referenced in any HTML file!")
        uniqueness_valid = False
    else:
        print(f"REPETITION DETECTED! {tb} is shared across: {pages}")
        uniqueness_valid = False

# Also check for any cross-page repetitions between blog-details-ma-diligence.html and blog-details-whistleblower.html
ma_images = {bname for bname, pges in image_usage.items() if 'blog-details-ma-diligence.html' in pges}
wb_images = {bname for bname, pges in image_usage.items() if 'blog-details-whistleblower.html' in pges}

# Check team photos (author card)
print(f"\nMA Diligence content images: {ma_images}")
print(f"Whistleblower content images: {wb_images}")
overlap = ma_images.intersection(wb_images)
print(f"Overlap between both new briefing pages: {overlap}")
if len(overlap) == 0:
    print("PASS: ZERO OVERLAP between M&A Diligence and Whistleblower pages!")
else:
    print(f"WARNING: Overlap found: {overlap}")

print("\n==================================================================")
print("4. VISUAL HASH / PERCEPTUAL UNIQUENESS CHECK")
print("==================================================================")
# Ensure none of the 6 target assets is a visual copy of any other image in the site
all_site_images = glob.glob(os.path.join(ws, "assets", "images", "**", "*.*"), recursive=True)
all_site_images = [f for f in all_site_images if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

def get_dhash(img_path, hash_size=8):
    im = Image.open(img_path).convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
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

visual_collision = False
for folder, fname in target_assets:
    target_path = os.path.join(ws, "assets", "images", folder, fname)
    t_hash = get_dhash(target_path)
    
    for other_path in all_site_images:
        if os.path.abspath(other_path) == os.path.abspath(target_path):
            continue
        # Also skip template mirror of the same file
        if os.path.basename(other_path) == fname:
            continue
            
        o_hash = get_dhash(other_path)
        dist = hamming_dist(t_hash, o_hash)
        
        # dhash distance < 4 indicates nearly identical visual content
        if dist < 4:
            print(f"VISUAL DUPLICATE DETECTED! {fname} is visually identical to {os.path.basename(other_path)} (dist={dist})")
            visual_collision = True

if not visual_collision:
    print("PASS: Perceptual hash verification confirmed ALL 6 target images are 100% VISUALLY UNIQUE from all other site images!")
else:
    print("FAIL: Visual collision detected!")

print("\nVERIFICATION COMPLETE!")
