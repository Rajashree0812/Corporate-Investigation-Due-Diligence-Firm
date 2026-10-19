# Veritas Intelligence — Corporate Investigation & Due Diligence Firm
### Premium HTML5 & Bootstrap 5 Website Template

**Veritas Intelligence** is a commercial-grade, multi-page HTML website template engineered for corporate investigation firms, forensic intelligence consultancies, due diligence practices, risk advisory boutiques, and white-collar defense advisory teams.

Designed for high-consequence corporate environments, this template communicates discretion, trust, evidentiary integrity, and enterprise prestige through deep navy tones, charcoal typography, refined borders, and muted gold accents.

> **Commercial Distribution Ready**: Fully compliant with ThemeForest, TemplateMonster, and bespoke corporate client standards. Zero backend dependencies; runs immediately out-of-the-box using **VS Code Live Server**.

---

## 1. Key Features & Highlights

- **11 Production-Ready HTML Pages**: Comprehensive multi-page corporate architecture.
- **Two Distinct Homepages**:
  - `index.html`: General Corporate Investigations & Due Diligence landing page.
  - `index-2.html`: Asymmetrical Corporate Intelligence, Risk Advisory & Geopolitical Telemetry landing page.
- **Light & Dark Mode**:
  - Light mode enabled by default.
  - Dark mode with carefully calibrated contrast, inputs, cards, borders, and shadows.
  - State saved to `localStorage` key `itserve_theme` (with legacy fallback `itSupportTheme`).
  - Inline head script prevents unstyled theme flicker.
- **Right-to-Left (RTL) Support**:
  - Dedicated `assets/css/rtl.css` with bidirectional layout flipping for Arabic, Hebrew, and Persian.
  - RTL toggle control saved to `localStorage` key `itserve_direction` (with legacy fallback `itSupportRTL`).
- **Interactive JavaScript Features**:
  - Real-time blog search and multi-category filtering (`assets/js/blog-filter.js`).
  - Interactive practice area filter on the Services page.
  - Client-side form validation with realistic demo-state notifications (`assets/js/form-validation.js`).
  - Live customizable countdown timer for portal launch (`assets/js/main.js`).
  - Metric counters animated upon viewport entry via `IntersectionObserver`.
  - Sticky navbar with background blur and back-to-top smooth scrolling.
- **100% Local Realistic Photography**:
  - 36 distinct, realistic high-resolution photographs locally stored in `assets/images/`.
  - Zero duplicate photos across hero banners, service cards, leadership portraits, and blog posts.
  - Sourced under commercial-friendly open licenses (see `IMAGE-LICENSES.md`).
- **Zero Framework / Zero Build Step**:
  - Standard HTML5, Bootstrap 5, Bootstrap Icons, Vanilla ES6+ JavaScript.
  - No React, Vue, Angular, Node build scripts, or backend requirements.

---

## 2. Page Directory

| File | Page Name | Primary Sections & Features |
| :--- | :--- | :--- |
| `index.html` | **Home Page 1 (Corporate Investigations)** | Hero banner, metrics counters, services preview, 4-stage investigation process, industries served, confidential consultation banner, client testimonials, latest insights, footer. |
| `index-2.html` | **Home Page 2 (Corporate Intelligence)** | Asymmetrical hero layout, 4 collection disciplines (OSINT, HUMINT, Forensics, Cyber), strategic practice matrix, sector focus, live telemetry indicator, risk briefings. |
| `about.html` | **About Us** | Mission statement, 4 core values (Integrity, Discretion, Accuracy, Accountability), two-decade history timeline, evidentiary methodology, 6 partner profiles, ethics compliance statement. |
| `services.html` | **Services Overview** | Filterable practice area tabs, all 9 core services with capability checklists, service deliverables, scoping FAQ accordion. |
| `service-details.html` | **Service Details Template** | Detailed M&A due diligence case study, business challenges, 4-phase investigation workflow, concrete deliverables, working FAQ accordion, indicative scope cards. |
| `blog.html` | **Intelligence Briefings (Blog)** | Editorial hero, live search input, 5 category filter buttons, 6 responsive article cards, dynamic results counter, pagination demo, newsletter subscription. |
| `blog-details.html` | **Case Analysis (Blog Details)** | Featured case article, interactive table of contents, structured subheadings, quote callouts, comparison table, social share triggers, author bio, related briefings. |
| `contact.html` | **Contact & Confidential Intake** | Consultation hero, validated multi-field intake form (Name, Corporate Email, Firm, Practice Area, Preferred Method, Message, Consent), 4 global hubs (London, New York, Singapore, Zurich), styled map graphic, FAQs. |
| `pricing.html` | **Engagement Models & Pricing** | Three structured tiers (Pre-Transaction, Comprehensive Diligence, Complex Forensics), detailed comparison table, indicative pricing disclosures, retainer FAQs. |
| `404.html` | **404 Case File Not Located** | Minimalist corporate error layout, branded vault photography, quick navigation links. |
| `coming-soon.html` | **Client Portal Launch** | Atmospheric full-screen background, live days/hours/minutes countdown timer, early access email form, return navigation. |

---

## 3. Technology Stack & Dependencies

