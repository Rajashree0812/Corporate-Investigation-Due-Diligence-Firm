import glob, re
from collections import defaultdict

files = sorted(glob.glob('*.html'))
img_tag_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

page_images = {}
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    imgs = [m.group(1) for m in img_tag_re.finditer(c) if not any(k in m.group(1).lower() for k in ['logo', 'favicon', 'client'])]
    page_images[f] = imgs

print('=== CROSS-PAGE IMAGE REUSE CHECK ===')
all_content_imgs = defaultdict(list)
for f, imgs in page_images.items():
    for img in imgs:
        all_content_imgs[img].append(f)

for img, p_list in sorted(all_content_imgs.items()):
    if len(p_list) > 1:
        print(f'{img} appears in: {p_list}')
