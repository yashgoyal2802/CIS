# Retail supply chain (supplier to warehouse to store/customer): AI use, India first, global comparators

Compiled 7 Oct 2026. Grades: A = read in primary document; B = primary exists but seen only via summary (WebFetch summary, aggregator copy, search snippet of a primary); C = press/vendor/consulting only; X = unverified or conflicting, do not cite.
Caveat on method: WebFetch returns a model summary, not raw text. Items marked A were read from text I extracted locally with pdftotext (downloads folder) or that WebFetch quoted from the page itself with page cites. Everything else is B or lower. I did NOT read the Delhivery, Amazon, Flipkart, Reliance primary files in full.

## 1. Summary: how well documented is AI use, by component

Overall: AI use is well documented qualitatively but poorly documented quantitatively. Almost no company discloses an AI-attributed KPI (accuracy, % cost saved) in a filing. The quantified numbers that exist are automation/robotics counts (Walmart, Amazon, Delhivery, Ocado), not AI outcomes. For India, the data on the system (logistics cost, ULIP, e-way bill) is good; data on AI use inside retailers is thin.

| Component | Evidence | Why |
|---|---|---|
| Demand forecasting and planning | SOME | Peer-reviewed (M5 competition, Flipkart INFORMS paper 2026) and Ocado "AI-driven demand forecasting" statement, but no filing gives a quantified forecast-accuracy result. Consulting ranges (McKinsey 20-50% error cut) are grade C/X. |
| Supplier management / procurement | THIN | Nothing found for the named companies. Generic vendor/consulting claims only. |
| Inbound logistics / inbound appointments | THIN | Amazon FC inbound appointment capacity algorithms (C). Nothing quantified. |
| Inventory optimisation / network allocation | SOME | Flipkart planning platform (B, no figures seen), Walmart computer-vision inventory mapping (C), Walmart inventory +2.6% y/y vs sales (C). |
| Warehouse/DC operations and robotics | STRONG | Walmart (10-K qualitative A; % automation C), Amazon 1M robots / DeepFleet +10% (B), Delhivery sort capacity (B), Ocado robotic picking and UPH (A). |
| Transport and route optimisation | SOME | Delhivery ML list (B), Ocado Swift Router (A), Amazon India dynamic routing (B), academic Amazon Last Mile Routing Challenge (C). No quantified Indian result. |
| Cold chain | THIN | Mostly infrastructure statistics (cold storage capacity, losses), almost no AI evidence. Reliance "AI cameras farm to shelf" (C). |
| Last-mile | SOME | Shadowfax SF Maps/SF Shield (C, company blog), Delhivery ETA prediction (B), Amazon India (B). Volumes available, AI effect not. |
| Reverse logistics / returns | THIN | Nothing found in this pass (not searched deeply; see gaps). |
| Control tower / visibility | SOME (India: policy-level) | ULIP / Logistics Data Bank 2.0 (A, PIB) are government visibility platforms; retailer-level control towers not documented. |

Candidate-industry implication: retail supply chain is a good choice for workflow mapping and for India system data, but weak for "how much AI, quantified" unless the project is willing to rely on grade B/C figures or on academic case papers. Grocery retail inside India (DMart) is the weakest of all: see section 4.

## 2. Workflow decomposition (for the project)

Supplier/procurement and demand planning -> inbound (supplier to DC, FTL/LTL, appointment scheduling) -> DC/warehouse (receive, putaway, store, pick, pack, sort; cold/ambient) -> inventory allocation across network (DC to store replenishment, dark store/store/FC allocation) -> middle-mile and line-haul transport -> last-mile (store pick-up or delivery) -> reverse logistics (returns, RTO, markdowns, liquidation) -> overlay: control tower/visibility and exception management; cold chain runs through the DC-transport-store legs for perishables.
The decomposition above is my framing, not taken from a single source; Walmart 10-K p9 (A) describes the same flow only at a high level (192 US distribution facilities, 179 outside the US, private fleet plus common carriers).

## 3. Documented AI/automation use, by company and component

