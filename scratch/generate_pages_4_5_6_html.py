import os, shutil

workspace = r"c:\Users\thand\Desktop\Website"
template_dir = r"c:\Users\thand\Desktop\Website\veritas-intelligence-template"

# -----------------------------------------------------------------------------
# Common template parts
# -----------------------------------------------------------------------------
header_html = """<!DOCTYPE html>
<html lang="en" data-bs-theme="light" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{PAGE_TITLE} — Veritas Intelligence</title>
  <meta name="description" content="{META_DESC}">
  <meta name="keywords" content="{META_KEYWORDS}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{PAGE_TITLE}">
  <meta property="og:description" content="{META_DESC}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="{FEATURED_IMG}">
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  
  <!-- Stylesheets -->
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/bootstrap-icons.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="assets/css/rtl.css">

  <script>
    (function () {
      const theme = localStorage.getItem('itserve_theme') || localStorage.getItem('itSupportTheme') || 'light';
      document.documentElement.setAttribute('data-bs-theme', theme);
      const dir = localStorage.getItem('itserve_direction') || localStorage.getItem('itSupportRTL') || 'ltr';
      document.documentElement.setAttribute('dir', dir);
    })();
  </script>
</head>
<body>

  <!-- Navigation -->
  <header>
    <nav class="navbar navbar-expand-lg navbar-veritas" aria-label="Main navigation">
      <div class="container">
        <a class="navbar-brand" href="index.html">
          <img src="assets/images/logo.svg" data-light-src="assets/images/logo.svg" data-dark-src="assets/images/logo-light.svg" alt="Veritas Intelligence Logo" class="navbar-brand-logo" width="220" height="44">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarMain">
          <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Home <i class="bi bi-chevron-down nav-chevron"></i>
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="index.html"><i class="bi bi-building me-2 text-gold"></i> Corporate Investigations</a></li>
                <li><a class="dropdown-item" href="index-2.html"><i class="bi bi-cpu me-2 text-gold"></i> Corporate Intelligence</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="about.html">About Us</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Services <i class="bi bi-chevron-down nav-chevron"></i>
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="services.html"><i class="bi bi-grid-3x3-gap me-2 text-gold"></i> All Practice Areas</a></li>
                <li><hr class="dropdown-divider my-1"></li>
                <li><a class="dropdown-item" href="service-corporate-investigations.html"><i class="bi bi-search me-2 text-gold"></i> Corporate Investigations</a></li>
                <li><a class="dropdown-item" href="service-executive-screening.html"><i class="bi bi-person-check me-2 text-gold"></i> Executive Screening</a></li>
                <li><a class="dropdown-item" href="service-ma-due-diligence.html"><i class="bi bi-briefcase me-2 text-gold"></i> M&amp;A Due Diligence</a></li>
                <li><a class="dropdown-item" href="service-fraud-misconduct.html"><i class="bi bi-file-earmark-lock me-2 text-gold"></i> Fraud &amp; Misconduct</a></li>
                <li><a class="dropdown-item" href="service-vendor-risk.html"><i class="bi bi-shield-check me-2 text-gold"></i> Vendor Risk Management</a></li>
                <li><a class="dropdown-item" href="service-corporate-intelligence.html"><i class="bi bi-cpu me-2 text-gold"></i> Corporate Intelligence</a></li>
                <li><a class="dropdown-item" href="service-litigation-support.html"><i class="bi bi-journal-bookmark me-2 text-gold"></i> Litigation Support</a></li>
                <li><a class="dropdown-item" href="service-asset-tracing.html"><i class="bi bi-graph-up-arrow me-2 text-gold"></i> Asset Tracing &amp; Recovery</a></li>
                <li><a class="dropdown-item" href="service-cyber-investigations.html"><i class="bi bi-shield-lock me-2 text-gold"></i> Cyber Risk &amp; Digital Forensics</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="pricing.html">Pricing</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Insights <i class="bi bi-chevron-down nav-chevron"></i>
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="blog.html"><i class="bi bi-journal-text me-2 text-gold"></i> Intelligence Briefings (Blog)</a></li>
                <li><a class="dropdown-item active" href="blog-details.html"><i class="bi bi-file-text me-2 text-gold"></i> Case Analysis (Blog Details)</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="contact.html">Contact</a>
            </li>
          </ul>

          <div class="d-flex align-items-center gap-2 navbar-nav-cta">
            <!-- Theme Toggle -->
            <button class="btn-control-toggle theme-toggle-btn" type="button" aria-label="Toggle dark/light theme" title="Toggle Theme">
              <i class="bi bi-moon-stars-fill"></i>
            </button>
            <!-- RTL Toggle -->
            <button class="btn-control-toggle btn-rtl-toggle rtl-toggle-btn" type="button" aria-label="Toggle RTL layout" title="Toggle RTL">
              <span class="rtl-btn-text">RTL</span>
            </button>
            <a href="contact.html" class="btn btn-gold btn-sm">
              <i class="bi bi-lock-fill"></i> Discuss a Case
            </a>
          </div>
        </div>
      </div>
    </nav>
  </header>
"""

