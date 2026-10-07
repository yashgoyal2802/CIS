# AI in Indian grocery retail and its supply chain: stage-by-stage evidence and fit check

Compiled 7 Oct 2026. Builds on `retail_supply_chain.md` (same folder), which covers supply-chain AI broadly. This note narrows to grocery retail and quick commerce, re-reads the primary files in `downloads/`, and tests whether the topic is viable after the mentor said banking is outside his area.
Grades: A = read in the original document text; B = primary exists but seen only through a summary; C = press/vendor/consultancy; X = unverified, do not cite.

## 1. Verdict

Viable, but with a different shape from the lending study. The workflow is clear and the Indian scene is rich (inventory-led quick commerce, DMart, Reliance, More). Quantified AI outcomes in company filings are close to absent, so the central finding will be a disclosure gap, backed by one or two interviews or expert inputs as primary data. Banking remains stronger on data; grocery is stronger on mentor fit.

Re-scored on the earlier weights (total = sum(weight x score) / 5, scores 1-5, judgement calls):

| Criterion (weight) | Grocery / retail supply chain | Rationale |
|---|---|---|
| Credible public data on AI use (25%) | 2 | Filings are qualitative (Eternal, Walmart, Tesco, Ahold) or silent (DMart, zero AI mentions). One quantified Indian case (More Retail, 2021) is vendor co-authored. |
| Workflow breaks into stages (20%) | 5 | Sourcing to last mile is a standard chain; comparators exist (Walmart, Ocado, Tesco). |
| Gaps where AI is underused (20%) | 4 | Fresh wastage, supplier management, dark-store forecasting under the inventory-led model, and the KPI disclosure gap itself. All still hypotheses. |
| Quantifiable impact (15%) | 2 | Ocado UPH +7.9% (A) is robotics plus software; More Retail is the only Indian forecast-accuracy number. |
| Recruiter appeal and India relevance (10%) | 4 | Quick commerce, retail, FMCG and supply-chain roles. |
| Manageable in 80 hours (10%) | 3 | Sources are on hand, but interviews must be arranged and the evidence is thin. |
| **Total** | **66 / 100** | Earlier scorecard: banking 81, insurance 68, e-commerce 63. |

## 2. Workflow used (my framework, not a published taxonomy)

1 Sourcing and supplier management; 2 Demand forecasting and assortment planning; 3 Inbound, DC and warehouse operations; 4 Inventory allocation and replenishment (DC to store or dark store); 5 Store and dark-store operations; 6 Last-mile delivery; 7 Customer ordering, support and returns; 8 Pricing, promotion and markdown (cross-stage); 9 Cold chain, food safety and compliance (cross-stage).

## 3. Evidence by stage

