import os, re
from PIL import Image

# Check all html files and print what images are used in each section of blog-details-ma-diligence.html and blog-details-whistleblower.html
for page in ['blog-details.html', 'blog-details-ma-diligence.html', 'blog-details-whistleblower.html']:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"=== {page} ===")
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', content)
    for img in imgs:
        if not img.endswith('.svg'):
            fp = img.replace('/', os.sep)
            if os.path.exists(fp):
                sz = Image.open(fp).size
                print(f"  {img} (Size: {sz})")
            else:
                print(f"  {img} (MISSING)")
