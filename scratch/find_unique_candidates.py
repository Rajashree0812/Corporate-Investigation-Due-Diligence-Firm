import os, glob
from PIL import Image

ws = r"c:\Users\thand\Desktop\Website"
scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# All existing images in assets/images/
all_site_images = glob.glob(os.path.join(ws, "assets", "images", "**", "*.*"), recursive=True)
all_site_images = [f for f in all_site_images if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Exclude our 6 target files from site comparison so we compare candidates against all OTHER site images
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

site_hashes = {}
for sf in base_site_images:
    site_hashes[sf] = get_dhash(sf)

print(f"Loaded {len(site_hashes)} site image hashes.")

# Now check all images in scratch
scratch_files = glob.glob(os.path.join(scratch, "*.*"))
scratch_files = [f for f in scratch_files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

truly_unique = []
for sc in scratch_files:
    try:
        sc_im = Image.open(sc)
        if sc_im.width < 1200 or sc_im.height < 600:
            continue
        sc_hash = get_dhash(sc_im)
        min_dist = 999
        closest_img = ""
        for sf, shash in site_hashes.items():
            d = hamming_dist(sc_hash, shash)
            if d < min_dist:
                min_dist = d
                closest_img = os.path.basename(sf)
        
        # If min_dist >= 10, it is visually very different from everything on site
        if min_dist >= 8:
            truly_unique.append((min_dist, sc, sc_im.size, closest_img))
    except Exception as e:
        pass

truly_unique.sort(key=lambda x: x[0], reverse=True)
print(f"\nFound {len(truly_unique)} scratch images with min distance >= 8:")
for dist, path, size, closest in truly_unique[:30]:
    print(f"  Dist={dist:2d} | Size={size} | Closest={closest} | File={os.path.basename(path)}")
