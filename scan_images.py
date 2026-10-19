import glob
import re
import os
from collections import defaultdict

html_files = sorted(glob.glob('*.html'))
print(f'Total HTML files in root: {len(html_files)}')

img_src_counts = defaultdict(list)
bg_img_counts = defaultdict(list)

img_tag_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
bg_re = re.compile(r'url\(["\']?([^"\'\)]+)["\']?\)', re.IGNORECASE)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # img tags
    for m in img_tag_re.finditer(content):
        src = m.group(1)
        tag_str = m.group(0)[:140]
        # extract alt attribute if present
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', tag_str, re.IGNORECASE)
        alt = alt_match.group(1) if alt_match else 'no-alt'
        img_src_counts[src].append((f, alt, tag_str))
        
    # inline style background images
    for m in bg_re.finditer(content):
        src = m.group(1)
        if any(src.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg']):
            bg_img_counts[src].append((f, m.group(0)))

print('\n=============================================')
print('IMAGE USAGE AUDIT')
print('=============================================')

content_images_multi = []
logos_multi = []

for src, uses in sorted(img_src_counts.items(), key=lambda x: len(x[1]), reverse=True):
    is_logo = any(k in src.lower() for k in ['logo', 'favicon', 'client', 'blackstone', 'kroll', 'fti', 'pinkerton', 'clifford', 'maersk'])
    if len(uses) > 1:
        if is_logo:
            logos_multi.append((src, len(uses)))
        else:
            content_images_multi.append((src, uses))

print(f'\n[LOGOS & BRAND ICONS repeated across pages] ({len(logos_multi)}):')
for src, count in logos_multi:
    print(f'  - {src}: {count} occurrences')

print(f'\n[CONTENT IMAGES REPEATED ACROSS MULTIPLE PLACES] ({len(content_images_multi)}):')
for src, uses in content_images_multi:
    print(f'\n>>> Image: {src} (Used {len(uses)} times):')
    for f, alt, tag in uses:
        print(f'    * Page: {f} | Alt: "{alt}"')

print(f'\n[UNIQUE CONTENT IMAGES] ({len([s for s, u in img_src_counts.items() if len(u) == 1])}):')
for src, uses in sorted(img_src_counts.items()):
    if len(uses) == 1:
        f, alt, _ = uses[0]
        print(f'  - {src} (1x in {f})')
