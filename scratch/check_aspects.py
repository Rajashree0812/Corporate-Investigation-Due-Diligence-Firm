import os
from PIL import Image

artifacts_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"

# Let's check aspect ratios and dimensions of the chosen candidates:
# 1. Consult: scoping_proposal_1791912865538.jpg (1200, 896) or case_scoping_spotlight_1791957173104.jpg (1200, 896)
# 2. Assess: beneficial_ownership_1791905876590.jpg (1376, 768)
# 3. Investigate: internal_investigation_1791905942006.jpg (1376, 768)
# 4. Report: risk_briefing_cta_1791960276856.jpg (1200, 896) or cross_border_ma_1791905904638.jpg (1376, 768)

candidates = {
    "consult_scoping": os.path.join(artifacts_dir, "scoping_proposal_1791912865538.jpg"),
    "consult_case": os.path.join(artifacts_dir, "case_scoping_spotlight_1791957173104.jpg"),
    "assess_beneficial": os.path.join(artifacts_dir, "beneficial_ownership_1791905876590.jpg"),
    "investigate_internal": os.path.join(artifacts_dir, "internal_investigation_1791905942006.jpg"),
    "investigate_fraud": os.path.join(artifacts_dir, "financial_fraud_1791883611509.jpg"),
    "report_risk": os.path.join(artifacts_dir, "risk_briefing_cta_1791960276856.jpg"),
    "report_ma": os.path.join(artifacts_dir, "cross_border_ma_1791905904638.jpg")
}

for k, v in candidates.items():
    if os.path.exists(v):
        with Image.open(v) as im:
            print(f"{k}: size={im.size}, aspect={im.width/im.height:.3f}")
