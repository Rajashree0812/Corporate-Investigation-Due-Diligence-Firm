import os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# -------------------------------------------------------------
# Paths
# -------------------------------------------------------------
workspace = r"c:\Users\thand\Desktop\Website"
template_dir = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"
scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

# Output directories
hero_dir = os.path.join(workspace, "assets", "images", "hero")
blog_dir = os.path.join(workspace, "assets", "images", "blog")
banner_dir = os.path.join(workspace, "assets", "images", "banners")

tmpl_hero_dir = os.path.join(template_dir, "assets", "images", "hero")
tmpl_blog_dir = os.path.join(template_dir, "assets", "images", "blog")
tmpl_banner_dir = os.path.join(template_dir, "assets", "images", "banners")

for d in [hero_dir, blog_dir, banner_dir, tmpl_hero_dir, tmpl_blog_dir, tmpl_banner_dir]:
    os.makedirs(d, exist_ok=True)

# -------------------------------------------------------------
# Fonts setup
# -------------------------------------------------------------
def get_font(name, size):
    font_path = os.path.join(r"C:\Windows\Fonts", name)
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 52)
font_subtitle = get_font("segoeuib.ttf", 36)
font_h2 = get_font("segoeuib.ttf", 30)
font_body_bold = get_font("segoeuib.ttf", 24)
font_body = get_font("segoeui.ttf", 22)
font_mono = get_font("consolab.ttf", 20)
font_small = get_font("segoeui.ttf", 18)
font_small_bold = get_font("segoeuib.ttf", 18)

# -------------------------------------------------------------
# Asset 1: hero-blog-details-ma.jpg (3840 x 2160)
# London River Thames, Tower Bridge, Canary Wharf / City skyline
# -------------------------------------------------------------
print("Building Asset 1: hero-blog-details-ma.jpg...")
src_city = os.path.join(scratch, "blog_city_towers.jpg")
im_city = Image.open(src_city)
# Crop to 16:9 (3840 x 2160) from 3840 x 2560
w, h = im_city.size
target_h = int(w * 9 / 16) # 2160
top_crop = int((h - target_h) * 0.45) # Keep balanced bridge and towers
im_city_cropped = im_city.crop((0, top_crop, w, top_crop + target_h))
im_city_cropped = im_city_cropped.resize((3840, 2160), Image.Resampling.LANCZOS)

# Subtle contrast & atmospheric warmth
im_city_cropped = ImageEnhance.Contrast(im_city_cropped).enhance(1.08)
im_city_cropped = ImageEnhance.Color(im_city_cropped).enhance(1.05)

hero_ma_path = os.path.join(hero_dir, "hero-blog-details-ma.jpg")
im_city_cropped.save(hero_ma_path, "JPEG", quality=95)
shutil.copy2(hero_ma_path, os.path.join(tmpl_hero_dir, "hero-blog-details-ma.jpg"))
print("  Saved Asset 1:", hero_ma_path, im_city_cropped.size)


# -------------------------------------------------------------
# Asset 2: blog-detail-featured-ma.jpg (3840 x 2160)
# Bespoke M&A Risk Architecture & UBO Decomposition Matrix
# -------------------------------------------------------------
print("Building Asset 2: blog-detail-featured-ma.jpg...")
im_ma_diag = Image.new("RGB", (3840, 2160), "#0a121e")
draw_ma = ImageDraw.Draw(im_ma_diag)

# Grid lines background
grid_color = (25, 42, 65)
for x in range(0, 3840, 80):
    draw_ma.line([(x, 0), (x, 2160)], fill=grid_color, width=1)
for y in range(0, 2160, 80):
    draw_ma.line([(0, y), (3840, y)], fill=grid_color, width=1)

# Subtle dark vignette / gradient
overlay = Image.new("RGBA", (3840, 2160), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)
ov_draw.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89, 140), width=3) # Gold border
# Corner brackets
corner_len = 80
bracket_color = (197, 160, 89, 255)
# Top-left
ov_draw.line([(60, 60), (60 + corner_len, 60)], fill=bracket_color, width=6)
ov_draw.line([(60, 60), (60, 60 + corner_len)], fill=bracket_color, width=6)
# Top-right
ov_draw.line([(3780, 60), (3780 - corner_len, 60)], fill=bracket_color, width=6)
ov_draw.line([(3780, 60), (3780, 60 + corner_len)], fill=bracket_color, width=6)
# Bottom-left
ov_draw.line([(60, 2100), (60 + corner_len, 2100)], fill=bracket_color, width=6)
ov_draw.line([(60, 2100), (60, 2100 - corner_len)], fill=bracket_color, width=6)
# Bottom-right
ov_draw.line([(3780, 2100), (3780 - corner_len, 2100)], fill=bracket_color, width=6)
ov_draw.line([(3780, 2100), (3780, 2100 - corner_len)], fill=bracket_color, width=6)

im_ma_diag.paste(Image.alpha_composite(Image.new("RGBA", (3840, 2160), (0,0,0,0)), overlay), (0,0))
draw_ma = ImageDraw.Draw(im_ma_diag)

