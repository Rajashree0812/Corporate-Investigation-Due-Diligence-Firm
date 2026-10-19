import os, json, re
from PIL import Image

trans = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript.jsonl'
art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

prompts = {}
with open(trans, 'r', encoding='utf-8') as f:
    for line in f:
        if 'generate_image' in line:
            obj = json.loads(line)
            for c in obj.get('tool_calls', []):
                if c.get('name') == 'generate_image':
                    args = c.get('args', {})
                    prompts[args.get('ImageName', '').strip('"')] = args.get('Prompt', '')

# Check usage in html
used_in_html = {}
for h in os.listdir('.'):
    if h.endswith('.html'):
        with open(h, 'r', encoding='utf-8') as hf:
            content = hf.read()
            matches = re.findall(r'assets/images/([^\s"\'\)>]+)', content)
            for m in matches:
                b = os.path.basename(m)
                used_in_html.setdefault(b, []).append(h)

print(f"Total HTML files checked: {len([h for h in os.listdir('.') if h.endswith('.html')])}")

print("\n--- NO-HUMAN ARTIFACT CANDIDATES ---")
for f in sorted(os.listdir(art_dir)):
    if f.endswith(('.jpg', '.png')) and not f.startswith('media_'):
        name = re.sub(r'_\d+\.(jpg|png)$', '', f)
        p = prompts.get(name, '')
        has_human_words = any(w in p.lower() for w in ['partner', 'counsel', 'director', 'investigator', 'analyst', 'people', 'person', 'human', 'face', 'hand', 'silhouette', 'executive', 'team', 'men', 'women'])
        no_human_explicit = any(w in p.lower() for w in ['no human', 'no people', 'no face', 'no hand', 'no person', 'empty '])
        if no_human_explicit or not has_human_words:
            fp = os.path.join(art_dir, f)
            sz = Image.open(fp).size
            print(f"FILE: {f} | {sz} | NAME: {name}")
            print(f"PROMPT: {p}\n")
