import os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# -------------------------------------------------------------
# Paths
# -------------------------------------------------------------
workspace = r"c:\Users\thand\Desktop\Website"
template_dir = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"
scratch = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch"

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

font_title = get_font("segoeuib.ttf", 48)
font_subtitle = get_font("segoeuib.ttf", 34)
font_h2 = get_font("segoeuib.ttf", 28)
font_body_bold = get_font("segoeuib.ttf", 22)
font_body = get_font("segoeui.ttf", 20)
font_mono = get_font("consolab.ttf", 19)
font_small = get_font("segoeui.ttf", 17)
font_small_bold = get_font("segoeuib.ttf", 17)

def save_dual(im, folder_type, fname):
    r_path = os.path.join(workspace, "assets", "images", folder_type, fname)
    t_path = os.path.join(template_dir, "assets", "images", folder_type, fname)
    im.save(r_path, "JPEG", quality=95)
    shutil.copy2(r_path, t_path)
    print(f"Saved {fname} ({im.size}) to root and template.")

def crop_and_scale_4k(src_path, top_bias=0.5):
    im = Image.open(src_path)
    w, h = im.size
    th = int(w * 9 / 16)
    if th <= h:
        top = int((h - th) * top_bias)
        im_c = im.crop((0, top, w, top + th))
    else:
        tw = int(h * 16 / 9)
        left = int((w - tw) * 0.5)
        im_c = im.crop((left, 0, left + tw, h))
    return im_c.resize((3840, 2160), Image.Resampling.LANCZOS)

# ==============================================================================
# 1. CARD 4: SANCTIONS & THIRD-PARTY VENDOR RISK
# ==============================================================================
print("\n--- Generating Card 4 Assets (Sanctions & Third-Party Vendor Risk) ---")

# Hero: container_ship_sea.jpg (5280 x 3956 -> 3840 x 2160)
print("1.1 Hero: hero-blog-details-sanctions.jpg")
im_hero_sanc = crop_and_scale_4k(os.path.join(scratch, "container_ship_sea.jpg"), top_bias=0.35)
im_hero_sanc = ImageEnhance.Contrast(im_hero_sanc).enhance(1.05)
save_dual(im_hero_sanc, "hero", "hero-blog-details-sanctions.jpg")

# Featured Diagram: blog-detail-featured-sanctions.jpg
print("1.2 Featured Diagram: blog-detail-featured-sanctions.jpg")
im_sanc_diag = Image.new("RGB", (3840, 2160), "#0a121e")
draw_sanc = ImageDraw.Draw(im_sanc_diag)

# Grid
for x in range(0, 3840, 80):
    draw_sanc.line([(x, 0), (x, 2160)], fill=(22, 38, 60), width=1)
for y in range(0, 2160, 80):
    draw_sanc.line([(0, y), (3840, y)], fill=(22, 38, 60), width=1)

# Outer frame & corner brackets
draw_sanc.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89, 160), width=3)
c_len = 80
gold_b = (197, 160, 89)
for cx, cy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_sanc.line([(cx, cy), (cx + dx * c_len, cy)], fill=gold_b, width=6)
    draw_sanc.line([(cx, cy), (cx, cy + dy * c_len)], fill=gold_b, width=6)

# Header block
draw_sanc.rectangle([(120, 110), (3720, 240)], fill=(14, 25, 42), outline=(197, 160, 89, 120), width=2)
draw_sanc.text((150, 130), "FIGURE 1: MULTI-TIER SECONDARY SANCTIONS EVASION & TRANSSHIPMENT INTERMEDIARY MATRIX", fill=(245, 245, 245), font=font_title)
draw_sanc.text((150, 195), "VERITAS INTELLIGENCE COMPLIANCE & REGULATORY TELEMETRY  |  CLASSIFICATION: FORENSIC INVESTIGATIVE PROTOCOL  |  OCTOBER 2026", fill=(197, 160, 89), font=font_mono)

