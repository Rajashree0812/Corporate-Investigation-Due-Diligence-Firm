import os, re
from PIL import Image

# 1. Collect all images referenced across all HTML files in Website
used_images = set()
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as hf:
            for m in re.findall(r'assets/images/([^\s"\'\)>]+)', hf.read()):
                used_images.add(os.path.basename(m))

print(f"Total images referenced across all HTML files: {len(used_images)}")

# 2. Check all files in artifacts/
art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'
art_files = [f for f in os.listdir(art_dir) if f.endswith(('.jpg', '.png')) and not f.startswith('media_')]

print(f"\nTotal artifact files: {len(art_files)}")

# 3. Check which images in assets/images or artifacts are NOT in used_images
# Let's inspect their descriptions / prompts and sizes
import json
trans = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript.jsonl'
prompts = {}
with open(trans, 'r', encoding='utf-8') as f:
    for line in f:
        if 'generate_image' in line:
            obj = json.loads(line)
            for c in obj.get('tool_calls', []):
                if c.get('name') == 'generate_image':
                    args = c.get('args', {})
                    prompts[args.get('ImageName', '').strip('"')] = args.get('Prompt', '')

for f in sorted(art_files):
    name = re.sub(r'_\d+\.(jpg|png)$', '', f)
    # Check if this exact file was copied into assets
    # We can check prompt
    p = prompts.get(name, '')
    print(f"ARTIFACT: {f}")
    print(f"   Name: {name} | Size: {Image.open(os.path.join(art_dir, f)).size}")
    print(f"   Prompt: {p[:120]}...\n")
