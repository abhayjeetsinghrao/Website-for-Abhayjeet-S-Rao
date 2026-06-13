# Website — Abhayjeet Singh Rao

Personal professional website for Abhayjeet Singh Rao, Counsel, New Delhi.
Live at: https://officeofabhayjeetsinghrao.com
Hosted on GitHub Pages with custom domain.

## Development workflow

- All changes go to branch `claude/website-maintenance-tv9k5`
- User merges PRs into `main`; GitHub Pages deploys from `main`
- Never push directly to `main`

## Site structure

```
index.html          — main single-page site
privacy-policy.html
robots.txt
sitemap.xml
f1915e146c4820a15e518a99e72fa175.txt   — IndexNow key
insights/           — individual SEO pages (one per case)
```

## Adding a new insight — MANDATORY STEPS

### Step 1 — Web-search verification (NON-NEGOTIABLE)
Before writing or committing any article, verify every factual claim with live
web search. The script `scripts/verify_insight.py` automates this:

```bash
# Requires: pip install anthropic && export ANTHROPIC_API_KEY=...
python3 scripts/verify_insight.py insights/<slug>.html
```

The script must return **PASS** before the article is committed. A FLAG verdict
requires all listed corrections to be applied and the script re-run. A FAIL or
ERROR means the article must not be published.

**For every article, verify manually:**
- [ ] Case / legal event is real and published
- [ ] Case number (SCC, UKHL, PCA Case No., EWHC, etc.) is correct
- [ ] Court and year are correct
- [ ] Key legal holdings accurately reflect the actual judgment
- [ ] Statutory provisions cited exist and are correctly named

### Step 2 — Create the HTML page
Create `insights/<slug>.html` — copy any existing insight page as template.

### Step 3 — Add to index.html
Add an insight card to `index.html` at `<!-- inject-newest-here -->` (newest first).

### Step 4 — Update sitemap
Add the URL to `sitemap.xml`.

### Step 5 — Commit and push

Every insight page must have:
- Unique `<title>`, `<meta name="description">`, `<meta name="keywords">`
- `<link rel="canonical">` and `<link rel="sitemap">`
- OG / Twitter meta tags
- Article + LegalCase (or Event) JSON-LD structured data
- Bar Council of India disclaimer modal (sessionStorage-based)
- Related insights section (3 links)

## Content plan — publishing queue

### Series A — Supreme Court of India (criminal & commercial) — PUBLISHED

All 10 articles published June 9–18, 2026. Web-search verified before publication.

| # | Slug | Citation | Date |
|---|------|----------|------|
| 1 | `lalita-kumari-v-govt-up.html` | Lalita Kumari v. Govt. of U.P. — (2014) 2 SCC 1 | 9 June 2026 |
| 2 | `dataram-singh-v-state-up.html` | Dataram Singh v. State of U.P. — (2018) 3 SCC 22 | 10 June 2026 |
| 3 | `toofan-singh-v-state-tamil-nadu.html` | Toofan Singh v. State of Tamil Nadu — (2021) 4 SCC 1 | 11 June 2026 |
| 4 | `rajnesh-v-neha.html` | Rajnesh v. Neha — (2021) 2 SCC 324 | 12 June 2026 |
| 5 | `pioneer-urban-land-v-union-india-ibc.html` | Pioneer Urban Land & Infrastructure Ltd. v. Union of India — **(2019) 8 SCC 416** | 13 June 2026 |
| 6 | `k-bhaskaran-v-sankaran-vaidhyan-balan.html` | K. Bhaskaran v. Sankaran Vaidhyan Balan — (1999) 7 SCC 510 | 14 June 2026 |
| 7 | `noor-aga-v-state-punjab.html` | Noor Aga v. State of Punjab — (2008) 16 SCC 417 | 15 June 2026 |
| 8 | `swiss-ribbons-v-union-india.html` | Swiss Ribbons Pvt. Ltd. v. Union of India — (2019) 4 SCC 17 | 16 June 2026 |
| 9 | `siddharth-v-state-up.html` | Siddharth v. State of U.P. — (2022) 1 SCC 676 | 17 June 2026 |
| 10 | `state-of-haryana-v-bhajan-lal.html` | State of Haryana v. Bhajan Lal — 1992 Supp (1) SCC 335 | 18 June 2026 |

**Notes:** Case #5 corrected from "v. Govindan Raghavan (2019) 5 SCC 725" (consumer protection) to correct IBC homebuyers case: **v. Union of India (2019) 8 SCC 416**. K. Bhaskaran territorial jurisdiction holding noted as overruled by Dashrath Rupsingh Rathod (2014) 9 SCC 129; five-component test survives.

### Series B — English Commercial Law — PUBLISHED

All 8 articles published June 19–26, 2026.

| # | Slug | Citation | Date |
|---|------|----------|------|
| 1 | `fiona-trust-v-privalov.html` | Fiona Trust & Holding Corp v. Privalov — [2007] UKHL 40 | 19 June 2026 |
| 2 | `transfield-shipping-v-mercator-achilleas.html` | Transfield Shipping v. Mercator Shipping (The Achilleas) — [2008] UKHL 48 | 20 June 2026 |
| 3 | `singularis-holdings-v-daiwa.html` | Singularis Holdings Ltd v. Daiwa Capital Markets Europe Ltd — [2019] UKSC 50 | 21 June 2026 |
| 4 | `vtb-capital-v-nutritek.html` | VTB Capital plc v. Nutritek International Corp — [2013] UKSC 5 | 22 June 2026 |
| 5 | `mareva-compania-naviera-v-international-bulkcarriers.html` | Mareva Compania Naviera SA v. International Bulkcarriers SA — [1975] 2 Lloyd's Rep 509 | 23 June 2026 |
| 6 | `raiffeisen-zentralbank-v-rbs.html` | Raiffeisen Zentralbank Osterreich AG v. Royal Bank of Scotland plc — [2010] EWHC 1392 (Comm) | 24 June 2026 |
| 7 | `cavendish-square-v-makdessi.html` | Cavendish Square Holding BV v. Makdessi — [2015] UKSC 67 | 25 June 2026 |
| 8 | `lehman-brothers-international-europe-cass.html` | Lehman Brothers International (Europe) (In Administration) v. CRC Credit Fund Ltd — [2012] UKSC 6 | 26 June 2026 |

### Series C — PCA / International Arbitration (published)

| Slug | Citation | Date |
|------|----------|------|
| `pakistan-india-indus-waters-pca-arbitration.html` | Pakistan v. Republic of India, PCA Case No. 2023-01 — Award on the Competence of the Court, 6 July 2023; Award on Issues of General Interpretation, 8 August 2025 | 8 June 2026 |
| `india-notice-modify-indus-waters-treaty.html` | India's Notice for Modification of the IWT, 25 January 2023; India's Abeyance Declaration, 23 April 2025 — IWT Art. XII; VCLT Arts. 54, 62 | 8 June 2026 |

**Verification status:** Both articles web-search verified and corrected (6 July 2023 award date confirmed; PCA Case No. 2023-01 confirmed; April 2025 abeyance declaration and August 2025 general interpretation award incorporated).