footer_html = """
  <!-- Global Footer -->
  <footer class="footer-veritas" aria-label="Global footer">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4 col-md-6">
          <a href="index.html" class="navbar-brand footer-brand d-inline-block mb-3" aria-label="Veritas Intelligence Home">
            <img src="assets/images/logo.svg" data-light-src="assets/images/logo.svg" data-dark-src="assets/images/logo-light.svg" alt="Veritas Intelligence Logo" class="navbar-brand-logo footer-brand-logo" width="220" height="44">
          </a>
          <p class="footer-brand-desc">
            Veritas Intelligence is an international corporate investigation, forensic intelligence, and due diligence consultancy advising corporate leadership, boards of directors, and global legal counsel.
          </p>
          <div class="d-flex gap-2">
            <span class="badge bg-dark border border-secondary text-light small"><i class="bi bi-shield-check text-gold"></i> ISO 27001 Certified Protocols</span>
          </div>
          <div class="footer-social-links">
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="btn-social" aria-label="LinkedIn" title="LinkedIn">
              <i class="bi bi-linkedin"></i>
            </a>
            <a href="https://x.com" target="_blank" rel="noopener noreferrer" class="btn-social" aria-label="X (formerly Twitter)" title="X">
              <i class="bi bi-twitter-x"></i>
            </a>
            <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="btn-social" aria-label="YouTube" title="YouTube">
              <i class="bi bi-youtube"></i>
            </a>
            <a href="mailto:inquiries@veritasintelligence.com" class="btn-social" aria-label="Confidential Email" title="Confidential Email">
              <i class="bi bi-envelope-fill"></i>
            </a>
          </div>
        </div>

        <div class="col-lg-2 col-md-6">
          <h4 class="footer-col-title">Navigation</h4>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Veritas</a></li>
            <li><a href="services.html">Practice Areas</a></li>
            <li><a href="pricing.html">Fee Structures</a></li>
            <li><a href="blog.html">Briefings &amp; Insights</a></li>
            <li><a href="contact.html">Confidential Intake</a></li>
          </ul>
        </div>

        <div class="col-lg-3 col-md-6">
          <h4 class="footer-col-title">Practice Areas</h4>
          <ul class="footer-links">
            <li><a href="service-corporate-investigations.html">Corporate Investigations</a></li>
            <li><a href="service-executive-screening.html">Executive Integrity Screening</a></li>
            <li><a href="service-ma-due-diligence.html">M&amp;A Due Diligence</a></li>
            <li><a href="service-fraud-misconduct.html">Fraud &amp; Financial Misconduct</a></li>
            <li><a href="service-vendor-risk.html">Vendor Risk Management</a></li>
            <li><a href="service-asset-tracing.html">Asset Tracing &amp; Recovery</a></li>
          </ul>
        </div>

        <div class="col-lg-3 col-md-6">
          <h4 class="footer-col-title">Confidential Intake</h4>
          <div class="footer-contact-item">
            <i class="bi bi-geo-alt-fill text-gold flex-shrink-0"></i>
            <span>100 Bishopsgate, Level 24, London EC2N 4AG, United Kingdom</span>
          </div>
          <div class="footer-contact-item">
            <i class="bi bi-shield-lock-fill text-gold flex-shrink-0"></i>
            <span>Emergency Operations: +44 20 7946 0912</span>
          </div>
          <div class="footer-contact-item">
            <i class="bi bi-key-fill text-gold flex-shrink-0"></i>
            <span>Secure Inquiries: pgp@veritasintelligence.com</span>
          </div>
          <a href="contact.html" class="btn btn-outline-gold btn-sm mt-2 w-100">
            <i class="bi bi-lock-fill me-1"></i> Open Encrypted Intake
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="mb-0">&copy; 2026 Veritas Intelligence Ltd. All rights reserved. Operating under strict attorney-client privilege protocols and international compliance standards.</p>
        <div class="d-flex gap-3 justify-content-center mt-2 mt-md-0">
          <a href="contact.html" class="text-muted text-decoration-none small">Confidentiality Agreement</a>
          <span class="text-muted small">&bull;</span>
          <a href="contact.html" class="text-muted text-decoration-none small">Security Protocols</a>
          <span class="text-muted small">&bull;</span>
          <a href="contact.html" class="text-muted text-decoration-none small">Terms of Engagement</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

# =============================================================================
# Page 4: blog-details-sanctions.html
# =============================================================================
page_4_body = """
  <main id="main-content">
    <!-- Article Header Hero -->
    <section class="page-hero" aria-label="Article header">
      <img src="assets/images/hero/hero-blog-details-sanctions.jpg" alt="Commercial maritime container shipping vessel entering international deepwater port terminal for sanctions and export control vetting" class="page-hero-img" width="3840" height="2160">
      <div class="container page-hero-content">
        <span class="badge-gold mb-3">Compliance &amp; Trade Sanctions</span>
        <h1 class="display-5 fw-bold mb-3">Navigating Secondary Sanctions &amp; Third-Party Vendor Risk in 2026</h1>
        <div class="d-flex flex-wrap align-items-center gap-3 text-light text-opacity-75 small mb-0">
          <span><i class="bi bi-person-fill text-gold me-1"></i> Amira Khalil, Head of Global Sanctions &amp; Trade Compliance</span>
          <span>&bull;</span>
          <span><i class="bi bi-calendar3 text-gold me-1"></i> July 2026</span>
          <span>&bull;</span>
          <span><i class="bi bi-clock text-gold me-1"></i> 5 min read</span>
          <span>&bull;</span>
          <span class="badge bg-secondary-subtle text-secondary">Sanctions Practice</span>
        </div>
      </div>
    </section>

    <!-- Article Content & Sidebar -->
    <section class="section-padding" aria-label="Article content">
      <div class="container">
        <div class="row g-5">
          <!-- Main Editorial Body (Left 8 cols) -->
          <article class="col-lg-8">
            <!-- Featured Photographic Asset -->
            <div class="mb-4">
              <img src="assets/images/blog/blog-detail-featured-sanctions.jpg" alt="Figure 1: Multi-Tier Secondary Sanctions Evasion and Transshipment Intermediary Matrix detailing prohibited exporters, free trade zone hubs, and maritime telemetry" class="img-fluid rounded border shadow-sm w-100" width="3840" height="2160">
              <small class="text-muted d-block mt-2 fst-italic">Figure 1: Multi-Tier Secondary Sanctions Evasion &amp; Transshipment Intermediary Matrix &ndash; unmasking re-export hubs, dark fleet maritime vectors, and falsified bills of lading.</small>
            </div>

            <!-- Lead Paragraph -->
            <p class="lead text-secondary">
              The enforcement landscape for global sanctions has undergone a structural transformation. Regulatory authorities—including the U.S. Department of the Treasury’s Office of Foreign Assets Control (OFAC), the UK Office of Financial Sanctions Implementation (OFSI), and the European Commission—are aggressively penalizing corporate counterparties who participate in indirect or secondary evasion schemes.
            </p>

            <p class="text-muted">
              For multinational corporations, compliance officers, and general counsel, conventional automated database screening is no longer defensible. Sophisticated illicit supply networks bypass direct restrictions by deploying layered intermediaries, free trade zone transshipment conduits, and deceptive maritime trade practices engineered to conceal sanctioned origin and beneficial ownership.
            </p>

            <!-- Table of Contents -->
            <div class="p-4 bg-surface border rounded my-4">
              <h3 class="h6 text-uppercase tracking-wider text-gold mb-3"><i class="bi bi-list-nested me-2"></i> Table of Contents</h3>
              <ol class="small text-muted mb-0 ps-3">
                <li class="mb-1"><a href="#section-landscape" class="text-decoration-none text-secondary">1. The Expanding Web of Secondary Sanctions &amp; Intermediary Evasion</a></li>
                <li class="mb-1"><a href="#section-transshipment" class="text-decoration-none text-secondary">2. Transshipment Hub Telemetry: Free Trade Zones &amp; Relabeling</a></li>
                <li class="mb-1"><a href="#section-maritime" class="text-decoration-none text-secondary">3. Dark Fleet Maritime Vectors: AIS Spoofing &amp; High-Seas Transfers</a></li>
                <li class="mb-1"><a href="#section-defensible" class="text-decoration-none text-secondary">4. Defensible Vendor Audits &amp; Regulatory Safe Harbor Protection</a></li>
              </ol>
            </div>

            <!-- Section 1 -->
            <h2 class="h4 mt-5 mb-3" id="section-landscape">1. The Expanding Web of Secondary Sanctions &amp; Intermediary Evasion</h2>
            <p class="text-muted">
              Under modern secondary sanctions regimes, non-U.S. and non-EU entities risk complete exclusion from Western correspondent banking and clearing systems if they facilitate material transactions for designated targets. Prohibited parties evade primary restrictions by incorporating front companies in non-aligned jurisdictions—including the UAE, Central Asia, and Southeast Asia.
            </p>
            <p class="text-muted">
              These entities maintain nominal corporate officers, generic commercial registrations, and bank accounts in mid-tier financial centers. However, their sole economic objective is acquiring restricted dual-use components, industrial machinery, or high-technology items on behalf of designated military-industrial conglomerates.
            </p>

            <!-- Strategic Callout -->
            <div class="p-4 bg-surface border-start border-gold border-4 rounded my-4">
              <h3 class="h5 mb-2"><i class="bi bi-exclamation-triangle text-gold me-2"></i> Enforcement Alert for Corporate Counsel</h3>
              <p class="small text-muted mb-0">
                Regulatory bodies enforce strict liability standards. Claiming ignorance of an intermediary's undisclosed Russian, Iranian, or DPRK end-user does not insulate an exporter or vendor from multi-million dollar penalties or criminal prosecution if red flags were commercially identifiable.
              </p>
            </div>

            <!-- Section 2 -->
            <h2 class="h4 mt-5 mb-3" id="section-transshipment">2. Transshipment Hub Telemetry: Free Trade Zones &amp; Relabeling</h2>
            <p class="text-muted">
              A primary vector in illicit trade diversion occurs within customs-bonded free trade zones (FTZs). Goods enter an FTZ under compliant export paperwork, where the original commercial invoices and bills of lading are systematically cancelled and reissued.
            </p>
            <p class="text-muted">
              Transshipment brokers frequently alter the Harmonized System (HS) commodity codes to mischaracterize high-priority export control items as benign commercial equipment. Minimal repacking or cosmetic alterations are then used to manufacture fraudulent certificates of origin, obscuring the product's ultimate chain of custody.
            </p>

            <!-- Key Risk Indicators Table -->
            <div class="table-responsive my-4">
              <table class="table table-bordered table-hover align-middle">
                <thead class="table-dark">
                  <tr>
                    <th>Evasion Vector</th>
                    <th>Observable Red Flag</th>
                    <th>Veritas Forensic Counter-Measure</th>
                  </tr>
                </thead>
                <tbody class="small">
                  <tr>
                    <td><strong>Nominee Intermediary</strong></td>
                    <td>Newly registered LLC with no verifiable commercial footprint or digital existence.</td>
                    <td>Comprehensive OSINT registry genealogy &amp; physical site substantiation.</td>
                  </tr>
                  <tr>
                    <td><strong>Circular Bill of Lading</strong></td>
                    <td>Consignee listed as offshore logistics agent rather than operating industrial manufacturer.</td>
                    <td>Customs manifest reconstruction &amp; ultimate receiver verification.</td>
                  </tr>
                  <tr>
                    <td><strong>Unusual Remittance Route</strong></td>
                    <td>Wire transfers originating from third-party currency exchanges or obscure offshore accounts.</td>
                    <td>SWIFT wire provenance tracking &amp; financial nexus deconstruction.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Section 3 -->
            <h2 class="h4 mt-5 mb-3" id="section-maritime">3. Dark Fleet Maritime Vectors: AIS Spoofing &amp; High-Seas Transfers</h2>
            <p class="text-muted">
              In maritime commodity and industrial transit, sanctions evaders utilize "dark fleet" tactics. Vessels deliberately disable Automatic Identification System (AIS) transponders when transiting sensitive maritime corridors or generate false GPS coordinates (AIS spoofing) to disguise docking at sanctioned terminals.
            </p>
            <p class="text-muted">
              Ship-to-ship (STS) cargo transfers are conducted in international waters outside normal coastal jurisdiction, followed by frequent changes of flag-of-convenience registries and ownership transfers among single-ship special purpose vehicles (SPVs).
            </p>

            <!-- Section 4 -->
            <h2 class="h4 mt-5 mb-3" id="section-defensible">4. Defensible Vendor Audits &amp; Regulatory Safe Harbor Protection</h2>
            <p class="text-muted">
              To establish defensible regulatory compliance under OFAC and EU frameworks, organizations must demonstrate that their vendor vetting procedures go beyond passive database lookups. An investigative compliance protocol must combine deep corporate registry extraction, beneficial ownership deconstruction, and real-time shipping telemetry verification.
            </p>
            <p class="text-muted">
              Veritas Intelligence provides institutional clients with certified evidentiary audits that satisfy regulatory safe harbor requirements, arming general counsel with rigorous documentation to contest regulatory enforcement actions or terminate hazardous vendor relationships without commercial dispute.
            </p>

            <!-- Social Share Bar -->
            <div class="p-3 bg-surface border rounded mt-5 d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div class="d-flex align-items-center gap-2">
                <span class="small fw-bold text-muted">Share Briefing:</span>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Link copied to clipboard'); return false;"><i class="bi bi-link-45deg"></i> Copy Link</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: LinkedIn share dialog'); return false;"><i class="bi bi-linkedin"></i> LinkedIn</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Email share intent'); return false;"><i class="bi bi-envelope"></i> Email</a>
              </div>
              <div class="small text-muted">
                Document Reference: #BRIEF-2026-SANCTIONS-VEND
              </div>
            </div>

            <!-- Author Bio Card -->
            <div class="p-4 bg-surface border rounded mt-4">
              <div class="d-flex align-items-center gap-3">
                <img src="assets/images/team/team-amira-khalil.jpg" alt="Amira Khalil, Head of Global Sanctions &amp; Trade Compliance" class="rounded-circle border" width="72" height="72" style="object-fit: cover;">
                <div>
                  <h3 class="h5 mb-1">About Amira Khalil</h3>
                  <div class="small text-gold mb-1">Head of Global Sanctions &amp; Trade Compliance, Dubai &ndash; London</div>
                  <p class="small text-muted mb-0">
                    Amira advises multinational corporate boards, commercial lenders, and international energy traders on trade controls, secondary sanctions, and third-party risk mitigation across the Middle East, Central Asia, and Europe.
                  </p>
                </div>
              </div>
            </div>
          </article>

          <!-- Sidebar (Right 4 cols) -->
          <aside class="col-lg-4" aria-label="Sidebar">
            <div class="sidebar-sticky-wrap">
              <!-- Contact Inquiry Callout -->
              <div class="card-veritas p-4 mb-4">
                <span class="badge-gold mb-2">Practice Advisory</span>
                <h3 class="h5 mb-2">Commission Vendor Risk Review</h3>
                <p class="small text-muted mb-3">
                  Evaluating high-risk international suppliers, logistics intermediaries, or freight forwarding counterparties? Speak confidentially with our sanctions intelligence practice.
                </p>
                <a href="contact.html" class="btn btn-gold btn-sm w-100">
                  <i class="bi bi-shield-lock-fill me-1"></i> Request Confidential Consultation
                </a>
              </div>

              <!-- Related Insights -->
              <div class="card-veritas p-4 mb-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Related Briefings</h3>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Due Diligence</span>
                  <h4 class="h6 mb-1"><a href="blog-details.html" class="text-decoration-none text-dark dark-text-light">Uncovering Hidden Beneficial Ownership in Complex Offshore Vehicles</a></h4>
                  <small class="text-muted">October 2026 &bull; 6 min read</small>
                </div>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Risk Management</span>
                  <h4 class="h6 mb-1"><a href="blog-details-ma-diligence.html" class="text-decoration-none text-dark dark-text-light">Red Flags in Cross-Border M&amp;A: Beyond Standard Financial Audits</a></h4>
                  <small class="text-muted">September 2026 &bull; 8 min read</small>
                </div>
                <div>
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Corporate Intelligence</span>
                  <h4 class="h6 mb-1"><a href="blog-details-osint-litigation.html" class="text-decoration-none text-dark dark-text-light">The Role of Open-Source Intelligence in High-Stakes Commercial Litigation</a></h4>
                  <small class="text-muted">June 2026 &bull; 9 min read</small>
                </div>
              </div>

              <!-- Topic Tags -->
              <div class="card-veritas p-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Practice Tags</h3>
                <div class="d-flex flex-wrap gap-2">
                  <span class="badge bg-surface border text-secondary">#SanctionsCompliance</span>
                  <span class="badge bg-surface border text-secondary">#VendorRiskManagement</span>
                  <span class="badge bg-surface border text-secondary">#SecondarySanctions</span>
                  <span class="badge bg-surface border text-secondary">#SupplyChainVetting</span>
                  <span class="badge bg-surface border text-secondary">#TradeCompliance</span>
                  <span class="badge bg-surface border text-secondary">#MaritimeTelemetry</span>
                </div>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- Sanctions Spotlight Card -->
    <section class="section-padding-sm bg-surface border-top" aria-label="Call to action">
      <div class="container">
        <div class="cta-spotlight-card">
          <div class="row align-items-stretch g-4 g-lg-5">
            <div class="col-lg-6">
              <div class="cta-spotlight-content">
                <span class="cta-pill-badge mb-3"><i class="bi bi-shield-check"></i> Trade Integrity Engagement</span>
                <h2 class="cta-spotlight-title mb-3">Commission Rapid Vendor &amp; Sanctions Due Diligence</h2>
                <p class="cta-spotlight-desc mb-4">
                  Deploy specialist trade compliance investigators and forensic data analysts to vet critical international vendors, logistics intermediaries, and supply chains against secondary sanctions exposure.
                </p>
                <div class="cta-spotlight-metrics mb-4">
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Deployment Window</span>
                    <strong class="cta-metric-value">24&ndash;48 Hours Post-Mandate</strong>
                  </div>
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Regulatory Standard</span>
                    <strong class="cta-metric-value">OFAC, EU &amp; OFSI Defensible</strong>
                  </div>
                </div>
                <div class="d-flex flex-wrap gap-3">
                  <a href="contact.html" class="btn btn-gold btn-lg">
                    <i class="bi bi-chat-text-fill"></i> Initiate Scoping Call
                  </a>
                  <a href="service-vendor-risk.html" class="btn btn-outline-white btn-lg btn-white">
                    <i class="bi bi-shield-check"></i> Explore Vendor Practice
                  </a>
                </div>
              </div>
            </div>
            <div class="col-lg-6 cta-spotlight-img-col">
              <div class="cta-spotlight-img-wrap">
                <img src="assets/images/banners/banner-blog-details-sanctions.jpg" alt="Commercial cargo port terminal with gantry cranes and shipping vessels under customs and sanctions compliance inspection" class="cta-spotlight-img" width="3840" height="2160" loading="lazy">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