# 4 Operational Lanes across width (columns from left to right)
lane_data_sanc = [
    {
        "col": 0,
        "title": "TIER 1: ORIGIN & BENEFICIARY",
        "badge": "[PROHIBITED EXPORTER]",
        "badge_color": (220, 53, 69),
        "steps": [
            ("Sanctioned Manufacturer", "Tier-1 military/aerospace dual-use producer in blocked territory."),
            ("Concealed Ultimate Principal", "OFAC SDN Listed beneficial owner holding 50%+ hidden equity."),
            ("Nominee Front Contract", "Commercial invoice issued through shell LLC with fabricated destination."),
            ("Capital Sourcing Vector", "Cryptographic clearing & offshore escrow in non-FATF jurisdiction.")
        ]
    },
    {
        "col": 1,
        "title": "TIER 2: TRANSSHIPMENT CONDUITS",
        "badge": "[FREE TRADE ZONE HUB]",
        "badge_color": (255, 193, 7),
        "steps": [
            ("Re-Export Logistic Center", "Goods transit customs-bonded warehouse in UAE / Central Asia."),
            ("Bills of Lading Switching", "Consignee re-labeled with falsified Harmonized System (HS) codes."),
            ("Freight Forwarder Obfuscation", "Intermediary 3PL brokerage masking original bill of lading origin."),
            ("Value-Added Relabeling", "Minimal repackaging to claim fraudulent certificate of origin.")
        ]
    },
    {
        "col": 2,
        "title": "TIER 3: MARITIME TELEMETRY",
        "badge": "[DARK FLEET & AIS SPOOF]",
        "badge_color": (23, 162, 184),
        "steps": [
            ("AIS Transponder Dark Activity", "Automatic Identification System switched off in sensitive straits."),
            ("Ship-to-Ship (STS) Transfers", "Offshore cargo transfer outside territorial customs surveillance."),
            ("Flag-of-Convenience Switching", "Vessel re-flagged across multiple non-compliant registries."),
            ("Corporate Fleet Layering", "Single-ship SPV registered under trust in Panama / Marshall Islands.")
        ]
    },
    {
        "col": 3,
        "title": "TIER 4: VERITAS DEFENSE AUDIT",
        "badge": "[EVIDENTIARY REMEDIATION]",
        "badge_color": (40, 167, 69),
        "steps": [
            ("Automated Registry Vetting", "Global corporate register cross-matching & secondary sanctions filter."),
            ("Satellite Radar Triangulation", "Synthetic Aperture Radar (SAR) confirms actual vessel coordinates."),
            ("Banking Correspondent Defense", "SWIFT MT103 / MT202 audit trail defensible for US/EU regulators."),
            ("General Counsel Red Flag Dossier", "Court-admissible exhibit file ready for DOJ, OFAC & BIS disclosures.")
        ]
    }
]

col_w = 860
gap = 35
start_x = 120
start_y = 280
card_h = 1720

for lane in lane_data_sanc:
    lx = start_x + lane["col"] * (col_w + gap)
    draw_sanc.rectangle([(lx, start_y), (lx + col_w, start_y + card_h)], fill=(12, 22, 38), outline=(35, 60, 95), width=2)
    # Column Header
    draw_sanc.rectangle([(lx, start_y), (lx + col_w, start_y + 110)], fill=(18, 32, 54), outline=(197, 160, 89, 80), width=1)
    draw_sanc.text((lx + 25, start_y + 22), lane["title"], fill=(255, 255, 255), font=font_subtitle)
    # Badge
    draw_sanc.rectangle([(lx + 25, start_y + 70), (lx + 320, start_y + 100)], fill=(20, 30, 48), outline=lane["badge_color"], width=2)
    draw_sanc.text((lx + 35, start_y + 73), lane["badge"], fill=lane["badge_color"], font=font_mono)
    
    # Render steps
    step_y = start_y + 140
    for idx, (head, desc) in enumerate(lane["steps"]):
        box_h = 360
        draw_sanc.rectangle([(lx + 25, step_y), (lx + col_w - 25, step_y + box_h)], fill=(16, 28, 48), outline=(45, 75, 115), width=2)
        # Step marker
        draw_sanc.rectangle([(lx + 45, step_y + 25), (lx + 105, step_y + 65)], fill=(197, 160, 89), outline=None)
        draw_sanc.text((lx + 58, step_y + 30), f"0{idx+1}", fill=(10, 18, 30), font=font_body_bold)
        
        draw_sanc.text((lx + 125, step_y + 32), head, fill=(240, 240, 240), font=font_h2)
        
        # Wrapped description
        words = desc.split()
        lines = []
        cur = ""
        for w in words:
            test = cur + (" " if cur else "") + w
            if len(test) > 42:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur:
            lines.append(cur)
            
        text_y = step_y + 90
        for l in lines:
            draw_sanc.text((lx + 45, text_y), l, fill=(180, 195, 215), font=font_body)
            text_y += 38
            
        # Checkpoint pill
        draw_sanc.rectangle([(lx + 45, step_y + box_h - 60), (lx + 360, step_y + box_h - 20)], fill=(10, 20, 34), outline=(197, 160, 89, 120), width=1)
        draw_sanc.text((lx + 60, step_y + box_h - 52), "[SANCTION SCREEN: PASS]", fill=(197, 160, 89), font=font_mono)
        
        step_y += box_h + 30

