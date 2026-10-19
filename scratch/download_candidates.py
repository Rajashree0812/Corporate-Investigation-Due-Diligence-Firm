import urllib.request
import os
from PIL import Image

scratch_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Test downloads of potential 4K aesthetic, zero-human photography
photos = {
    # 01 Consult: Luxury fountain pen on formal legal contract / bilateral agreement (zero humans)
    "consult_pen_contract": "https://images.unsplash.com/photo-1450133064473-71024230f91b?q=90&w=3840&auto=format&fit=crop",
    "consult_fountain_pen": "https://images.unsplash.com/photo-1455390582262-044cdead277a?q=90&w=3840&auto=format&fit=crop",
    
    # 02 Assess: High-tech data triangulation / glowing cyber analytics network / threat radar (zero humans)
    "assess_data_charts": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=90&w=3840&auto=format&fit=crop",
    "assess_cyber_telemetry": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?q=90&w=3840&auto=format&fit=crop",
    "assess_network_nodes": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=90&w=3840&auto=format&fit=crop",
    
    # 03 Investigate: Forensic financial spreadsheet audit / ledger / analysis still life (zero humans)
    "investigate_audit_ledger": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=90&w=3840&auto=format&fit=crop",
    "investigate_magnifier_docs": "https://images.unsplash.com/photo-1586281380349-632531db7ed4?q=90&w=3840&auto=format&fit=crop",
    
    # 04 Report: Executive court gavel & legal briefs / luxury boardroom debrief suite (zero humans)
    "report_gavel_brief": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=90&w=3840&auto=format&fit=crop",
    "report_boardroom_luxury": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?q=90&w=3840&auto=format&fit=crop"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in photos.items():
    dest = os.path.join(scratch_dir, f"{name}.jpg")
    if not os.path.exists(dest):
        try:
            print(f"Downloading {name}...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
                f.write(resp.read())
            with Image.open(dest) as im:
                print(f"  -> Success: {name} ({im.size})")
        except Exception as e:
            print(f"  -> Error {name}: {e}")
    else:
        with Image.open(dest) as im:
            print(f"Already exists: {name} ({im.size})")
