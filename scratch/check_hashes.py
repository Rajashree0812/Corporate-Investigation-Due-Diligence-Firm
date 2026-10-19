import os, hashlib

workspace = r"c:\Users\thand\Desktop\Website"
artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

def get_hash(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# Collect hashes of all images in assets/images
asset_hashes = {}
for root, dirs, files in os.walk(os.path.join(workspace, "assets", "images")):
    for f in files:
        if f.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            p = os.path.join(root, f)
            h = get_hash(p)
            asset_hashes[h] = os.path.relpath(p, workspace)

test_files = [
    "case_scoping_spotlight_1791957173104.jpg",
    "about_advisory_spotlight_1791957294424.jpg",
    "scoping_proposal_1791912865538.jpg",
    "beneficial_ownership_1791905876590.jpg",
    "corp_intel_hero_1791911016830.jpg",
    "financial_fraud_1791883611509.jpg",
    "internal_investigation_1791905942006.jpg",
    "cross_border_ma_1791905904638.jpg",
    "risk_briefing_cta_1791960276856.jpg",
    "investigative_history_archive_1791978075346.jpg"
]

print("=== Comparing Artifacts against All Assets in Website ===")
for tf in test_files:
    p = os.path.join(artifacts_dir, tf)
    if os.path.exists(p):
        h = get_hash(p)
        if h in asset_hashes:
            print(f"MATCH: {tf} is identical to: {asset_hashes[h]}")
        else:
            print(f"UNIQUE (Not in assets): {tf}")
