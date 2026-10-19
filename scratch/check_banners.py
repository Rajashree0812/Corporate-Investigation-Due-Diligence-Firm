import os, re

banners = {}
for h in os.listdir('.'):
    if h.endswith('.html'):
        with open(h, 'r', encoding='utf-8') as f:
            c = f.read()
        for m in re.findall(r'assets/images/banners/[^"\'\>\s]+', c):
            banners.setdefault(m, set()).add(h)

for b, pages in sorted(banners.items()):
    print(f'{b} -> {pages}')
