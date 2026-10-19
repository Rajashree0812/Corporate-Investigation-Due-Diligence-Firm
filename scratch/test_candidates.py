import os
from PIL import Image

art_dir = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e'

# Let's inspect which images have humans vs no humans by checking prompts and visual inspection
files = [
    'banner_404.jpg',
    'transaction_feasibility_1791957393659.jpg',
    'scoping_proposal_1791912865538.jpg',
    'risk_briefing_cta_1791960276856.jpg',
    'blog_mandate_cta_1791957823858.jpg',
    'about_advisory_spotlight_1791957294424.jpg',
    'case_scoping_spotlight_1791957173104.jpg',
    'home_corporate_hero_1791960604778.jpg',
    'financial_fraud_1791883611509.jpg',
    'ma_due_diligence_1791883574148.jpg',
    'cross_border_ma_1791905904638.jpg',
    'internal_investigation_1791905942006.jpg'
]

for f in files:
    fp = os.path.join(art_dir, f) if f != 'banner_404.jpg' else 'assets/images/banners/banner-404.jpg'
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"{f}: {im.size}")
