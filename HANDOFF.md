# CIS project handoff (written 7 Oct 2026)

Read this file first. It is meant to let a fresh session continue without any earlier context.

## 1. What this is

Yash Goyal (PGPM PPM-022-159) is doing a Course of Independent Study (CIS): 80 hours, 2 credits, empirical, written report plus faculty-panel defence. Faculty mentor: Prof. Abhishek Jha. See `CIS Course outline.docx`.
- Grading weights: problem definition 20%, research method 20%, discussion and recommendation 20% (needs a contingency plan), presentations 20%, insights 10%, fieldwork effort 10%.
- Weekly update to the mentor; fortnightly in-person meeting.
- The outline says all work must be owned by the student and violations get an F on AI use. Treat everything drafted here as material for Yash to review, edit and own before submission.

## 2. Study design (same for any industry)

Map the end-to-end workflow into stages, research which AI is used in each stage, for what, and how much (primary or credible sources only), then find where AI is missing, partial or unmeasured and propose improvements as hypotheses. Separate real adoption gaps from gaps that are only disclosure gaps. No causal claims. Every figure carries a source type and year.
Evidence grades used in the notes: A = read in the original document; B = primary exists but seen only via a summary; C = press, vendor or consultancy; X = unverified, do not cite.

## 3. What happened, in order

1. Three industries were researched and compared: e-commerce, banking and lending, insurance claims. Scorecard result: banking 81, insurance 68, e-commerce 63 (`reports/AI industry choice for CIS.md`, notes in `research_notes/AI industry choice for CIS/`).
2. Banking was chosen and verified against primary documents (Bajaj, SBI, HDFC, ICICI, Axis, RBI FREE-AI) in `research_notes/Banking verification/`. A lending proposal was written: `CIS Proposal - AI in Indian Lending Workflow.docx`.
3. The mentor said banking is not his strong area. The topic was switched to **grocery retail and its supply chain in India**, keeping the same method and proposal format.
4. A new proposal was generated: `CIS Proposal - AI in Indian Grocery Retail Supply Chain.docx` (status: revised topic proposal for approval, 7 Oct 2026). It is NOT yet approved by the mentor.

## 4. Current topic: key findings so far

Full detail with page references is in `research_notes/Retail grocery supply chain/grocery_ai_stage_evidence.md` and `retail_supply_chain.md`.
- Re-scored fit about 66/100 on the earlier weights (data credibility 2, workflow 5, gaps 4, quantifiable impact 2, appeal 4, manageable 3). Banking was stronger on data; grocery is better for mentor fit.
- Workflow used (my framework, not a published taxonomy), 9 stages: sourcing and supplier management; demand forecasting and assortment; inbound, DC and warehouse; allocation and replenishment; store and dark-store operations; last mile; customer ordering, support and returns; pricing, promotion and markdown (cross-stage); cold chain, food safety and compliance (cross-stage).
- Evidence is thin and mostly qualitative.
  - Eternal Q4 FY26 shareholder letter: demand prediction, routing and supply chain "already use AI", no metrics; says AI will not stock dark-store shelves.
  - Swiggy Q1 FY27 letter: warehouse/store automation plus densification worth about INR 5 per order (a target); IOCC route to own inventory worth about 80 bps contribution margin.
  - DMart FY25 and FY26 annual reports and Aug 2026 call: zero AI or machine-learning mentions.
  - More Retail (AWS blog, Mar 2021, retailer plus vendor): forecast accuracy 24% to 76%, fresh wastage down up to 30%, in-stock 80% to 90%, gross profit +25%. The only quantified Indian forecasting case.
  - Global comparators read in primary text: Ocado (UPH +7.9%, about 50% robotic pick, four CFC closures in 2026), Tesco (AI route optimisation, qualitative), Ahold, Walmart, Spencer's (forecasting as roadmap).
- Proposed focus (scope B): forecasting and replenishment including fresh (deepest); dark-store/DC operations and last mile (medium); inventory-ownership shift (lighter); supplier management and cold chain as named evidence gaps.
- Hypotheses (not findings): fresh forecasting and markdown; dark-store assortment under inventory ownership; supplier and kirana-tier lead-time prediction; cold-chain shelf-life allocation.

## 5. Open questions for the mentor (already in the proposal)

1. Is a study based on disclosed metrics, a gap analysis and a few practitioner interviews acceptable, or are quantified before-and-after outcomes expected for every stage?
2. Centre on supermarket chains, quick commerce, or both? Proposed: both, with forecasting and replenishment as the common thread.

## 6. Next steps (priority order)

1. Get the mentor's reaction to the grocery proposal and the two questions above. Everything else depends on scope.
2. Pull and read the biggest evidence upgrades: Zepto updated DRHP (filed 8 Jun 2026; technology and risk sections), Flipkart INFORMS paper "Faster, Smarter, Leaner" (doi 10.1287/inte.2025.0282) via the college library, BigBasket/Tata Digital disclosures, Walmart Q4 FY26 call transcript (60% vs 65% automation conflict), Reliance AR retail section (currently only seen via summary), Delhivery AR FY26.
3. Update the evidence table in the proposal and the stage note as items are read. Keep grades honest.
4. Plan primary data: 2 to 4 practitioner interviews (retail planners, supply-chain managers) to cover the disclosure gap; draft an interview guide.
5. Regulatory screen from primary text: FSSAI dark-store licensing, FDI rules on marketplace inventory and the IOCC route, CCI cost-of-production regulations (May 2025), DPDP, Legal Metrology, Consumer Protection (E-Commerce) Rules.
6. Write the 80-hour plan (suggested: about 10 h workflow and source audit, 25 h forecasting deep dive, 15 h DC/dark-store and last mile, 10 h gap analysis, 8 h interviews, 7 h regulatory, 5 h buffer) and the contingency plan the rubric asks for. Fallbacks: return to lending (evidence in `research_notes/Banking verification/`) or narrow to forecasting only.
7. Establish the weekly/fortnightly mentor reporting rhythm.

## 7. Things to be careful about

- Many figures are self-reported or press-relayed; Zepto's 1,139 dark stores, 46,000 SKUs and INR 1,325 crore technology allocation come from press summaries of the U-DRHP and are not used as evidence yet. Vendor blogs (commmerce.com overstock claims, Analytics Vidhya on Zepto models) are C/X.
- "Not disclosed" does not mean "not adopted".
- Several quick-commerce details are as of mid-2026 and may change.

## 8. Repo layout and tooling

- Proposals and course outline: root `.docx` files. `RBI_FREEAI_report.pdf` is the RBI report used for banking.
- `reports/`: industry-choice report (markdown).
- `research_notes/`: notes per industry plus `downloads/` of primary PDFs and their extracted `.txt`. Work from the `.txt` files where they exist.
- Not in the repo: `research_notes/Retail grocery supply chain.zip` (141 MB, exceeds GitHub's 100 MB limit; it is an archive of the folder).
- Searching extracted text: `research_notes/Banking verification/downloads/banks/run1/g.py` prints regex matches with context per PDF page (`python g.py file.txt "regex" 200`).
- PDF to text: `pdftotext -layout in.pdf out.txt`. The proposal `.docx` files can be rebuilt by editing the XML of the existing one (same table styling: header fill 1F3A5F, 9 pt text).