# Header Section
draw_ma.rectangle([(100, 100), (3740, 260)], fill="#0f1d2e", outline="#c5a059", width=2)
draw_ma.text((140, 125), "VERITAS INTELLIGENCE | TRANSACTION FORENSICS & RISK ADVISORY PRACTICE", font=font_body_bold, fill="#c5a059")
draw_ma.text((140, 165), "FIGURE 1: CROSS-BORDER M&A FORENSIC RISK ARCHITECTURE & UBO DECOMPOSITION MATRIX", font=font_title, fill="#ffffff")

# Status badges top right
draw_ma.rectangle([(3120, 130), (3700, 185)], fill="#b02a37", outline="#dc3545", width=2)
draw_ma.text((3145, 142), "STRICTLY RESTRICTED // DEAL PRIVILEGE", font=font_body_bold, fill="#ffffff")
draw_ma.text((3125, 205), "CASE: M&A-8942-LON | JURISDICTION: CROSS-BORDER UK / EU / BVI", font=font_mono, fill="#98a6b5")

# Center Hierarchy Diagram:
# Level 1: Acquirer
draw_ma.rectangle([(1320, 340), (2520, 500)], fill="#15273e", outline="#c5a059", width=3)
draw_ma.rectangle([(1340, 355), (1500, 390)], fill="#c5a059")
draw_ma.text((1352, 362), "ACQUIRER", font=font_small_bold, fill="#0a121e")
draw_ma.text((1520, 362), "UK PRIVATE EQUITY CONSORTIUM (FUND IX)", font=font_h2, fill="#ffffff")
draw_ma.text((1340, 410), "Primary Deal Vehicle | Capital Allocation: £420M | Transaction Advisory Mandate", font=font_body, fill="#b0c4de")
draw_ma.text((1340, 445), "Verified Compliance Status: CLEAN UBO LINEAGE (100% REGULATORY AUDIT PASS)", font=font_small_bold, fill="#28a745")

# Connection lines from Level 1 to Level 2
draw_ma.line([(1920, 500), (1920, 580)], fill="#c5a059", width=4)
draw_ma.line([(720, 580), (3120, 580)], fill="#c5a059", width=4)

draw_ma.line([(720, 580), (720, 660)], fill="#c5a059", width=4)
draw_ma.line([(1920, 580), (1920, 660)], fill="#c5a059", width=4)
draw_ma.line([(3120, 580), (3120, 660)], fill="#c5a059", width=4)

# Level 2 Boxes (Three Intermediary Vehicles)
# Box 2A (Left): Luxembourg SPV
draw_ma.rectangle([(220, 660), (1220, 960)], fill="#112235", outline="#3b6998", width=2)
draw_ma.rectangle([(240, 680), (460, 715)], fill="#1d4ed8")
draw_ma.text((255, 687), "HOLDING CO. 01", font=font_small_bold, fill="#ffffff")
draw_ma.text((480, 687), "LUXEMBOURG S.À R.L.", font=font_h2, fill="#ffffff")
draw_ma.text((240, 735), "Jurisdiction: Luxembourg (RCS B-204.819) | Share Capital: €12.5M", font=font_body, fill="#cad8e8")
draw_ma.text((240, 775), "Nominee Board: 2 Local Corporate Service Providers", font=font_body, fill="#cad8e8")
draw_ma.rectangle([(240, 825), (1200, 935)], fill="#1a141e", outline="#b02a37", width=2)
draw_ma.text((260, 840), "FORENSIC FINDING // CONCEALED ENCUMBRANCE:", font=font_small_bold, fill="#ff6b6b")
draw_ma.text((260, 875), "Undisclosed share-pledge agreement executed in favour of offshore trust.", font=font_body, fill="#ffc9c9")
draw_ma.text((260, 905), "Pledge triggered automatically upon 50%+ ownership change.", font=font_mono, fill="#fca5a5")

# Box 2B (Center): BVI Nominee Trust
draw_ma.rectangle([(1420, 660), (2420, 960)], fill="#161b2c", outline="#dc3545", width=3)
draw_ma.rectangle([(1440, 680), (1660, 715)], fill="#b02a37")
draw_ma.text((1455, 687), "HIGH RISK SPV", font=font_small_bold, fill="#ffffff")
draw_ma.text((1680, 687), "BVI OFFSHORE VEHICLE", font=font_h2, fill="#ffffff")
draw_ma.text((1440, 735), "Jurisdiction: British Virgin Islands | Reg: BVI-IBC 194820", font=font_body, fill="#cad8e8")
draw_ma.text((1440, 775), "Statutory Ownership: 100% Nominee Bearer Trust Structure", font=font_body, fill="#cad8e8")
draw_ma.rectangle([(1440, 825), (2400, 935)], fill="#2b1115", outline="#dc3545", width=2)
draw_ma.text((1460, 840), "CRITICAL SANCTION ALERT // DIRECT UBO LINK:", font=font_small_bold, fill="#ff4d4f")
draw_ma.text((1460, 875), "Lineage decomposition reveals Tier-1 Sanctioned Person (SDN list)", font=font_body, fill="#ffffff")
draw_ma.text((1460, 905), "holding 42.8% beneficial economic interest via revocable mandate.", font=font_mono, fill="#ff7875")