save_dual(im_sanc_diag, "blog", "blog-detail-featured-sanctions.jpg")

# Bottom Banner: sanctions_port_terminal.jpg
print("1.3 Bottom Banner: banner-blog-details-sanctions.jpg")
im_banner_sanc = crop_and_scale_4k(os.path.join(scratch, "sanctions_port_terminal.jpg"), top_bias=0.4)
im_banner_sanc = ImageEnhance.Contrast(im_banner_sanc).enhance(1.08)
save_dual(im_banner_sanc, "banners", "banner-blog-details-sanctions.jpg")


# ==============================================================================
# 2. CARD 5: OSINT IN COMMERCIAL LITIGATION
# ==============================================================================
print("\n--- Generating Card 5 Assets (OSINT in Commercial Litigation) ---")

# Hero: osint_data_network.jpg (3840 x 2555 -> 3840 x 2160)
print("2.1 Hero: hero-blog-details-osint.jpg")
im_hero_osint = crop_and_scale_4k(os.path.join(scratch, "osint_data_network.jpg"), top_bias=0.3)
im_hero_osint = ImageEnhance.Contrast(im_hero_osint).enhance(1.06)
save_dual(im_hero_osint, "hero", "hero-blog-details-osint.jpg")

# Featured Diagram: blog-detail-featured-osint.jpg
print("2.2 Featured Diagram: blog-detail-featured-osint.jpg")
im_osint_diag = Image.new("RGB", (3840, 2160), "#0a121e")
draw_osint = ImageDraw.Draw(im_osint_diag)

# Grid
for x in range(0, 3840, 80):
    draw_osint.line([(x, 0), (x, 2160)], fill=(22, 38, 60), width=1)
for y in range(0, 2160, 80):
    draw_osint.line([(0, y), (3840, y)], fill=(22, 38, 60), width=1)

# Outer frame & corner brackets
draw_osint.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89, 160), width=3)
for cx, cy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_osint.line([(cx, cy), (cx + dx * c_len, cy)], fill=gold_b, width=6)
    draw_osint.line([(cx, cy), (cx, cy + dy * c_len)], fill=gold_b, width=6)

# Header block
draw_osint.rectangle([(120, 110), (3720, 240)], fill=(14, 25, 42), outline=(197, 160, 89, 120), width=2)
draw_osint.text((150, 130), "FIGURE 1: CROSS-BORDER OSINT TRIANGULATION & COURT-ADMISSIBLE EVIDENTIARY PROTOCOL", fill=(245, 245, 245), font=font_title)
draw_osint.text((150, 195), "VERITAS LITIGATION INTELLIGENCE PRACTICE  |  EVIDENTIARY INTEGRITY: FRE RULE 902(11) COMPLIANT  |  OCTOBER 2026", fill=(197, 160, 89), font=font_mono)

