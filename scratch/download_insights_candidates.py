import urllib.request
import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Test downloads of high-aesthetic, zero-human 4K photography for the 3 insight cards:
candidates = {
    # 1. Sanctions Risk & Maritime Transshipment: Aerial / open sea container cargo vessel
    "sanctions_cargo_vessel": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=90&w=3840&auto=format&fit=crop",
    "sanctions_port_terminal": "https://images.unsplash.com/photo-1578575437130-527eed3abbec?q=90&w=3840&auto=format&fit=crop",
    
    # 2. OSINT & Commercial Litigation: Digital network intelligence, OSINT digital breadcrumbs, cyber terminal
    "osint_cyber_matrix": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=90&w=3840&auto=format&fit=crop",
    "osint_data_network": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=90&w=3840&auto=format&fit=crop",
    "osint_digital_code": "https://images.unsplash.com/photo-1510511459019-5dee997ddfef?q=90&w=3840&auto=format&fit=crop",
    
    # 3. Asset Tracing & Sovereign Asset Recovery: High-security modern vault / bullion / safe deposit boxes
    "asset_tracing_vault_door": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?q=90&w=3840&auto=format&fit=crop",
    "asset_tracing_gold_bars": "https://images.unsplash.com/photo-1610375461246-83df859d849d?q=90&w=3840&auto=format&fit=crop",
    "asset_tracing_deposit_boxes": "https://images.unsplash.com/photo-1501167786227-4cba60f6d58f?q=90&w=3840&auto=format&fit=crop"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in candidates.items():
    dest = os.path.join(scratch_dir, f"{name}.jpg")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        with Image.open(dest) as im:
            print(f"Success: {name} ({im.size})", flush=True)
    except Exception as e:
        print(f"Error {name}: {e}", flush=True)