# Box 2C (Right): Cyprus Debt Conduit
draw_ma.rectangle([(2620, 660), (3620, 960)], fill="#112235", outline="#3b6998", width=2)
draw_ma.rectangle([(2640, 680), (2880, 715)], fill="#d97706")
draw_ma.text((2655, 687), "DEBT CONDUIT", font=font_small_bold, fill="#0a121e")
draw_ma.text((2900, 687), "CYPRUS HOLDINGS LTD", font=font_h2, fill="#ffffff")
draw_ma.text((2640, 735), "Jurisdiction: Nicosia, Cyprus (HE 384912) | Intercompany Lender", font=font_body, fill="#cad8e8")
draw_ma.text((2640, 775), "Purported Function: Treasury & Cross-Border Group Financing", font=font_body, fill="#cad8e8")
draw_ma.rectangle([(2640, 825), (3600, 935)], fill="#261c14", outline="#d97706", width=2)
draw_ma.text((2660, 840), "FINANCIAL FORENSIC FLAG // SUBORDINATED LOAN:", font=font_small_bold, fill="#fbbf24")
draw_ma.text((2660, 875), "£14.2M uncommercial back-to-back loan with 18.5% default penalty", font=font_body, fill="#fde68a")
draw_ma.text((2660, 905), "designed to siphon operating dividends out of target entities.", font=font_mono, fill="#fef08a")

# Connection lines from Level 2 to Level 3
draw_ma.line([(720, 960), (720, 1050)], fill="#3b6998", width=3)
draw_ma.line([(1920, 960), (1920, 1050)], fill="#dc3545", width=4)
draw_ma.line([(3120, 960), (3120, 1050)], fill="#d97706", width=3)

draw_ma.line([(720, 1050), (3120, 1050)], fill="#c5a059", width=4)
draw_ma.line([(1920, 1050), (1920, 1130)], fill="#c5a059", width=4)

# Level 3 Box: Target Operating Companies
draw_ma.rectangle([(920, 1130), (2920, 1370)], fill="#15273e", outline="#c5a059", width=3)
draw_ma.rectangle([(940, 1150), (1180, 1185)], fill="#059669")
draw_ma.text((955, 1157), "TARGET ASSET", font=font_small_bold, fill="#ffffff")
draw_ma.text((1200, 1157), "CONTINENTAL MANUFACTURING & INDUSTRIAL HOLDINGS", font=font_h2, fill="#ffffff")
draw_ma.text((940, 1205), "Operational Footprint: 14 Manufacturing Facilities in Germany, Poland & Czech Republic", font=font_body, fill="#cad8e8")
draw_ma.text((940, 1245), "Reported Financials: €310M Revenue | €42M EBITDA | 2,800 FTE Employees", font=font_body, fill="#cad8e8")
draw_ma.text((940, 1285), "Forensic Liability Exposure: €22.6M Unfunded Environmental Remediation & Unrecorded Pension Deficits", font=font_body_bold, fill="#fbbf24")
draw_ma.text((940, 1325), "LEGAL RECOMMENDATION: ESCROW HOLD-BACK OF £45M + FULL INDEMNITY REQUIRED PRIOR TO CLOSE", font=font_small_bold, fill="#34d399")

# Red Flag Summary Cards (3 Columns across bottom)
y_cards = 1430
card_h = 440

# Card 1: Sanction Risk
draw_ma.rectangle([(140, y_cards), (1280, y_cards + card_h)], fill="#16101a", outline="#dc3545", width=2)
draw_ma.rectangle([(170, y_cards + 25), (420, y_cards + 65)], fill="#dc3545")
draw_ma.text((185, y_cards + 33), "ALERT INDICATOR 01", font=font_small_bold, fill="#ffffff")
draw_ma.text((440, y_cards + 33), "UBO SANCTIONS EXPOSURE", font=font_subtitle, fill="#ffffff")
draw_ma.text((170, y_cards + 85), "Nominee Layering Depth: 6 Levels Across BVI, Cyprus & UAE", font=font_body_bold, fill="#ff7875")
draw_ma.text((170, y_cards + 130), "• Ultimate beneficial owner identified via hidden power of attorney.", font=font_body, fill="#d1d5db")
draw_ma.text((170, y_cards + 175), "• Individual designated under UK OFSI & EU Russia Sanctions Regime.", font=font_body, fill="#d1d5db")
draw_ma.text((170, y_cards + 220), "• Severe OFAC secondary sanctions risk for UK/US lenders in transaction.", font=font_body, fill="#d1d5db")
draw_ma.text((170, y_cards + 270), "DEFENSE ACTION FOR DEAL COUNSEL:", font=font_small_bold, fill="#c5a059")
draw_ma.text((170, y_cards + 310), "Trigger mandatory Section 7 material adverse change termination clause", font=font_body, fill="#f9fafb")
draw_ma.text((170, y_cards + 350), "or require divestment to independent blind trust with OFSI clearance.", font=font_body, fill="#f9fafb")
draw_ma.text((170, y_cards + 395), "RISK RATING: CRITICAL / BLOCKING DEFECT", font=font_mono, fill="#ef4444")

