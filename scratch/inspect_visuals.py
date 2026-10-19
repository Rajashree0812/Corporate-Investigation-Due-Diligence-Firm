import os
from PIL import Image

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
scratch = os.path.join(brain_dir, "scratch")

files = [
    ("confidential_conference.jpg", scratch),
    ("case_files_audit.jpg", scratch),
    ("operations_center_screens.jpg", scratch),
    ("boardroom_strategy.jpg", scratch),
    ("team_consultation.jpg", scratch),
    ("social_network_analysis.png", scratch),
    ("legal_contract_signature.jpg", scratch),
    ("financial_dashboard.jpg", scratch),
    ("forensic_accounting_ledger.jpg", scratch),
    ("internal_investigation_1791905942006.jpg", brain_dir),
    ("cross_border_ma_1791905904638.jpg", brain_dir),
    ("investigative_history_archive_1791978075346.jpg", brain_dir),
    ("corp_intel_hero_1791911016830.jpg", brain_dir)
]

for name, folder in files:
    p = os.path.join(folder, name)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"{name}: size={im.size}, mode={im.mode}")
