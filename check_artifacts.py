import os, json

artifact_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'
transcript_path = os.path.join(artifact_dir, r'.system_generated\logs\transcript_full.jsonl')

name_to_prompt = {}
if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                for c in data.get('tool_calls', []):
                    if c.get('name') == 'generate_image':
                        args = c.get('args', {})
                        n = args.get('ImageName')
                        p = args.get('Prompt')
                        if n and p:
                            name_to_prompt[n] = p
            except:
                pass

for f in sorted(os.listdir(artifact_dir)):
    if f.endswith('.jpg'):
        base = f.split('_179')[0]
        prompt = name_to_prompt.get(base, 'NO PROMPT RECORDED')
        print(f'{f} ({base}) -> {prompt[:100]}...')