# Card 2: Undisclosed Debt
draw_ma.rectangle([(1340, y_cards), (2480, y_cards + card_h)], fill="#1a1610", outline="#d97706", width=2)
draw_ma.rectangle([(1370, y_cards + 25), (1620, y_cards + 65)], fill="#d97706")
draw_ma.text((1385, y_cards + 33), "ALERT INDICATOR 02", font=font_small_bold, fill="#0a121e")
draw_ma.text((1640, y_cards + 33), "RELATED-PARTY DEBT CONDUIT", font=font_subtitle, fill="#ffffff")
draw_ma.text((1370, y_cards + 85), "Subordinated Intercompany Loan: £14.2M at 18.5% Interest", font=font_body_bold, fill="#fcd34d")
draw_ma.text((1370, y_cards + 130), "• Loan agreement executed 6 weeks prior to auction launch.", font=font_body, fill="#d1d5db")
draw_ma.text((1370, y_cards + 175), "• Onerous acceleration covenant: 100% repayment due upon closing.", font=font_body, fill="#d1d5db")
draw_ma.text((1370, y_cards + 220), "• Siphons 48% of operating free cash flow directly to offshore vendor.", font=font_body, fill="#d1d5db")
draw_ma.text((1370, y_cards + 270), "DEFENSE ACTION FOR DEAL COUNSEL:", font=font_small_bold, fill="#c5a059")
draw_ma.text((1370, y_cards + 310), "Condition completion on full legal novation and debt extinguishment", font=font_body, fill="#f9fafb")
draw_ma.text((1370, y_cards + 350), "without cash leakage; deduct face value from purchase consideration.", font=font_body, fill="#f9fafb")
draw_ma.text((1370, y_cards + 395), "RISK RATING: HIGH / ADJUSTED VALUATION IMPACT", font=font_mono, fill="#f59e0b")

# Card 3: Evidentiary Audit Trail
draw_ma.rectangle([(2540, y_cards), (3680, y_cards + card_h)], fill="#101a14", outline="#059669", width=2)
draw_ma.rectangle([(2570, y_cards + 25), (2820, y_cards + 65)], fill="#059669")
draw_ma.text((2585, y_cards + 33), "AUDIT VERIFICATION", font=font_small_bold, fill="#ffffff")
draw_ma.text((2840, y_cards + 33), "DEFENSIBLE EVIDENTIARY TRAIL", font=font_subtitle, fill="#ffffff")
draw_ma.text((2570, y_cards + 85), "Admissibility Protocol: English Commercial Court & LCIA Admissible", font=font_body_bold, fill="#6ee7b7")
draw_ma.text((2570, y_cards + 130), "• Certified corporate registry gazettes and filings apostilled.", font=font_body, fill="#d1d5db")
draw_ma.text((2570, y_cards + 175), "• Discrete human source interviews across 3 financial hubs.", font=font_body, fill="#d1d5db")
draw_ma.text((2570, y_cards + 220), "• Complete financial ledger reconstruction and bank statement matching.", font=font_body, fill="#d1d5db")
draw_ma.text((2570, y_cards + 270), "DELIVERABLE SPECIFICATION:", font=font_small_bold, fill="#c5a059")
draw_ma.text((2570, y_cards + 310), "Comprehensive Red Flag Due Diligence Dossier + Counsel Affidavit", font=font_body, fill="#f9fafb")
draw_ma.text((2570, y_cards + 350), "supporting warranty & indemnity (W&I) insurance special endorsement.", font=font_body, fill="#f9fafb")
draw_ma.text((2570, y_cards + 395), "VERITAS STATUS: FULL EVIDENTIARY SUBSTANTIATION", font=font_mono, fill="#10b981")

# Footer Bar
draw_ma.rectangle([(100, 1930), (3740, 2040)], fill="#0d1825", outline="#c5a059", width=2)
draw_ma.text((140, 1955), "VERITAS FORENSIC INTEGRITY HASH: SHA-256: 9e4f1a07c3b88d22e091b4fae7264880c59218d6a048731b5c2194e80312", font=font_mono, fill="#94a3b8")
draw_ma.text((140, 1995), "CONFIDENTIAL M&A INTELLIGENCE BRIEFING | AUTHOR: MARCUS VANCE, MANAGING DIRECTOR | VERITAS INTELLIGENCE UK", font=font_small_bold, fill="#c5a059")
draw_ma.text((3100, 1975), "PRACTICE: TRANSACTION FORENSICS // OCTOBER 2026", font=font_body_bold, fill="#ffffff")

feat_ma_path = os.path.join(blog_dir, "blog-detail-featured-ma.jpg")
im_ma_diag.save(feat_ma_path, "JPEG", quality=95)
shutil.copy2(feat_ma_path, os.path.join(tmpl_blog_dir, "blog-detail-featured-ma.jpg"))
print("  Saved Asset 2:", feat_ma_path, im_ma_diag.size)


