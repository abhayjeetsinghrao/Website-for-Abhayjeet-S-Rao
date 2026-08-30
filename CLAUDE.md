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

### Series D — Civil Procedure Code (Supreme Court of India) — PUBLISHED

All 8 articles published July 1–8, 2026. Web-search verified 8 July 2026
before generation (verify_insight.py unavailable in remote environment — no
ANTHROPIC_API_KEY; verification done with live web search per case).

| # | Slug | Citation | Date |
|---|------|----------|------|
| 1 | `dalpat-kumar-v-prahlad-singh.html` | Dalpat Kumar v. Prahlad Singh — (1992) 1 SCC 719 | 1 July 2026 |
| 2 | `wander-v-antox-india.html` | Wander Ltd. v. Antox India P. Ltd. — 1990 Supp SCC 727 | 2 July 2026 |
| 3 | `satyadhyan-ghosal-v-deorajin-debi.html` | Satyadhyan Ghosal v. Sm. Deorajin Debi — AIR 1960 SC 941 | 3 July 2026 |
| 4 | `state-of-up-v-nawab-hussain.html` | State of U.P. v. Nawab Hussain — (1977) 2 SCC 806 | 4 July 2026 |
| 5 | `saleem-bhai-v-state-maharashtra.html` | Saleem Bhai v. State of Maharashtra — (2003) 1 SCC 557 | 5 July 2026 |
| 6 | `rahul-s-shah-v-jinendra-kumar-gandhi.html` | Rahul S. Shah v. Jinendra Kumar Gandhi — (2021) 6 SCC 418 | 6 July 2026 |
| 7 | `ramrameshwari-devi-v-nirmala-devi.html` | Ramrameshwari Devi v. Nirmala Devi — (2011) 8 SCC 249 | 7 July 2026 |
| 8 | `scg-contracts-v-ks-chamankar-infrastructure.html` | SCG Contracts India Pvt. Ltd. v. K.S. Chamankar Infrastructure Pvt. Ltd. — (2019) 12 SCC 210 | 8 July 2026 |

**Notes:** Hub page has a `#civil-procedure` section (site now 44 articles / 6
practice areas — hero stats and meta counts updated site-wide). Wander & Antox
citation format is `1990 Supp SCC 727` (no parentheses year). Satyadhyan Ghosal
predates SCC — AIR citation used.

**Template gotcha (fixed 8 July 2026):** the hero block of insight pages uses
LITERAL `—` and `·` characters, not `&mdash;`/`&middot;` entities. A generator
doing string-replace against entity forms will silently fail and leave the
template page's tag/H1/citation on every generated page. After generating,
always verify the `<h1 class="art-title">` and `<div class="art-citation">` of
each page — not just `<title>` and JSON-LD.

### Series E — Constitutional Law & Writs (Supreme Court of India) — PUBLISHED

All 8 articles published August 23–30, 2026. Web-search verified 30 August 2026
before generation (verify_insight.py unavailable in remote environment — no
ANTHROPIC_API_KEY; verification done with live web search per case).

| # | Slug | Citation | Date |
|---|------|----------|------|
| 1 | `kesavananda-bharati-v-state-kerala.html` | Kesavananda Bharati v. State of Kerala — (1973) 4 SCC 225 | 23 Aug 2026 |
| 2 | `maneka-gandhi-v-union-india.html` | Maneka Gandhi v. Union of India — (1978) 1 SCC 248 | 24 Aug 2026 |
| 3 | `ep-royappa-v-state-tamil-nadu.html` | E.P. Royappa v. State of Tamil Nadu — (1974) 4 SCC 3 | 25 Aug 2026 |
| 4 | `dk-basu-v-state-west-bengal.html` | D.K. Basu v. State of West Bengal — (1997) 1 SCC 416 | 26 Aug 2026 |
| 5 | `sr-bommai-v-union-india.html` | S.R. Bommai v. Union of India — (1994) 3 SCC 1 | 27 Aug 2026 |
| 6 | `l-chandra-kumar-v-union-india.html` | L. Chandra Kumar v. Union of India — (1997) 3 SCC 261 | 28 Aug 2026 |
| 7 | `shreya-singhal-v-union-india.html` | Shreya Singhal v. Union of India — (2015) 5 SCC 1 | 29 Aug 2026 |
| 8 | `ks-puttaswamy-v-union-india.html` | K.S. Puttaswamy (Retd.) v. Union of India — (2017) 10 SCC 1 | 30 Aug 2026 |

**Notes:** Hub page has a `#constitutional-law` section (site now 52 articles /
7 practice areas — hero stats and meta counts updated site-wide). D.K. Basu's
guidelines judgment of 18 Dec 1996 is `(1997) 1 SCC 416`; a later order in the
same matter carries a different citation, so do not conflate them. Puttaswamy
expressly overruled M.P. Sharma and Kharak Singh; the ADM Jabalpur majority was
held seriously flawed and overruled in the plurality opinion — phrase that
distinction carefully. Shreya Singhal struck down s. 66A but **upheld** s. 69A
and only **read down** s. 79.

**Generator lesson applied:** `gen_series_e.py` asserts on every hero
replacement (`assert html.count(old) == 1`), so a missed anchor fails the run
instead of shipping template text. Reuse that pattern for future series.

## Blog section (`blog/`, 37 posts, added PR #8)

Separate from `insights/`. Audited 30 August 2026 (PR #11) — three defects found
and fixed: BCI disclaimer was missing from all 37 pages, one page had an `<a>`
tag inside JSON-LD breaking the whole block, and 21 pages had nested `<a>` tags
in related-article cards. **Any new blog post must carry the BCI disclaimer
modal**, keep JSON-LD values plain-text, and never nest an anchor inside the
outer card link.
