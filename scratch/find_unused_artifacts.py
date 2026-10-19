import os
from PIL import Image

art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

# Load thumbnail of all assets in assets/images
asset_thumbs = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith(('.jpg', '.png')) and not f.startswith(('hero-blog-details-ma', 'blog-detail-featured-ma', 'hero-blog-details-whistleblower', 'blog-detail-featured-whistleblower')):
            fp = os.path.join(root, f)
            try:
                im = Image.open(fp).resize((64, 64)).convert('L')
                asset_thumbs[fp] = list(im.getdata())
            except:
                pass

print(f"Loaded {len(asset_thumbs)} asset image fingerprints.")

# Now check all artifacts
art_files = [f for f in os.listdir(art_dir) if f.endswith(('.jpg', '.png')) and not f.startswith('media_')]

completely_unused = []
used_matches = []

for af in art_files:
    af_path = os.path.join(art_dir, af)
    try:
        im = Image.open(af_path).resize((64, 64)).convert('L')
        pix = list(im.getdata())
        min_diff = 999999
        best_match = None
        for fp, apix in asset_thumbs.items():
            diff = sum(abs(a - b) for a, b in zip(pix, apix)) / len(pix)
            if diff < min_diff:
                min_diff = diff
                best_match = fp
        if min_diff < 5.0: # Close match (upscaled or identical)
            used_matches.append((af, best_match, min_diff))
        else:
            completely_unused.append((af, min_diff, best_match))
    except Exception as e:
        print(f"Error {af}: {e}")

print(f"\nCOMPLETELY UNUSED ARTIFACTS ({len(completely_unused)}):")
for af, diff, best in completely_unused:
    print(f"  {af} (min_diff: {diff:.2f} vs {best})")

print(f"\nMATCHED/USED ARTIFACTS ({len(used_matches)}):")
for af, best, diff in used_matches:
    print(f"  {af} -> {best} (diff: {diff:.2f})")