### 3.1 Walmart (global comparator)
- A. Walmart Inc. Form 10-K FY2026 (FYE 31 Jan 2026), URL https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm . Also read the Annual Report to Shareholders PDF text (local: downloads/walmart_ars_fy26/ars.txt).
  - "We continue to invest in supply chain automation and our fulfillment and delivery capabilities" (10-K p9, ARS PDF p11). 192 distribution facilities in US, 179 outside (p9).
  - "Our strategies increasingly include the use of AI-powered tools ... associate productivity and operational efficiency" (p6). Risk factor says AI is used "to improve efficiencies of our supply chain, operations" (ARS PDF p19).
  - Capex FY2026 total $26,642m (printed p36 of ARS; the category headings are scrambled in text extraction so I cannot state the supply-chain share; do not cite a split). FY2027 capex guided $25-27bn "with a focus on technology, supply chain and customer-facing initiatives" (printed p42, ARS PDF p44).
  - The 10-K contains NO automation percentage and no mention of Symbotic in the portion I read (first ~100k chars of the 10-K via WebFetch; ARS text searched in full for "automat").
- C. Automation figures from Q4 FY26 earnings call, reported by Supply Chain Dive, 23 Feb 2026 (https://www.supplychaindive.com/news/walmart-supply-chain-automation-q4-earnings/812721/): about 60% of US stores receive part of freight from automated DCs; roughly half of e-commerce fulfilment-centre volume automated; 23 of 42 regional DCs being retrofitted; over 1 million US associates with handheld devices using computer vision to map inventory; 35% of store-fulfilled orders delivered in under three hours in Q4; global inventory +2.6% y/y. Upgrade to B/A by reading the call transcript (marketbeat/aol copies exist; Walmart investor site not tried).
- X. One search summary stated "65% of stores serviced by automation by end FY2026" and "costs per unit improve about 20%". The 65% conflicts with the 60% above (likely a 2026 target vs achieved); the 20% not traced. Do not cite either.

### 3.2 Amazon (incl. India)
- B. 1 million robots deployed across 300+ facilities; DeepFleet generative-AI model improves robot-fleet travel efficiency by 10%; announced 1 Jul 2025 (aboutamazon.com article; fetched via summary, exact URL to confirm; digitalcommerce360 and aibusiness.com carry the same, C). Check "10%" wording: it is travel time/efficiency of the fleet, not whole-FC cost.
- B. Amazon India (aboutamazon.in, "Amazon India delivery network explained", https://www.aboutamazon.in/news/operations/amazon-india-delivery-network-explained, fetched via summary, undated page, content references 2025 and 2026): storage 43 million cubic feet in 16 states; nearly 2,000 last-mile delivery stations; AI used for pick-path optimisation, capacity management, dynamic route optimisation, address matching for unstructured Indian addresses; 55 crore+ items delivered to Prime members same/next day in 2025 (+40%); Amazon Now targeting 300+ cities with 100+ urban fulfilment centres. No AI-attributed KPI.
- C. Amazon India 2026 investment announcements (INR 2,800 crore 2026; USD 13bn added 25 Jun 2026 for AI/cloud, mostly AWS not retail supply chain): press only. Do not treat as supply-chain AI spend.
- C. Amazon Last Mile Routing Research Challenge (MIT CTL, winners announced 30 Jul 2021, USD 175,000 prizes; Transportation Science special issue planned). https://routingchallenge.mit.edu/ . Useful as the best public academic dataset on real-world route sequencing; not India.

### 3.3 Delhivery
- B. FY2025 (FYE 31 Mar 2025) Annual Report, directors' report text as reproduced by Arihant Capital (https://www.arihantcapital.com/company-information/directors-report/68151); the original AR PDF not fetched: "used machine learning extensively to build ... intelligent geo-location, network design, route optimisation, load aggregation, expected time of arrival prediction, product identification and fraud detection"; 45 fully/semi-automated sortation centres and 111 gateways; rated automated sort capacity 8.2 million shipments/day; automated material handling at Bhiwandi, Tauru, Bengaluru; system-directed floor operations, path-expectation algorithms, machine-vision guided truck loading; 18,833 PIN codes. Date of AR filing 16 May 2025 (as reported by the summary).
- C. Network scale figures (99.5% population, 85 fulfilment centres, 158 processing centres, 4,494 last-mile centres, 3.95m km/day) from a search summary of the AR; unverified against the PDF.
- Gap: no quantified AI outcome (e.g. ETA accuracy, cost per shipment attributable to ML). FY2026 AR (published mid-2026) not checked.

### 3.4 Flipkart / Ekart
- B. Agarwal et al. (22 authors, Flipkart), "Faster, Smarter, Leaner: How Flipkart Optimized Its Supply Chain to Unlock Growth", INFORMS Journal on Applied Analytics, vol 56 issue 1, 2026, doi 10.1287/inte.2025.0282, https://pubsonline.informs.org/doi/10.1287/inte.2025.0282 . Bibliographic data and abstract read via Crossref; the INFORMS site returned 403, so I did not see the quantified results. Abstract: central planning platform since 2021 (forecasting plus optimisation layers, ML and operations research) gave "significant reductions in costs and higher delivery speeds through better inventory, capacity, and network flow planning". This is the best Indian peer-reviewed supply-chain-AI case I found; action: get the full PDF through the institution library for numbers.
- C. Ekart franchise outlets (300+, target 1,000+ by end 2026) and "AI demand forecasting in warehouses" claim: Inc42 / search snippets only.

### 3.5 Reliance Retail
- B. Annual Report 2025-26, retail section (https://www.ril.com/ar2025-26/retail.html, via summary): "Adoption of AI and advanced analytics across the value chain" (strengths); JioMart 3,100+ stores serving 5,100+ pincodes across 1,200+ cities; RCPL 3m+ outlets through 5,000+ distributors. No warehouse-automation or forecasting figure in the retail section as summarised.
- B/C. FY2024-25 AR (https://www.ril.com/ar2024-25/retail.html): capex INR 33,696 crore for Reliance Retail (+37.5%) per a press summary (C); 600+ dark stores (C, indianretailer). "AI cameras from farm to shelf" statement appears in a conference interview page and a press summary (C).
- Local file downloads/ril_ir_ar2526 (from another thread) not reviewed.

### 3.6 DMart (Avenue Supermarts)
- A (negative finding). Annual Reports FY2024-25 and FY2025-26 (local text files downloads/dmart_ar_fy2025 and dmart_ar_fy2026): searching the text for "artificial intelligence", "machine learning" and "AI" returns zero hits in both. Supply chain description is distribution centres (consolidating buying and transport through large DCs, solar-powered DC, motion-sensor lighting pilot showing 60% energy drop at a DC, FY25 p65 PDF), inventory audits, 8 new fulfilment centres for Avenue E-Commerce in FY26 (FY26 PDF p46). The FY26 AR says "opportunities to simplify and automate" in general terms (PDF p18). The Aug 2026 concall text also has no AI/forecast hits (grep). Conclusion: DMart discloses no AI in supply chain. This is evidence of thin disclosure, not of no use.
- C. Revenue FY25 INR 593.6bn, 415 stores (Simply Wall St); FY26 500 stores per the FY26 BRSR boundary statement (A, PDF p122).

### 3.7 Shadowfax, Ecom Express, Blue Dart
- C. Shadowfax: UDRHP-I (updated draft red herring prospectus, filed 2025; primary not fetched): FY2025 orders 436.36 million; H1 FY26 294.45 million; 14,758 pin codes at 30 Sep 2025 (press summaries). Company blog claims in-house "SF Maps" engine and "SF Shield" anomaly detection on ~2 million daily deliveries (company marketing, C). Action: pull the RHP/prospectus from SEBI or BSE and read the technology section; likely upgrade to A.
- Ecom Express: acquired by Delhivery (search mention; deal details not verified). No AI data found.
- Blue Dart: no figures found; an AR check (DHL Group/Blue Dart Express AR FY2025-26) is outstanding.

### 3.8 Ocado (global comparator, grocery-specific)
- A. Ocado Group Annual Report and Accounts 2025 (FY25, year to Nov 2025), local text downloads/ocado_ar2025/ocado.txt. Source URL https://cdn.prod.website-files.com/667974bf1bf45146cf81ef19/6a033e1173eb5d5f5b744e73_Ocado_ARA2025_Spreads_Hyperlink_Single.pdf (page numbers below are PDF pages):
  - "AI-driven demand forecasting and inventory management" listed in the Ocado Intelligent Automation proposition (p4), qualitative.
  - 72 million OSP orders delivered worldwide in FY25; international weekly volumes +26% (p3, p7).
  - On-Grid Robotic Pick live in 10 CFCs; most advanced CFC picking c.50% of volumes robotically (p3); Auto Frame Load in 12 CFCs (p7).
  - CFC labour productivity (UPH) +7.9% (headline "+8%", p3; detail p7 area); Ocado Swift Router (routing/short lead-time delivery) enabled in 9 CFCs, up to 2-hour windows (p7); partner delivery drops per shift (DP8) +22% in under a year at two CFCs with intensive support (p7).
  - Four CFC closures in early 2026 (Baltimore, Groveland, Pleasant Prairie, Calgary) are disclosed; useful counter-evidence that automation does not guarantee unit economics.
- C. "100+ applications of AI" is from Ocado's website/search snippet, not in the AR text I searched. Cite as C.
- The AR attributes productivity to robotics plus software, not to AI alone.

### 3.9 Zebra / Locus (as cited deployments)
Not researched in this pass (time). Open item.

## 4. Gaps and thin evidence (hypotheses, not findings)

All below are hypotheses based on absence of evidence in this pass.
- H1. Supplier management/procurement: AI use likely exists (supplier risk, price/forecast collaboration) but is not disclosed by Indian retailers. Likely biggest documentation gap.
- H2. Inbound: appointment scheduling, dock/slot planning, and supplier-to-DC freight matching are probably underdigitised in India's grocery chains, where supplier delivery to DC is manual and fragmented (DMart consolidates through DCs but says nothing on tech).
- H3. Cold chain: India's constraint appears to be physical capacity and temperature compliance rather than AI; AI value is probably in shelf-life based allocation and route/temperature monitoring. Evidence thin; cold-storage statistics found are from aggregators (see section 5).
- H4. Returns/RTO: e-commerce RTO and returns are a known cost in India but I found no quantified AI use (fraud/RTO prediction appears in Delhivery's ML list only as "fraud detection").
- H5. Forecasting for fresh/perishable and hyperlocal SKUs: academic benchmarks (M5) are on ambient Walmart US data; fresh and Indian kirana-adjacent demand is probably under-researched.
- H6. Traditional trade: most Indian grocery volume moves via distributors and kiranas (RCPL "5,000+ distributors, 3m+ outlets"); AI use in that tier is probably minimal and unmeasured.
- H7. Listed Indian grocers (DMart) provide no AI disclosure at all, so a grocery-retail-only India project would rely on interviews, concall transcripts or third-party sources.

## 5. India relevance and data availability

- A. Logistics cost: DPIIT/NCAER "Assessment of Logistics Cost in India": 7.97% of GDP and 9.09% of non-services output for 2023-24, INR 24.01 lakh crore; hybrid method with primary data from 3,500+ industry stakeholders plus MoSPI, RBI and GSTN secondary data; benchmark freight cost per tonne-km; smaller firms bear higher costs. Source read: PIB explainer "From Growth Engine to Global Edge: Supercharging India's Logistics", 27 Nov 2025 (local: downloads/dpiit_logistics_cost/dpiit.pdf; URL https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251127708001.pdf). So the figure is A for the PIB document, B for the underlying NCAER/DPIIT report (not read). The commonly cited 13-14% of GDP is described in the same PIB text as based on partial or external data.
- B. NCAER earlier report (Dec 2023), 7.8-8.9% of GDP for 2021-22: via search snippet only. The NCAER PDF URL (https://www.ncaer.org/wp-content/uploads/2023/12/NCAER_Report_LogisticsCost2023.pdf) returned no file on download (empty); not read. Try again via a browser.
- A. PIB "Logistics: India's growth engine", 16 Aug 2025 (local: downloads/pib_logistics_growth_engine_aug2025/; URL https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/aug/doc2025816613701.pdf): National Logistics Policy launched Sep 2022; PM GatiShakti launched Oct 2021, NMP brings 57 central ministries/departments, all 36 states/UTs, 1,700 data layers; ULIP recorded 100 crore API transactions in Mar 2025 and enables shipment ETAs; Logistics Data Bank averages 45 lakh+ unique container searches a month; GST said to improve transport time by 33% "according to several studies" (not a primary estimate, do not cite as a finding); e-way bill mandatory for goods over INR 50,000 moving between states; sector employs 22 million+.
- A. PIB 27 Nov 2025: LDB 2.0 syncs with ULIP APIs (container, vehicle, railway FNR tracking); SMILE city logistics plans in 8 pilot cities (maps e-commerce delivery routes, warehousing clusters); LEADS 2025 objective-data share 32.5%; IPRS 3.0.
- C. ULIP scale from search snippets: 36-37 systems from 8-10 ministries, 1,800 data fields, 118 APIs, 160 crore transactions by Aug 2025, 1,000+ companies registered, 76 NDAs (taxtmi, business-standard, Economic Survey snippets). Figures differ across sources, treat as indicative; X on exact system counts.
- C. Logistics Performance Index rank 38 (World Bank 2023) from search snippet; verify at World Bank LPI site.
- Not obtained: Economic Survey 2025-26 logistics section text (searches returned secondary pages only); GST/e-way bill monthly volumes (GSTN/GST Council data not fetched); NITI Aayog logistics-related reports; Ministry of Commerce NLP text. These are the next primary pulls.
- Data usable for the project: logistics cost by component and firm size (dashboard from DPIIT), e-way bill/FASTag derived corridor data (Gati Shakti), ULIP API data for ETA, LDB. All are system-level; none identifies retail AI use. No public retailer-level SKU, inventory or transport data in India was found.
- Cold chain context (C, aggregators citing government/ICAR/NCCD; not verified): 8,815 cold storage units, 40.2 million MT capacity, deficit ~35 million MT; post-harvest loss ranges 6.70-15.88% (fruit), 4.58-12.44% (vegetables) (ICAR-type study as quoted in an answer to Parliament, Rajya Sabha PQ 20 Dec 2024 appears in results at https://rsdebate.nic.in/bitstream/123456789/753312/1/PQ_266_20122024_U2954_p221_p224.pdf, not opened). A claim of "only 10% of perishables use cold chain, INR 92,000 crore annual loss" is X (unsourced).

## 6. Consulting, analyst and academic sources

- C/X. McKinsey "AI-driven forecasting reduces errors by 20-50%, lost sales -65%, inventory -20 to 50%": appears only in vendor/blog copies; I did not locate the McKinsey document. Treat as X until the original (likely McKinsey "Succeeding in the AI supply-chain revolution", 2021) is read and the exact wording and year confirmed.
- C. Gartner: 72% of supply chain organisations say they have deployed GenAI, only 23% have a formal AI strategy ("2025 data", from a Stealth Agents summary; Gartner Peer Community page exists https://www.gartner.com/peer-community/oneminuteinsights/generative-ai-supply-chain-transformation-zoo, not read). Earlier survey: Nov 2023, 127 leaders, half plan GenAI in 12 months (C). Mixed respondent bases; low confidence.
- C. NASSCOM-EY AI Adoption Index: India 2024 score 2.47 (4-point scale) vs 2.45 in 2022; 87% of firms in middle stages; Index 2.0 surveyed 500 companies across 7 sectors including CPG and retail and transport and logistics (indiaai.gov.in summaries). Sector split for retail not obtained.
- C. M5 forecasting competition: 42,840 hierarchical Walmart sales series; Makridakis et al., International Journal of Forecasting (2022 special issue). ScienceDirect blocked (403). Details such as the number of teams and the improvement over benchmark are unverified here; get via arXiv/author copy.
- Not searched: BCG, Bain; peer-reviewed Indian-grocery forecasting or route-optimisation papers.

## 7. Source status log

Blocked or failed: INFORMS (403), ScienceDirect M5 papers (403), NCAER PDF (empty download), aboutamazon.com first guessed URL (404, second worked via summary), Economic Survey (not located as primary).
Downloaded folders created by this task: downloads/ocado_ar2025, downloads/dpiit_logistics_cost, downloads/pib_logistics_growth_engine_aug2025. (Other folders under downloads/ were already present from other threads; I used only the Walmart 10-K/ARS and DMart AR/concall texts from them.)

## 8. Suggested next pulls (priority)

1. Walmart Q4 FY26 transcript (to settle 60% vs 65%) and Walmart investor/ESG supply chain material.
2. Delhivery AR FY2026 PDF (BSE/NSE) and Shadowfax RHP: search for "machine learning" and quantified outcomes.
3. Flipkart INFORMS paper full text for numbers.
4. Economic Survey 2025-26 logistics section and NLP 2022 original (commerce.gov.in/PIB); GSTN e-way bill volumes.
5. McKinsey/BCG/Bain original reports; M5 paper text.
6. Zebra/Locus deployment case studies; Blue Dart AR; Reliance AR 2024-25 full text.
