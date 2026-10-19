import os, shutil, math
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

workspace = r"c:\Users\thand\Desktop\Website"
template_dir = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"

blog_dir = os.path.join(workspace, "assets", "images", "blog")
tmpl_blog_dir = os.path.join(template_dir, "assets", "images", "blog")

def get_font(name, size):
    font_path = os.path.join(r"C:\Windows\Fonts", name)
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 46)
font_subtitle = get_font("segoeuib.ttf", 32)
font_h2 = get_font("segoeuib.ttf", 26)
font_body_bold = get_font("segoeuib.ttf", 22)
font_body = get_font("segoeui.ttf", 20)
font_mono = get_font("consolab.ttf", 19)
font_small = get_font("segoeui.ttf", 17)
font_small_bold = get_font("segoeuib.ttf", 17)

def save_dual(im, fname):
    r_path = os.path.join(blog_dir, fname)
    t_path = os.path.join(tmpl_blog_dir, fname)
    im.save(r_path, "JPEG", quality=95)
    shutil.copy2(r_path, t_path)
    print(f"Saved {fname} ({im.size}) to root and template.")

# ==============================================================================
# 1. DIAGRAM 4: SANCTIONS & TRANSSHIPMENT MARITIME NEXUS
# Geometry: Horizontal split-flow with central FTZ hub circle & satellite vectors
# ==============================================================================
print("Generating DISTINCT Diagram 4 (Sanctions)...")
im_sanc = Image.new("RGB", (3840, 2160), "#08111d")
draw_s = ImageDraw.Draw(im_sanc)

# Background diagonal hatch / fine grid
for x in range(0, 3840, 100):
    draw_s.line([(x, 0), (x, 2160)], fill=(18, 30, 48), width=1)
for y in range(0, 2160, 100):
    draw_s.line([(0, y), (3840, y)], fill=(18, 30, 48), width=1)

# Outer frame & corner brackets
draw_s.rectangle([(80, 80), (3760, 2080)], outline=(197, 160, 89, 150), width=3)
gold = (197, 160, 89)
for cx, cy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_s.line([(cx, cy), (cx + dx * 80, cy)], fill=gold, width=6)
    draw_s.line([(cx, cy), (cx, cy + dy * 80)], fill=gold, width=6)

# Header
draw_s.rectangle([(120, 110), (3720, 250)], fill=(13, 23, 38), outline=gold, width=2)
draw_s.text((150, 130), "FIGURE 1: MULTI-TIER SECONDARY SANCTIONS EVASION & TRANSSHIPMENT INTERMEDIARY MATRIX", fill=(255, 255, 255), font=font_title)
draw_s.text((150, 195), "TRADE CONTROLS & OFAC COMPLIANCE PRACTICE  |  GLOBAL MARITIME & TRANSSHIPMENT TELEMETRY  |  OCTOBER 2026", fill=gold, font=font_mono)

# Layout: 3 Horizontal Broad Bands with Center Circular Hub
# Left Column: Prohibited Origins & Sanctioned Exporters (Red accent)
draw_s.rectangle([(140, 300), (1050, 1050)], fill=(22, 16, 26), outline=(220, 53, 69), width=3)
draw_s.rectangle([(140, 300), (1050, 380)], fill=(176, 42, 55))
draw_s.text((170, 325), "TIER 1: SANCTIONED SOURCE & EXPORTER", fill=(255, 255, 255), font=font_subtitle)
draw_s.text((170, 410), "Prohibited Entity / SDN Listing:", fill=gold, font=font_body_bold)
draw_s.text((170, 445), "• Designated state-backed dual-use manufacturer.", fill=(220, 230, 245), font=font_body)
draw_s.text((170, 485), "• Concealed military-industrial end-user nexus.", fill=(220, 230, 245), font=font_body)
draw_s.text((170, 525), "• Controlled commodities: EAR99 / CCL Dual-Use items.", fill=(220, 230, 245), font=font_body)
draw_s.rectangle([(170, 580), (1020, 740)], fill=(32, 18, 28), outline=(220, 53, 69), width=2)
draw_s.text((190, 600), "INITIAL INVOICE DIVERSION:", fill=(255, 107, 107), font=font_small_bold)
draw_s.text((190, 635), "Invoice issued via newly formed front LLC in non-aligned territory.", fill=(255, 201, 201), font=font_body)
draw_s.text((190, 675), "Consignment routed away from direct commercial shipping lanes.", fill=(255, 201, 201), font=font_body)
draw_s.rectangle([(170, 780), (1020, 1000)], fill=(16, 24, 38), outline=(50, 80, 120), width=1)
draw_s.text((190, 800), "FINANCIAL NEXUS AUDIT:", fill=gold, font=font_small_bold)
draw_s.text((190, 835), "SWIFT wire payments split across third-party currency houses.", fill=(200, 215, 235), font=font_body)
draw_s.text((190, 875), "Escrow executed in offshore non-FATF compliant accounts.", fill=(200, 215, 235), font=font_body)
draw_s.text((190, 930), "[STATUS: OFAC SDN MATCH // RED FLAG CRITICAL]", fill=(220, 53, 69), font=font_mono)

