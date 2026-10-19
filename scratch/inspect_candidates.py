import os, glob
from PIL import Image

artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

# Let's inspect images in artifacts
files = [
    "beneficial_ownership_1791905876590.jpg",
    "internal_investigation_1791905942006.jpg",
    "cross_border_ma_1791905904638.jpg",
    "corporate_investigations_1791883501360.jpg",
    "executive_screening_1791883533720.jpg",
    "financial_fraud_1791883611509.jpg",
    "ma_due_diligence_1791883574148.jpg",
    "corp_intel_hero_1791911016830.jpg",
    "scoping_proposal_1791912865538.jpg",
    "services_hero_1791961043460.jpg",
    "service_details_hero_1791961248361.jpg",
    "about_hero_1791960866326.jpg",
    "home_corporate_hero_1791960604778.jpg",
    "about_advisory_spotlight_1791957294424.jpg",
    "case_scoping_spotlight_1791957173104.jpg",
    "transaction_feasibility_1791957393659.jpg",
    "risk_briefing_cta_1791960276856.jpg",
    "newsletter_briefing_1791955826007.jpg",
    "investigative_history_archive_1791978075346.jpg"
]

for fname in files:
    fpath = os.path.join(artifacts_dir, fname)
    if os.path.exists(fpath):
        with Image.open(fpath) as im:
            print(f"{fname}: size={im.size}, mode={im.mode}")
