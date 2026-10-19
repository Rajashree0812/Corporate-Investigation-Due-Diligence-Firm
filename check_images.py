import glob
import re

seen = set()
for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    for m in re.finditer(r'<img[^>]+>', content):
        tag = m.group(0)
        src_match = re.search(r'src=["\']([^"\']+)["\']', tag)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', tag)
        if src_match:
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else ''
            if src not in seen:
                seen.add(src)
                print(f'{src} -> {alt}')
