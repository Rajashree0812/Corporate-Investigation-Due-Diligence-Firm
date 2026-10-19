import os
from PIL import Image

images_dir = 'assets/images'
print('=== RESOLUTION AUDIT FOR ALL IMAGES IN ASSETS/IMAGES ===')

low_res = []
for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            filepath = os.path.join(root, f)
            try:
                with Image.open(filepath) as im:
                    w, h = im.width, im.height
                    # 4K standard is 3840 wide (or 2160+ for portrait/square)
                    is_4k = (w >= 3840 or h >= 2160 or (w >= 2160 and h >= 2160))
                    if not is_4k:
                        low_res.append((filepath, f'{w}x{h}', os.path.getsize(filepath)))
            except Exception as e:
                print(f'Error reading {filepath}: {e}')

print(f'\nTotal images below 4K resolution (w < 3840 and h < 2160): {len(low_res)}')
for p, res, sz in sorted(low_res, key=lambda x: x[0]):
    print(f'  - {p}: {res} ({sz} bytes)')