# =============================================================================
# Page 5: blog-details-osint-litigation.html
# =============================================================================
page_5_body = """
  <main id="main-content">
    <!-- Article Header Hero -->
    <section class="page-hero" aria-label="Article header">
      <img src="assets/images/hero/hero-blog-details-osint.jpg" alt="Global satellite telecommunications and planetary cyber intelligence network nodes displaying open-source investigative telemetry" class="page-hero-img" width="3840" height="2160">
      <div class="container page-hero-content">
        <span class="badge-gold mb-3">Corporate Intelligence &amp; Trial Evidence</span>
        <h1 class="display-5 fw-bold mb-3">The Role of Open-Source Intelligence in High-Stakes Commercial Litigation</h1>
        <div class="d-flex flex-wrap align-items-center gap-3 text-light text-opacity-75 small mb-0">
          <span><i class="bi bi-person-fill text-gold me-1"></i> Sophia Chen, Director of OSINT &amp; Litigation Intelligence</span>
          <span>&bull;</span>
          <span><i class="bi bi-calendar3 text-gold me-1"></i> June 2026</span>
          <span>&bull;</span>
          <span><i class="bi bi-clock text-gold me-1"></i> 9 min read</span>
          <span>&bull;</span>
          <span class="badge bg-secondary-subtle text-secondary">Litigation Practice</span>
        </div>
      </div>
    </section>

    <!-- Article Content & Sidebar -->
    <section class="section-padding" aria-label="Article content">
      <div class="container">
        <div class="row g-5">
          <!-- Main Editorial Body (Left 8 cols) -->
          <article class="col-lg-8">
            <!-- Featured Photographic Asset -->
            <div class="mb-4">
              <img src="assets/images/blog/blog-detail-featured-osint.jpg" alt="Figure 1: Cross-Border OSINT Triangulation and Court-Admissible Evidentiary Protocol detailing raw data intake, forensic timestamping, de-anonymization, and trial exhibits" class="img-fluid rounded border shadow-sm w-100" width="3840" height="2160">
              <small class="text-muted d-block mt-2 fst-italic">Figure 1: Cross-Border OSINT Triangulation &amp; Court-Admissible Evidentiary Protocol &ndash; transforming web fragments, registry filings, and satellite breadcrumbs into defensible trial exhibits.</small>
            </div>

            <!-- Lead Paragraph -->
            <p class="lead text-secondary">
              In complex commercial disputes, international arbitrations, and cross-border fraud claims, litigation counsel frequently confront adversaries who utilize offshore secrecy jurisdictions, nominee directors, and deliberately fragmented digital footprints to obscure material facts and assets.
            </p>

            <p class="text-muted">
              While open-source intelligence (OSINT) was once regarded as an informal research technique, contemporary dispute strategy requires a rigorous, forensically defensible methodology. Transforming publicly accessible web fragments, historical corporate registries, satellite telemetry, and social relationship graphs into court-admissible evidence demands strict evidentiary chain-of-custody protocols.
            </p>

            <!-- Table of Contents -->
            <div class="p-4 bg-surface border rounded my-4">
              <h3 class="h6 text-uppercase tracking-wider text-gold mb-3"><i class="bi bi-list-nested me-2"></i> Table of Contents</h3>
              <ol class="small text-muted mb-0 ps-3">
                <li class="mb-1"><a href="#section-arch" class="text-decoration-none text-secondary">1. Beyond Search Engines: The Forensic Architecture of Modern OSINT</a></li>
                <li class="mb-1"><a href="#section-chain" class="text-decoration-none text-secondary">2. Cryptographic Evidence Preservation &amp; Chain-of-Custody Integrity</a></li>
                <li class="mb-1"><a href="#section-linking" class="text-decoration-none text-secondary">3. Cross-Docket Disambiguation &amp; Piercing Nominee Networks</a></li>
                <li class="mb-1"><a href="#section-admissibility" class="text-decoration-none text-secondary">4. Defeating Hearsay Challenges: FRE Rule 902(11) Self-Authenticating Records</a></li>
              </ol>
            </div>

            <!-- Section 1 -->
            <h2 class="h4 mt-5 mb-3" id="section-arch">1. Beyond Search Engines: The Forensic Architecture of Modern OSINT</h2>
            <p class="text-muted">
              Commercial litigation OSINT is fundamentally distinct from conventional internet searches. It involves systematic querying across specialized, multi-jurisdictional databases: gazette notices, maritime AIS vessel tracking, aircraft transponder archives (ADS-B), real property deeds, patent registers, and deep web archives.
            </p>
            <p class="text-muted">
              Adversaries often attempt to sanitize digital trails upon the initiation of disputes. Forensic OSINT investigators capture historical snapshots, recover altered regulatory disclosures, and cross-index digital footprints across non-traditional platforms to reconstruct events with chronological exactitude.
            </p>

            <!-- Strategic Callout -->
            <div class="p-4 bg-surface border-start border-gold border-4 rounded my-4">
              <h3 class="h5 mb-2"><i class="bi bi-shield-check text-gold me-2"></i> Evidentiary Standard for Trial Teams</h3>
              <p class="small text-muted mb-0">
                A screenshot is not evidence. Unverified digital grabs are routinely struck down in commercial courtrooms on authentication or hearsay grounds. Every digital exhibit must be captured with cryptographic hash signatures, RFC 3161 timestamps, and complete HTTP header records.
              </p>
            </div>

            <!-- Section 2 -->
            <h2 class="h4 mt-5 mb-3" id="section-chain">2. Cryptographic Evidence Preservation &amp; Chain-of-Custody Integrity</h2>
            <p class="text-muted">
              Under Federal Rule of Evidence 902(13) and 902(14) in the United States—and equivalent common-law principles in the UK High Court and Singapore International Commercial Court—electronic evidence generated by an electronic process or system can be authenticated through written certification by a qualified forensic custodian.
            </p>
            <p class="text-muted">
              Veritas Intelligence utilizes dedicated forensic capture workstations that archive digital material directly into standardized WARC (Web ARChive) containers, computing SHA-256 cryptographic hashes immediately upon intake. Third-party RFC 3161 cryptographic timestamp tokens are affixed to establish immutable proof that the data existed in an identical state at the precise second of capture.
            </p>

            <!-- Section 3 -->
            <h2 class="h4 mt-5 mb-3" id="section-linking">3. Cross-Docket Disambiguation &amp; Piercing Nominee Networks</h2>
            <p class="text-muted">
              Fraudulent actors deliberately employ common aliases, corporate formations with overlapping names, or professional nominees to defeat crude automated database searches. Our OSINT specialists employ link analysis and entity resolution algorithms to cross-reference corporate officers across disparate registers worldwide.
            </p>
            <p class="text-muted">
              By correlating shared registered office addresses, legal agents, phone number prefixes, and corporate formation dates, we establish conclusive corporate alter-ego relationships that provide trial counsel with the factual predicate necessary to pierce the corporate veil.
            </p>

            <!-- Section 4 -->
            <h2 class="h4 mt-5 mb-3" id="section-admissibility">4. Defeating Hearsay Challenges: FRE Rule 902(11) Self-Authenticating Records</h2>
            <p class="text-muted">
              The ultimate utility of commercial intelligence is measured by its performance during judicial examination. Our partners regularly author sworn expert affidavits and witness statements detailing our investigation tradecraft, search parameters, and chain-of-custody documentation.
            </p>
            <p class="text-muted">
              By packaging raw OSINT findings into structured, indexed trial compendiums supported by custodian certifications under FRE 902(11), we ensure that critical evidence is admitted without the delay and expense of calling individual foreign registry clerks or web administrators to testify.
            </p>

            <!-- Social Share Bar -->
            <div class="p-3 bg-surface border rounded mt-5 d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div class="d-flex align-items-center gap-2">
                <span class="small fw-bold text-muted">Share Briefing:</span>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Link copied to clipboard'); return false;"><i class="bi bi-link-45deg"></i> Copy Link</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: LinkedIn share dialog'); return false;"><i class="bi bi-linkedin"></i> LinkedIn</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Email share intent'); return false;"><i class="bi bi-envelope"></i> Email</a>
              </div>
              <div class="small text-muted">
                Document Reference: #BRIEF-2026-OSINT-LIT
              </div>
            </div>

            <!-- Author Bio Card -->
            <div class="p-4 bg-surface border rounded mt-4">
              <div class="d-flex align-items-center gap-3">
                <img src="assets/images/team/team-sophia-chen.jpg" alt="Sophia Chen, Director of OSINT &amp; Litigation Intelligence" class="rounded-circle border" width="72" height="72" style="object-fit: cover;">
                <div>
                  <h3 class="h5 mb-1">About Sophia Chen</h3>
                  <div class="small text-gold mb-1">Director of OSINT &amp; Litigation Intelligence, London &ndash; New York</div>
                  <p class="small text-muted mb-0">
                    Sophia specializes in complex digital evidentiary recovery, cross-border corporate intelligence, and OSINT tradecraft for major commercial litigation practices, arbitration boutiques, and multi-jurisdictional judgment creditors.
                  </p>
                </div>
              </div>
            </div>
          </article>

          <!-- Sidebar (Right 4 cols) -->
          <aside class="col-lg-4" aria-label="Sidebar">
            <div class="sidebar-sticky-wrap">
              <!-- Contact Inquiry Callout -->
              <div class="card-veritas p-4 mb-4">
                <span class="badge-gold mb-2">Practice Advisory</span>
                <h3 class="h5 mb-2">Consult on Litigation Evidence</h3>
                <p class="small text-muted mb-3">
                  Preparing for high-stakes commercial litigation, international arbitration, or worldwide freezing proceedings? Retain our evidence specialists.
                </p>
                <a href="contact.html" class="btn btn-gold btn-sm w-100">
                  <i class="bi bi-shield-lock-fill me-1"></i> Request Confidential Consultation
                </a>
              </div>

              <!-- Related Insights -->
              <div class="card-veritas p-4 mb-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Related Briefings</h3>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Due Diligence</span>
                  <h4 class="h6 mb-1"><a href="blog-details.html" class="text-decoration-none text-dark dark-text-light">Uncovering Hidden Beneficial Ownership in Complex Offshore Vehicles</a></h4>
                  <small class="text-muted">October 2026 &bull; 6 min read</small>
                </div>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Fraud Prevention</span>
                  <h4 class="h6 mb-1"><a href="blog-details-whistleblower.html" class="text-decoration-none text-dark dark-text-light">Conducting Defensible Internal Investigations Under Whistleblower Protections</a></h4>
                  <small class="text-muted">August 2026 &bull; 7 min read</small>
                </div>
                <div>
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Asset Recovery</span>
                  <h4 class="h6 mb-1"><a href="blog-details-asset-recovery.html" class="text-decoration-none text-dark dark-text-light">Tracing Dissipated Sovereign &amp; Corporate Assets Across Multi-Jurisdictional Hubs</a></h4>
                  <small class="text-muted">May 2026 &bull; 8 min read</small>
                </div>
              </div>

              <!-- Topic Tags -->
              <div class="card-veritas p-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Practice Tags</h3>
                <div class="d-flex flex-wrap gap-2">
                  <span class="badge bg-surface border text-secondary">#LitigationSupport</span>
                  <span class="badge bg-surface border text-secondary">#OSINT</span>
                  <span class="badge bg-surface border text-secondary">#TrialEvidence</span>
                  <span class="badge bg-surface border text-secondary">#FRE90211</span>
                  <span class="badge bg-surface border text-secondary">#CorporateIntelligence</span>
                  <span class="badge bg-surface border text-secondary">#DigitalChainOfCustody</span>
                </div>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- OSINT Spotlight Card -->
    <section class="section-padding-sm bg-surface border-top" aria-label="Call to action">
      <div class="container">
        <div class="cta-spotlight-card">
          <div class="row align-items-stretch g-4 g-lg-5">
            <div class="col-lg-6">
              <div class="cta-spotlight-content">
                <span class="cta-pill-badge mb-3"><i class="bi bi-journal-bookmark-fill"></i> Dispute Intelligence Engagement</span>
                <h2 class="cta-spotlight-title mb-3">Retain Commercial Litigation Intelligence Support</h2>
                <p class="cta-spotlight-desc mb-4">
                  Empower trial teams with court-admissible open-source intelligence dossiers, adverse party asset mapping, and certified forensic affidavits for high-stakes dispute resolution.
                </p>
                <div class="cta-spotlight-metrics mb-4">
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Deployment Window</span>
                    <strong class="cta-metric-value">Immediate Case Intake</strong>
                  </div>
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Evidentiary Standard</span>
                    <strong class="cta-metric-value">FRE 902(11) &amp; Civil Procedure Defensible</strong>
                  </div>
                </div>
                <div class="d-flex flex-wrap gap-3">
                  <a href="contact.html" class="btn btn-gold btn-lg">
                    <i class="bi bi-chat-text-fill"></i> Initiate Scoping Call
                  </a>
                  <a href="service-litigation-support.html" class="btn btn-outline-white btn-lg btn-white">
                    <i class="bi bi-journal-bookmark"></i> Explore Litigation Practice
                  </a>
                </div>
              </div>
            </div>
            <div class="col-lg-6 cta-spotlight-img-col">
              <div class="cta-spotlight-img-wrap">
                <img src="assets/images/banners/banner-blog-details-osint.jpg" alt="Commercial litigation intelligence workstation with financial district light trails reflecting in judicial quarter" class="cta-spotlight-img" width="3840" height="2160" loading="lazy">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

# =============================================================================
# Page 6: blog-details-asset-recovery.html
# =============================================================================
page_6_body = """
  <main id="main-content">
    <!-- Article Header Hero -->
    <section class="page-hero" aria-label="Article header">
      <img src="assets/images/hero/hero-blog-details-asset-recovery.jpg" alt="International wealth capital and offshore banking center towers illuminated along dark coastal waterfront" class="page-hero-img" width="3840" height="2160">
      <div class="container page-hero-content">
        <span class="badge-gold mb-3">Fraud Prevention &amp; Cross-Border Recovery</span>
        <h1 class="display-5 fw-bold mb-3">Tracing Dissipated Sovereign &amp; Corporate Assets Across Multi-Jurisdictional Hubs</h1>
        <div class="d-flex flex-wrap align-items-center gap-3 text-light text-opacity-75 small mb-0">
          <span><i class="bi bi-person-fill text-gold me-1"></i> Julian Sterling, Partner &ndash; Asset Tracing &amp; Recovery Practice</span>
          <span>&bull;</span>
          <span><i class="bi bi-calendar3 text-gold me-1"></i> May 2026</span>
          <span>&bull;</span>
          <span><i class="bi bi-clock text-gold me-1"></i> 8 min read</span>
          <span>&bull;</span>
          <span class="badge bg-secondary-subtle text-secondary">Asset Recovery Practice</span>
        </div>
      </div>
    </section>

    <!-- Article Content & Sidebar -->
    <section class="section-padding" aria-label="Article content">
      <div class="container">
        <div class="row g-5">
          <!-- Main Editorial Body (Left 8 cols) -->
          <article class="col-lg-8">
            <!-- Featured Photographic Asset -->
            <div class="mb-4">
              <img src="assets/images/blog/blog-detail-featured-asset-recovery.jpg" alt="Figure 1: Multi-Jurisdictional Sovereign and Corporate Asset Tracing Architecture detailing dissipation inception, offshore conduits, store-of-value assets, and judicial enforcement" class="img-fluid rounded border shadow-sm w-100" width="3840" height="2160">
              <small class="text-muted d-block mt-2 fst-italic">Figure 1: Multi-Jurisdictional Sovereign &amp; Corporate Asset Tracing Architecture &ndash; mapping defalcated capital flows, offshore discretionary trust shields, and judicial attachment remedies.</small>
            </div>

            <!-- Lead Paragraph -->
            <p class="lead text-secondary">
              When corrupt sovereign officials, rogue corporate executives, or judgment debtors misappropriate substantial institutional capital, they do not leave liquid funds in standard commercial bank accounts. Defalcated capital is converted with extraordinary speed into multi-tiered offshore structures, discretionary trusts, and illiquid luxury assets dispersed across non-cooperative jurisdictions.
            </p>

            <p class="text-muted">
              Recovering these funds requires a coordinated strategy that bridges investigative tradecraft and cross-border civil enforcement. Successful asset recovery demands prompt evidentiary mapping to support emergency injunctive relief—including Worldwide Freezing Orders (WFOs), Norwich Pharmacal disclosure orders, and discovery under 28 U.S.C. § 1782—before assets are dissipated beyond the reach of creditors.
            </p>

            <!-- Table of Contents -->
            <div class="p-4 bg-surface border rounded my-4">
              <h3 class="h6 text-uppercase tracking-wider text-gold mb-3"><i class="bi bi-list-nested me-2"></i> Table of Contents</h3>
              <ol class="small text-muted mb-0 ps-3">
                <li class="mb-1"><a href="#section-flight" class="text-decoration-none text-secondary">1. The Velocity of Capital Flight: How Sovereigns &amp; Fraudsters Conceal Assets</a></li>
                <li class="mb-1"><a href="#section-veil" class="text-decoration-none text-secondary">2. Piercing the Offshore Veil: Discretionary Trusts &amp; Nominee Protections</a></li>
                <li class="mb-1"><a href="#section-tangible" class="text-decoration-none text-secondary">3. Locating Tangible Wealth: Real Estate, Superyachts &amp; Numbered Bullion Vaults</a></li>
                <li class="mb-1"><a href="#section-injunction" class="text-decoration-none text-secondary">4. Coordinated Judicial Action: Worldwide Freezing Orders (WFO) &amp; Section 1782</a></li>
              </ol>
            </div>

            <!-- Section 1 -->
            <h2 class="h4 mt-5 mb-3" id="section-flight">1. The Velocity of Capital Flight: How Sovereigns &amp; Fraudsters Conceal Assets</h2>
            <p class="text-muted">
              The primary weapon of the fraudulent debtor is velocity. Liquidity is moved across four or more banking jurisdictions within twenty-four hours using sham consultancy fees, round-tripping wire transactions, and fraudulent trade finance letters of credit.
            </p>
            <p class="text-muted">
              By dispersing capital across mid-shore operating entities and offshore asset-holding vehicles, targets deliberately exploit jurisdictional borders, regulatory delays, and sovereign sovereignty doctrines to stymie judgment enforcement.
            </p>

            <!-- Strategic Callout -->
            <div class="p-4 bg-surface border-start border-gold border-4 rounded my-4">
              <h3 class="h5 mb-2"><i class="bi bi-lightning-charge text-gold me-2"></i> Emergency Action Protocol</h3>
              <p class="small text-muted mb-0">
                Asset tracing is a race against dissipation. Evidentiary gathering must proceed on an ex parte, confidential basis. Alerting the target prior to the entry of freezing injunctions frequently triggers instantaneous transfer of liquid holdings to uncooperative banking centers.
              </p>
            </div>

            <!-- Section 2 -->
            <h2 class="h4 mt-5 mb-3" id="section-veil">2. Piercing the Offshore Veil: Discretionary Trusts &amp; Nominee Protections</h2>
            <p class="text-muted">
              A standard obstacle in sovereign asset recovery is the irrevocable discretionary trust or private foundation (such as a Liechtenstein <em>Anstalt</em> or Panamanian foundation). Targets argue that they retain neither legal nor beneficial title to the assets held by the trustee.
            </p>
            <p class="text-muted">
              However, forensic scrutiny frequently reveals that the target exercises de facto control as an unrecorded "protector" or via private letters of wishes directing investment decisions. By establishing that the trust is a legal sham engineered to defeat existing creditors, Veritas equips recovery counsel with the evidence required to secure court orders declaring the assets available for enforcement.
            </p>

            <!-- Section 3 -->
            <h2 class="h4 mt-5 mb-3" id="section-tangible">3. Locating Tangible Wealth: Real Estate, Superyachts &amp; Numbered Bullion Vaults</h2>
            <p class="text-muted">
              Liquid capital is routinely funneled into high-value tangible assets that are perceived to be immune to bank seizures: prime commercial real estate in global financial capitals, private aviation registered under offshore trusts, maritime superyachts flagged in open registries, and allocated physical gold bars housed in secure freeports.
            </p>
            <p class="text-muted">
              Veritas deploys multidisciplinary investigative methods—combining satellite imagery, flight and marine transponder analysis, real estate registry deed extraction, and confidential human source intelligence—to link ostensibly unconnected luxury assets directly to the debtor.
            </p>

            <!-- Section 4 -->
            <h2 class="h4 mt-5 mb-3" id="section-injunction">4. Coordinated Judicial Action: Worldwide Freezing Orders (WFO) &amp; Section 1782</h2>
            <p class="text-muted">
              Asset intelligence achieves its ultimate value when paired with judicial enforcement remedies. In common-law jurisdictions, the English High Court's Worldwide Freezing Order (Mareva Injunction) is an exceptionally potent remedy that compels debtors to disclose all global assets exceeding a specified threshold under penalty of contempt.
            </p>
            <p class="text-muted">
              Simultaneously, under 28 U.S.C. § 1782, foreign litigants can obtain sweeping federal court discovery in the United States to subpoena correspondent clearing banks in New York, uncovering international US Dollar SWIFT wire records that pinpoint the exact depository accounts where stolen capital settled.
            </p>

            <!-- Social Share Bar -->
            <div class="p-3 bg-surface border rounded mt-5 d-flex flex-wrap justify-content-between align-items-center gap-3">
              <div class="d-flex align-items-center gap-2">
                <span class="small fw-bold text-muted">Share Briefing:</span>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Link copied to clipboard'); return false;"><i class="bi bi-link-45deg"></i> Copy Link</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: LinkedIn share dialog'); return false;"><i class="bi bi-linkedin"></i> LinkedIn</a>
                <a href="#" class="btn btn-sm btn-outline-secondary" onclick="alert('Demo: Email share intent'); return false;"><i class="bi bi-envelope"></i> Email</a>
              </div>
              <div class="small text-muted">
                Document Reference: #BRIEF-2026-ASSET-RECOV
              </div>
            </div>

            <!-- Author Bio Card -->
            <div class="p-4 bg-surface border rounded mt-4">
              <div class="d-flex align-items-center gap-3">
                <img src="assets/images/team/team-julian-sterling.jpg" alt="Julian Sterling, Partner – Asset Tracing &amp; Recovery Practice" class="rounded-circle border" width="72" height="72" style="object-fit: cover;">
                <div>
                  <h3 class="h5 mb-1">About Julian Sterling</h3>
                  <div class="small text-gold mb-1">Partner &ndash; Asset Tracing &amp; Cross-Border Recovery Practice, London &ndash; Geneva</div>
                  <p class="small text-muted mb-0">
                    Julian has spearheaded complex multi-jurisdictional asset recovery actions across more than thirty countries, assisting sovereign nations, insolvency practitioners, and international commercial judgment creditors in reclaiming billions in defalcated assets.
                  </p>
                </div>
              </div>
            </div>
          </article>

          <!-- Sidebar (Right 4 cols) -->
          <aside class="col-lg-4" aria-label="Sidebar">
            <div class="sidebar-sticky-wrap">
              <!-- Contact Inquiry Callout -->
              <div class="card-veritas p-4 mb-4">
                <span class="badge-gold mb-2">Practice Advisory</span>
                <h3 class="h5 mb-2">Instruct Asset Tracing Counsel</h3>
                <p class="small text-muted mb-3">
                  Facing an uncooperative judgment debtor, dissipated sovereign funds, or complex offshore shielding vehicles? Speak confidentially with our asset recovery partners.
                </p>
                <a href="contact.html" class="btn btn-gold btn-sm w-100">
                  <i class="bi bi-shield-lock-fill me-1"></i> Request Confidential Consultation
                </a>
              </div>

              <!-- Related Insights -->
              <div class="card-veritas p-4 mb-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Related Briefings</h3>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Due Diligence</span>
                  <h4 class="h6 mb-1"><a href="blog-details.html" class="text-decoration-none text-dark dark-text-light">Uncovering Hidden Beneficial Ownership in Complex Offshore Vehicles</a></h4>
                  <small class="text-muted">October 2026 &bull; 6 min read</small>
                </div>
                <div class="mb-3 pb-3 border-bottom">
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Corporate Intelligence</span>
                  <h4 class="h6 mb-1"><a href="blog-details-osint-litigation.html" class="text-decoration-none text-dark dark-text-light">The Role of Open-Source Intelligence in High-Stakes Commercial Litigation</a></h4>
                  <small class="text-muted">June 2026 &bull; 9 min read</small>
                </div>
                <div>
                  <span class="badge bg-secondary-subtle text-secondary small mb-1">Risk Advisory</span>
                  <h4 class="h6 mb-1"><a href="blog-details-ma-diligence.html" class="text-decoration-none text-dark dark-text-light">Red Flags in Cross-Border M&amp;A: Beyond Standard Financial Audits</a></h4>
                  <small class="text-muted">September 2026 &bull; 8 min read</small>
                </div>
              </div>

              <!-- Topic Tags -->
              <div class="card-veritas p-4">
                <h3 class="h6 text-uppercase tracking-wider mb-3">Practice Tags</h3>
                <div class="d-flex flex-wrap gap-2">
                  <span class="badge bg-surface border text-secondary">#AssetTracing</span>
                  <span class="badge bg-surface border text-secondary">#AssetRecovery</span>
                  <span class="badge bg-surface border text-secondary">#WorldwideFreezingOrder</span>
                  <span class="badge bg-surface border text-secondary">#Section1782</span>
                  <span class="badge bg-surface border text-secondary">#CrossBorderFraud</span>
                  <span class="badge bg-surface border text-secondary">#OffshoreHavens</span>
                </div>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- Asset Recovery Spotlight Card -->
    <section class="section-padding-sm bg-surface border-top" aria-label="Call to action">
      <div class="container">
        <div class="cta-spotlight-card">
          <div class="row align-items-stretch g-4 g-lg-5">
            <div class="col-lg-6">
              <div class="cta-spotlight-content">
                <span class="cta-pill-badge mb-3"><i class="bi bi-graph-up-arrow"></i> Recovery Enforcement Engagement</span>
                <h2 class="cta-spotlight-title mb-3">Instruct Cross-Border Asset Tracing Specialists</h2>
                <p class="cta-spotlight-desc mb-4">
                  Deploy our multidisciplinary investigative teams to identify, immobilize, and repatriate dissipated institutional, sovereign, or private wealth across complex offshore havens.
                </p>
                <div class="cta-spotlight-metrics mb-4">
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Deployment Window</span>
                    <strong class="cta-metric-value">24-Hour Emergency Freezing Action</strong>
                  </div>
                  <div class="cta-metric-item">
                    <span class="cta-metric-label">Injunction Strategy</span>
                    <strong class="cta-metric-value">Worldwide Freezing Orders &amp; Norwich Pharmacal</strong>
                  </div>
                </div>
                <div class="d-flex flex-wrap gap-3">
                  <a href="contact.html" class="btn btn-gold btn-lg">
                    <i class="bi bi-chat-text-fill"></i> Initiate Scoping Call
                  </a>
                  <a href="service-asset-tracing.html" class="btn btn-outline-white btn-lg btn-white">
                    <i class="bi bi-graph-up-arrow"></i> Explore Recovery Practice
                  </a>
                </div>
              </div>
            </div>
            <div class="col-lg-6 cta-spotlight-img-col">
              <div class="cta-spotlight-img-wrap">
                <img src="assets/images/banners/banner-blog-details-asset-recovery.jpg" alt="Pure fine gold bullion bars and sovereign reserve assets secured under international court freezing orders" class="cta-spotlight-img" width="3840" height="2160" loading="lazy">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