# Bottom Left Column: Dark Fleet Maritime Vectors (Cyan/Amber)
draw_s.rectangle([(140, 1120), (1050, 1980)], fill=(14, 24, 40), outline=(23, 162, 184), width=3)
draw_s.rectangle([(140, 1120), (1050, 1200)], fill=(19, 78, 94))
draw_s.text((170, 1145), "TIER 2: MARITIME AIS SPOOFING & STS", fill=(255, 255, 255), font=font_subtitle)
draw_s.text((170, 1230), "Deceptive Shipping Practices:", fill=(23, 162, 184), font=font_body_bold)
draw_s.text((170, 1265), "• AIS transponders disabled during straits transit.", fill=(220, 230, 245), font=font_body)
draw_s.text((170, 1305), "• Synthetic coordinates broadcasted via shore transmitters.", fill=(220, 230, 245), font=font_body)
draw_s.text((170, 1345), "• Ship-to-Ship (STS) midnight offshore cargo transfers.", fill=(220, 230, 245), font=font_body)
draw_s.rectangle([(170, 1400), (1020, 1600)], fill=(12, 32, 48), outline=(23, 162, 184), width=2)
draw_s.text((190, 1420), "VESSEL RE-FLAGGING ANOMALIES:", fill=(100, 210, 255), font=font_small_bold)
draw_s.text((190, 1455), "Multiple flag-of-convenience registrations in 18-month span.", fill=(190, 230, 255), font=font_body)
draw_s.text((190, 1495), "Single-ship SPV owned by bearer share offshore corporation.", fill=(190, 230, 255), font=font_body)
draw_s.text((190, 1545), "[SATELLITE SAR RADAR: VESSEL POSITION CONFIRMED]", fill=(40, 167, 69), font=font_mono)
draw_s.rectangle([(170, 1640), (1020, 1920)], fill=(18, 28, 45), outline=(50, 80, 120), width=1)
draw_s.text((190, 1665), "CARGO MANIFEST DISCREPANCIES:", fill=gold, font=font_small_bold)
draw_s.text((190, 1700), "Draught change telemetry proves cargo offload occurred in dark zone.", fill=(200, 215, 235), font=font_body)
draw_s.text((190, 1740), "Bills of lading reissued with falsified ports of origin.", fill=(200, 215, 235), font=font_body)

# Center Nexus: Transshipment FTZ Hub
draw_s.rectangle([(1150, 480), (2680, 1800)], fill=(16, 28, 48), outline=(255, 193, 7), width=3)
draw_s.rectangle([(1150, 480), (2680, 580)], fill=(180, 120, 10))
draw_s.text((1200, 510), "CENTRAL TRANSSHIPMENT CONDUIT: FREE TRADE ZONE (FTZ)", fill=(255, 255, 255), font=font_subtitle)

