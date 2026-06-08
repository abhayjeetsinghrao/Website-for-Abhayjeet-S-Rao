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

### Series A — Supreme Court of India (criminal & commercial)

Proposed 10-insight schedule (dates TBD, to be published over ~20 days):

| # | Case | Topic |
|---|------|-------|
| 1 | Lalita Kumari v. Govt. of U.P. — (2014) 2 SCC 1 | FIR mandatory registration, police duty |
| 2 | Dataram Singh v. State of U.P. — (2018) 3 SCC 22 | Custody vs. arrest distinction, bail |
| 3 | Toofan Singh v. State of Tamil Nadu — (2021) 4 SCC 1 | NDPS — confessions before customs officers |
| 4 | Rajnesh v. Neha — (2021) 2 SCC 324 | Interim maintenance — uniform guidelines |
| 5 | Pioneer Urban Land and Infrastructure Ltd v. Govindan Raghavan — (2019) 5 SCC 725 | IBC — homebuyers as financial creditors |
| 6 | K. Bhaskaran v. Sankaran Vaidhyan Balan — (1999) 7 SCC 510 | Section 138 NI Act — dishonour of cheque |
| 7 | Noor Aga v. State of Punjab — (2008) 16 SCC 417 | NDPS — reverse burden of proof |
| 8 | Swiss Ribbons Pvt. Ltd. v. Union of India — (2019) 4 SCC 17 | IBC constitutional validity |
| 9 | Siddharth v. State of U.P. — (2022) 1 SCC 676 | Arrest not automatic on filing of charge sheet |
| 10 | State of Haryana v. Bhajan Lal — 1992 Supp (1) SCC 335 | FIR quashing — seven-category guidelines |

### Series B — EWHC Commercial Division

Landmark Commercial Court cases — to be built as a dedicated series on the site, showcasing expertise in English commercial law (aligns with LLM in International Commercial Law, University of Limerick).

Proposed cases (order TBD):

| # | Case | Topic |
|---|------|-------|
| 1 | Fiona Trust & Holding Corp v. Privalov [2007] UKHL 40 | Arbitration clauses — separability and one-stop adjudication |
| 2 | The Achilleas (Transfield Shipping v. Mercator Shipping) [2008] UKHL 48 | Remoteness of damage — assumption of responsibility |
| 3 | Singularis Holdings Ltd v. Daiwa Capital Markets Europe Ltd [2019] UKSC 50 | Fraud — attribution of director's knowledge to company |
| 4 | VTB Capital plc v. Nutritek International Corp [2013] UKSC 5 | Jurisdiction — piercing the corporate veil |
| 5 | Mareva Compania Naviera SA v. International Bulkcarriers SA [1975] 2 Lloyd's Rep 509 | Freezing injunctions — origins of the Mareva order |
| 6 | Raiffeisen Zentralbank Osterreich AG v. Royal Bank of Scotland plc [2010] EWHC 1392 | Misrepresentation — reasonable reliance in banking |
| 7 | Cavendish Square Holding BV v. Makdessi [2015] UKSC 67 | Penalty clauses — rule against penalties recast |
| 8 | Lehman Brothers International (Europe) (In Administration) [2012] UKSC 6 | Client money — segregation and insolvency waterfall |

### Series C — PCA / International Arbitration (published)

| Slug | Citation | Date |
|------|----------|------|
| `pakistan-india-indus-waters-pca-arbitration.html` | Pakistan v. Republic of India, PCA Case No. 2023-01 — Award on the Competence of the Court, 6 July 2023; Award on Issues of General Interpretation, 8 August 2025 | 8 June 2026 |
| `india-notice-modify-indus-waters-treaty.html` | India's Notice for Modification of the IWT, 25 January 2023; India's Abeyance Declaration, 23 April 2025 — IWT Art. XII; VCLT Arts. 54, 62 | 8 June 2026 |

**Verification status:** Both articles web-search verified and corrected (6 July 2023 award date confirmed; PCA Case No. 2023-01 confirmed; April 2025 abeyance declaration and August 2025 general interpretation award incorporated).