# Pages config
pages = [
    {
        "filename": "blog-details-sanctions.html",
        "title": "Navigating Secondary Sanctions & Third-Party Vendor Risk in 2026",
        "desc": "A forensic intelligence framework for identifying concealed intermediary ownership in transshipment hubs and avoiding secondary sanctions exposure.",
        "keywords": "secondary sanctions, third party vendor risk, export control, transshipment hubs, OFAC compliance, dark fleet maritime",
        "featured_img": "assets/images/blog/blog-detail-featured-sanctions.jpg",
        "body": page_4_body
    },
    {
        "filename": "blog-details-osint-litigation.html",
        "title": "The Role of Open-Source Intelligence in High-Stakes Commercial Litigation",
        "desc": "Transforming publicly available registry fragments, digital footprints, and geospatial breadcrumbs into defensible, court-admissible trial evidence.",
        "keywords": "OSINT commercial litigation, court admissible evidence, FRE 902(11), asset mapping, corporate intelligence, trial exhibits",
        "featured_img": "assets/images/blog/blog-detail-featured-osint.jpg",
        "body": page_5_body
    },
    {
        "filename": "blog-details-asset-recovery.html",
        "title": "Tracing Dissipated Sovereign & Corporate Assets Across Multi-Jurisdictional Hubs",
        "desc": "Practical legal and investigative frameworks for identifying real estate, maritime vessels, and nominee trusts across multi-jurisdictional banking centers.",
        "keywords": "asset tracing, sovereign asset recovery, worldwide freezing orders, Mareva injunction, 28 USC 1782, offshore trusts",
        "featured_img": "assets/images/blog/blog-detail-featured-asset-recovery.jpg",
        "body": page_6_body
    }
]

for p in pages:
    page_content = header_html.replace("{PAGE_TITLE}", p["title"])\
                              .replace("{META_DESC}", p["desc"])\
                              .replace("{META_KEYWORDS}", p["keywords"])\
                              .replace("{FEATURED_IMG}", p["featured_img"])
    page_content += p["body"]
    page_content += footer_html
    
    root_p = os.path.join(workspace, p["filename"])
    tmpl_p = os.path.join(template_dir, p["filename"])
    
    with open(root_p, "w", encoding="utf-8") as fp:
        fp.write(page_content)
    with open(tmpl_p, "w", encoding="utf-8") as fp:
        fp.write(page_content)
        
    print(f"Generated and synchronized: {p['filename']}")

print("\nAll 3 new blog details pages created successfully!")
