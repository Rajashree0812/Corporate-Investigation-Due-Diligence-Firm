import glob
import re
from collections import defaultdict
from PIL import Image
import os

html_files = sorted(glob.glob('*.html'))
img_tag_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

by_src = defaultdict(list)
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        for idx, line in enumerate(fp):
            for m in img_tag_re.finditer(line):
                src = m.group(1)
                by_src[src].append((f, idx + 1))

print('=== ALL DUPLICATES (COUNT > 1) ===')
for src, occurrences in sorted(by_src.items(), key=lambda x: len(x[1]), reverse=True):
    if len(occurrences) > 1:
        dim = 'N/A'
        norm = src.replace('/', os.sep)
        if os.path.exists(norm):
            try:
                with Image.open(norm) as im:
                    dim = f'{im.width}x{im.height}'
            except:
                dim = 'SVG/other'
        is_logo = any(k in src.lower() for k in ['logo', 'favicon', 'client', 'blackstone', 'kroll', 'fti', 'pinkerton', 'clifford', 'maersk'])
        print(f'\n{"[LOGO]" if is_logo else "[CONTENT]"} {src} ({len(occurrences)} times, dim={dim}):')
        for f, line_no in occurrences:
            print(f'   - {f}:{line_no}')