lane_data_osint = [
    {
        "col": 0,
        "title": "PHASE I: DATA HARVESTING",
        "badge": "[RAW TELEMETRY INTAKE]",
        "badge_color": (23, 162, 184),
        "steps": [
            ("Corporate Registry Extraction", "Harvesting historical share transfers, officer filings & gazette records."),
            ("Litigation Docket Cross-Search", "Querying PACER, High Court rolls & international arbitration records."),
            ("Geospatial & Marine Tracking", "Aggregating ADS-B flight logs, marine AIS fixes & satellite imagery."),
            ("Social Graph Footprint", "Mapping professional relationships, alumni ties & undisclosed affinities.")
        ]
    },
    {
        "col": 1,
        "title": "PHASE II: FORENSIC TIMESTAMP",
        "badge": "[CRYPTOGRAPHIC CHAIN]",
        "badge_color": (40, 167, 69),
        "steps": [
            ("Cryptographic SHA-256 Hash", "Generating instantaneous cryptographic hashes for web/document grabs."),
            ("RFC 3161 Timestamp Authority", "Binding digital evidence to legally recognized third-party time tokens."),
            ("Wayback Archive Forensics", "Reconstructing deleted target webpages, disclaimers & altered profiles."),
            ("Original Source Preservation", "WARC / MHTML container archiving with unedited HTTP headers.")
        ]
    },
    {
        "col": 2,
        "title": "PHASE III: DE-ANONYMIZATION",
        "badge": "[ADVERSARIAL LINKING]",
        "badge_color": (255, 193, 7),
        "steps": [
            ("Nominee Layer Piercing", "Linking nominee directors across hundreds of disparate entity nodes."),
            ("Corporate Asset Association", "Connecting luxury real estate / jets to underlying corporate shell."),
            ("Disambiguation Matrix", "Eliminating false positives through multi-vector identifier matching."),
            ("Source Credibility Grading", "Admiralty Code rating (A1 to F6) assessing reliability of all facts.")
        ]
    },
    {
        "col": 3,
        "title": "PHASE IV: COURT PACKAGING",
        "badge": "[ADMISSIBLE EXHIBITS]",
        "badge_color": (197, 160, 89),
        "steps": [
            ("Sworn Investigator Affidavit", "Drafting witness statement detailing provenance and search methodology."),
            ("Federal Rule 902(11) Vetting", "Ensuring electronic records qualify as self-authenticating business records."),
            ("Cross-Examination Defense", "Pre-trial hostile audit of every exhibit to defeat hearsay challenges."),
            ("Trial Exhibit Compendium", "Bespoke trial-ready binders with interactive digital document linking.")
        ]
    }
]

for lane in lane_data_osint:
    lx = start_x + lane["col"] * (col_w + gap)
    draw_osint.rectangle([(lx, start_y), (lx + col_w, start_y + card_h)], fill=(12, 22, 38), outline=(35, 60, 95), width=2)
    # Header
    draw_osint.rectangle([(lx, start_y), (lx + col_w, start_y + 110)], fill=(18, 32, 54), outline=(197, 160, 89, 80), width=1)
    draw_osint.text((lx + 25, start_y + 22), lane["title"], fill=(255, 255, 255), font=font_subtitle)
    draw_osint.rectangle([(lx + 25, start_y + 70), (lx + 340, start_y + 100)], fill=(20, 30, 48), outline=lane["badge_color"], width=2)
    draw_osint.text((lx + 35, start_y + 73), lane["badge"], fill=lane["badge_color"], font=font_mono)
    
    step_y = start_y + 140
    for idx, (head, desc) in enumerate(lane["steps"]):
        box_h = 360
        draw_osint.rectangle([(lx + 25, step_y), (lx + col_w - 25, step_y + box_h)], fill=(16, 28, 48), outline=(45, 75, 115), width=2)
        draw_osint.rectangle([(lx + 45, step_y + 25), (lx + 105, step_y + 65)], fill=(197, 160, 89), outline=None)
        draw_osint.text((lx + 58, step_y + 30), f"0{idx+1}", fill=(10, 18, 30), font=font_body_bold)
        
        draw_osint.text((lx + 125, step_y + 32), head, fill=(240, 240, 240), font=font_h2)
        
        words = desc.split()
        lines = []
        cur = ""
        for w in words:
            test = cur + (" " if cur else "") + w
            if len(test) > 42:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur:
            lines.append(cur)
            
        text_y = step_y + 90
        for l in lines:
            draw_osint.text((lx + 45, text_y), l, fill=(180, 195, 215), font=font_body)
            text_y += 38
            
        draw_osint.rectangle([(lx + 45, step_y + box_h - 60), (lx + 360, step_y + box_h - 20)], fill=(10, 20, 34), outline=(197, 160, 89, 120), width=1)
        draw_osint.text((lx + 60, step_y + box_h - 52), "[EVIDENTIARY AUDIT: PASS]", fill=(197, 160, 89), font=font_mono)
        
        step_y += box_h + 30

save_dual(im_osint_diag, "blog", "blog-detail-featured-osint.jpg")

