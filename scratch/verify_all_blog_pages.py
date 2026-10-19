import os, glob, re, hashlib
from PIL import Image

ws = r"c:\Users\thand\Desktop\Website"
tmpl = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"

all_target_assets = [
    # Card 2
    ("hero", "hero-blog-details-ma.jpg"),
    ("blog", "blog-detail-featured-ma.jpg"),
    ("banners", "banner-blog-details-ma.jpg"),
    # Card 3
    ("hero", "hero-blog-details-whistleblower.jpg"),
    ("blog", "blog-detail-featured-whistleblower.jpg"),
    ("banners", "banner-blog-details-whistleblower.jpg"),
    # Card 4
    ("hero", "hero-blog-details-sanctions.jpg"),
    ("blog", "blog-detail-featured-sanctions.jpg"),
    ("banners", "banner-blog-details-sanctions.jpg"),
    # Card 5
    ("hero", "hero-blog-details-osint.jpg"),
    ("blog", "blog-detail-featured-osint.jpg"),
    ("banners", "banner-blog-details-osint.jpg"),
    # Card 6
    ("hero", "hero-blog-details-asset-recovery.jpg"),
    ("blog", "blog-detail-featured-asset-recovery.jpg"),
    ("banners", "banner-blog-details-asset-recovery.jpg")
]

print("==================================================================")
print("1. VERIFYING ALL TARGET ASSET DIMENSIONS (TRUE 4K: 3840x2160)")
print("==================================================================")
all_dim_pass = True
for folder, fname in all_target_assets:
    p_r = os.path.join(ws, "assets", "images", folder, fname)
    p_t = os.path.join(tmpl, "assets", "images", folder, fname)
    
    if not os.path.exists(p_r) or not os.path.exists(p_t):
        print(f"FAILED: Missing {fname}")
        all_dim_pass = False
        continue
    
    im_r = Image.open(p_r)
    im_t = Image.open(p_t)
    
    if im_r.size == (3840, 2160) and im_t.size == (3840, 2160):
        print(f"PASS [4K 3840x2160]: {fname:36s} (Size: {im_r.size}, Format: {im_r.format})")
    else:
        print(f"FAIL: {fname} size root={im_r.size}, tmpl={im_t.size}")
        all_dim_pass = False

print(f"Dimensions Check: {'ALL 15 TARGET ASSETS ARE 4K (3840x2160)' if all_dim_pass else 'FAILED'}")

print("\n==================================================================")
print("2. VERIFYING ROOT <-> TEMPLATE BYTE-FOR-BYTE SYNCHRONIZATION")
print("==================================================================")
all_sync_pass = True
check_files = [
    os.path.join("assets", "images", folder, fname) for folder, fname in all_target_assets
] + [
    "blog.html",
    "blog-details.html",
    "blog-details-ma-diligence.html",
    "blog-details-whistleblower.html",
    "blog-details-sanctions.html",
    "blog-details-osint-litigation.html",
    "blog-details-asset-recovery.html"
]

for rf in check_files:
    fr = os.path.join(ws, rf)
    ft = os.path.join(tmpl, rf)
    
    with open(fr, 'rb') as f1, open(ft, 'rb') as f2:
        m1 = hashlib.md5(f1.read()).hexdigest()
        m2 = hashlib.md5(f2.read()).hexdigest()
    if m1 == m2:
        print(f"SYNC PASS: {os.path.basename(rf):36s} -> MD5: {m1}")
    else:
        print(f"SYNC FAIL: {rf} MISMATCH!")
        all_sync_pass = False

print(f"Sync Check: {'ALL FILES 100% SYNCHRONIZED' if all_sync_pass else 'FAILED'}")

print("\n==================================================================")
print("3. VERIFYING CARD CLICKABILITY & REDIRECTIONS IN BLOG.HTML")
print("==================================================================")
with open(os.path.join(ws, "blog.html"), "r", encoding="utf-8") as fp:
    blog_content = fp.read()

expected_cards = [
    ("Card 1", "blog-details.html", "Uncovering Hidden Beneficial Ownership"),
    ("Card 2", "blog-details-ma-diligence.html", "Red Flags in Cross-Border M&amp;A"),
    ("Card 3", "blog-details-whistleblower.html", "Conducting Defensible Internal Investigations"),
    ("Card 4", "blog-details-sanctions.html", "Navigating Secondary Sanctions"),
    ("Card 5", "blog-details-osint-litigation.html", "The Role of Open-Source Intelligence"),
    ("Card 6", "blog-details-asset-recovery.html", "Tracing Dissipated Sovereign &amp; Corporate Assets")
]

card_blocks = re.findall(r'<div class="col-md-6 col-lg-4 blog-item-col".*?</div>\s*</div>\s*</div>\s*</div>', blog_content, re.DOTALL)
print(f"Found {len(card_blocks)} blog cards in blog.html.")

click_pass = True
for idx, (c_name, exp_target, title_snip) in enumerate(expected_cards):
    card_html = card_blocks[idx]
    has_pos_rel = "card-veritas insight-card position-relative" in card_html
    has_stretched = f'<a href="{exp_target}" class="stretched-link">' in card_html
    has_img_link = f'<a href="{exp_target}"' in card_html
    has_btn = "read-briefing-btn" in card_html
    
    if has_pos_rel and has_stretched and has_img_link and has_btn:
        print(f"CLICK PASS: {c_name} -> points to '{exp_target}' with full-card clickability & stretched-link")
    else:
        print(f"CLICK FAIL: {c_name} (pos_rel={has_pos_rel}, stretched={has_stretched}, img_link={has_img_link}, btn={has_btn})")
        click_pass = False

print(f"Cards Clickability: {'ALL 6 CARDS REDIRECT FULLY TO DEDICATED PAGES' if click_pass else 'FAILED'}")

print("\n==================================================================")
print("4. VISUAL HASH / PERCEPTUAL UNIQUENESS CHECK")
print("==================================================================")
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
for folder, fname in all_target_assets:
    target_path = os.path.join(ws, "assets", "images", folder, fname)
    t_hash = get_dhash(target_path)
    
    for other_path in all_site_images:
        if os.path.abspath(other_path) == os.path.abspath(target_path):
            continue
        if os.path.basename(other_path) == fname:
            continue
            
        o_hash = get_dhash(other_path)
        dist = hamming_dist(t_hash, o_hash)
        
        if dist < 4:
            print(f"VISUAL DUPLICATE! {fname} identical to {os.path.basename(other_path)} (dist={dist})")
            visual_collision = True

if not visual_collision:
    print("PASS: Perceptual hash verification confirmed ALL 15 target images are 100% VISUALLY UNIQUE with ZERO COLLISIONS!")
else:
    print("FAIL: Visual collision detected!")

print("\n==================================================================")
print("VERIFICATION COMPLETE!")
print("==================================================================")
