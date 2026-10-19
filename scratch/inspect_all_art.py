import os, re
from PIL import Image

# Let's inspect all artifact files and see what they depict
art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

# Let's inspect all candidates
for f in sorted(os.listdir(art_dir)):
    if f.endswith(('.jpg', '.png')) and not f.startswith('media_'):
        fp = os.path.join(art_dir, f)
        im = Image.open(fp)
        print(f"{f}: {im.size} (aspect: {im.size[0]/im.size[1]:.2f})")
