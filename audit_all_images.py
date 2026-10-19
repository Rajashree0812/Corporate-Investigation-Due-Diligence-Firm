import glob
import re
import os
from PIL import Image

html_files = sorted(glob.glob('*.html'))
img_tag_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

records = []
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        for m in img_tag_re.finditer(line):
            src = m.group(1)
            tag_str = m.group(0)
            alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag_str, re.IGNORECASE)
            alt = alt_m.group(1) if alt_m else ''
            
            # get image dimensions if file exists
            norm_src = src.replace('/', os.sep)
            dim = 'N/A'
            fsize = 0
            if os.path.exists(norm_src):
                fsize = os.path.getsize(norm_src)
                try:
                    with Image.open(norm_src) as im:
                        dim = f'{im.width}x{im.height}'
                except Exception:
                    dim = 'vector/error'

            records.append({
                'file': f,
                'line': idx + 1,
                'src': src,
                'alt': alt,
                'dim': dim,
                'size': fsize
            })

print(f'Total img elements in project: {len(records)}')

# Group by normalized src
by_src = {}
for r in records:
    by_src.setdefault(r['src'], []).append(r)

print('\n=== ALL IMAGES AND OCCURRENCE COUNTS ===')
for src, recs in sorted(by_src.items(), key=lambda x: len(x[1]), reverse=True):
    is_logo = any(k in src.lower() for k in ['logo', 'favicon', 'client', 'blackstone', 'kroll', 'fti', 'pinkerton', 'clifford', 'maersk'])
    print(f'Count {len(recs):2d} | Dim: {recs[0]["dim"]:11s} | {"[LOGO]" if is_logo else "[IMG] "} {src}')