# Central Visual Matrix Box
draw_s.rectangle([(1220, 640), (2610, 1080)], fill=(10, 18, 32), outline=(197, 160, 89), width=2)
draw_s.text((1250, 670), "INTERMEDIARY RELABELING & BILL OF LADING SWITCHING", fill=gold, font=font_h2)
draw_s.text((1250, 720), "1. Consignment Enters Bonded Warehouse: Goods arrive under valid customs manifest.", fill=(230, 240, 255), font=font_body)
draw_s.text((1250, 770), "2. Harmonized System (HS) Code Alteration: Code manipulated to benign industrial goods.", fill=(230, 240, 255), font=font_body)
draw_s.text((1250, 820), "3. Minimal Transformation Processing: Repackaged to claim fraudulent local origin certificate.", fill=(230, 240, 255), font=font_body)
draw_s.text((1250, 870), "4. New Consignee Assignment: Layered 3PL logistics broker named as nominal importer.", fill=(230, 240, 255), font=font_body)
draw_s.text((1250, 930), "[AUDIT ACTION: BILL OF LADING LINEAGE TRACED TO SOURCE]", fill=(40, 167, 69), font=font_mono)

# Connecting arrows
draw_s.line([(1050, 675), (1150, 675)], fill=(220, 53, 69), width=6)
draw_s.line([(1050, 1550), (1150, 1550)], fill=(23, 162, 184), width=6)

draw_s.rectangle([(1220, 1140), (2610, 1720)], fill=(12, 22, 36), outline=(60, 100, 150), width=2)
draw_s.text((1250, 1170), "CROSS-BORDER INTERMEDIARY SHELL DECOMPOSITION", fill=(255, 255, 255), font=font_h2)
draw_s.text((1250, 1220), "• Holding SPV 01: Dubai Multi Commodities Centre (DMCC) Registered Entity.", fill=(200, 215, 235), font=font_body)
draw_s.text((1250, 1270), "• Holding SPV 02: Central Asian Trading Brokerage with Nominee Directors.", fill=(200, 215, 235), font=font_body)
draw_s.text((1250, 1320), "• Banking Channel: Non-SWIFT Alternative Messaging Rails utilized for settlement.", fill=(200, 215, 235), font=font_body)
draw_s.text((1250, 1380), "IDENTIFIED RED FLAGS:", fill=(255, 107, 107), font=font_body_bold)
draw_s.text((1250, 1420), "-> Zero physical employees at registered free-zone office address.", fill=(255, 200, 200), font=font_body)
draw_s.text((1250, 1460), "-> Intermediary incorporated within 90 days of export restriction rollout.", fill=(255, 200, 200), font=font_body)
draw_s.text((1250, 1500), "-> Margin on multi-million dollar transaction compressed to sub-1% fee.", fill=(255, 200, 200), font=font_body)
draw_s.text((1250, 1570), "[INTERMEDIARY EVASION NETWORK VERIFIED // DISCLOSURE PREPARED]", fill=gold, font=font_mono)

# Right Column: Veritas Forensic Shield & Legal Safe Harbor
draw_s.rectangle([(2780, 300), (3700, 1980)], fill=(12, 26, 32), outline=(40, 167, 69), width=3)
draw_s.rectangle([(2780, 300), (3700, 380)], fill=(25, 120, 50))
draw_s.text((2810, 325), "TIER 3: VERITAS REGULATORY DEFENSE", fill=(255, 255, 255), font=font_subtitle)

# Arrow from Center to Right
draw_s.line([(2680, 1140), (2780, 1140)], fill=(40, 167, 69), width=6)

draw_s.text((2810, 420), "GENERAL COUNSEL REMEDIATION PROTOCOL", fill=gold, font=font_h2)
draw_s.text((2810, 480), "1. Immediate Contractual Suspension:", fill=(240, 240, 240), font=font_body_bold)
draw_s.text((2810, 515), "Invoking Sanctions Compliance Clause and escrow freeze.", fill=(200, 225, 215), font=font_body)

draw_s.text((2810, 590), "2. OFAC Voluntary Self-Disclosure (VSD):", fill=(240, 240, 240), font=font_body_bold)
draw_s.text((2810, 625), "Packaging certified evidentiary dossier before regulator inquiries.", fill=(200, 225, 215), font=font_body)