# Bottom Banner: towers_reflection.jpg (3840 x 2160 native)
print("2.3 Bottom Banner: banner-blog-details-osint.jpg")
im_banner_osint = crop_and_scale_4k(os.path.join(scratch, "towers_reflection.jpg"), top_bias=0.5)
im_banner_osint = ImageEnhance.Contrast(im_banner_osint).enhance(1.08)
save_dual(im_banner_osint, "banners", "banner-blog-details-osint.jpg")


# ==============================================================================
# 3. CARD 6: TRACING DISSIPATED SOVEREIGN & CORPORATE ASSETS
# ==============================================================================
print("\n--- Generating Card 6 Assets (Tracing Dissipated Sovereign & Corporate Assets) ---")

# Hero: wm_cand_15.jpg (5579 x 3366 -> 3840 x 2160)
print("3.1 Hero: hero-blog-details-asset-recovery.jpg")
im_hero_asset = crop_and_scale_4k(os.path.join(scratch, "wm_cand_15.jpg"), top_bias=0.45)
im_hero_asset = ImageEnhance.Contrast(im_hero_asset).enhance(1.08)
save_dual(im_hero_asset, "hero", "hero-blog-details-asset-recovery.jpg")

# Featured Diagram: blog-detail-featured-asset-recovery.jpg
print("3.2 Featured Diagram: blog-detail-featured-asset-recovery.jpg")
im_asset_diag = Image.new("RGB", (3840, 2160), "#0a121e")
draw_asset = ImageDraw.Draw(im_asset_diag)

# Grid
for x in range(0, 3840, 80):
    draw_asset.line([(x, 0), (x, 2160)], fill=(22, 38, 60), width=1)
for y in range(0, 2160, 80):
    draw_asset.line([(0, y), (3840, y)], fill=(22, 38, 60), width=1)

# Outer frame & corner brackets
draw_asset.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89, 160), width=3)
for cx, cy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_asset.line([(cx, cy), (cx + dx * c_len, cy)], fill=gold_b, width=6)
    draw_asset.line([(cx, cy), (cx, cy + dy * c_len)], fill=gold_b, width=6)

# Header block
draw_asset.rectangle([(120, 110), (3720, 240)], fill=(14, 25, 42), outline=(197, 160, 89, 120), width=2)
draw_asset.text((150, 130), "FIGURE 1: MULTI-JURISDICTIONAL SOVEREIGN & CORPORATE ASSET TRACING ARCHITECTURE", fill=(245, 245, 245), font=font_title)
draw_asset.text((150, 195), "VERITAS ASSET TRACING & RECOVERY PRACTICE  |  CROSS-BORDER ENFORCEMENT & MAREVA PROTOCOLS  |  OCTOBER 2026", fill=(197, 160, 89), font=font_mono)

lane_data_asset = [
    {
        "col": 0,
        "title": "LAYER 1: DISSIPATION INCEPTION",
        "badge": "[LIQUIDITY OUTFLOW]",
        "badge_color": (220, 53, 69),
        "steps": [
            ("Defalcated Treasury Capital", "State funds / corporate equity diverted via sham advisory retainers."),
            ("Fictitious Trade Financing", "Inflated import/export letters of credit routing cash offshore."),
            ("Round-Tripping Remittances", "Multiple rapid SWIFT transfers through correspondent bank accounts."),
            ("Real-Time Liquidity Drain", "Accelerated transfer prior to formal petition of insolvency or indictment.")
        ]
    },
    {
        "col": 1,
        "title": "LAYER 2: OFFSHORE CONDUIT",
        "badge": "[NOMINEE FOUNDATIONS]",
        "badge_color": (255, 193, 7),
        "steps": [
            ("BVI & Cayman Entity Tiers", "Layered IBCs structured with nominee professional directors."),
            ("Discretionary Trust Shielding", "Liechtenstein Anstalt & Jersey trusts severing legal ownership."),
            ("Bearer Share / Nominee Bonds", "Private agreements preserving beneficial dominion in secrecy."),
            ("Intercompany Loan Fabrications", "Unsecured subordinate notes creating phantom debt claims on assets.")
        ]
    },
    {
        "col": 2,
        "title": "LAYER 3: ASSET STORE-OF-VALUE",
        "badge": "[IDENTIFIED PROCEEDS]",
        "badge_color": (23, 162, 184),
        "steps": [
            ("Prime Global Real Estate", "Penthouses & commercial towers held in anonymous holding LLCs."),
            ("Maritime Superyachts & Aviation", "Bermuda/Isle of Man flagged vessels leased to true beneficial owner."),
            ("Numbered Bullion Depositories", "Physical gold bars & precious metals secured in duty-free freeports."),
            ("Art & Antiquities Vaults", "Geneva Freeport storage receipts concealing convertible capital.")
        ]
    },
    {
        "col": 3,
        "title": "LAYER 4: RECOVERY ENFORCEMENT",
        "badge": "[REPATRIATION & FREEZING]",
        "badge_color": (40, 167, 69),
        "steps": [
            ("Worldwide Freezing Order (WFO)", "High Court Mareva injunction immobilizing global accounts simultaneously."),
            ("US 28 U.S.C. Section 1782 Action", "Federal court discovery compelling US clearing banks for wire trails."),
            ("Norwich Pharmacal Relief", "Equitable disclosure orders forcing offshore registered agents to reveal UBO."),
            ("Judicial Liquidation & Seizure", "Appointing court receivers and repatriating assets to judgment creditor.")
        ]
    }
]

