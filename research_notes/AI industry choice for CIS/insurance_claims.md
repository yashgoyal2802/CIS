# AI in the Insurance Workflow with a Focus on Claims (India emphasis, global examples)

Research date: 2026-10-06. Method: web search plus page fetches (about 22 tool calls). Many India figures come from secondary summaries of IRDAI and NHA documents. I could not open the primary PDFs, so each such figure is flagged. Credibility tags: [P] primary (regulator, company filing, official release), [S] secondary (news or trade press repeating a primary), [V] vendor or marketing claim, [C] consulting report (methodology often opaque).

Workflow map (for part (a)): distribution/lead generation -> underwriting and pricing -> policy issuance -> servicing -> CLAIMS (FNOL -> triage -> documentation -> assessment/surveying -> fraud detection -> settlement -> subrogation -> grievance handling) -> renewals/retention. Claims-stage evidence below is much deeper than evidence for the other stages. My searches this session focused on claims, so distribution, underwriting, servicing and renewals were NOT researched and are listed under Gaps.

---

## Q1. Which stages have the best-documented, quantified AI impact, and which are thinly documented?

### Takeaway
Quantified, attributable claims figures exist for FNOL and triage, fully automated simple-claim settlement (Lemonade), motor image assessment (Ping An, Tractable, Indian insurers), fraud screening in public schemes (PM-JAY), and document automation. Most are single-company, self-reported and loosely defined (for example "reduction in processing time"). I found no audited, comparable, cross-insurer benchmarks. Indian insurer figures are mostly qualitative or target-based, not measured outcomes.

### Cited Findings

