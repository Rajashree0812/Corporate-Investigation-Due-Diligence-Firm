import os
import hashlib
from collections import defaultdict

images_dir = 'assets/images'
hashes = defaultdict(list)

for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg')):
            filepath = os.path.join(root, f)
            with open(filepath, 'rb') as fp:
                data = fp.read()
            h = hashlib.sha256(data).hexdigest()
            size = len(data)
            hashes[(h, size)].append(filepath)

print('=== IDENTICAL IMAGE FILES ON DISK (Same content hash) ===')
duplicates_found = 0
for (h, size), filelist in hashes.items():
    if len(filelist) > 1:
        # Check if they are just client logos or identical content images
        print(f'\nDuplicate hash {h[:12]} ({size} bytes):')
        for p in filelist:
            print(f'   - {p}')
        duplicates_found += 1

print(f'\nTotal duplicate image clusters on disk: {duplicates_found}')
