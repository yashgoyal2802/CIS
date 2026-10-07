# AI in Retail Banking and Lending Workflow (India emphasis)

Research date: 2026-10-06. About 24 searches/fetches. Credibility tags: [P] primary (regulator, company filing, or management statement), [S] secondary (press reporting a primary), [V] vendor/marketing or low-grade aggregator. Many figures reached me only through search-result summaries or press pieces. Items marked UNVERIFIED must be checked against the primary document before use. Several primary PDFs (RBI FREE-AI report, Business Standard SBI article) could not be fetched (CAPTCHA, 403, binary), so their numbers come from secondary summaries.

## 0. Workflow decomposition (stage map used in this note)

Takeaway: Retail lending can be split into 9 stages: (1) acquisition and marketing, (2) onboarding, KYC and V-CIP, (3) underwriting and scoring, (4) fraud detection, (5) sanction and disbursal, (6) servicing and customer support, (7) collections and recovery, (8) portfolio monitoring and early warning, (9) compliance and AML. Stages 1, 3, 6 and 7 carry the most disclosed AI activity. Stages 8 and 9 are the least documented with numbers.

### Cited Findings
- RBI's supervisory survey of 612 entities (Jan-May 2025) found 583 AI applications. Roughly 15.6% were customer support, 11.8% sales and marketing, 13.7% credit underwriting. This gives a rough stage-wise distribution of Indian adoption. — [Khaitan summary of RBI survey](https://www.khaitanco.com/sites/default/files/2025-08/Ergo%20-%20FREE%20AI%20Framework%20-%2028%20Augusut%202025.pdf) and [search summary](https://www.medianama.com/2025/08/223-rbi-committee-sector-specific-models-ai/), 2025. [S of P]. Percentages came via search summary, not the PDF. Verify in the RBI report.
- Only 20.8% of 612 surveyed entities were deploying or developing AI, and 67% were interested. — [Medianama on RBI FSR/FREE-AI](https://www.medianama.com/2025/09/223-rbi-warns-on-ai-in-banking-sector-and-opportunities/), 2025. [S]
- Axis Bank's AI/ML supports underwriting, line management, early-warning detection and portfolio monitoring. — [Axis Q4FY26 investor presentation](https://www.axis.bank.in/docs/default-source/shareholders/financial-results-and-other-information/investor-presentations/2025---2026/investor-presentation-for-the-quarter-ended-31st-march-2026.pdf), 2026. [P] (as summarized in search, not read in full)

### Inferences
- Adoption is skewed to front-office and customer-facing stages (support, sales, underwriting). Back-end monitoring and compliance appear less disclosed.

### Gaps
- No single official stage-by-stage adoption breakdown beyond the RBI survey split. The RBI report itself should be read directly (rbi.org.in, report dated 13 Aug 2025).

## Q1. Which stages have the best-documented, quantified AI impact, and which are thin?

### Takeaway
Best quantified: servicing/sales/collections bots at Bajaj Finance (management commentary), automated underwriting at Upstart (US, filings), Account Aggregator-enabled lending (Sahamati), and consulting-estimated productivity (McKinsey). Thinnest: bank-level underwriting impact at HDFC/ICICI (qualitative only), early warning, AML, and bias/outcome results.

### Cited Findings
Acquisition, sales, and servicing (India)
- Bajaj Finance Q1 FY27: AI bots handle 71% of DIY customer-service volumes; 27 bots live; 17 of 118 agentic applications deployed; bot/voice-bot-led disbursements Rs 2,500 crore in the quarter; management projects Rs 11,000-12,000 crore for FY27; voice bots contributed 17-18% of loan originations (about 20% with data bots); underwriting efficiency gain 20%+; voice AI costs about one-third of human agents. — [Medianama, Aug 2026](https://www.medianama.com/2026/08/223-bajaj-finances-71-customer-service-2500-crores-disbursements/). [S of P: management earnings-call commentary]
- Bajaj Finance Q4 FY26: bot-generated disbursals Rs 1,895 crore; FY27 target Rs 12,103 crore; 72% of interactions self-served by bots; 30% of remaining outbound agents are AI voice agents; 6,632 debt-collection receipts via AI text bots in Q4 (zero in Q3); peak Diwali day 600,000 loans processed vs 100,000 without AI; 60 face-recognition cameras deployed, target 1,000 in FY27; autonomous-agent target cut from 800+ to 600+ for FY27 and sales removed from scope. — [Medianama, May 2026](https://www.medianama.com/2026/05/223-q4fy26-bajaj-finance-autonomous-agent-target-800-600-fy27/). [S of P]
- Bajaj conversational bots disbursed over Rs 5,520 crore personal loans in FY2026; opex-to-NII 32.8% in Q3 FY26 vs 33.1% a year earlier (the 30 bp improvement is not attributable to AI alone). — search summary of Bajaj disclosures; see [Bajaj Finserv Annual Report FY25](https://www.bajajfinserv.in/finserv-digital-annual-report-fy25/transformation-through-technology.html) and Medianama links above. [S]. UNVERIFIED against the original investor presentation.
- Viral claim "10 AI bots replaced about 1,500 agents, cost down about 70%" — [Trak.in](https://trak.in/stories/bajaj-finance-fires-1500-humans-hire-10-ai-bots-costs-cut-by-70/). [V/low-grade secondary]. Conflicts in tone with the later management data (one-third cost per agent). Do not use without the primary call transcript.
- Axis Bank: end-to-end digital lending was about 77% of unsecured business-loan disbursements; ADI GenAI staff chatbot used by 87,000 employees in FY26 (45,000 prior year), 32.5 lakh+ queries; AXIOM AI operating model with 5 focus areas including zero-ops document processing and fraud/credit assurance. — [Axis investor presentation Q4FY26](https://www.axis.bank.in/docs/default-source/shareholders/financial-results-and-other-information/investor-presentations/2025---2026/investor-presentation-for-the-quarter-ended-31st-march-2026.pdf), 2026. [P] via search summary. The 77% is digital lending, not necessarily AI-underwritten.
- HDFC Bank FY26: Neev in-house GenAI platform; 5 AI use cases in production, 14 in development; about 50% reduction in eligibility-search effort for home loan pre-approvals; tech investment about $1 billion over 5-6 years. — [Financial Express B2B](https://www.financialexpressb2b.com/futech/features/from-22000-crore-in-ai-led-business-to-faster-loan-journeys-how-ai-is-paying-off-for-sbi-hdfc-bank-and-icici-bank-12392577), 2026 [S]; [HDFC Bank IR 2025-26](https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2025-26/reports/HDFC_Bank_IR26.pdf) [P]. A BusinessToday piece on the annual report found no quantified AI lending result. [S](https://www.businesstoday.in/technology/artificial-intelligence/story/hdfc-bank-bets-big-on-ai-with-in-house-genai-platform-neev-plans-to-transform-customer-service-lending-and-operations-542375-2026-07-11)
- HDFC trade-finance GenAI extracts document fields with "high confidence" (no number). — HDFC IR 2025-26. [P]
- ICICI Bank FY26: AI/GenAI used for portfolio monitoring, onboarding, fraud detection, document extraction, servicing. No headline AI number; tech expense about 11% of opex (11.4% in Q1FY27). — [Financial Express B2B](https://www.financialexpressb2b.com/futech/features/from-22000-crore-in-ai-led-business-to-faster-loan-journeys-how-ai-is-paying-off-for-sbi-hdfc-bank-and-icici-bank-12392577) [S]; ICICI [Form 6-K FY2026](https://www.sec.gov/Archives/edgar/data/0001103838/000095010326011004/dp250272_ex9901.pdf) [P].
- SBI: Rs 22,000 crore of business from AI-generated analytical leads across home, Xpress Credit, gold, MSME (FY26-FY27 per source). — Financial Express B2B link above. [S]
- SBI used AI to underwrite nearly Rs 1 trillion of MSME loans in FY26 (statement attributed to Amara). — [Business Standard, Aug 2026](https://www.business-standard.com/industry/banking/sbi-uses-ai-to-underwrite-nearly-1-trillion-msme-loans-in-fy26-amara-126081201303_1.html). [S]. Page returned 403; headline only.
- SBI claims (over 60% of personal loans under Rs 10 lakh via pre-approved digital channel, under 4-hour disbursal; MSME early-warning models flagging stress up to 90 days ahead) came from a search summary with no clear source. UNVERIFIED. Treat as leads only.

Underwriting and alternative data
- Account Aggregator: FY26 about Rs 3.82 lakh crore across 3.68 crore loans; 8.4% of India retail+MSME lending by value (11.8% by volume); new-to-credit 18.2% of originations by volume; women 19.8% of volume; banks 47.3% of AA-enabled lending value in H2 FY26; home/LAP AA loans Rs 20,777 crore, +624% YoY. — [IANS on Sahamati report, Aug 2026](https://ianslive.in/indias-account-aggregator-ecosystem-drives-rs-382-lakh-crore-loans-in-fy26--20260827133606). [S of P; Sahamati is the RBI-recognised SRO, industry-body self-reporting]
- AA FY25: about Rs 1.67 lakh crore across 189 lakh loans (estimated); 780+ FIs, 269+ million consents processed. — [Sahamati H2 FY25 impact report](https://sahamati.org.in/the-credit-reimagined-account-aggregator-aa-impact-report-h2-fy25/) [P-ish, industry body]; [YourStory](https://yourstory.com/2025/03/india-account-aggregator-system-facilitates-loan-disbursement-rs-462b-h1-fy25). Note: AA data is a data rail, not AI per se. Link to AI is inference.
- Upstart (US): 91% of loans fully automated in 2025; model approves 41.4% more applicants and gives 33.1% lower APRs vs traditional model at equal loss (company-defined). — [Upstart 2025 Annual Report](https://ir.upstart.com/static-files/77673faa-918f-48b8-a6e2-d30846f896f2) [P but self-serving]; [Investing.com Q3 2025](https://www.investing.com/news/company-news/upstart-q3-2025-slides-revenue-soars-71-yoy-automation-reaches-91-93CH-4332493) [S]. Another search snippet gives 44% more approvals and 16% lower APR, so figures vary by period and definition.
- BIS Working Paper 1244 (Feb 2025): Italian banks investing in AI credit scoring dampened the countercyclical effects of relationship lending on firms' credit supply. — [BIS WP 1244](https://www.bis.org/publ/work1244.htm). [P, peer-style central bank research]
- McKinsey: credit analyst productivity +20-60% using multiagent systems for credit memos, about 30% faster decisions; GenAI could add 2.8-4.7% of industry revenue ($200-340bn). — [McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise) and [McKinsey GenAI economic potential](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier). [Consulting estimates, not realised results]

Collections
- McKinsey: GenAI in customer assistance and collections can cut opex up to 40% and lift recoveries about 10%; end-to-end collections transformation up to 30% productivity. — [McKinsey](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-promise-of-generative-ai-for-credit-customer-assistance). [Consulting, "up to" figures]
- Bajaj collections data above (6,632 receipts) is small and early.

Fraud
- RBI Annual Report 2024-25: 23,953 bank fraud cases (down 34%); Rs 36,014 crore amount (nearly 3x, mostly from re-reporting 122 cases worth Rs 18,674 crore); over 92% of fraud value in advances/loans; digital-payment frauds 56% of cases but about Rs 520 crore. — [Business Standard](https://www.business-standard.com/finance/news/bank-fraud-amount-triples-in-fy25-despite-drop-in-number-of-cases-rbi-125052900696_1.html), [Medianama](https://www.medianama.com/2025/06/223-rbi-annual-report-2024-25-central-bank-agenda/), 2025. [S of P]. Implication: loan-book fraud (credit-side) is the value problem; payment fraud is the count problem.
- MuleHunter.AI (RBIH): 23 banks implemented by 10 Dec 2025; Canara Bank reports 95% accuracy on mule accounts; RBI will not disclose number of mule accounts found. — [Medianama RTI, Dec 2025](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/), [The420](https://the420.in/rbi-mulehunter-ai-banks-fraud-detection-canara-pnb-ml-tool-2025/). [S]. Accuracy is unaudited bank claim.

KYC/V-CIP
- RBI KYC Master Direction update (28 Nov 2025) consolidated V-CIP; deepfake/presentation-attack detection added Aug 2025. — [HyperVerge blog](https://hyperverge.co/blog/rbi-video-kyc-guidelines/). [V]. Verify in RBI text. I found no reliable national V-CIP volume or fraud-reduction number.

### Inferences
- Bajaj is the best-documented Indian case for AI across sales, servicing and collections because management gives quarterly numbers. It is also unusual: an NBFC with a tech-led culture.
- Large banks describe use cases but rarely give outcome metrics, so "quantified impact with source" for HDFC/ICICI/SBI will mostly be qualitative or press-reported.
- Bajaj trimming its autonomous-agent target (800 to 600, sales dropped) is evidence that scaling agentic AI is harder than guided.

### Gaps
- No verified quantified impact (approval lift, loss reduction) for AI underwriting at any Indian bank from a primary source.
- No primary quantification of early-warning-system hit rates (SBI 90-day claim unverified).
- No national V-CIP drop-off or fraud-catch data; no AML false-positive reduction data from Indian banks found.
- Claims of "AI scoring improves default prediction 15-25%, reduces defaults up to 30% in India" appeared in a search summary with no traceable source. UNVERIFIED. Do not cite.

## Q2. Best primary/official sources and credibility

### Takeaway
Best: RBI FREE-AI report (Aug 2025), RBI Annual Report and Financial Stability Report, RBI Digital Lending Directions 2025, bank integrated annual reports/investor decks/earnings-call transcripts, Sahamati reports, BIS/FSI papers, Upstart filings. Press and vendor blogs are useful for locating claims but must be traced back.

### Cited Findings
- RBI FREE-AI Committee report published 13 Aug 2025: 7 Sutras, 26 recommendations, 6 pillars (Infrastructure, Policy, Capacity, Governance, Protection, Assurance). — [RBI report PDF](https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF) [P, not readable by my fetch tool; download manually]; [KPMG India](https://kpmg.com/in/en/insights/2025/08/rbi-free-ai-committee-report-on-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence.html); [Storyboard18](https://www.storyboard18.com/digital/rbi-unveils-free-ai-framework-to-drive-ethical-ai-adoption-in-finance-78934.htm).
- HDFC Bank Integrated Annual Report 2025-26 — [PDF](https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2025-26/reports/HDFC_Bank_IR26.pdf) [P]. HDFC 2024-25 AR — [PDF](https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2024-25/HDFC_Bank_Annual_Report_2024_25-310202.pdf) [P].
- Kotak Q4FY26 investor presentation (AI/ML cross-sell engine) — [PDF](https://www.kotak.bank.in/content/dam/Kotak/investor-relation/Financial-Result/QuarterlyReport/FY-2026/q4/investor-presentation/Q4FY26-Investor-Presentation.pdf) [P]. Only a one-line mention found in search.
- ICICI files Form 6-K with SEC (English, full reports) — [FY2026 6-K](https://www.sec.gov/Archives/edgar/data/0001103838/000095010326005960/dp245411_6k.htm) [P].
- BIS: [FSI Insights No 63 Regulating AI in the financial sector](https://www.bis.org/fsi/publ/insights63.pdf), [BIS WP 1244](https://www.bis.org/publ/work1244.pdf), [FSB monitoring AI adoption](https://www.fsb.org/uploads/P101025.pdf), [Census CES-WP-25-07 US banks' AI and small-business lending](https://www2.census.gov/ces/wp/2025/CES-WP-25-07.pdf). [P]
- Other surveys: [IIF-EY 2024 AI/ML survey](https://www.iif.com/portals/0/Files/content/Innovation/2024%20IIF-EY%20Survey%20Report%20on%20AI_ML%20Use%20in%20Financial%20Services_Public%2001.08.25.pdf); [US Treasury AI in Financial Services](https://home.treasury.gov/system/files/136/Artificial-Intelligence-in-Financial-Services.pdf); [OSFI-FCAC](https://www.osfi-bsif.gc.ca/en/about-osfi/reports-publications/osfi-fcac-risk-report-ai-uses-risks-federally-regulated-financial-institutions). Not read in depth.
- EY India: GenAI productivity gains up to 46% in Indian banking ops by 2030 — [EY India](https://www.ey.com/en_in/newsroom/2025/03/gen-ai-to-drive-productivity-gains-of-up-to-46-percent-in-indian-banking-ops-by-2030). [Consulting forecast]; not read in full.
- Low-grade: "65% of FIs deployed AI in credit scoring by 2025 (Accenture)" appeared only on [stealthagents.com](https://stealthagents.com/research/ai-credit-scoring-automation) [V/aggregator]. UNVERIFIED.
- Not accessed: NASSCOM, BCG, Bain, Deloitte India reports; RBI Report on Trend and Progress 2024-25 and Payment Systems Report. Listed as sources to pull next.

### Inferences
- For an MBA project, anchor on RBI documents plus earnings-call transcripts (Bajaj, HDFC, Axis) and use consulting numbers only as labeled estimates.

### Gaps
- I could not open RBI PDFs or the FSR text directly; page-level citations need a manual pass.
- Did not verify NASSCOM/BCG/Bain/Deloitte India figures.

## Q3. Where are the real gaps in AI adoption in Indian lending?

### Takeaway
Evidence shows a low base (about one in five regulated entities deploying AI), thin governance (explainability and bias testing are rare), and under-documented stages (early warning, AML, collections analytics for secured/rural/MSME, vernacular). Gap proposals should be framed as hypotheses.

### Cited Findings
- Only 15% of 127 AI-using entities used interpretation tools or audit logs; 35% validated for bias and fairness; 38% preferred simple rule-based models for explainability and legacy compatibility. — [Medianama/RBI survey summary](https://www.medianama.com/2025/08/223-rbi-committee-sector-specific-models-ai/) and [Khaitan](https://www.khaitanco.com/sites/default/files/2025-08/Ergo%20-%20FREE%20AI%20Framework%20-%2028%20Augusut%202025.pdf), 2025. [S of P]
- FREE-AI recommendations include AI sandboxes, indigenous financial-sector AI models, audit, incident reporting. — [Coingeek](https://coingeek.com/rbi-committee-proposes-framework-for-ethical-ai-in-finance/), [Mondaq](https://www.mondaq.com/india/financial-services/1672260/rbis-move-toward-ethical-and-responsible-ai-in-financial-sector). [S]
- RBI's FSR flagged concentration in critical third-party cloud/AI providers, herding from similar models, opacity and AI-enabled cyber and deepfake risk. — [Medianama](https://www.medianama.com/2025/09/223-rbi-warns-on-ai-in-banking-sector-and-opportunities/) [S of P].
- Loan/advances portfolio accounts for over 92% of bank fraud value (FY25), while published AI fraud work centres on payments/mules. — [Business Standard](https://www.business-standard.com/finance/news/bank-fraud-amount-triples-in-fy25-despite-drop-in-number-of-cases-rbi-125052900696_1.html). [S of P]
- Bajaj's own difficulty scaling agentic sales automation (target cut) shows implementation gap. — [Medianama May 2026](https://www.medianama.com/2026/05/223-q4fy26-bajaj-finance-autonomous-agent-target-800-600-fy27/).
- AA new-to-credit share was 18.2% by volume and women 19.8% (FY26), implying under-served segments remain. — [IANS](https://ianslive.in/indias-account-aggregator-ecosystem-drives-rs-382-lakh-crore-loans-in-fy26--20260827133606).
- Secured lending via AA grew fast but small (home/LAP Rs 20,777 crore vs Rs 3.82 lakh crore total). — same source (my arithmetic: about 5%).

### Inferences (hypotheses, not findings)
1. Credit-side fraud and early warning: large rupee losses sit in advances but public AI evidence is mostly payments fraud. Candidate project: framework for AI-led early warning/loan-fraud detection in MSME/corporate-retail portfolios.
2. Explainability and fairness operations: low audit-log and bias-test rates against RBI FREE-AI expectations. Candidate: compliance-readiness gap analysis for retail credit models.
3. AA-plus-AI underwriting for secured and new-to-credit borrowers (home/LAP, women, gig workers).
4. Collections: Bajaj voice/text bots are early; vernacular, soft-bucket and secured-vehicle collections analytics under RBI recovery-conduct norms are under-documented.
5. Smaller lenders (co-op banks, small NBFCs, regional rural banks) lack data and talent; sandbox and shared-model opportunity (inferred from FREE-AI recommendations).

### Gaps
- No quantified evidence of gap size beyond the survey; hypotheses need interviews or filings analysis.
- No verified data on AI use in AML/transaction monitoring in India.

## Q4. India context, regulation and risk

### Takeaway
India has strong digital public infrastructure (UPI, AA, V-CIP) and a dense, recently updated rulebook: Digital Lending Directions 2025, KYC Master Direction update, FREE-AI (recommendations, not law), DPDP Rules 2025 (core duties effective by May 2027).

### Cited Findings
- RBI (Digital Lending) Directions 2025: REs fully responsible for LSP actions; disbursal and repayment must flow directly between borrower and RE accounts (no LSP pass-through); multi-lender LSP displays must be unbiased with KFS and APR; DLA reporting from 15 Jun 2025; multi-lender provisions effective 1 Nov 2025. — [Legal500](https://www.legal500.com/intelligence/india/finance-and-banking/reserve-bank-of-india-digital-lending-directions-2025), [Argus Partners](https://www.argus-p.com/updates/updates/rbi-digital-lending-directions-2025-an-overview/), [Saraf Partners](https://sarafpartners.com/rbi-notifies-the-rbi-digital-lending-directions-2025/). [S, law-firm summaries of RBI text]
- DPDP Rules notified 14 Nov 2025; Consent Manager rules from 13 Nov 2026; main duties (notice, consent, breach reporting) from about 13-14 May 2027; max penalty Rs 250 crore for security-safeguard failure. — [PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf) [P], [Consent.in](https://www.consent.in/blog/dpdp-rules), [Finacle](https://www.finacle.com/insights/blogs/beyond-compliance-dpdp-2025/).
- RBI FREE-AI seven sutras and 26 recommendations (listed above); published 13 Aug 2025. — [KPMG](https://kpmg.com/in/en/insights/2025/08/rbi-free-ai-committee-report-on-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence.html). Report is a committee recommendation, not binding regulation (my reading; confirm in RBI text).
- V-CIP and deepfake detection requirements (see Q1). [V source]; verify.
- Paytm: AI-based credit assessment claims approval and disbursal within 2 minutes (company marketing [V]); Paytm acts as LSP; financial-services distribution revenue Rs 672 crore in Q3 FY26 (+34% YoY); postpaid relaunch 1 lakh customers in three months. — [Paytm page](https://paytm.com/loans-credit-cards/personal-loan/), [Medianama](https://www.medianama.com/2026/02/223-paytm-wallet-revival-after-postpaid-q3-fy26/). Nothing found on PhonePe lending metrics.
- Model/third-party risk: see FSR points in Q3. Bias evidence: BIS FSI Insights 63 on regulating AI — [BIS](https://www.bis.org/fsi/publ/insights63.pdf).

### Inferences
- Digital Lending Directions put explicit accountability on banks and NBFCs for LSP algorithms; this shapes any proposal involving fintech partners.
- Timing matters: DPDP main duties (May 2027) land during any proposal's implementation horizon.

### Gaps
- No verified PhonePe, UPI-credit-line, or Kotak/ICICI lending-AI metrics. UPI credit-line data not searched.
- Did not read the FREE-AI recommendations list in full from the RBI PDF.

## Q5. Feasibility for an 80-hour solo project and suggested scope

### Takeaway
Full-workflow coverage is infeasible at depth. Recommended sub-scope: "AI in credit risk monitoring and collections for Indian retail/MSME lending, anchored on Bajaj Finance, SBI, Axis, with an RBI FREE-AI and Digital Lending compliance lens", or alternatively "AI-led early warning and credit-side fraud gap".

### Cited Findings
- Best open data for a case study: Bajaj quarterly commentary (Medianama links above), HDFC/Axis/ICICI filings, Sahamati reports, RBI Annual Report fraud tables, FREE-AI survey data.

### Inferences (my judgment, not sourced)
- Suggested hour budget (approximate): stage map and source audit 15h; deep dive on 2 stages, e.g., underwriting+AA and collections, 30h; gap analysis with 3 proposals 15h; regulatory/risk screen 10h; write-up and slides 10h.
- Option A (recommended): Collections plus early warning. Data: Bajaj, Axis, SBI, McKinsey. Gap: credit-side early warning and vernacular/soft collections. Risk: SBI early-warning claims unverified, so verify first.
- Option B: AA-enabled underwriting for new-to-credit and secured lending. Data: Sahamati is strong, public; AI link is weaker.
- Option C: AI governance readiness (FREE-AI vs. survey results). Data is policy-heavy and less quantitative.
- First actions: download the RBI FREE-AI PDF manually; pull Bajaj Q4FY26 and Q1FY27 call transcripts; verify SBI claims; collect HDFC IR26 AI section.

### Gaps
- No time-boxed validation of data access (transcripts, paywalled reports).