| Stage | What was read | Grade | Depth |
|---|---|---|---|
| 1 Sourcing | Eternal lists "supply-chain management" among AI uses but gives no detail; says AI "will not ... negotiate with suppliers in tier 2 cities" (Q4FY26 letter, PDF p5). Reliance AR retail page: "scaled sourcing", no AI detail. | A / B | None |
| 2 Forecasting | Eternal: "Demand prediction, route optimisation, supply-chain management, customer experience, fraud detection, catalogue quality, and partner support already use AI" (p5), no metrics. More Retail (AWS blog, 12 Mar 2021, co-written by More Retail and Ganit): 600+ supermarkets, 6,000+ store-SKU combinations; forecast accuracy 24% to 76%; fresh-produce wastage down by up to 30%; in-stock 80% to 90%; gross profit +25%; earlier statistical models were as low as 40% accurate. Spencer's FY26 AR (PDF p23): Nature's Basket roadmap "deeper inventory integration, demand forecasting, customer analytics". DMart: zero hits for AI or machine learning in AR FY25, AR FY26 and the Aug 2026 call text. | A | Some (one quantified case, 2021) |
| 3 Inbound, DC, warehouse | Eternal: "17 million square feet of warehousing and dark store space" (p4). Swiggy Q1FY27 letter (PDF p14): "densification and warehouse/store automation" is expected to add INR 5 per order of the ~INR 30 per order needed for break-even (a target, not a result). Ocado AR 2025: CFC labour productivity +7.9%, robotic pick about 50% in the most advanced CFC, four CFC closures in 2026 (comparator). | A | Strong abroad, target only in India |
| 4 Allocation, replenishment | Eternal (1P model in quick commerce from Q1FY26, p3/p7) and Swiggy (IOCC status lets Instamart own inventory, ~80 bps contribution margin, p16) both move to inventory ownership. These are model changes, not AI claims. Walmart ARS (p8): "increasingly include the use of AI-powered tools ... operational efficiency". | A | Some (model shift, no AI metric) |
| 5 Store, dark-store ops | Eternal: "It will not stock shelves in a dark store" (p5); 2,243 stores at end Q4FY26 (p7). Ahold Delhaize AR 2025 (p32): AI "contributes to supply chain optimization". | A | Some |
| 6 Last mile | Tesco AR 2025 (p17): "We utilise AI to optimise the routes our drivers take". Delhivery AR FY25 ML list (B, in `retail_supply_chain.md`). No Indian quantified result. | A / B | Some |
| 7 Customer | Eternal: natural language search and Healthy Mode on Zomato (p6); Amazon Rufus and Meesho bot in `ecommerce.md`. Grocery-specific evidence not found. | A | Some |
| 8 Pricing, promotion | Nothing on AI in Indian grocery pricing or markdown found. | n/a | None |
| 9 Cold chain, compliance | FSSAI actions on dark stores and Maharashtra FDA licence suspensions are press-reported (C). Cold-chain capacity figures are aggregator-sourced (C). No AI evidence. | C | None |

Not used as evidence: Zepto's 1,139 dark stores, 46,000 SKUs and INR 1,325 crore technology allocation (U-DRHP, via press summaries only, B/C; the U-DRHP itself was not opened). "Multi-model ARIMA/Prophet/LSTM at Zepto" comes from an Analytics Vidhya blog (C/X). Vendor claims of 20-42% overstock cuts for Indian chains (commmerce.com) are C/X.

## 4. Gaps (hypotheses, not findings)

- G1. Fresh-produce forecasting and markdown: More Retail shows value in 2021, but no listed grocer reports wastage, in-stock or forecast accuracy today. Open question: adoption gap or disclosure gap.
- G2. Dark-store assortment and replenishment under inventory ownership: forecast misses now become the platform's own write-offs (the shift in G2 is documented by Eternal and Swiggy, the AI link is inferred).
- G3. Supplier and B2B/kirana distribution: RCPL cites 5,000+ distributors and 3m+ outlets; no AI disclosure at that tier.
- G4. Cold chain and shelf-life-based allocation: no AI evidence in this pass.
- G5. Measurement: no common KPI (forecast error, availability, wastage) is disclosed across Indian grocers.

## 5. Regulatory screen (to be read from primary text)

- FDI rules on marketplace inventory and the IOCC route: Swiggy letter (A, p16) confirms domestic ownership crossed 50% on 1 Jul 2026 and the IOCC route will let Instamart own inventory. Government scrutiny of dark-store ownership is press-reported (C).
- FSSAI dark-store licensing and food-safety actions (C).
- CCI cost-of-production regulations, May 2025 (C), relevant to pricing AI.
- DPDP Rules for customer data (primary: PIB, already in `AI industry choice for CIS` notes).
- Legal Metrology and Consumer Protection (E-Commerce) Rules not researched.

## 6. Risks

- Primary AI disclosure is thin; a proposal must not promise stage-by-stage outcomes.
- More Retail figures are vendor co-authored, 2021, and one retailer.
- Several filings were read as extracted PDF text; Reliance AR retail page and Delhivery were seen only via summary.
- Zepto and Flipkart primary documents (U-DRHP, INFORMS paper numbers) are the best upgrade targets.

## 7. Next pulls

1. Zepto U-DRHP technology and risk sections (SEBI/BSE copy).
2. Flipkart INFORMS paper full text via library.
3. Walmart Q4 FY26 call transcript (60% vs 65% automation).
4. Spencer's, More Retail and Reliance AR text for supply-chain disclosures.
5. FSSAI and DPIIT primary notifications on dark stores and inventory-led models.
6. Two to four practitioner interviews (retail planners, supply-chain managers) as primary data.