for lane in lane_data_asset:
    lx = start_x + lane["col"] * (col_w + gap)
    draw_asset.rectangle([(lx, start_y), (lx + col_w, start_y + card_h)], fill=(12, 22, 38), outline=(35, 60, 95), width=2)
    # Header
    draw_asset.rectangle([(lx, start_y), (lx + col_w, start_y + 110)], fill=(18, 32, 54), outline=(197, 160, 89, 80), width=1)
    draw_asset.text((lx + 25, start_y + 22), lane["title"], fill=(255, 255, 255), font=font_subtitle)
    draw_asset.rectangle([(lx + 25, start_y + 70), (lx + 350, start_y + 100)], fill=(20, 30, 48), outline=lane["badge_color"], width=2)
    draw_asset.text((lx + 35, start_y + 73), lane["badge"], fill=lane["badge_color"], font=font_mono)
    
    step_y = start_y + 140
    for idx, (head, desc) in enumerate(lane["steps"]):
        box_h = 360
        draw_asset.rectangle([(lx + 25, step_y), (lx + col_w - 25, step_y + box_h)], fill=(16, 28, 48), outline=(45, 75, 115), width=2)
        draw_asset.rectangle([(lx + 45, step_y + 25), (lx + 105, step_y + 65)], fill=(197, 160, 89), outline=None)
        draw_asset.text((lx + 58, step_y + 30), f"0{idx+1}", fill=(10, 18, 30), font=font_body_bold)
        
        draw_asset.text((lx + 125, step_y + 32), head, fill=(240, 240, 240), font=font_h2)
        
        words = desc.split()
        lines = []
        cur = ""
        for w in words:
            test = cur + (" " if cur else "") + w
            if len(test) > 42:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur:
            lines.append(cur)
            
        text_y = step_y + 90
        for l in lines:
            draw_asset.text((lx + 45, text_y), l, fill=(180, 195, 215), font=font_body)
            text_y += 38
            
        draw_asset.rectangle([(lx + 45, step_y + box_h - 60), (lx + 360, step_y + box_h - 20)], fill=(10, 20, 34), outline=(197, 160, 89, 120), width=1)
        draw_asset.text((lx + 60, step_y + box_h - 52), "[JUDICIAL ATTACHMENT: ACTIVE]", fill=(197, 160, 89), font=font_mono)
        
        step_y += box_h + 30

save_dual(im_asset_diag, "blog", "blog-detail-featured-asset-recovery.jpg")

# Bottom Banner: asset_tracing_gold_bars.jpg (3840 x 2560 -> 3840 x 2160)
print("3.3 Bottom Banner: banner-blog-details-asset-recovery.jpg")
im_banner_asset = crop_and_scale_4k(os.path.join(scratch, "asset_tracing_gold_bars.jpg"), top_bias=0.5)
im_banner_asset = ImageEnhance.Contrast(im_banner_asset).enhance(1.08)
save_dual(im_banner_asset, "banners", "banner-blog-details-asset-recovery.jpg")

print("\nALL 9 ASSETS BUILT AND SYNCHRONIZED SUCCESSFULLY!")