**Industry-level claims adoption and impact (consulting, secondary or vendor-adjacent)**
- BCG (2025): only 7% of surveyed insurers have brought AI to scale, and about two-thirds remain in pilots. About 70% of scaling challenges are people, organisation and process, not technology. Service and operations staff given AI knowledge assistants show productivity gains above 30%. [C] — [BCG, Insurance Leads in AI Adoption](https://www.bcg.com/publications/2025/insurance-leads-ai-adoption-now-time-to-scale)
- BCG, as relayed by a search summary (not verified on the BCG page): AI claims applications bring cost reductions up to 20% and claim-speed gains up to 50% on complex claims. Simple claims could see real-time resolution for up to 70% and 30-50% lower operating cost. The claim "over 90% of claims events still processed without automation" came from the same search summary and I could not trace it to a primary page. Treat both as UNVERIFIED until checked against [BCG Platinion, Closing the 5 Billion Automation Gap](https://www.bcgplatinion.com/insights/closing-the-5-billion-euro-automation-gap-how-insurers-navigate-the-path-to-an-intelligent-core?local=es) and [BCG, How Insurers Can Supercharge Strategy with AI](https://www.bcg.com/publications/2025/how-insurers-can-supercharge-strategy-with-artificial-intelligence). [C/S]
- A McKinsey figure of "full AI adoption 34% (up from 8%)" and benchmark claims of "cycle time 30 to 7.5 days" and "cost per claim $40-60 to $25-36" appeared only in an aggregator search summary with no traceable primary source. DO NOT USE without verification. [S, unverified]

**Company-level claims AI (global)**
- Lemonade FY2025 10-K: roughly 55% of claims were automated, with instant or near-instant processing from start to finish. AI Jim takes the first notice of loss with no human 96% of the time. 1,282 employees at 31 Dec 2025, about 3 million customers. [P, SEC filing, FY2025] — [Lemonade 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm). Caveat: "automated" is Lemonade's own definition. The book is mostly renters, home and pet insurance, so simple claims dominate. The 10-K is the best primary source for this.
- Allianz "Project Nemo" (Australia, live July 2025): seven task agents (planner, cyber, coverage, weather, fraud, payout, audit). About 80% cut in processing and settlement time for food-spoilage claims under AUD 500, taking days to hours. Live in under 100 days. A human still makes the final payout decision. [P, company news, 2025] — [Allianz](https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html). Secondary: [insuranceNEWS.com.au](https://www.insurancenews.com.au/insurtech/ai-trial-provides-blueprint-for-future-allianz-says). Narrow scope, one product line.
- Ping An (China): "Smart Quick Claim" launched across life, auto and health in 2024, with branded "one-sentence reporting, one-click upload, one-minute validation". Image damage assessment, OCR bill recognition and biometrics. Source for the programme: [Ping An 2024 results presentation](https://group.pingan.com/resource/pingan/IR-Docs/2025/pingan-ar24-presentation.pdf) [P]. The specific numbers (60% first-time pass rate improvement, 3.65 bn model calls) came from an aggregator ([AI CERTs](https://www.aicerts.ai/news/ping-ans-insurtech-value-unlock-momentum/)) and need checking against the deck. [S, unverified]. SOA also has a Greater China AI report: [SOA 2025](https://www.soa.org/globalassets/assets/files/resources/research-report/2025/ai-insurance-greater-china-report.pdf) [peer-reviewed-adjacent, not read].
- Tokio Marine: partnered with Tractable (computer vision) for auto damage assessment, "weeks to minutes" per trade press. [S] — [Dig-In](https://www.dig-in.com/news/tokio-marine-taps-tractable-ai-for-claims). Tokio Marine Insurance UAE reports 90% faster claims processing with Kodak Alaris document automation, 3x daily volume and 60% fewer exceptions. [V, vendor-linked press] — [Khaleej Times](https://www.khaleejtimes.com/business/tokio-marine-insurance-uae-simplifies-claims-with-kodak-alaris-ai-driven-automation). Tokio Marine & Nichido with SHIFT on gen-AI for fraud and claims optimisation: [PR Newswire](https://www.prnewswire.com/news-releases/shift-provides-tokio-marine--nichido-fire-insurance-with-new-generative-ai-capabilities-for-fraud-detection-and-claims-processing-optimization-initiatives-302541742.html) [V]. Different entity from the Japanese parent. Do not conflate.
- Zurich: AI on personal-injury claims cut handling from about an hour to seconds in trials, and a Quantexa decision-intelligence partnership for fraud was announced October 2025. [S] — [Carrier Management tag page / search result](https://www.carriermanagement.com/tag/artificial-intelligence-claims/). I did not open the underlying article.
- Swiss Re "ClaimsGenAI": a reinsurer tool for claims; the page returned HTTP 403 so I have no figures. [Swiss Re page](https://www.swissre.com/risk-knowledge/advancing-societal-benefits-digitalisation/how-generative-ai-is-transforming-insurance-claims-claimsgenai.html) — to be retrieved manually.
- AXA, Progressive: no quantified claims-AI figures retrieved. Not searched in depth. UNVERIFIED and listed as a gap.

**Indian insurers (claims AI)**
- Star Health: about 20% of claims processed via AI today, aiming above 50% of (routine) cashless claims within two years. 85% of claim value is cashless. Human work to focus on exceptions, high-value claims and fraud. [S, news citing management, 10 Mar 2026] — [Angel One](https://www.angelone.in/news/market-updates/star-health-expects-most-cashless-claims-to-be-settled-by-ai-within-2-years). A tech-spend rise from Rs 120 cr to Rs 200 cr by FY27 and "average cashless approval about 2 hours" appeared in a search summary only. [S, unverified]. "AI-processed" is undefined, and it is a target, not an outcome.
- ICICI Lombard: claims itself as first with an AI/OCR-based health claim automation that can run the process in "just a minute", with investigation turnaround "a day or less". Also AI car-inspection from photos. [V, company blog/trade press, undated] — [ICICI Lombard blog](https://www.icicilombard.com/blogs/health-insurance/mb/icici-lombard-first-to-launch-ai-automated-health-insurance-claims), [Analytics India Mag](https://analyticsindiamag.com/ai-features/how-icici-lombard-leverages-ai-and-analytics-for-automated-processing-of-insurance-claims/).
- Bajaj Allianz General: "Motor on the Spot" in the Caringly Yours app, where the customer uploads damage images and small claims settle within about 30 minutes up to certain amounts. Stated claim settlement ratio 99.2% for FY2024. [V/S] — [Bajaj Allianz claims page](https://www.bajajgeneralinsurance.com/general-insurance-claims.html), [PolicyBazaar](https://www.policybazaar.com/insurance-companies/bajaj-allianz-car-insurance/claim/). No AI-attributed share of claims published.
- Digit: video-based motor own-damage survey. Acko: ML models for claim estimation and payout. Edelweiss has AI car inspection. [S] — see ICICI/Analytics India links above. No percentages found.
- HDFC Ergo: nothing quantified retrieved. Unsearched. Gap.

**Fraud (India, public scheme)**
- NHA National Anti-Fraud Unit, FY2025-26: 2,842 hospitals penalised (Rs 114.06 cr); 2,003 de-empanelled and 839 suspended; Rs 678.47 cr of suspicious claims blocked before payment. More than 100 continuously refined algorithms. Auto-adjudication flags such as gender-package mismatches and repeat once-only procedures. Hospital Vulnerability Index dashboard. Biometric authentication for dialysis. Scheme has 35,908 empanelled hospitals; Rs 48,828 cr spent on treatment in 2025-26. [S, medicaldialogues citing NHA Annual Report 2025-26] — [Medical Dialogues](https://medicaldialogues.in/news/health/hospital-diagnostics/ayushman-bharat-fraud-national-health-authority-slaps-rs-114-crore-penalty-on-2842-hospitals-175384). Also [ETV Bharat](https://www.etvbharat.com/en/bharat/violation-of-guidelines-under-ab-pmjay-several-hospitals-de-empanelled-enn26080703609). The earlier figure of Rs 562.4 cr fake claims detected is at [IBTimes India](https://www.ibtimes.co.in/government-detects-rs-562-4-crore-fake-ab-pmjay-claims-implements-ai-based-monitoring-curb-fraud-879401) [S]. The cleanest source would be the PIB/Parliament reply or the NHA annual report.
- Industry rule of thumb "about 15% of health claims contain some fraud element" and "Rs 600-800 cr annual losses" are from a general explainer with no traceable primary source. UNVERIFIED, do not rely on them. [S] — [IndiaAI](https://indiaai.gov.in/article/tackling-the-terrors-of-insurance-fraud-with-ai)

### Inferences
- Best documented: FNOL/triage and simple-claim automation (Lemonade, 10-K), motor photo assessment (several firms, mostly vendor or press), and fraud screening in PM-JAY (government data). Thinly documented: subrogation, grievance handling, settlement/leakage analytics, reinsurance recovery, and any stage in India with measured outcomes.
- Typical metric families are speed (hours or minutes), share automated, cost per claim and fraud blocked. Few sources give accuracy, customer-satisfaction effects, false-positive or wrongful-denial rates.
- Global leaders cherry-pick low-severity, high-frequency claims. This is a design pattern a proposal could reuse in India (small-ticket health, OPD, motor own damage).

### Gaps
- Distribution/lead gen, underwriting and pricing, policy issuance, servicing, renewals/retention: NOT researched this round. Needs a separate pass (candidates: Acko, Digit, Policybazaar, HDFC Ergo; Swiss Re sigma on underwriting).
- AXA, Progressive, Allianz Trade, Zurich and HDFC Ergo primary figures; Swiss Re ClaimsGenAI numbers (403); Capgemini World Insurance Report; NASSCOM; Munich Re.
- No independent audit of any vendor or insurer automation claim.

---

## Q2. What are the best primary and official sources?

### Takeaway
Use IRDAI Annual Report and Handbook (claims, grievances), NHA annual reports/PIB replies, SEC filings (Lemonade), insurer annual reports and public disclosures, and regulator documents for the regulatory layer. Treat consulting and press as secondary and vendor case studies as marketing.

### Cited Findings
- IRDAI Annual Report 2024-25 (primary, accessed here only via a secondary summary). Health: 3.26 cr claims, Rs 94,248 cr paid (another snippet says 94,247), average claim Rs 28,910, 87% settled, 8% repudiated, about 5% pending, about 58% cashless. Life settlement 97.82% (individual) and 99.68% (group). Motor premium Rs 99,093 cr (+7.97%). Grievances 2,57,790 (+20%), of which general and health 1,37,361, with about 69% of those claims-related. [S] — [Algates summary](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/). Verify against irdai.gov.in before citing.
- Earlier IRDAI report coverage: health claim rejections up 19.1% in FY24. [S] — [Business Standard](https://www.business-standard.com/amp/finance/personal-finance/health-insurance-claims-rejection-up-19-10-in-fy24-irdai-report-124122700754_1.html) (snippet only, not opened). Further context: [Business Standard, Jan 2026](https://www.business-standard.com/finance/personal-finance/paying-claims-or-pushing-back-what-irdai-data-reveals-about-insurers-126010100580_1.html).
- IRDAI (Insurance Fraud Monitoring Framework) Guidelines, 2025: issued 9 Oct 2025, effective 1 Apr 2026, replaces the 2013 circular. Requires board-approved anti-fraud policy, Fraud Monitoring Committee, behavioural analytics encouraged, fraud data reported to the Insurance Information Bureau for a national database. [S] — [TaxGuru](https://taxguru.in/corporate-law/irdai-insurance-fraud-monitoring-framework-guidelines-2025.html), [Ankura](https://ankura.com/insights/playbook-to-unlocking-the-power-of-irdais-2025-insurance-fraud-monitoring-framework). Primary PDF: [IRDAI](https://irdai.gov.in/documents/37343/366029/%E0%A4%86%E0%A4%88%E0%A4%86%E0%A4%B0+%E0%A4%A1%E0%A5%80%E0%A4%8F%E0%A4%86%E0%A4%88+(%E0%A4%AC%E0%A5%80%E0%A4%AE%E0%A4%BE+%E0%A4%A7%E0%A5%8B%E0%A4%96%E0%A4%BE%E0%A4%A7%E0%A4%A1%E0%A4%BC%E0%A5%80+%E0%A4%A8%E0%A4%BF%E0%A4%97%E0%A4%B0%E0%A4%BE%E0%A4%A8%E0%A5%80+%E0%A4%A2%E0%A4%BE%E0%A4%82%E0%A4%9A%E0%A4%BE)+%E0%A4%A6%E0%A4%BF%E0%A4%B6%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6,+2025+_+IRDAI+(Insurance+Fraud+Monitoring+Framework)+Guidelines,+2025.pdf/99fa5c70-aee2-43af-d52b-50818f53c1df?version=1.1&t=1760095258963&download=true) (not opened).
- Lemonade SEC filings and shareholder letters (primary, quarterly): [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm), [Q4 2024 letter](https://www.lemonade.com/investor-relations-bo/wp-content/uploads/2025/04/LMND-Shareholder-Letter-Q4-2024.pdf).
- Ping An annual results decks: [2024 deck](https://group.pingan.com/resource/pingan/IR-Docs/2025/pingan-ar24-presentation.pdf).
- Peer-reviewed or academic leads (only titles seen): MDPI Risks on EU AI Act bias in life/health underwriting ([doi](https://doi.org/10.3390/risks13090160)); an IJRSI paper on challenges of national health insurance ([RSIS](https://rsisinternational.org/journals/ijrsi/uploads/vol13-iss4-pg1119-1124-202605_pdf.pdf)); a ResearchGate paper "AI-Based Fraud Detection in Insurance Claim in India" ([link](https://www.researchgate.net/publication/403118464_AI-Based_Fraud_Detection_in_Insurance_Claim_in_India)). Quality unassessed; likely low-tier journals.

### Inferences
- Claim "settlement ratio" tables in comparison sites (Ditto, PolicyX, Plum) are derived from IRDAI disclosures, but are marketing-driven. Go to the IRDAI Annual Report, the insurer public disclosures (mandatory claims data), or the IRDAI Handbook.
- Insurer annual reports in India rarely quantify AI impact. Earnings calls and investor decks are likelier sources.

### Gaps
- I did not open any IRDAI primary PDF, Swiss Re sigma, Munich Re, Capgemini WIR, McKinsey or NASSCOM report. These are the first things to pull manually.

---

## Q3. Where are the real gaps in AI adoption in Indian insurance claims?

### Takeaway
There is no measured evidence in this session to prove under-use; inference only. Candidates: low-value, high-volume claim automation beyond insurer-stated pilots, claim-rejection explainability, grievance handling, subrogation (motor third-party), and standardised hospital data.

### Cited Findings
- The sector is large and complaint-heavy: 2,57,790 grievances in FY25 (+20%), about 69% of general/health complaints claims-related; 8% of health claims repudiated. [S, IRDAI annual report via Algates] — [link](https://algatesinsurance.in/irdai-annual-report-2024-25-highlights/)
- Star Health's own AI share is about 20% of claims, with a goal above 50% in two years. [S] — [Angel One](https://www.angelone.in/news/market-updates/star-health-expects-most-cashless-claims-to-be-settled-by-ai-within-2-years)
- The National Health Claims Exchange (NHCX), built by NHA with IRDAI, aims to standardise claims and give insurers structured machine-readable data for faster adjudication and fraud detection. As of July 2024, 34 insurers/TPAs and 300+ hospitals were on it. [S] — [Digital Health News](https://www.digitalhealthnews.com/irdai-plans-to-onboard-health-exchange-and-bima-sugam-by-august-1), [NHA PDF](https://nathealthindia.org/wp-content/uploads/2025/06/National-Health-Claims-Exchange_Latest.pdf), [Knowledge Ridge](https://www.knowledgeridge.com/expert-views/nhcx-streamlining-health-insurance-claims/). I have no current adoption figure.
- Gen-AI claims comms at scale exists elsewhere (one major carrier handling about 50,000 claims communications a day per BCG). [C] — [BCG](https://www.bcg.com/publications/2025/insurance-leads-ai-adoption-now-time-to-scale). No Indian equivalent found.

### Inferences (my analysis; label as hypotheses to test)
- Gap 1, rejection and repudiation reasoning: with 8% of health claims repudiated and claims the dominant grievance driver, an explainable claim-denial review and customer-communication layer looks underserved. I found no Indian insurer publishing results here.
- Gap 2, hospital-side cost/tariff anomaly detection beyond fraud: PM-JAY has 100+ algorithms, but I found no evidence of the same rigour in private health claims (inference).
- Gap 3, small-ticket and OPD/motor own-damage straight-through processing: Allianz Nemo and Lemonade show the pattern; Indian firms (Bajaj 30-minute motor) have pilots but no published share-automated metric.
- Gap 4, grievance/ombudsman triage: no AI examples found at all. A candidate for a proposal.
- Gap 5, subrogation and third-party motor (MACT) recovery: no AI evidence found in India or globally in this pass.
- Gap 6, vernacular, voice-first FNOL for rural and PM-JAY populations: not researched; hypothesis only.

### Gaps
- No data on per-insurer AI penetration; the IRDAI WG-AI (below) is itself tasked with mapping adoption, so official numbers may appear after its report.

---

## Q4. Data availability and credibility of sources

### Takeaway
Claims outcome data is public (IRDAI, insurer disclosures), but AI-attribution data is not. A solo project can quantify the problem (claims, rejections, grievances) from official data but must rely on self-reported figures for AI impact.

### Cited Findings
- Lemonade: audited filings, with self-defined "automated". [P]
- IRDAI and NHA: official but only seen here through news summaries; the numbers show small discrepancies (for example Rs 94,247 vs 94,248 cr). [S]
- Vendor/press case studies (Kodak Alaris, SHIFT, Tractable, ICICI Lombard blogs): marketing. [V]
- Aggregator "AI statistics" pages (CMARIX, Sprinklr, Klover.ai, insurnest, agentive and similar) surfaced in searches. Not used as evidence because there was no traceable method. [S/V]
- Date issue: one source says the IRDAI AI working group order was dated 17 June 2026 ([Taxguru-based summary](https://taxguru.in/corporate-law/irdai-forms-ai-working-group-strengthen-governance-insurance-sector.html)), another says 19 June 2026 ([Insurance Business](https://www.insurancebusinessmag.com/asia/news/technology/indias-insurance-regulator-steps-in-to-govern-ai-adoption-579846.aspx)). Check the IRDAI order.

### Inferences
- Triangulate each Indian figure with at least two sources and record the original document name and page.

### Gaps
- Public IRDAI disclosure tables by insurer (claims paid, ageing, repudiation) were not pulled directly; do so for the shortlist insurers.

---

## Q5. India relevance (IRDAI, Bima Sugam, PM-JAY, cashless, settlement ratios)

### Takeaway
India's health claims system combines a high cashless share (about 58%), a repudiation rate of about 8%, large public-scheme volume and new digital rails (NHCX, Bima Sugam). That makes health claims the natural AI focus.

### Cited Findings
- FY25 health claims figures: see Q2 (IRDAI Annual Report via secondary). [S]
- Star Health: settlement ratio reported at 99.06% for FY2025 in a ranking article; Aditya Birla Health and Niva Bupa reported 100% claims settled within three months. [S, an aggregator ranking, check IRDAI disclosures] — [Ditto](https://joinditto.in/health-insurance/top-10-claim-settlement-ratio-health-insurance-companies/). Note: claim settlement ratio counts claims by number and excludes partial deductions, so it can mask short-payment and disputes (my caution).
- Regulatory timelines referenced for cashless authorisation: 1 hour for pre-admission and 3 hours for post-discharge. [S] — [Angel One](https://www.angelone.in/news/market-updates/star-health-expects-most-cashless-claims-to-be-settled-by-ai-within-2-years)
- PM-JAY: see fraud figures above. [S]
- Bima Sugam: an online insurance marketplace approved by IRDAI; onboarding of Health Exchange and Bima Sugam targeted for 1 August (year per source, 2024 likely). [S] — [Digital Health News](https://www.digitalhealthnews.com/irdai-plans-to-onboard-health-exchange-and-bima-sugam-by-august-1). Current go-live status not verified.

### Inferences
- NHCX plus Bima Sugam create a standardised data layer; the AI opportunity is building models on that structured stream.

### Gaps
- Bima Sugam operational status and volumes in 2026; NHCX 2026 adoption; ABDM link to claims; IRDAI's cashless-everywhere circular details. Not retrieved.

---

## Q6. Risks and regulation (IRDAI, DPDP, explainability, bias, NAIC, EU AI Act)

### Takeaway
IRDAI is just starting its AI governance work (working group, mid-2026), with claims processing and fraud prevention explicitly in scope. The EU AI Act classifies life and health insurance pricing/risk assessment as high-risk; claims and fraud are not specifically listed in Annex III.

### Cited Findings
- IRDAI Working Group on AI (WG-AI): constituted June 2026, chaired by Prof. Sandeep K. Shukla (IIIT Hyderabad). Members from CERT-In, ReBIT, life, general and standalone health insurers, IRDAI CISO Deepak Gaikwad as convener. Three months to report. Mandate: map AI adoption, ethical/explainable AI frameworks, audit frameworks, stress testing, with a specific focus on claims processing and fraud detection. [S] — [Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/technology/indias-insurance-regulator-steps-in-to-govern-ai-adoption-579846.aspx), [TaxGuru](https://taxguru.in/corporate-law/irdai-forms-ai-working-group-strengthen-governance-insurance-sector.html), [Sarvada commentary](https://sarvada.ai/ai-insurtech/irdai-ai-audit-framework-readiness-insurers-brokers-india-2026). The report is due about September 2026; I did not check whether it has been published.
- IRDAI Fraud Monitoring Framework 2025 effective 1 April 2026 (see Q2). [S]
- EU AI Act: AI for risk assessment and pricing in life and health insurance is Annex III high-risk; Articles 9-15 obligations apply from 2 August 2026 per the sources, though one source mentions "Council-adopted timeline" planning, implying possible delay (digital omnibus). Treat the date as UNVERIFIED. [S] — [Annex III text](https://artificialintelligenceact.eu/annex/3/), [Modulos](https://www.modulos.ai/blog/eu-ai-act-annex-iii-draft-guidelines-what-changed/), [EU AI Compass](https://euaicompass.com/eu-ai-act-for-insurance.html), [MDPI Risks](https://doi.org/10.3390/risks13090160)
- NAIC Model Bulletin on AI systems (Dec 2023): 24 states plus DC adopted as of 1 April 2026; CA, CO, NY, TX use their own frameworks. Requires a written AIS program, governance, audit and third-party vendor management. [S] — [Quarles](https://www.quarles.com/newsroom/publications/nearly-half-of-states-have-now-adopted-naic-model-bulletin-on-insurers-use-of-ai), [Actuary.info](https://actuary.info/insights/ai-regulation-insurance-naic-2026)
- DPDP Act 2023: I did not retrieve a source. Known only from general knowledge, so unverified here: the Act governs consent and processing of personal data, health data being sensitive in practice; rules and phased commencement need checking at meity.gov.in.

### Inferences
- A claims-AI proposal in India must handle health-data consent (DPDP), human review of denials, audit trails and vendor management. An explainable-denial design aligns with the likely WG-AI direction.
- Fraud detection is generally outside EU high-risk (the draft guidance says pricing is high-risk even with fraud features), so claims and fraud AI are lower-regulation than underwriting AI (inference).

### Gaps
- DPDP specifics, IRDAI existing IT/outsourcing/cyber guidelines, IRDAI Protection of Policyholders' Interests regulations (claim timelines), bias evidence in Indian claims. Not retrieved.

---

## Q7. Feasibility for an 80-hour solo project and suggested narrowed sub-scope

### Takeaway (my recommendation, not sourced)
Narrow to Indian health insurance claims, specifically cashless pre-authorisation and claim rejection/repudiation and grievance. Reasons: best official data, a policy hook (NHCX, 8% repudiation, 1-hour/3-hour cashless timelines, WG-AI claims focus), and public AI fraud evidence from PM-JAY.

### Cited Findings
- Data supports it: IRDAI numbers (Q2), NHA fraud actions (Q1), Star Health AI target (Q1), regulatory timeline (Q5). Links above.

### Inferences
- Rough 80-hour plan (my estimate): about 15 h workflow mapping from IRDAI/NHA docs; about 25 h building an evidence table for each claims stage; about 15 h India gap analysis, using insurer disclosures for 4-5 insurers (Star, HDFC Ergo, Niva Bupa, ICICI Lombard, Bajaj Allianz); about 15 h proposal design and sizing; about 10 h risk/regulation and writing.
- Alternative: motor own-damage claims, which have richer global CV evidence (Tractable, Ping An), but weaker Indian data and a thinner policy hook.
- Proposal ideas for the gap section: explainable repudiation review assistant, small-ticket cashless auto-adjudication on NHCX data, grievance triage. Each needs a sourced baseline.

### Gaps
- Primary-source extraction (IRDAI PDFs, insurer disclosures) is the main time risk. A solo student cannot access proprietary claims data, so any impact sizing will be scenario-based.

---

## Source-quality and verification list for the report writer
- Safe to cite as primary: Lemonade 10-K FY2025; Allianz Project Nemo release.
- Cite with "as reported by": IRDAI Annual Report 2024-25 figures, NHA FY2025-26 figures, Star Health target, WG-AI details, IRDAI fraud guidelines.
- Do not cite without verification: McKinsey 34%/8%; "30 to 7.5 days" and "$40-60 to $25-36"; "over 90% claims events unautomated"; Ping An 60% pass-rate and 3.65 bn calls; 15% health-fraud and Rs 600-800 cr; Star Health Rs 120 to 200 cr tech spend and 2-hour approval; EU AI Act 2 Aug 2026 date; Zurich "hour to seconds".