draw_s.text((2810, 700), "3. Supply Chain Vendor Termination:", fill=(240, 240, 240), font=font_body_bold)
draw_s.text((2810, 735), "Legally defensible termination without liability for breach.", fill=(200, 225, 215), font=font_body)

draw_s.text((2810, 810), "4. Correspondent Bank Certification:", fill=(240, 240, 240), font=font_body_bold)
draw_s.text((2810, 845), "Providing clearing institutions with forensic proof of zero taint.", fill=(200, 225, 215), font=font_body)

draw_s.rectangle([(2810, 940), (3670, 1340)], fill=(16, 36, 44), outline=(40, 167, 69), width=2)
draw_s.text((2830, 965), "REGULATORY SAFE HARBOR CHECKLIST:", fill=(40, 167, 69), font=font_body_bold)
draw_s.text((2830, 1010), "[PASS] Pre-Transaction UBO Lineage Vetting", fill=(220, 245, 230), font=font_mono)
draw_s.text((2830, 1055), "[PASS] Vessel Satellite SAR Telemetry Corroboration", fill=(220, 245, 230), font=font_mono)
draw_s.text((2830, 1100), "[PASS] End-User Certificate Physical Site Inspection", fill=(220, 245, 230), font=font_mono)
draw_s.text((2830, 1145), "[PASS] Full SWIFT MT103 Banking Trail Reconstruction", fill=(220, 245, 230), font=font_mono)
draw_s.text((2830, 1190), "[PASS] Board-Approved Sanctions Compliance Audit", fill=(220, 245, 230), font=font_mono)
draw_s.text((2830, 1260), "OUTCOME: COMPLETE MITIGATION OF PENALTIES", fill=gold, font=font_body_bold)

draw_s.rectangle([(2810, 1420), (3670, 1900)], fill=(10, 20, 30), outline=gold, width=2)
draw_s.text((2830, 1450), "EVIDENTIARY AUDIT SUMMARY", fill=gold, font=font_h2)
draw_s.text((2830, 1500), "Dossier Reference: #VER-SANC-2026-FTZ", fill=(180, 195, 215), font=font_mono)
draw_s.text((2830, 1540), "Target Intermediary: Disclosed in Full Dossier", fill=(180, 195, 215), font=font_body)
draw_s.text((2830, 1580), "Jurisdiction Scope: UAE / Central Asia / EU", fill=(180, 195, 215), font=font_body)
draw_s.text((2830, 1620), "Primary Regulator: U.S. OFAC & UK OFSI", fill=(180, 195, 215), font=font_body)
draw_s.text((2830, 1680), "LEGAL WORK-PRODUCT PRIVILEGED // STRICT DISCRETION", fill=(220, 53, 69), font=font_mono)

save_dual(im_sanc, "blog-detail-featured-sanctions.jpg")


# ==============================================================================
# 2. DIAGRAM 5: OSINT RADAR & CROSS-BORDER TRIANGULATION MESH
# Geometry: Concentric circular radar sweep with radiating intelligence nodes
# ==============================================================================
print("Generating DISTINCT Diagram 5 (OSINT)...")
im_osint = Image.new("RGB", (3840, 2160), "#060d17")
draw_o = ImageDraw.Draw(im_osint)

# Draw concentric radar rings around center (1920, 1180)
cx, cy = 1920, 1180
for r in [200, 400, 600, 800, 1000, 1200]:
    draw_o.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(20, 42, 65), width=2)

# Radial radar crosshairs
draw_o.line([(cx - 1300, cy), (cx + 1300, cy)], fill=(25, 55, 85), width=2)
draw_o.line([(cx, cy - 900), (cx, cy + 900)], fill=(25, 55, 85), width=2)

# Diagonal radar sweeps (45 deg)
d_len = 1000
for angle in [30, 60, 120, 150, 210, 240, 300, 330]:
    rad = math.radians(angle)
    px = cx + int(d_len * math.cos(rad))
    py = cy + int(d_len * math.sin(rad))
    draw_o.line([(cx, cy), (px, py)], fill=(18, 38, 58), width=1)

