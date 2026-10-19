import glob
import re
from collections import defaultdict

html_files = sorted(glob.glob('*.html'))
img_src_counts = defaultdict(list)
img_tag_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    for m in img_tag_re.finditer(content):
        src = m.group(1)
        tag_str = m.group(0)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', tag_str, re.IGNORECASE)
        alt = alt_match.group(1) if alt_match else 'no-alt'
        img_src_counts[src].append((f, alt, tag_str[:160]))

print('=== REPEATED CONTENT IMAGES ===')
repeated_count = 0
for src, uses in sorted(img_src_counts.items(), key=lambda x: len(x[1]), reverse=True):
    is_logo = any(k in src.lower() for k in ['logo', 'favicon', 'client', 'blackstone', 'kroll', 'fti', 'pinkerton', 'clifford', 'maersk'])
    if len(uses) > 1 and not is_logo:
        repeated_count += 1
        print(f'\n[REPEATED] {src} (Used {len(uses)} times):')
        for f, alt, tag in uses:
            print(f'   -> File: {f}')
            print(f'      Alt: "{alt}"')

print(f'\nTotal non-logo repeated image sources: {repeated_count}')
