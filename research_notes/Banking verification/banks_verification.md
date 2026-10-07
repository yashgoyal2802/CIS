# Verification of AI claims: SBI, HDFC Bank, Axis Bank, ICICI Bank (plus Kotak)

Prepared 2026-10-06. Method: primary documents were downloaded, converted to text with pdftotext (or HTML stripped), and searched. Nothing in the downloaded files was treated as instructions. Page numbers are PDF page numbers of the file I read; printed report page numbers are given where I could read them. Downloads are in `D:\PGPM PPM-022-159\Broad-Custom\CIS\research_notes\Banking verification\downloads\banks\run1\`.

## Summary table

| # | Claim | Verdict | Best primary source |
|---|---|---|---|
| 1a | SBI: AI underwrote nearly Rs 1 trillion of MSME loans | PARTIAL | SBI AR FY26 (BRE: Rs 99,505 cr sanctioned in FY26); the "nearly Rs 1 lakh crore" wording is the MD's speech, not a document |
| 1b | SBI: Rs 22,000 crore business from AI leads | PARTIAL (number not found as stated; contradicted as an annual figure) | SBI Analyst Presentation Q4FY26 and Q1FY27 |
| 1c | SBI: >60% of personal loans under Rs 10 lakh via pre-approved digital channel in <4 hours | NOT-FOUND | none |
| 1d | SBI: MSME early-warning flags up to 90 days ahead | NOT-FOUND (qualitative EWS disclosure only) | SBI AR FY25 p21; no lead time anywhere |
| 2a | HDFC Bank: 5 use cases in production, 14 in development | VERIFIED-PRIMARY | HDFC Q4FY26 earnings call, 18 Apr 2026 |
| 2b | HDFC Bank: ~50% reduction in eligibility-search effort (home loan pre-approvals) | VERIFIED-PRIMARY | HDFC Integrated Annual Report 2025-26 |
| 3a | Axis: 77% of unsecured business loan disbursements end-to-end digital | VERIFIED-PRIMARY | Axis Investor Presentation Q1FY27 (18 Jul 2026) |
| 3b | Axis: GenAI chatbot used by 87,000 staff | PARTIAL | Axis Integrated Annual Report 2025-26 (87,000+ in MD letter, but 84,000 elsewhere in same report) |
| 3c | Axis: AI collections / early warning disclosures | VERIFIED-PRIMARY (qualitative plus one volume metric) | Axis IAR 2025-26; Q1FY27 presentation |
| 4 | ICICI: quantified AI disclosures | PARTIAL (few, operational counts only) | ICICI Annual Report 2025-26 (HTML) |

---

## 1. SBI

### 1a. "AI underwrote nearly Rs 1 trillion of MSME loans" — PARTIAL

- Where the claim comes from: a speech, not a report. Hans India (13 Aug 2026), reporting SBI MD Rama Mohan Rao Amara at FIBAC: "In FY26, in 12 months time, we are able to underwrite loans up to Rs 5 crore... Almost Rs 1 lakh crore we were able to underwrite." Business Standard carried the same story (12 Aug 2026) but returned HTTP 403 to my fetch, so I could not read it directly. The Hans India article does not cite a document. URL: https://www.thehansindia.com/business/market-compass/sbi-deploys-ai-for-rs-1-l-cr-msme-loan-underwriting-1108862
- Primary document support: SBI Annual Report 2025-26, PDF p63 (printed p61): "Business Rule Engine (BRE) is a single credit risk model developed for SME loans up to 5 crore to sanction loans faster and innovatively, and to enable straight-through processing (STP)... Since its launch in January 2024, the Bank has processed/sanctioned 3.99 lakh proposals amounting to 1,52,942 crore. In FY 2025-26, 2.43 lakh proposals amounting to 99,505 crore were sanctioned."
- Reading: Rs 99,505 crore matches "nearly Rs 1 lakh crore" and the "up to Rs 5 crore" ticket cap. The AR calls it a "credit risk model" / "Business Rule Engine" with STP. It does not use the word "AI" for BRE. So "AI underwrote" is the MD's framing; the AR describes a rules and credit-risk-model engine. Caveat for the paper: a BRE is closer to automated decisioning than to machine learning or generative AI.
- Document: SBI Annual Report 2025-26 (FY26), file "Annual Report FY2026.pdf". Publication date not stated in the extract.
- URL: https://sbi.bank.in/documents/17836/58092042/Annual+Report+FY2026.pdf/0f165880-8752-4d67-6d87-422984f5cc3f

### 1b. "Rs 22,000 crore business from AI leads" — PARTIAL

- Secondary source: Financial Express B2B (18 Aug 2026) attributes it to SBI Chairman C.S. Setty at the Q1 FY27 results interaction ("This aggregated to Rs 22,000 crore"). A search summary of the Q1FY27 call (TipRanks) did not contain the figure when I fetched it, so I could not confirm the quote against a transcript. I did not find the SBI Q1FY27 transcript itself.
- Primary figures I could read (SBI Analyst Presentation Q1FY27, PDF p34, dated 7 Aug 2026): "Advances Through Analytical Leads (Rs crore) ... 1,80,518 [FY26] ... 33,377 [Q1 FY26] 44,759 [Q1 FY27] ... 34.1% YoY Growth" and a segment split for Q1FY27 that includes "Retail Loans 22,396 Cr ... SMEBU 8,928 Cr, REHBU 2,041 Cr, ABU 11,395 Cr".
- Reading: the Rs 22,000 crore figure most likely corresponds to the retail piece of Q1FY27 analytical-lead advances (Rs 22,396 crore), not to a full-year total and not to all AI business. This is my inference, not an SBI statement. The whole-bank figures are Rs 1,80,518 crore for FY26 and Rs 44,759 crore for Q1FY27. Do not cite "Rs 22,000 crore" as SBI's AI-lead total without that caveat.
- Also: SBI AR FY26 PDF p109 (printed p107): "Approximate income earned 1,80,518 crore in advances and 194 crore in JV commission from leads generated through your Bank's Analytics function in FY 2026". The wording says "income earned", which is a mislabel in the report; the Q4FY26 presentation (PDF p42) shows the same Rs 1,80,518 crore as "Advances Through Analytical Leads", and the FY25 AR (PDF p89, printed ~87) gave "business worth Rs 1.24 Lakh Crore" for FY25.
- URLs: https://sbi.bank.in/documents/17836/1275616/07082026_SBI+Analyst+Presentation+Q1FY27.pdf/6e4ca530-1666-574e-22fb-f9e19d553ef5?t=1786091443352 ; https://sbi.bank.in/documents/17836/53469043/SBI+Analyst+Presentation+Q4FY26.pdf/42112857-ac47-31a1-4d7d-4eb4f74d9598?t=1778230228279 ; secondary: https://www.financialexpressb2b.com/futech/features/from-22000-crore-in-ai-led-business-to-faster-loan-journeys-how-ai-is-paying-off-for-sbi-hdfc-bank-and-icici-bank-12392577

### 1c. ">60% of personal loans under Rs 10 lakh disbursed via pre-approved digital channel in <4 hours" — NOT-FOUND

- Searched the SBI AR FY25, AR FY26, Q4FY26 and Q1FY27 presentations and the Q1FY27 press release for "4 hours", "four hours", "60%", "within ... hours". No match. I also read the Hans India, Outlook Business and Rozana Spokesman versions of the FIBAC story; none contain it.
- Related facts that are in the documents: AR FY26 PDF p100: "2.00+ lakh Pre-approved Personal Loans (PAPLs); 0.55+ lakh Real Time Personal Loan (RTPL) sanctioned" (YONO, FY26). AR FY26 PDF p54: Pre-Approved Pension Loan "can be availed digitally through YONO, INB and Contact Centre in 4 clicks only". Q4FY26 presentation PDF p42: digital PAPL Rs 15,564 crore. The "4" in public material is "4 clicks", not "4 hours". It is possible the claim was garbled from "4 clicks".
- Not verified; treat as unsupported.

### 1d. "MSME early-warning flags up to 90 days ahead" — NOT-FOUND

- No lead time appears in any SBI document I read or in the three press versions of the FIBAC story. The press says only: "AI-based early warning signals to identify vulnerable exposures before delinquencies emerge, by analysing sector-specific, market and other publicly available information" (Outlook Business, 12 Aug 2026).
- Primary qualitative text: SBI AR FY25 PDF p21: "To achieve sustainable, risk-adjusted growth, we are leveraging advanced analytics for credit underwriting, portfolio monitoring, and early warning detection." SBI AR FY26 PDF p118 describes a Board-approved "framework for Early Warning Signals (EWS) and Red Flagging of Accounts (RFA)" (regulatory fraud-framework language). SBI Sustainability Report within AR FY26 (PDF p492, printed p128): analytics "can help in identifying customer needs, strengthening credit underwriting and detecting early signs of stress or fraud".
- Q1FY27 call summary (TipRanks, secondary): "intensifying monitoring, using tools like PRISM to detect stress early". This is SMA-level talk with no days-ahead figure. Note "90 days" in the AR is the NPA threshold and SMA-2 is 61-90 days (AR FY26 PDF p384); that may be the source of the confusion.
- URL: https://www.tipranks.com/news/company-announcements/state-bank-of-india-q1-fy27-earnings-call-highlights ; https://www.outlookbusiness.com/corporate/sbi-uses-ai-to-underwrite-nearly-1-lakh-cr-in-msme-loans-in-fy26

### Other quantified SBI AI facts

- AR FY26, Sustainability Report, PDF p492 (printed p128): "67 laterally recruited data scientists... over 140 AI and ML models that are live in production, spanning credit risk scoring, fraud detection, customer segmentation, cross-sell propensity and operational efficiency optimisation." (PDF p486 says "45+ data scientists, 140+ live ML models"; the report is internally inconsistent on headcount.) AR FY25 PDF p89 (printed ~87): "45+ data scientists and 145+ live models".
- AR FY26 PDF p109: "launch of 15 domain specific generative AI chatbots for internal use"; AskSBI (Gen AI) accessed by "over 78,581 employees" (PDF p96); in-house team of "100+" analytics/AI experts; MuleHunter.AI adopted; AIBET policy (generative and agentic AI) instituted.
- Hans India (13 Aug 2026): AI/LLM cheque processing for amounts up to Rs 10,000, "approximately 25% of the bank's cheque volumes" (MD speech). SBI Q1FY27 presentation PDF p34 confirms GenAI cheque processing for cheques up to Rs 10,000 (no volume share).
- AR FY26 PDF p465: AI/ML engine used to identify High-Risk and Very High-Risk branches; "suo moto investigations were conducted in 1,736 branches".
- AR FY26 PDF p63: Digi Sugam cash-flow-based digital loan up to Rs 50 lakh (Aug 2025); PABL 1.11 lakh loans worth Rs 5,513 crore in FY26 (Q4FY26 presentation: PABL Rs 6,765 crore on slide 42; the two numbers differ, so the figures for PABL are not reconciled).
- No SBI figure for AI in collections, contact rate, roll-back or EWS hit rate was found.

---

## 2. HDFC Bank

### 2a. "5 use cases in production, 14 in development" — VERIFIED-PRIMARY

- Exact quote: "We already have 5 use cases in production and 14 more in development, improving turnaround times, first-time right outcomes, and freeing mid-office and back-office capacity for customer-facing roles." Context: the CEO describes the in-house unified AI platform (Model Context Protocol, Agentic Studio, Agentic Mesh).
- Document: HDFC Bank Q4 FY26 earnings conference call transcript, 18 April 2026 (filed with NSE 24 Apr 2026), PDF p5.
- Note: the claim is from the FY26 earnings call, not from the FY25 annual report. I searched both HDFC annual reports (FY25 and FY26) for "in production" / "in development" and found nothing, so do not cite the annual report for it. FY25 AR (CEO letter, PDF p17) says instead: "We have identified more than 15 lighthouse programmes that we will implement with GenAI".
- URL: https://nsearchives.nseindia.com/corporate/HDFCBANK_24042026154113_SEintimationTranscriptofearningscall18April2026.pdf

### 2b. "~50% reduction in eligibility-search effort for home-loan pre-approvals" — VERIFIED-PRIMARY

- Exact quote: "Advanced analytics and Artificial Intelligence (AI) now enables the pre-approved loan limits to surface across NetBanking, MobileBanking and WhatsApp Banking-- reducing eligibility search effort by approximately 50 per cent and accelerating loan processing."
- Document: HDFC Bank Integrated Annual Report 2025-26, section "Digital Leadership and Analytics" under the home loan business, PDF p49 (printed p51). Publication date not stated in the extract (FY26 report).
- Caveat: it is "search effort" (a customer or employee effort measure), with no stated baseline or measurement method.
- URL: https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2025-26/reports/HDFC_Bank_IR26.pdf

### Other quantified or relevant HDFC facts

- IAR 2025-26 PDF p3: Credit STP for cards: "a sharp reduction in processing time--from several hours to near real-time in certain use cases" (no percentage). Retail assets AI list: Business Rule Engine for real-time credit decisioning and instant approvals incl. NTB; AI document processing; AI lead nurturing with voice bots; Project CQR for complaints; customer analytics for lead prioritisation. MSME working capital: "Early outcomes demonstrate a meaningful reduction in processing timelines" (no number).
- IAR 2025-26 PDF p95 (printed p98), wholesale: "Internally, the Bank is developing accelerated underwriting processes... Early warning systems powered by analytics have already been introduced." No metric.
- IAR 2025-26 PDF p162: roadmap lists "Retail Assets, Home Loan, Cards & Collections: ... Portfolio monitoring & early warning systems". No metrics for collections.
- Q4FY26 call, PDF p5: digital adoption "97% for payments and service transactions and 92% for acquisition journeys"; in-house Lakehouse is live. (Different from the AI-specific claims; quote verbatim from the transcript before using.)
- IAR 2024-25 PDF p17: "more than 15 lighthouse programmes" with GenAI.
- Secondary (FE B2B, 18 Aug 2026): about $1 billion technology investment over five to six years attributed to the CEO. I did not locate it in the transcript text I searched; unverified.

---

## 3. Axis Bank

### 3a. "77% of unsecured business loan disbursements end-to-end digital" — VERIFIED-PRIMARY

- Exact quote: "24x7 Business loans : End to End digital lending contributes ~77% to overall unsecured BL disbursements".
- Document: Axis Bank Investor Presentation, Quarterly Results Q1FY27, dated 18 July 2026, PDF p24 (slide 23), in the Small Business Banking section.
- Note: a 24 Jun 2026 media roundtable (FintechBizNews, 24 Jun 2026) said "Nearly 75%", so 75% (June) and 77% (Q1FY27 deck) are different data points. This is a "digital lending" disbursement share, not an AI metric as such.
- URL: https://www.axis.bank.in/docs/default-source/shareholders/financial-results-and-other-information/corporate-announcements/intimations-to-stock-exchanges/investor-presentation-q1fy27-18-07-2026.pdf ; secondary: https://www.fintechbiznews.com/fintech-technology/axis-banks-75-unsecured-loans-managed-digitally

### 3b. "GenAI chatbot used by 87,000 staff" — PARTIAL

- Exact quote (Axis Integrated Annual Report 2025-26, MD & CEO statement, PDF p68, printed p68): "Adi, our Gen AIpowered assistant which has now reached 87,000+ employees with an increase of ~250% yoy for processing queries".
- Conflict inside the same report: PDF p110: "Axis Deep Intelligence (ADI), our GenAI-based internal assistant, now supports over 84,000 employees, resolving more than 81% of branch-level queries, with ~35,000 monthly users handling ~2.8 lakh queries." PDF p111: "ADI adoption across ~86% of the employee base". So "reached 87,000+" (cumulative reach) vs "supports over 84,000" and ~35,000 monthly active users. The 87,000 figure is real but is "reached", not active usage.
- Earlier year: FY25 Statutory Reports (Board's Report) PDF p27: ADI "used across 5500+ branches across India and assists 100,000+ employees" and p56: "more than 104,000 employees" (the FY25 figure appears to be headcount supported, not usage).
- Q1FY27 deck PDF p15: "~0.74 Mn No. of queries processed in ADI"; "93K Copilot users". Q1FY27 call: "Adi handled ~7.4 lakhs queries".
- URL: https://www.axis.bank.in/annual-reports/2025-2026/pdf/annual-report-for-the-year-2025-2026.pdf

### 3c. AI in collections / early warning — VERIFIED-PRIMARY (qualitative, one volume metric)

- Collections, IAR 2025-26 MD & CEO statement, PDF p67: "Our progress is especially visible in collections, where sustained investments in analytics, AIdriven capabilities and digital channels are delivering measurable, ongoing benefits across Personal Loans, Credit Cards and Business Loans. We are structurally reducing reliance on outsourced collection agencies to strengthen customer contact, governance and compliance, supported by AI bots and scorebased inhousing that can meaningfully reduce agency and callcentre allocations." Same page: "we expect AI to drive meaningful bottomline impact over the next 18-24 months".
- Collections metric, Q1FY27 investor presentation PDF p15 (AXIOM slide): "18 Mn+ Collections: Bot-based calling" (YTD, i.e. Q1FY27, per the slide note "numbers represent YTD unless otherwise stated"). No contact rate, roll-back or cost figure is given.
- Early warning, IAR 2025-26 PDF p95 (SME): "a robust early warning and monitoring architecture, incorporating real-time internal and external data signals along with transaction-level monitoring". PDF p100 (wholesale): "portfolio analytics, early warning systems, and calibrated underwriting frameworks". Q1FY27 deck PDF p24: "EWS portfolio monitoring indicates risks under control". No hit rate or lead time.
- Credit and fraud: IAR PDF p111: "100+ machine learning models deployed across credit risk, financial crime, marketing, and collections" and AXIOM "Assurance Strengthening (50+ credit models)"; Q1FY27 deck: "55+ Credit models", "~320% YoY improvement in fraud value prevention". IAR PDF p66: SME growth with "deeper use of analytics across underwriting and monitoring"; "~87% of incremental sanctions were to SME3 and better-rated customers".
- URLs: IAR link above; Q1FY27 deck link above.

### Other quantified Axis AI facts (IAR 2025-26 PDF p110-111; Q1FY27 deck p15)

- AXIOM (FY26): "Zero Ops (115 Mn+ AI-led document services), Conversational Interfaces (10 Mn+ customer chat interactions), Enterprise Knowledge (ADI adoption across ~86% of the employee base), RM Copilot (~66% of branch sales covered through AI-assisted pitch practice)".
- Q1FY27 deck: "~34 Mn AI-assisted doc reading", "~1.05 Mn AI-assisted Onboarding", "0.75 Mn+ Sales & Service Bot based interactions", "~2.1 Mn Mins RM Calls analysed".
- IAR PDF p67: digital journeys "that earlier took 4-5 weeks can now be generated in less than a day" (text extraction shows "45 weeks"; the hyphen was lost, so read "4-5 weeks" as my interpretation); ISO 42001 certification.
- IAR PDF p141: Adi (HR) handled 61% more HR queries in FY26. Axis also reports "Amber" engaged "more than 45,000 employees through over 87,000 chats" (PDF p139), another place "87,000" appears and is a different thing (chat count). Watch for confusion with the 87,000 staff claim.
- Business Standard (25 Jun 2026) via search summary: target of "more than 50 per cent AI coverage of calls by FY27" (not read directly; unverified).

---

## 4. ICICI Bank

Documents: ICICI Annual Report 2025-26 HTML chapters (icici.bank.in/ms/aboutus/annual-reports/2025-26/html/...), FY25 HTML chapters, Q4FY26 investor presentation and Q3FY26 call transcript (no AI content found in the latter two by keyword search). I could not fetch the full PDF annual report (guessed URLs returned 404) or the SEC Form 20-F (SEC returned an "undeclared automated tool" block). Publication dates for the AR chapters are not stated on the pages.

### Quantified disclosures found (all operational counts, no business-impact metrics)

- "Our Business Strategy" chapter, AI section: "More than 100 autonomous bots have been deployed to process inbound customer communications ensuring faster resolution" and "More than 150 autonomous bots have been deployed to automate repetitive and human-intensive workflows". URL: https://www.icici.bank.in/ms/aboutus/annual-reports/2025-26/html/our-business-strategy.html
- Same chapter, portfolio monitoring: "Portfolio monitoring summary generated for thousands of companies using AI models... Millions of pages indexed across public filings, annual reports, earnings call transcripts, news feed and sector reports to generate insights... with nearly 100% trace-to-source integrity."
- Same chapter, qualitative: use cases "portfolio monitoring, customer onboarding, fraud detection, document extraction and summarisation, content generation and customer servicing"; "enterprise AI platform"; AI reasoning tools summarise "financial documents, GST reports, transaction statements and analyst reports" for the underwriting team; facial recognition screened against negative databases in onboarding; OneSCF uses "smart engines that incorporate GST data, bureau checks and AI-driven algorithms for credit assessment"; "data insights through analytics are being used for portfolio monitoring and identification of early warning signals in the existing portfolio" (corporate book; same sentence also appears in FY25).
- Collections: only a list mention ("deployed across ... collections, fraud prevention and internal compliance functions" via startup collaboration). No metric.
- FE B2B (18 Aug 2026), secondary: technology expenses "11% of operating expenses in FY26; 11.4% in Q1FY27" (CFO). Not verified in a primary document.

### Not found

- The "AI-based pre-delinquency management engine using more than 100 variables to create multiple microsegments" appeared in one web search summary (no document named). It is absent from the FY25 and FY26 annual-report chapters I downloaded (FY23 and FY24 HTML chapters did not load). Status: NOT-FOUND in the documents read; do not cite without locating the original (possibly an older annual report or a 20-F).
- No ICICI figure for AI in collections (contact rate, roll-back, cost), early-warning hit rate or lead time, or fraud-loss reduction.

---

## 5. Kotak Mahindra Bank (quick pass)

Document: Kotak Integrated Annual Report 2025-26 (downloaded, 9.3 MB). URL: https://www.kotak.bank.in/content/dam/Kotak/investor-relation/Financial-Result/Annual-Reports/FY-2026/kotak-mahindra-bank/Kotak-Mahindra-Bank-Limited-FY26.pdf

- PDF p31: "machine-learning based fraud monitoring that enables real-time anomaly detection. This allows rapid account-level intervention, often within minutes."
- PDF p10 (Chairman/CEO letter): "we have voice agents interacting with them directly"; "knowledge assistants and sales enablement tools"; "real gains in developer productivity". No numbers.
- PDF p310: "Kompanion has received lakhs queries from thousands of daily active users." PDF p309: in-house "Kotak AI platform"; more than a million analytics queries per month on the data platform.
- PDF p24: "Early warning triggers are embedded within the [Risk Appetite] framework" (risk-appetite thresholds, not an AI model).
- PDF p17 and p43: "33% Reduction in Complaint Resolution Turnaround Time"; "~13% Technology Spend as % of Operating Expenses".
- No quantified AI disclosure on collections, underwriting or early warning found.

---

## 6. Cross-bank: quantified facts on collections, EWS, credit decisioning, fraud

| Bank | Collections | Early warning | Credit decisioning | Fraud |
|---|---|---|---|---|
| SBI | None | Qualitative only; no lead time or hit rate | BRE: Rs 99,505 cr of SME loans <=Rs 5 cr sanctioned in FY26 (1.53 lakh cr since Jan 2024); 140+ live ML models incl. credit risk scoring; Rs 1,80,518 cr advances via analytical leads | AI/ML branch risk engine; 1,736 suo moto branch investigations; MuleHunter.AI |
| HDFC | None (roadmap mention only) | "Early warning systems powered by analytics have already been introduced" (wholesale); no metrics | BRE real-time decisioning; credit STP for cards "several hours to near real-time" | None quantified in the AR text read |
| Axis | "18 Mn+" bot-based collection calls in Q1FY27; in-housing and fewer agency allocations (no numbers) | EWS architecture, no metrics | 55+ credit models; 100+ ML models across credit risk, fin crime, marketing, collections | "~320% YoY improvement in fraud value prevention" (Q1FY27 deck) |
| ICICI | None | Corporate book EWS (qualitative) | AI summaries for underwriting (no counts besides "thousands of companies") | Facial match in onboarding (qualitative) |
| Kotak | None | None | None | Real-time ML detection, "often within minutes" |

Observation: none of the five banks disclosed an AI collections contact rate, roll-back rate or cost-to-collect figure, nor an early-warning hit rate or lead time, in the documents read. Axis is the only one with a collections AI volume metric.

---

## 7. Documents not fetched or incompletely read

- Business Standard (12 Aug 2026, both URLs): HTTP 403.
- SEC EDGAR (ICICI Form 20-F and 6-K): blocked by SEC automated-tool policy.
- ICICI full annual report PDF (FY25 and FY26): URL not found; used the bank's HTML chapters instead.
- Axis FY25 full annual report PDF: not found at the guessed URL; I read the "Welcome to Axis Bank" and "Statutory reports" PDFs only.
- SBI, ICICI and Axis Q4FY26 earnings-call transcripts (SBI and ICICI Q4): not downloaded or not searched fully. SBI Q1FY27 transcript not found. HDFC Q4FY26 transcript was read only for AI terms.
- Kotak earnings calls and BRSR not reviewed.
- BRSR sections for the banks were not searched for AI metrics beyond what appears in the combined annual-report PDFs.

## 8. Source list (primary)

- SBI Annual Report 2025-26: https://sbi.bank.in/documents/17836/58092042/Annual+Report+FY2026.pdf/0f165880-8752-4d67-6d87-422984f5cc3f
- SBI Annual Report 2024-25: https://sbi.bank.in/corporate/SBIAR2425/SBI-AR-2024-25.pdf
- SBI Analyst Presentation Q4FY26 and Q1FY27 (links in 1b)
- HDFC Bank Integrated Annual Report 2025-26: https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2025-26/reports/HDFC_Bank_IR26.pdf
- HDFC Bank Integrated Annual Report 2024-25: https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2024-25/HDFC_Bank_Annual_Report_2024_25-310202.pdf
- HDFC Bank Q4FY26 call transcript (18 Apr 2026): NSE link in 2a
- Axis Integrated Annual Report 2025-26 and Q1FY27 presentation (links in 3a, 3b)
- Axis FY25 Statutory Reports: https://www.axisbank.com/annual-reports/2024-2025/pdf/Statutory%20reports.pdf
- ICICI AR 2025-26 HTML: https://www.icici.bank.in/ms/aboutus/annual-reports/2025-26/html/our-business-strategy.html
- Kotak IAR 2025-26 (link in section 5)