# Outer frame & corner brackets
draw_o.rectangle([(80, 80), (3760, 2080)], outline=gold, width=3)
for cpx, cpy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_o.line([(cpx, cpy), (cpx + dx * 80, cpy)], fill=gold, width=6)
    draw_o.line([(cpx, cpy), (cpx, cpy + dy * 80)], fill=gold, width=6)

# Header
draw_o.rectangle([(120, 110), (3720, 250)], fill=(12, 22, 36), outline=gold, width=2)
draw_o.text((150, 130), "FIGURE 1: CROSS-BORDER OSINT TRIANGULATION & COURT-ADMISSIBLE EVIDENTIARY PROTOCOL", fill=(255, 255, 255), font=font_title)
draw_o.text((150, 195), "LITIGATION INTELLIGENCE PRACTICE  |  EVIDENTIARY INTEGRITY: FRE RULE 902(11) & (14)  |  OCTOBER 2026", fill=gold, font=font_mono)

# Center Target Node (The Court-Admissible Exhibit Compendium)
draw_o.rectangle([(cx - 360, cy - 180), (cx + 360, cy + 180)], fill=(18, 32, 54), outline=gold, width=4)
draw_o.rectangle([(cx - 340, cy - 160), (cx + 340, cy - 105)], fill=gold)
draw_o.text((cx - 320, cy - 150), "ADMISSIBLE TRIAL RECORD", fill=(10, 18, 30), font=font_subtitle)
draw_o.text((cx - 320, cy - 85), "Certified Forensic Exhibit Compendium", fill=(255, 255, 255), font=font_body_bold)
draw_o.text((cx - 320, cy - 45), "• SHA-256 Hash Signed & RFC 3161 Timestamped", fill=(200, 225, 245), font=font_body)
draw_o.text((cx - 320, cy - 10), "• Sworn Investigator Rule 902(11) Affidavit Attached", fill=(200, 225, 245), font=font_body)
draw_o.text((cx - 320, cy + 25), "• Pre-Emptive Hearsay Audit Passed for High Court", fill=(40, 167, 69), font=font_body_bold)
draw_o.text((cx - 320, cy + 85), "[STATUS: READY FOR JUDICIAL FILING]", fill=gold, font=font_mono)

# 4 Corner Quad Pods radiating toward center:
# Top-Left: Registry Harvesting
draw_o.rectangle([(140, 310), (1080, 840)], fill=(12, 24, 40), outline=(23, 162, 184), width=3)
draw_o.rectangle([(140, 310), (1080, 380)], fill=(19, 78, 94))
draw_o.text((170, 330), "CLUSTER 01: CORPORATE REGISTRY HARVESTING", fill=(255, 255, 255), font=font_subtitle)
draw_o.text((170, 410), "Multi-Jurisdictional Registry Ingestion:", fill=(23, 162, 184), font=font_body_bold)
draw_o.text((170, 450), "• Companies House (UK), Delaware (US), BVI & Cayman IBCs.", fill=(210, 230, 250), font=font_body)
draw_o.text((170, 490), "• Historical share register changes & gazette announcements.", fill=(210, 230, 250), font=font_body)
draw_o.text((170, 530), "• Mortgages, debentures & unrecorded charges over shares.", fill=(210, 230, 250), font=font_body)
draw_o.text((170, 590), "De-Anonymization Vector:", fill=gold, font=font_body_bold)
draw_o.text((170, 630), "Direct mapping of recurring nominee corporate services providers.", fill=(210, 230, 250), font=font_body)
draw_o.text((170, 710), "[REGISTRY PROVENANCE: 100% CERTIFIED]", fill=(40, 167, 69), font=font_mono)
draw_o.line([(1080, 575), (cx - 360, cy - 90)], fill=(23, 162, 184), width=3)