# -------------------------------------------------------------
# Asset 3: banner-blog-details-ma.jpg (3840 x 2160)
# M&A Financial Intelligence Dashboard & Transaction Analytics
# -------------------------------------------------------------
print("Building Asset 3: banner-blog-details-ma.jpg...")
src_dash = os.path.join(scratch, "financial_dashboard.jpg")
im_dash = Image.open(src_dash)
# Crop to 16:9 (3840 x 2160) from 3840 x 2735
w_fd, h_fd = im_dash.size
target_h_fd = int(w_fd * 9 / 16) # 2160
top_crop_fd = int((h_fd - target_h_fd) * 0.45) # Perfectly frame laptop display & metrics
im_dash_cropped = im_dash.crop((0, top_crop_fd, w_fd, top_crop_fd + target_h_fd))
im_dash_cropped = im_dash_cropped.resize((3840, 2160), Image.Resampling.LANCZOS)

# Sophisticated dark contrast & rich warm corporate grading
im_dash_cropped = ImageEnhance.Contrast(im_dash_cropped).enhance(1.10)
im_dash_cropped = ImageEnhance.Color(im_dash_cropped).enhance(1.05)
im_dash_cropped = ImageEnhance.Brightness(im_dash_cropped).enhance(0.97)

banner_ma_path = os.path.join(banner_dir, "banner-blog-details-ma.jpg")
im_dash_cropped.save(banner_ma_path, "JPEG", quality=95)
shutil.copy2(banner_ma_path, os.path.join(tmpl_banner_dir, "banner-blog-details-ma.jpg"))
print("  Saved Asset 3:", banner_ma_path, im_dash_cropped.size)


# -------------------------------------------------------------
# Asset 4: hero-blog-details-whistleblower.jpg (3840 x 2160)
# Executive Investigation Legal Corridor & Privacy Suite
# -------------------------------------------------------------
print("Building Asset 4: hero-blog-details-whistleblower.jpg...")
src_suite = os.path.join(scratch, "executive_conference_3.jpg")
im_suite = Image.open(src_suite)
# Crop to 16:9 (3840 x 2160) from 3840 x 2563
w_s, h_s = im_suite.size
target_h_s = int(w_s * 9 / 16) # 2160
top_crop_s = int((h_s - target_h_s) * 0.40)
im_suite_cropped = im_suite.crop((0, top_crop_s, w_s, top_crop_s + target_h_s))
im_suite_cropped = im_suite_cropped.resize((3840, 2160), Image.Resampling.LANCZOS)

# Color grade: sophisticated moody architectural tone with rich contrast
im_suite_cropped = ImageEnhance.Contrast(im_suite_cropped).enhance(1.12)
im_suite_cropped = ImageEnhance.Brightness(im_suite_cropped).enhance(0.97)

hero_wb_path = os.path.join(hero_dir, "hero-blog-details-whistleblower.jpg")
im_suite_cropped.save(hero_wb_path, "JPEG", quality=95)
shutil.copy2(hero_wb_path, os.path.join(tmpl_hero_dir, "hero-blog-details-whistleblower.jpg"))
print("  Saved Asset 4:", hero_wb_path, im_suite_cropped.size)


# -------------------------------------------------------------
# Asset 5: blog-detail-featured-whistleblower.jpg (3840 x 2160)
# Digital Evidence Chain-of-Custody & Triaging Matrix
# -------------------------------------------------------------
print("Building Asset 5: blog-detail-featured-whistleblower.jpg...")
im_wb_diag = Image.new("RGB", (3840, 2160), "#0a121c")
draw_wb = ImageDraw.Draw(im_wb_diag)

# Evidentiary grid lines
grid_color_wb = (22, 38, 56)
for x in range(0, 3840, 80):
    draw_wb.line([(x, 0), (x, 2160)], fill=grid_color_wb, width=1)
for y in range(0, 2160, 80):
    draw_wb.line([(0, y), (3840, y)], fill=grid_color_wb, width=1)

# Outer border and brackets
draw_wb.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89), width=3)
# Brackets
for bx, by in [(60, 60), (3780, 60), (60, 2100), (3780, 2100)]:
    dx = corner_len if bx < 1920 else -corner_len
    dy = corner_len if by < 1080 else -corner_len
    draw_wb.line([(bx, by), (bx + dx, by)], fill=(197, 160, 89), width=6)
    draw_wb.line([(bx, by), (bx, by + dy)], fill=(197, 160, 89), width=6)

# Header Section
draw_wb.rectangle([(100, 100), (3740, 260)], fill="#0f1d2e", outline="#c5a059", width=2)
draw_wb.text((140, 125), "VERITAS INTELLIGENCE | SPECIAL INVESTIGATIONS & FORENSIC DIGITAL INTEGRITY", font=font_body_bold, fill="#c5a059")
draw_wb.text((140, 165), "FIGURE 1: DIGITAL EVIDENCE CHAIN-OF-CUSTODY & EPHEMERAL COMMUNICATIONS TRIAGING MATRIX", font=font_title, fill="#ffffff")