- **HTML5**: Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`).
- **CSS3**: Custom design tokens, CSS variables, flexbox, and CSS grid.
- **Bootstrap 5.3.3**: Grid layout, responsive utilities, dropdowns, and modals (`assets/css/bootstrap.min.css` & `assets/js/bootstrap.bundle.min.js`).
- **Bootstrap Icons 1.11.3**: Crisp vector icons with offline WOFF2/WOFF local font assets (`assets/css/bootstrap-icons.css` & `assets/fonts/`).
- **Google Fonts**: `Manrope` (headings), `Inter` (body), and `Cinzel` (serif accents).
- **Vanilla JavaScript**: ES6+ modules cleanly separated into dedicated functional files.

---

## 4. Folder Structure

```
veritas-intelligence-template/
├── index.html                 # Home Page 1 — Corporate Investigations
├── index-2.html               # Home Page 2 — Corporate Intelligence
├── about.html                 # About Us & Leadership Team
├── services.html              # Practice Areas Listing with Filters
├── service-details.html       # Service Details Template
├── blog.html                  # Insights / Blog Listing with Live Search
├── blog-details.html          # Editorial Article Details & Table of Contents
├── contact.html               # Contact Us with Form Validation & Hubs
├── pricing.html               # Engagement Frameworks & Comparison Table
├── 404.html                   # 404 Error Page
├── coming-soon.html           # Portal Launch Countdown Page
├── README.md                  # Template Documentation & Setup Guide
├── IMAGE-LICENSES.md          # Complete Asset Mapping & License Registry
└── assets/
    ├── css/
    │   ├── bootstrap.min.css       # Bootstrap 5.3.3 core styles
    │   ├── bootstrap-icons.css     # Bootstrap Icons 1.11.3 styles
    │   ├── style.css               # Main custom design system & dark mode variables
    │   ├── responsive.css          # Responsive media queries (320px – 1920px)
    │   ├── rtl.css                 # Right-to-Left bidirectional layout stylesheet
    │   └── fonts/                  # Offline icon font files (woff/woff2)
    ├── js/
    │   ├── bootstrap.bundle.min.js # Bootstrap 5 bundle (includes Popper)
    │   ├── main.js                 # Sticky nav, back-to-top, countdown, counters
    │   ├── theme.js                # Light/Dark mode switcher with localStorage
    │   ├── rtl.js                  # LTR/RTL layout toggle with localStorage
    │   ├── blog-filter.js          # Real-time search & category filter engine
    │   └── form-validation.js      # Client-side validation & demo alerts
    ├── fonts/                      # Bootstrap icon font binaries
    └── images/
        ├── logo.svg                # Vector brand logo (Light background)
        ├── logo-light.svg          # Vector brand logo (Dark background)
        ├── favicon.svg             # Shield monogram favicon
        ├── hero/                   # 9 unique high-resolution hero photographs
        ├── services/               # 8 unique practice area photographs
        ├── team/                   # 6 unique executive partner portraits
        ├── blog/                   # 7 unique article thumbnails & banner
        ├── about/                  # 3 unique firm & methodology photographs
        └── banners/                # 3 unique consultation & CTA photographs
```

---

## 5. Quick Start Guide

### Running via VS Code Live Server (Recommended)
1. Open the project root folder (`c:\Users\thand\Desktop\Website` or `veritas-intelligence-template/`) in **VS Code**.
2. Install the **Live Server** extension (by Ritwick Dey) from the VS Code Extensions marketplace if not already installed.
3. Right-click on `index.html` and select **"Open with Live Server"** (or click **Go Live** in the bottom status bar).
4. The template will load at `http://127.0.0.1:5500/index.html`.

### Running Locally without a Server
Because all CSS, JS, fonts, and images are linked locally using relative paths, you can also double-click any `.html` file to preview it directly in your web browser.

---

## 6. Customization Guide

### A. Modifying Brand Colors & Design Tokens
Open `assets/css/style.css`. The primary color tokens are defined at the top of the `:root` block:

```css
:root {
  /* Change Brand Palette */
  --navy-900: #0B1325;   /* Primary corporate dark */
  --gold-500: #C5A880;   /* Muted gold accent */
  --gold-400: #D8BD9B;   /* Light gold hover */
  --border-color: #E2E8F0; /* Subtle card border */
}
```

Dark mode colors can be configured independently in the `[data-bs-theme="dark"]` section of `style.css`.

### B. Connecting the Contact Form to a Backend
In `contact.html`, the contact form uses the class `.needs-veritas-validation`. By default, `assets/js/form-validation.js` intercepts submissions to perform client-side regex checks and display demo feedback.

To connect this to your production backend (e.g. PHP mailer, Node.js API, Formspree, or CRM webhook):
1. Add your endpoint to the `<form>` element:
   ```html
   <form action="https://your-api.com/v1/inquiry" method="POST">
   ```
2. In `assets/js/form-validation.js`, replace the `setTimeout` block with a `fetch()` call sending form data via JSON or FormData.

### C. Embedding a Live Interactive Map
In `contact.html`, an office map graphic placeholder is provided. To replace this with a live Google Maps or Mapbox iframe:
1. Locate the `<section aria-label="Global office map">` in `contact.html`.
2. Replace the `.card-veritas` placeholder container with your standard Google Maps `<iframe>`:
   ```html
   <iframe src="https://www.google.com/maps/embed?..." width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
   ```

---

## 7. Quality Assurance & Compliance Verification

- [x] **No Admin Dashboard**: Strictly front-end public corporate consulting template.
- [x] **No Fake Backend Claims**: Contact and newsletter forms explicitly display demo notices rather than claiming real encrypted storage.
- [x] **Zero Duplicate Photographs**: 36 unique high-resolution images across all placements.
- [x] **Light & Dark Mode**: Persistent via `itserve_theme` & legacy `itSupportTheme`.
- [x] **RTL Bidirectional Support**: Fully functional via `itserve_direction` & `itSupportRTL`.
- [x] **Interactive Blog Filter**: Live keyword search and category buttons tested in vanilla JS.
- [x] **Mobile-First Responsive Layout**: Refined from 320px up to 1920px wide screens.
- [x] **W3C Standards Compliant**: Valid semantic HTML5 and clean CSS.

---

&copy; 2026 Veritas Intelligence. All rights reserved.
