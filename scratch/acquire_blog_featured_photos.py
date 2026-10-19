import urllib.request
import urllib.parse
import json
import re
import os
from PIL import Image

scratch = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch'
brain_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

def search_unsplash_ids(query, limit=5):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(f"site:unsplash.com/photos {query}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    found = []
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            raw_links = re.findall(r'uddg=([^&"\']+)', html)
            for l in raw_links:
                dec = urllib.parse.unquote(l)
                if 'unsplash.com/photos/' in dec and not '/download' in dec:
                    m = re.search(r'unsplash\.com/photos/(?:[^/]+-)?([a-zA-Z0-9_-]{10,})', dec)
                    if m:
                        pid = m.group(1)
                        if pid not in [x[0] for x in found]:
                            found.append((pid, dec))
                            if len(found) >= limit:
                                break
    except Exception as e:
        print(f"Error searching '{query}': {e}")
    return found

def download_unsplash_4k(pid, out_name):
    url = f"https://images.unsplash.com/{pid}?q=90&w=3840&auto=format&fit=crop"
    dest = os.path.join(scratch, f"{out_name}.jpg")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            with open(dest, 'wb') as f:
                f.write(resp.read())
        im = Image.open(dest)
        print(f"Downloaded {out_name}: {im.size}")
        # Create preview
        thumb = im.copy()
        thumb.thumbnail((800, 450), Image.Resampling.LANCZOS)
        thumb.save(os.path.join(brain_dir, f"preview_{out_name}.jpg"), "JPEG", quality=85)
        return dest
    except Exception as e:
        print(f"Error downloading {pid}: {e}")
        return None

# Search queries for the 5 categories
topics = {
    "ma": "financial audit documents desk spreadsheet glasses calculator",
    "whistleblower": "confidential files archive security office",
    "sanctions": "container cargo ship port aerial terminal",
    "osint": "cyber security intelligence operation screen monitors",
    "asset_recovery": "luxury superyacht marina harbor sunset"
}

results = {}
for key, q in topics.items():
    print(f"\nSearching for {key}: '{q}'...")
    res = search_unsplash_ids(q, limit=4)
    results[key] = res
    for idx, (pid, link) in enumerate(res):
        out_name = f"cand_{key}_{idx+1}"
        download_unsplash_4k(pid, out_name)

print("\nCandidate search & download completed.")