draw_wb.rectangle([(3120, 130), (3700, 185)], fill="#0f766e", outline="#14b8a6", width=2)
draw_wb.text((3145, 142), "UPJOHN PRIVILEGE PROTOCOL ACTIVE", font=font_body_bold, fill="#ffffff")
draw_wb.text((3125, 205), "CASE: WB-2026-904 | SPECIAL COMMITTEE MANDATE", font=font_mono, fill="#98a6b5")

# 4 Investigation Pipeline Lanes
lane_w = 840
lane_gap = 60
lane_y = 330
lane_h = 1040

lanes_data = [
    {
        "title": "PHASE 1: SECURE INTAKE",
        "badge": "WHISTLEBLOWER TRIAGING",
        "badge_color": "#d97706",
        "items": [
            ("Secure Intake Channels", "Encrypted portal, whistleblower hotline, or privileged counsel letter."),
            ("Whistleblower Anonymity Firewall", "Identity masked behind blind tokens to prevent corporate reprisal."),
            ("Plausibility & Scope Matrix", "Triaging allegations against FCPA, accounting fraud, or antitrust thresholds."),
            ("Initial Threat Assessment", "Evaluating immediate evidence spoliation and flight risk factors.")
        ],
        "checkpoint": "EVIDENTIARY MANDATE ACTIVATED",
        "cp_color": "#f59e0b"
    },
    {
        "title": "PHASE 2: LEGAL PRIVILEGE",
        "badge": "UPJOHN PROTOCOL FIREWALL",
        "badge_color": "#b02a37",
        "items": [
            ("Special Committee Engagement", "Independent directors retain external counsel and forensic firm."),
            ("Upjohn Warning Execution", "Mandatory warning to employees: privilege belongs to company alone."),
            ("Document Preservation Hold", "Immediate suspension of automated email purging and backup rotations."),
            ("Work-Product Doctrine Shield", "Maintaining strict confidentiality firewall around working notes.")
        ],
        "checkpoint": "ATTORNEY PRIVILEGE SECURED",
        "cp_color": "#ef4444"
    },
    {
        "title": "PHASE 3: FORENSIC MIRRORING",
        "badge": "BITSTREAM ACQUISITION",
        "badge_color": "#1d4ed8",
        "items": [
            ("Hardware Write-Blockers", "Forensic physical acquisition of servers, executive laptops, and phones."),
            ("Ephemeral Telemetry Carving", "Extracting unallocated flash memory for Signal, WhatsApp, and Telegram artifacts."),
            ("Cryptographic Hash Logging", "Dual SHA-256 and MD5 bitstream hashing to guarantee zero tampering."),
            ("Privileged Redaction Matrix", "Keyword indexing filtering out personal and non-relevant employee data.")
        ],
        "checkpoint": "CHAIN-OF-CUSTODY UNBROKEN",
        "cp_color": "#3b82f6"
    },
    {
        "title": "PHASE 4: FINDINGS & RELIEF",
        "badge": "COMMITTEE REPORTING",
        "badge_color": "#059669",
        "items": [
            ("Transactional Corroboration", "Cross-matching chat logs with ERP journal vouchers and bank manifests."),
            ("Defalcation Quantification", "Forensic accounting ledger reconstruction confirming misappropriated funds."),
            ("Oral & Written Deliverable", "Privileged findings presented directly to Board Audit Committee."),
            ("Regulatory Voluntary Disclosure", "DOJ / SFO voluntary self-disclosure strategy to secure declination.")
        ],
        "checkpoint": "DEFENSIBLE RESOLUTION ACHIEVED",
        "cp_color": "#10b981"
    }
]

