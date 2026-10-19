import re

for page in ['blog-details-ma-diligence.html', 'blog-details-whistleblower.html']:
    print(f'=== {page} ===')
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', c):
        print('IMG:', m.group(0))
    for m in re.finditer(r'url\(["\']?([^"\'\)]+)["\']?\)', c):
        print('CSS URL:', m.group(1))