# Top-Right: Geospatial & Flight Telemetry
draw_o.rectangle([(2760, 310), (3700, 840)], fill=(12, 24, 40), outline=(255, 193, 7), width=3)
draw_o.rectangle([(2760, 310), (3700, 380)], fill=(180, 120, 10))
draw_o.text((2790, 330), "CLUSTER 02: GEOSPATIAL & PHYSICAL TELEMETRY", fill=(255, 255, 255), font=font_subtitle)
draw_o.text((2790, 410), "Physical Asset Movement Tracking:", fill=(255, 193, 7), font=font_body_bold)
draw_o.text((2790, 450), "• ADS-B transponder archives: Private aviation travel logs.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 490), "• Maritime AIS radar records: Superyacht berth locations.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 530), "• Satellite commercial imagery: Real estate development audits.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 590), "Corroboration Vector:", fill=gold, font=font_body_bold)
draw_o.text((2790, 630), "Matching physical executive presence to offshore signing dates.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 710), "[SATELLITE POSITIONING: VERIFIED SUB-METER]", fill=(40, 167, 69), font=font_mono)
draw_o.line([(2760, 575), (cx + 360, cy - 90)], fill=(255, 193, 7), width=3)

# Bottom-Left: Cryptographic Hash & Web Forensics
draw_o.rectangle([(140, 1380), (1080, 1980)], fill=(12, 24, 40), outline=(40, 167, 69), width=3)
draw_o.rectangle([(140, 1380), (1080, 1450)], fill=(25, 120, 50))
draw_o.text((170, 1400), "CLUSTER 03: CRYPTOGRAPHIC PRESERVATION", fill=(255, 255, 255), font=font_subtitle)
draw_o.text((170, 1480), "WARC / MHTML Container Archiving:", fill=(40, 167, 69), font=font_body_bold)
draw_o.text((170, 1520), "• Complete HTTP header preservation with unedited server IP.", fill=(210, 240, 220), font=font_body)
draw_o.text((170, 1560), "• Instantaneous SHA-256 cryptographic hash computation.", fill=(210, 240, 220), font=font_body)
draw_o.text((170, 1600), "• RFC 3161 qualified digital time-stamping authority token.", fill=(210, 240, 220), font=font_body)
draw_o.text((170, 1660), "Wayback Recovery:", fill=gold, font=font_body_bold)
draw_o.text((170, 1700), "Exposing deleted target admissions and altered biographical claims.", fill=(210, 240, 220), font=font_body)
draw_o.text((170, 1780), "[CHAIN OF CUSTODY: IMMUTABLE FORENSIC LOG]", fill=gold, font=font_mono)
draw_o.line([(1080, 1680), (cx - 360, cy + 90)], fill=(40, 167, 69), width=3)

# Bottom-Right: Litigation Docket Cross-Search
draw_o.rectangle([(2760, 1380), (3700, 1980)], fill=(12, 24, 40), outline=(197, 160, 89), width=3)
draw_o.rectangle([(2760, 1380), (3700, 1450)], fill=(140, 110, 50))
draw_o.text((2790, 1400), "CLUSTER 04: CROSS-DOCKET LITIGATION PACING", fill=(255, 255, 255), font=font_subtitle)
draw_o.text((2790, 1480), "Multi-Jurisdictional Docket Ingestion:", fill=gold, font=font_body_bold)
draw_o.text((2790, 1520), "• PACER (US Federal Court), High Court Rolls (UK), ICSID.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 1560), "• Unsealed depositions revealing concealed adverse party assets.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 1600), "• Prior bankruptcy filings unmasking historic nominee associates.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 1660), "Trial Utility:", fill=(255, 107, 107), font=font_body_bold)
draw_o.text((2790, 1700), "Deploying adversary's prior contradictory sworn statements at trial.", fill=(240, 230, 210), font=font_body)
draw_o.text((2790, 1780), "[CROSS-EXAMINATION IMPEACHMENT: ARMED]", fill=(40, 167, 69), font=font_mono)
draw_o.line([(2760, 1680), (cx + 360, cy + 90)], fill=gold, width=3)

save_dual(im_osint, "blog-detail-featured-osint.jpg")


# ==============================================================================
# 3. DIAGRAM 6: ASSET TRACING & INJUNCTION FUNNEL
# Geometry: Vertical 4-tier waterfall with funnel branches & golden depository
# ==============================================================================
print("Generating DISTINCT Diagram 6 (Asset Tracing)...")
im_asset = Image.new("RGB", (3840, 2160), "#0a1322")
draw_a = ImageDraw.Draw(im_asset)

# Background horizontal stripes / bars
for y in range(0, 2160, 60):
    draw_a.line([(0, y), (3840, y)], fill=(16, 28, 48), width=1)

# Outer frame & corner brackets
draw_a.rectangle([(80, 80), (3760, 2080)], outline=gold, width=3)
for cpx, cpy, dx, dy in [(60, 60, 1, 1), (3780, 60, -1, 1), (60, 2100, 1, -1), (3780, 2100, -1, -1)]:
    draw_a.line([(cpx, cpy), (cpx + dx * 80, cpy)], fill=gold, width=6)
    draw_a.line([(cpx, cpy), (cpx, cpy + dy * 80)], fill=gold, width=6)

# Header
draw_a.rectangle([(120, 110), (3720, 250)], fill=(16, 28, 48), outline=gold, width=2)
draw_a.text((150, 130), "FIGURE 1: MULTI-JURISDICTIONAL SOVEREIGN & CORPORATE ASSET TRACING ARCHITECTURE", fill=(255, 255, 255), font=font_title)
draw_a.text((150, 195), "CROSS-BORDER RECOVERY PRACTICE  |  WORLDWIDE FREEZING ORDERS & MAREVA ENFORCEMENT  |  OCTOBER 2026", fill=gold, font=font_mono)

# Tier 1 (Top Span): Sovereign / Corporate Capital Dissipation (Red)
draw_a.rectangle([(200, 300), (3640, 560)], fill=(28, 16, 24), outline=(220, 53, 69), width=3)
draw_a.rectangle([(220, 320), (520, 365)], fill=(176, 42, 55))
draw_a.text((235, 330), "TIER 1: CAPITAL FLIGHT INCEPTION", fill=(255, 255, 255), font=font_body_bold)
draw_a.text((540, 330), "DEFALCATED TREASURY LIQUIDITY // RAPID OUTFLOW", fill=(255, 107, 107), font=font_subtitle)
draw_a.text((220, 390), "• Misappropriation of state treasury / institutional loan capital through fictitious advisory retainers and inflated procurement.", fill=(220, 230, 245), font=font_body)
draw_a.text((220, 430), "• Velocity of Transfer: Liquidity moved through 4+ banking jurisdictions within 24 hours to impede pre-judgment discovery.", fill=(220, 230, 245), font=font_body)
draw_a.text((220, 470), "• Initial Clearing: Non-cooperative correspondent banks used to sever direct SWIFT transaction visibility.", fill=(220, 230, 245), font=font_body)
draw_a.text((220, 510), "[FORENSIC INTAKE: BANKING NEXUS IDENTIFIED // TRACING MANDATE ACTIVATED]", fill=gold, font=font_mono)

# Downward 3 Flow Arrows
for x in [800, 1920, 3040]:
    draw_a.line([(x, 560), (x, 660)], fill=gold, width=4)

# Tier 2 (Three Intermediate Shielding Nodes)
nodes_t2 = [
    ("BOX 2A: LIECHTENSTEIN ANSTALT", "Irrevocable Family Foundation", "Conceals beneficial rights under unrecorded 'Letter of Wishes'.", (800, 660)),
    ("BOX 2B: CAYMAN / BVI IBC TIERS", "Layered Holding Corporations", "Nominee corporate directors masking true beneficial shareholding.", (1920, 660)),
    ("BOX 2C: CHANNEL ISLANDS TRUST", "Discretionary Shielding Vehicle", "Purports to sever debtor's legal ownership to defeat judgment creditors.", (3040, 660))
]

w_box = 1000
for title, sub, desc, (cx, cy) in nodes_t2:
    draw_a.rectangle([(cx - w_box//2, cy), (cx + w_box//2, cy + 300)], fill=(16, 26, 42), outline=(255, 193, 7), width=2)
    draw_a.rectangle([(cx - w_box//2, cy), (cx + w_box//2, cy + 60)], fill=(180, 120, 10))
    draw_a.text((cx - w_box//2 + 20, cy + 18), title, fill=(255, 255, 255), font=font_body_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 85), sub, fill=gold, font=font_body_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 130), desc, fill=(220, 230, 245), font=font_body)
    draw_a.text((cx - w_box//2 + 20, cy + 190), "Forensic Countermeasure:", fill=(255, 107, 107), font=font_small_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 225), "Proving de facto control as 'protector' to pierce foundation veil.", fill=(200, 215, 235), font=font_body)
    draw_a.line([(cx, cy + 300), (cx, cy + 390)], fill=gold, width=4)

# Tier 3 (Three Identified Tangible Asset Stores)
nodes_t3 = [
    ("STORE 3A: PRIME REAL ESTATE", "London & New York Properties", "Luxury commercial and residential penthouses held via offshore LLCs.", (800, 1050)),
    ("STORE 3B: MARITIME & AVIATION", "Superyachts & Private Jets", "Flagged in open registries, chartered back to true debtor.", (1920, 1050)),
    ("STORE 3C: BULLION DEPOSITORIES", "Physical Gold Freeports", "Allocated pure gold bars stored in duty-free high-security vaults.", (3040, 1050))
]

for title, sub, desc, (cx, cy) in nodes_t3:
    draw_a.rectangle([(cx - w_box//2, cy), (cx + w_box//2, cy + 300)], fill=(12, 32, 44), outline=(23, 162, 184), width=2)
    draw_a.rectangle([(cx - w_box//2, cy), (cx + w_box//2, cy + 60)], fill=(19, 78, 94))
    draw_a.text((cx - w_box//2 + 20, cy + 18), title, fill=(255, 255, 255), font=font_body_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 85), sub, fill=(23, 162, 184), font=font_body_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 130), desc, fill=(200, 230, 245), font=font_body)
    draw_a.text((cx - w_box//2 + 20, cy + 190), "Evidentiary Linkage:", fill=gold, font=font_small_bold)
    draw_a.text((cx - w_box//2 + 20, cy + 225), "Deed signatures, flight logs, and vessel berth records direct to target.", fill=(200, 230, 245), font=font_body)
    draw_a.line([(cx, cy + 300), (cx, cy + 390)], fill=(40, 167, 69), width=4)

# Tier 4 (Bottom Broad Span): Judicial Enforcement & Freezing Matrix (Green)
draw_a.rectangle([(200, 1440), (3640, 1980)], fill=(10, 28, 22), outline=(40, 167, 69), width=3)
draw_a.rectangle([(220, 1460), (740, 1515)], fill=(25, 120, 50))
draw_a.text((235, 1475), "TIER 4: JUDICIAL ENFORCEMENT & ASSET ATTACHMENT", fill=(255, 255, 255), font=font_body_bold)

draw_a.text((220, 1540), "COORDINATED MULTI-JURISDICTIONAL RECOVERY PROTOCOLS:", fill=gold, font=font_h2)

draw_a.text((220, 1600), "1. English High Court Worldwide Freezing Order (WFO):", fill=(240, 255, 245), font=font_body_bold)
draw_a.text((220, 1635), "Immobilizing debtor's global assets up to value of judgment claim; penal notices enforce cross-border bank compliance.", fill=(200, 235, 215), font=font_body)

draw_a.text((220, 1700), "2. U.S. 28 U.S.C. Section 1782 Federal Discovery:", fill=(240, 255, 245), font=font_body_bold)
draw_a.text((220, 1735), "Subpoenaing New York correspondent clearing banks for international wire clearing trails and beneficiary statements.", fill=(200, 235, 215), font=font_body)

draw_a.text((220, 1800), "3. Norwich Pharmacal & Bankers Trust Orders:", fill=(240, 255, 245), font=font_body_bold)
draw_a.text((220, 1835), "Compelling offshore registered agents and local banking institutions to surrender identity of true underlying beneficial owner.", fill=(200, 235, 215), font=font_body)

draw_a.text((220, 1910), "[OUTCOME: SIMULTANEOUS GLOBAL RESTRAINT OF ASSETS // LIQUIDATION & REPATRIATION TO CREDITOR]", fill=gold, font=font_mono)

save_dual(im_asset, "blog-detail-featured-asset-recovery.jpg")

print("\nALL 3 DISTINCT DIAGRAMS GENERATED AND SYNCHRONIZED!")