for idx, lane in enumerate(lanes_data):
    lx = 140 + idx * (lane_w + lane_gap)
    draw_wb.rectangle([(lx, lane_y), (lx + lane_w, lane_y + lane_h)], fill="#111d2c", outline="#2a4365", width=2)
    
    # Header badge
    draw_wb.rectangle([(lx + 20, lane_y + 20), (lx + 320, lane_y + 55)], fill=lane["badge_color"])
    draw_wb.text((lx + 30, lane_y + 27), lane["badge"], font=font_small_bold, fill="#ffffff")
    draw_wb.text((lx + 20, lane_y + 70), lane["title"], font=font_h2, fill="#ffffff")
    
    # Items
    item_y = lane_y + 130
    for header, desc in lane["items"]:
        draw_wb.rectangle([(lx + 20, item_y), (lx + lane_w - 20, item_y + 160)], fill="#0c1624", outline="#1e2e42", width=1)
        draw_wb.text((lx + 35, item_y + 15), header, font=font_body_bold, fill="#c5a059")
        # Split desc across two lines if needed
        words = desc.split(" ")
        line1 = " ".join(words[:len(words)//2 + 2])
        line2 = " ".join(words[len(words)//2 + 2:])
        draw_wb.text((lx + 35, item_y + 55), line1, font=font_body, fill="#cad8e8")
        draw_wb.text((lx + 35, item_y + 90), line2, font=font_body, fill="#cad8e8")
        item_y += 180
    
    # Checkpoint box bottom of lane
    draw_wb.rectangle([(lx + 20, lane_y + lane_h - 100), (lx + lane_w - 20, lane_y + lane_h - 20)], fill="#162335", outline=lane["cp_color"], width=2)
    draw_wb.text((lx + 40, lane_y + lane_h - 68), "[VERIFIED]  " + lane["checkpoint"], font=font_body_bold, fill=lane["cp_color"])

    # Connecting arrows between lanes
    if idx < 3:
        arrow_x = lx + lane_w + 10
        arrow_y = lane_y + int(lane_h / 2)
        draw_wb.line([(arrow_x, arrow_y), (arrow_x + 40, arrow_y)], fill="#c5a059", width=4)
        draw_wb.polygon([(arrow_x + 40, arrow_y - 12), (arrow_x + 40, arrow_y + 12), (arrow_x + 55, arrow_y)], fill="#c5a059")

# Bottom Callout Cards (3 Key Pillars)
y_cards_wb = 1430
card_h_wb = 440

# Pillar 1: Ephemeral Communication Forensics
draw_wb.rectangle([(140, y_cards_wb), (1280, y_cards_wb + card_h_wb)], fill="#16121f", outline="#9333ea", width=2)
draw_wb.rectangle([(170, y_cards_wb + 25), (460, y_cards_wb + 65)], fill="#9333ea")
draw_wb.text((185, y_cards_wb + 33), "TECHNICAL SPECIALTY 01", font=font_small_bold, fill="#ffffff")
draw_wb.text((480, y_cards_wb + 33), "EPHEMERAL MESSAGING CARVING", font=font_subtitle, fill="#ffffff")
draw_wb.text((170, y_cards_wb + 85), "Signal, Telegram & WhatsApp Disappearing Chat Reconstruction", font=font_body_bold, fill="#d8b4fe")
draw_wb.text((170, y_cards_wb + 130), "• Automated message expiry leaves transient database artifacts in cache.", font=font_body, fill="#d1d5db")
draw_wb.text((170, y_cards_wb + 175), "• Deep unallocated flash memory carving recovers deleted chat fragments.", font=font_body, fill="#d1d5db")
draw_wb.text((170, y_cards_wb + 220), "• Reconstructed timelines prove executive collusion and kickback agreements.", font=font_body, fill="#d1d5db")
draw_wb.text((170, y_cards_wb + 270), "DEFENSE VALUE FOR SPECIAL COUNSEL:", font=font_small_bold, fill="#c5a059")
draw_wb.text((170, y_cards_wb + 310), "Refutes employee denials regarding off-channel communications", font=font_body, fill="#f9fafb")
draw_wb.text((170, y_cards_wb + 350), "and satisfies SEC / DOJ guidelines on personal device compliance.", font=font_body, fill="#f9fafb")
draw_wb.text((170, y_cards_wb + 395), "FORENSIC FIDELITY: BITSTREAM RECONSTRUCTION COMPLETE", font=font_mono, fill="#a855f7")

# Pillar 2: Upjohn Warning Standards
draw_wb.rectangle([(1340, y_cards_wb), (2480, y_cards_wb + card_h_wb)], fill="#1a1215", outline="#dc3545", width=2)
draw_wb.rectangle([(1370, y_cards_wb + 25), (1660, y_cards_wb + 65)], fill="#dc3545")
draw_wb.text((1385, y_cards_wb + 33), "LEGAL SAFEGUARD 02", font=font_small_bold, fill="#ffffff")
draw_wb.text((1680, y_cards_wb + 33), "UPJOHN WARNING STANDARDS", font=font_subtitle, fill="#ffffff")
draw_wb.text((1370, y_cards_wb + 85), "Maintaining Company-Held Privilege in Witness Interviews", font=font_body_bold, fill="#fca5a5")
draw_wb.text((1370, y_cards_wb + 130), "• Formal written acknowledgment administered prior to questioning.", font=font_body, fill="#d1d5db")
draw_wb.text((1370, y_cards_wb + 175), "• Clear notice that counsel represents entity, not the individual officer.", font=font_body, fill="#d1d5db")
draw_wb.text((1370, y_cards_wb + 220), "• Prevents employee claims of individual joint defense representation.", font=font_body, fill="#d1d5db")
draw_wb.text((1370, y_cards_wb + 270), "DEFENSE VALUE FOR SPECIAL COUNSEL:", font=font_small_bold, fill="#c5a059")
draw_wb.text((1370, y_cards_wb + 310), "Ensures interview transcripts and findings remain fully under Board control,", font=font_body, fill="#f9fafb")
draw_wb.text((1370, y_cards_wb + 350), "allowing selective waiver for regulatory cooperation or defense litigation.", font=font_body, fill="#f9fafb")
draw_wb.text((1370, y_cards_wb + 395), "PRIVILEGE INTEGRITY: 100% UNASSILABLE PROTOCOL", font=font_mono, fill="#ef4444")

# Pillar 3: Chain-of-Custody Certification
draw_wb.rectangle([(2540, y_cards_wb), (3680, y_cards_wb + card_h_wb)], fill="#0f1915", outline="#059669", width=2)
draw_wb.rectangle([(2570, y_cards_wb + 25), (2880, y_cards_wb + 65)], fill="#059669")
draw_wb.text((2585, y_cards_wb + 33), "CERTIFICATION 03", font=font_small_bold, fill="#ffffff")
draw_wb.text((2900, y_cards_wb + 33), "CHAIN-OF-CUSTODY CERTIFICATE", font=font_subtitle, fill="#ffffff")
draw_wb.text((2570, y_cards_wb + 85), "Federal Rules of Evidence Rule 902(11) & (14) Compliance", font=font_body_bold, fill="#6ee7b7")
draw_wb.text((2570, y_cards_wb + 130), "• Cryptographic SHA-256 fingerprint matching original disk image.", font=font_body, fill="#d1d5db")
draw_wb.text((2570, y_cards_wb + 175), "• Tamper-evident secure physical vault storage for original media.", font=font_body, fill="#d1d5db")
draw_wb.text((2570, y_cards_wb + 220), "• Expert witness qualification and forensic investigator affidavit ready.", font=font_body, fill="#d1d5db")
draw_wb.text((2570, y_cards_wb + 270), "DELIVERABLE SPECIFICATION:", font=font_small_bold, fill="#c5a059")
draw_wb.text((2570, y_cards_wb + 310), "Evidentiary Dossier, Forensic Audit Schedules & Expert Report", font=font_body, fill="#f9fafb")
draw_wb.text((2570, y_cards_wb + 350), "suitable for presentation to High Court, DOJ, SEC, or SFO.", font=font_body, fill="#f9fafb")
draw_wb.text((2570, y_cards_wb + 395), "ADMISSIBILITY STATUS: FULLY DEFENSIBLE AT LAW", font=font_mono, fill="#10b981")

# Footer Bar
draw_wb.rectangle([(100, 1930), (3740, 2040)], fill="#0d1825", outline="#c5a059", width=2)
draw_wb.text((140, 1955), "VERITAS FORENSIC INTEGRITY HASH: SHA-256: 3b7c84910cf2e4a9918bc3d047816f5529a174092b7c419e8512", font=font_mono, fill="#94a3b8")
draw_wb.text((140, 1995), "CONFIDENTIAL SPECIAL INQUIRY BRIEFING | AUTHOR: DAVID THORNE, SENIOR INVESTIGATION COUNSEL | VERITAS INTELLIGENCE UK", font=font_small_bold, fill="#c5a059")
draw_wb.text((3080, 1975), "PRACTICE: SPECIAL INVESTIGATIONS // OCTOBER 2026", font=font_body_bold, fill="#ffffff")

feat_wb_path = os.path.join(blog_dir, "blog-detail-featured-whistleblower.jpg")
im_wb_diag.save(feat_wb_path, "JPEG", quality=95)
shutil.copy2(feat_wb_path, os.path.join(tmpl_blog_dir, "blog-detail-featured-whistleblower.jpg"))
print("  Saved Asset 5:", feat_wb_path, im_wb_diag.size)


# -------------------------------------------------------------
# Asset 6: banner-blog-details-whistleblower.jpg (3840 x 2160)
# Secure Enterprise Server Telemetry Vault & Forensic Data Banks
# -------------------------------------------------------------
print("Building Asset 6: banner-blog-details-whistleblower.jpg...")
src_server = os.path.join(scratch, "wm_cand_12.jpg")
im_server = Image.open(src_server)
# Crop to 16:9 (3840 x 2160) from 4871 x 3513
w_sv, h_sv = im_server.size
target_h_sv = int(w_sv * 9 / 16) # 2740
top_crop_sv = int((h_sv - target_h_sv) * 0.40)
im_server_cropped = im_server.crop((0, top_crop_sv, w_sv, top_crop_sv + target_h_sv))
im_server_cropped = im_server_cropped.resize((3840, 2160), Image.Resampling.LANCZOS)

# Deep moody cyber grading: enhance deep cyan/gold forensic tone
im_server_cropped = ImageEnhance.Contrast(im_server_cropped).enhance(1.12)
im_server_cropped = ImageEnhance.Color(im_server_cropped).enhance(1.05)
im_server_cropped = ImageEnhance.Brightness(im_server_cropped).enhance(0.96)

banner_wb_path = os.path.join(banner_dir, "banner-blog-details-whistleblower.jpg")
im_server_cropped.save(banner_wb_path, "JPEG", quality=95)
shutil.copy2(banner_wb_path, os.path.join(tmpl_banner_dir, "banner-blog-details-whistleblower.jpg"))
print("  Saved Asset 6:", banner_wb_path, im_server_cropped.size)

print("\nALL 6 ASSETS SUCCESSFULLY BUILT AND SYNCHRONIZED!")
