import urllib.request
import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Curated 4K zero-human, highly aesthetic assets for the 4 industry sectors:
sector_candidates = {
    # 1. Banking & FinTech: High-tech digital crypto / financial technology / blockchain token architecture
    "sector_fintech": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?q=90&w=3840&auto=format&fit=crop",
    "sector_fintech_alt": "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?q=90&w=3840&auto=format&fit=crop",
    
    # 2. Energy & Infrastructure: Majestic modern wind turbines / clean energy infrastructure at sunset
    "sector_energy": "https://images.unsplash.com/photo-1466611653911-95081537e5b7?q=90&w=3840&auto=format&fit=crop",
    
    # 3. Life Sciences & Pharma: Precision laboratory glassware, scientific research vials in blue lighting
    "sector_pharma": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?q=90&w=3840&auto=format&fit=crop",
    
    # 4. Aerospace & Defense: Jet turbine aerospace propulsion / stealth aerospace engineering
    "sector_aerospace": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?q=90&w=3840&auto=format&fit=crop",
    "sector_aerospace_alt": "https://images.unsplash.com/photo-1517976487507-5b3a4a080c5e?q=90&w=3840&auto=format&fit=crop"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in sector_candidates.items():
    dest = os.path.join(scratch_dir, f"{name}.jpg")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        with Image.open(dest) as im:
            print(f"Success: {name} ({im.size})", flush=True)
    except Exception as e:
        print(f"Error {name}: {e}", flush=True)
