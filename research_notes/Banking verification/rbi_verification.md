# RBI / regulator primary-document verification (AI and fraud claims)

Verified 6 Oct 2026. Method: primary PDFs and pages from rbidocs.rbi.org.in, rbi.org.in, pib.gov.in, sahamati.org.in and docs.rbihub.in. RBI's PDF host returns a bot-challenge page to curl and WebFetch, so I read the PDFs inside the user's Chrome with pdf.js and extracted text. Quotes below are copied from that extracted text.

Local files: `downloads\rbi\primary_docs_2026-10-06\` holds the FREE-AI PDF and its extracted text. The other PDFs were read in-browser and are not saved to disk; Chrome's file-save from the extension was unreliable. Page numbers are printed page numbers unless I say "PDF p." Anything obtained only from press or search summaries is marked SECONDARY.

## Summary table

| # | Claim | Verdict |
|---|---|---|
| 1a | FREE-AI: 7 sutras, 26 recommendations, 612 entities, 20.8%, 583 apps, 15.6 / 11.8 / 13.7% | VERIFIED-PRIMARY |
| 1b | 127 AI users: 15% interpretation tools, 35% bias/fairness testing | VERIFIED-PRIMARY |
| 1c | "38% preferred simple rule-based models" | NOT-FOUND (a qualitative statement exists, with no 38% figure) |
| 1d | Binding or recommendatory | Recommendatory (committee report; RBI says it is still assessing it) |
| 2 | AR 2024-25: 23,953 cases, Rs 36,014 cr, >92% in advances | VERIFIED-PRIMARY, but later revised downward (see below) |
| 2b | Latest, FY26 | AR 2025-26: 10,114 cases, Rs 48,021 cr, with an important caveat |
| 3 | Digital Lending Directions 2025 | Mostly VERIFIED-PRIMARY. There is no explicit algorithm/AI disclosure rule. |
| 4 | KYC/V-CIP Nov 2025, deepfake/liveness | PARTIAL: liveness/spoof detection is required, "deepfake" appears nowhere, and AI use is optional |
| 5 | MuleHunter.AI | Banks: PARTIAL, 26 banks per RBI (31 and 23 figures are secondary). Accuracy: NOT-FOUND as a number in any RBI/RBIH document |
| 6 | Sahamati FY26 | VERIFIED-PRIMARY on the press release; the abridged report PDF is image-only and could not be read |
| 7 | FSR on AI, concentration, herding, third-party risk | PARTIAL: AI-linked market concentration and AI cyber risk are present; "herding" is absent; third-party risk appears only as an FSB point and a survey item |
| 8 | Early warning / red-flagging | VERIFIED-PRIMARY on the rules. No RBI outcome data on EWS effectiveness was found. |

## 1. FREE-AI Committee report

**Document:** *Report of the Committee to develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence (FREE-AI) in the Financial Sector*, RBI, 13 Aug 2025 (PDF, 2.8 MB).
URL: https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF
Listing page: https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1306

**1a. Sutras and recommendations (VERIFIED-PRIMARY).** Executive Summary, pp. iv-v:
- "the Committee formulated 7 Sutras that represent the core principles to guide AI adoption in the financial sector"
- "Under these six pillars, the report outlines 26 Recommendations for AI adoption in the financial sector."
- The sutras are: Trust is the Foundation; People First; Innovation over Restraint; Fairness and Equity; Accountability; Understandable by Design; Safety, Resilience and Sustainability.
- The 26 are split 13 innovation enablement and 13 risk mitigation (RBI Annual Report 2025-26, Box VI.2).

**Survey (VERIFIED-PRIMARY).**
- §3.3.1, p. 25: "The DoS administered a brief and objective survey among 612 supervised entities during February-May 2025". These were banks, NBFCs, ARCs and AIFIs, "representing close to 90% of the asset size". A separate FinTech Department survey covered 76 entities.
- §3.3.2, p. 25: "only 20.80% (127) of 612 surveyed entities were either using or developing AI systems". Footnote 35 defines adoption as at least one use case, either deployed or in development.
- §3.3.5, p. 27: "Out of the total 583 AI applications in production and under development, the most common applications were in customer support (15.60%), sales and marketing (11.80%), credit underwriting (13.70%), and cybersecurity (10.60%)."
- Footnote 38 defines credit underwriting as "Machine learning credit scoring models (personal loans, credit cards), Automated document data extraction (OCR/RPA for loan processing)". Note that credit underwriting is a broader category than credit scoring.

**1b. 127 AI users (VERIFIED-PRIMARY).** §3.3.13, pp. 31-32: "Of the 127 entities that reported use of AI, only 15% admitted to using interpretation tools like SHAP or LIME, and only 18% maintained audit logs. Although 35% validated for bias and fairness, such practices were limited to the development stages and did not extend to deployment."
- The same paragraph gives: 28% human-in-the-loop, 10% bias-mitigation protocols, 14% regular audits, 37% periodic retraining, 21% drift monitoring, 14% real-time performance monitoring.
- The 35% figure is therefore weaker than it sounds, because it applied to development only.

**1c. "38% preferred simple rule-based models" (NOT-FOUND).** No 38% figure appears in the text; the only "38" hits are a footnote number and a page number. What the report says:
- §3.3.4, p. 26: "Most respondents largely relied on simple rule based non learning AI models and moderately complex ML models, with limited adoption of advanced AI models."
- The same paragraph says simpler models were "preferred due to ease of implementation, compatibility with legacy systems, and greater control and explainability".
- Figure 4 ("Model Complexity") is a chart image that I could not read as text. A 38% share may sit inside that chart. Check the chart visually before using the number, and until then cite only the qualitative statement.

**1d. Binding or recommendatory (recommendatory).**
- The report is a committee report. Its own wording is "recommends" and "outlines 26 Recommendations". It is not an RBI Direction or Master Direction.
- RBI Annual Report 2025-26, §VI.58 and Box VI.2, p. ~99 (PDF p. 125), says: "The Department is undertaking an assessment of the Committee's report and recommendations, which will help in formulation of more specific guidance for the entities in the financial sector."
- So as of the 29 May 2026 Annual Report there was no binding AI instrument. I did not locate any later RBI AI direction. I did not run an exhaustive search of RBI circulars from June to October 2026, so confirm that before final submission.
- Annual Report 2025-26 URL: https://rbidocs.rbi.org.in/rdocs/AnnualReport/PDFs/0AR29052026F5B979AF274E445ABB1593EB226906335.PDF

## 2. Bank fraud statistics

**2a. RBI Annual Report 2024-25 (VERIFIED-PRIMARY).**
- Document: Chapter VI "Regulation, Supervision and Financial Stability", RBI Annual Report 2024-25, released 29 May 2025.
- URL: https://rbidocs.rbi.org.in/rdocs/AnnualReport/PDFs/06REGULATION29052025B32EB726AB144B19B7D887E0324650BE.PDF
- Table VI.2, printed p. 137 (PDF p. 19), "Fraud Cases - Bank Group-wise": 2024-25 total is 23,953 cases and Rs 36,014 crore. By bank group, public sector banks had 6,935 cases and Rs 25,667 cr; private banks had 14,233 cases and Rs 10,088 cr. 2023-24 was 36,060 cases and Rs 12,230 cr.
- Table VI.3, printed p. 138 (PDF p. 20), "Frauds Cases - Area of Operations": Advances were 7,950 cases and Rs 33,148 crore, which is 33.2% of cases and 92.1% of value. Card/Internet was 13,516 cases and Rs 520 cr (1.4% of value). Deposits were Rs 527 cr.
- The 92.1% share is the table's own figure; 33,148 / 36,014 = 92.0%.
- Notes on the tables: data cover frauds of Rs 1 lakh and above reported in the year. "Frauds reported in a year could have occurred several years prior to year of reporting." The amounts do not reflect loss. "Data pertaining to 2024-25 includes fraud classification in 122 cases amounting to ₹18,674 crore, pertaining to previous financial years", reported afresh after the Supreme Court judgment of 27 Mar 2023. Also "783 frauds amounting to ₹1,12,911 crore were withdrawn by banks due to non-compliance with the principles of natural justice".
- Cite the Rs 36,014 crore figure together with the 122-case reclassification effect (Rs 18,674 cr). Without it the "tripling" reads as a deterioration in fraud, which is misleading.

**2b. FY26 (latest; Annual Report 2025-26, 29 May 2026).**
- Same URL as 1d. Table VI.2 is on printed p. 105 and Table VI.3 on printed p. 106 (PDF pp. 131-132).
- FY26: 10,114 cases, Rs 48,021 crore. Public sector banks had 5,418 cases and Rs 35,709 cr; private banks had 3,956 cases and Rs 11,399 cr.
- The same table now restates FY25 as 23,722 cases and Rs 32,803 crore, and FY24 as 35,800 cases and Rs 11,013 cr. The FY25 figure was revised downward from the originally reported 23,953 and Rs 36,014 cr. Use the revised figures when comparing across years, and quote the originals only when citing the 2024-25 report.
- Table VI.3, FY26: Advances were 8,640 cases and Rs 40,774 cr (84.9% of value). Card/Internet/Digital Payments were 293 cases and Rs 29 cr, down from 13,332 cases in FY25.
- Note 6: "Data pertaining to 2025-26 includes fraud classification in 314 cases amounting to ₹30,199 crore, pertaining to previous financial years, reported afresh". About 63% of the FY26 amount is therefore older frauds re-classified.
- The Annual Report text (§VI.76) says that, although the number of frauds at public and private sector banks has reduced, the amount involved has increased over the years.
- Data are "Source: RBI Supervisory Returns".
- §VI.77: thematic supervisory studies in 2025-26 covered "adoption of AI in supervised entities (SEs)" and "efficacy of the transaction monitoring systems in major banks". No findings are published in the report.

## 3. RBI (Digital Lending) Directions, 2025

**Document:** Reserve Bank of India (Digital Lending) Directions, 2025, RBI/2025-26/36, DOR.STR.REC.19/21.07.001/2025-26, 8 May 2025.
URL: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0 (the PDF is linked from that page).

- **RE responsible for LSPs (VERIFIED-PRIMARY).** Para 5(vi): the RE "shall ensure that the LSPs engaged by them and the DLAs ... comply with these Directions". Para 5(vii): "any outsourcing agreement entered into by the RE with an LSP shall in no manner dilute or absolve the RE of its obligations under any statutory or regulatory provision, and the RE shall remain fully responsible and liable for all acts and omissions of the LSP."
- **Algorithm/AI disclosure (CONTRADICTED as an explicit rule).** The words "algorithm" and "artificial intelligence" do not appear anywhere in the Directions. The closest provision is Para 6(ii): "While the LSP may adopt any mechanism to match the request of borrowers with the lender (s) to offer a loan, it shall follow a consistent approach for similarly placed borrowers and products. The mechanism adopted by the LSP and any subsequent changes to this mechanism shall be properly documented." Para 6 applies to multi-lender RE-LSP arrangements and takes effect on 1 Nov 2025. The Directions define digital lending as "A remote and automated lending process", but impose no AI-specific duty.
- **Other points.** The Annual Report 2025-26 (§VI.28) summarises two reforms: a digital view of all matched loan offers with standardised disclosures (including the names of unmatched lenders), and a public directory of digital lending apps. The commencement clause (Para 2(ii)) makes the Directions effective immediately, except Para 6 (1 Nov 2025) and Para 17 (15 Jun 2025).
- **DLG (VERIFIED-PRIMARY).**
  - Para 18(i): "RE may enter into DLG arrangements only with a LSP/ other RE engaged as a LSP". The LSP providing DLG must be a company incorporated under the Companies Act, 2013.
  - Para 22: DLG is accepted only as cash deposited with the RE, a lien-marked fixed deposit with a scheduled commercial bank, or a bank guarantee.
  - Para 23(i): "total amount of DLG cover on any outstanding portfolio which is specified upfront shall not exceed five per cent of the total amount disbursed out of that loan portfolio".
  - Para 26(i): "RE shall invoke DLG within a maximum overdue period of 120 days". Para 26(ii): the DLG agreement must run for at least the longest loan tenor in the portfolio.
  - Para 27: disclosure requirements, including the RE ensuring that LSPs offering DLG publish the DLG portfolio details on their websites. I read only the opening of Para 27 and did not verify its detail.

## 4. KYC / V-CIP (Nov 2025)

**Document:** Reserve Bank of India (Commercial Banks - Know Your Customer) Directions, 2025, RBI/DOR/2025-26/169, DOR.AML.REC.No.88/14.01.002/2025-26, 28 Nov 2025. The copy I read is "Updated as on October 1, 2026". One of ten sector-wise KYC directions that replaced the 2016 Master Direction. I read only the commercial-banks version; the NBFC and other versions were not checked.
URL: https://rbidocs.rbi.org.in/rdocs/notification/PDFs/169MD.pdf

Verdict: PARTIAL. The V-CIP minimum standards are in Para 27, "(1) V-CIP Infrastructure", PDF pp. 31-32:
- 27(1)(iii): the application "shall be capable of preventing connection from IP addresses outside India or from spoofed IP addresses".
- 27(1)(v): "The application shall have components with face liveness / spoof detection as well as face matching technology with high degree of accuracy, even though the ultimate responsibility of any customer identification rests with the bank." The Explanation adds that specific facial gestures such as blinking or smiling are "not mandatory for liveness check".
- 27(1)(vi): "The bank may use appropriate artificial intelligence (AI) technology to ensure that the V-CIP is robust." This is optional ("may").
- 27(1)(vii): the bank must update its technology "based on experience of detected / attempted / 'near-miss' cases of forged identity" and "shall report any detected case of forged identity through V-CIP as a cyber event".
- I did not compare these provisions with the 2016 KYC Master Direction, so I cannot say whether Para 27(1)(v)-(vii) is new in November 2025. The Directions were a consolidation, so do not present it as a November 2025 change without checking.
- The terms "deepfake", "deep fake" and "synthetic" appear zero times. A requirement to detect deepfakes is therefore NOT-FOUND. Liveness and spoof detection are mandatory, and AI is only permitted. A vendor blog (HyperVerge) also says the "deepfake" claim is unconfirmed against primary text.
- Para 40 (PDF p. 40) separately says that, for ongoing due diligence, the bank "may consider adopting appropriate innovations including artificial intelligence and machine learning (AI and ML) technologies".

## 5. MuleHunter.AI

- **RBI Annual Report 2024-25 (primary),** §VI.54, printed p. 135 (PDF p. 17): "RBIH has developed 'MuleHunter.ai', a supervised ML model designed for near-real-time identification of mule accounts. The model leverages advanced AI/ML techniques to learn patterns of mule account activity from data, achieving higher accuracy as compared to the traditional systems. This solution is currently being tested and deployed in a few large public sector banks." No percentage.
- **RBI Annual Report 2025-26 (primary),** §VI.57, printed p. ~98 (PDF p. 124): "As on March 31, 2026, it has been implemented in 26 banks. Implementation is underway in four more banks, with plan to further scale it to more banks." Also: "The course of action, post assigning the confidence score of a suspected mule account by MuleHunter.ai, rests with the individual banks". The tool outputs a confidence score and does not decide.
- **RBIH documentation (primary):** https://docs.rbihub.in/mule-hunter. It claims "higher accuracy and lower false positives than existing systems" and says the model runs inside the bank's infrastructure with no PII exchanged. It also says an anonymised MIS extract is shared with RBIH "so that the model can be monitored for drift, false-positive trends and coverage consistency". **It gives no numeric accuracy.**
- **PIB, 12 May 2026 (primary):** I4C (MHA) and RBIH signed an MoU to share mule intelligence from the Suspect Registry for training "AI-driven fraud detection systems such as MuleHunter.ai implemented across banks". https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260277&reg=3&lang=1
- **PIB backgrounder, 13 May 2026 (primary):** says "Successful pilot tests with large public sector banks have shown encouraging results". No figures. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260497&reg=3&lang=1
- **SECONDARY, not verified against an RBI document:**
  - MediaNama, Dec 2025, reporting an RTI reply: 23 banks as of 10 Dec 2025. RBI declined to give the number of mule accounts identified, citing fiduciary capacity. https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/
  - Various press: "31 banks" (an RMA India item); accuracy of "85%+" or "up to 90%" or "3x manual". I could not tie these to an RBI or RBIH document; discard them.
- **Warning:** a search summary attributed "64 lenders (41 banks and 23 NBFCs)" to MuleHunter. That wording belongs to the Unified Lending Interface section of the PIB backgrounder, not MuleHunter. I did not confirm the exact ULI passage.

## 6. Sahamati / Account Aggregator FY26

**Primary document:** Sahamati press release, 27 Aug 2026, "Account Aggregator Powers ₹3.82 Lakh Crore in Credit, with Secured Lending Emerging as a New Growth Driver", citing "Credit Reimagined: Account Aggregator (AA) Impact Report H2 FY26".
URL: https://sahamati.org.in/media-article/account-aggregator-powers-%e2%82%b93-82-lakh-crore-in-credit-with-secured-lending-emerging-as-a-new-growth-driver/
Full report (abridged PDF): https://sahamati.org.in/wp-content/uploads/2026/08/Include-Abridged-Version-Account-Aggregator-AA-Impact-Report-H2-FY26.pdf. It has no text layer and I could not OCR it, so the methodology section is unread.

VERIFIED-PRIMARY for all four numbers, with qualifications:
- "Facilitating an estimated ₹3.82 lakh crore of loan disbursals across 3.68 crore loans. AA accounted for 8.4% of India's retail and MSME lending by value and 11.8% by loan volume". The figure is an estimate, and the 8.4% share is by value.
- "Among participating institutions, new-to-credit borrowers accounted for 18.2% of AA-enabled loan originations by volume, while women borrowers accounted for 19.8% of loan volumes and 19.1% of disbursed value." The 18.2% is a share by volume among participating institutions, not of all AA borrowers, and it is not an RBI statistic.
- Also: "Banks accounted for 47.3% of AA-enabled lending by value in H2 FY26"; home loans and LAP were 1.09 lakh loans worth Rs 20,777 crore in FY26.
- The press page's "Key findings" bullets lost digits in rendering (for example "4%", "68 crore", "8%", "2%"). The body paragraphs carry the correct numbers; quote only those.
- The source is an industry body's own impact report (Sahamati is an RBI-recognised SRO, per its 5 Jun 2026 release), and it has a stake in the technology. Sahamati's counts are not audited RBI data.

## 7. RBI Financial Stability Reports

**FSR June 2026 (latest, released 30 Jun 2026).** URL: https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/0FSRJUNE2026_300626A120EF6C37694C8C933181147F1379D7.PDF
- Foreword, PDF p. 5: "The global economy and the financial system are being reshaped by two profound forces—growing geopolitical fragmentation and technological disruption brought about by rapid advances in artificial intelligence (AI)."
- Overview, PDF p. 22: "vulnerabilities emanating from rising public debt, bond market fragilities, elevated asset valuations and concentrated exposures due to substantial investments in AI". This is AI-linked market concentration (stock valuations, hyperscaler debt financing, Charts 1.11-1.12, PDF pp. 29-31), not concentration in AI vendors or models.
- Ch. II, PDF p. 71: "AI-enabled cyber threats emerged as the leading perceived risk over the next 12 months (Chart 3 a)." The same survey chart ranks third-party / supply-chain risk as a separate option, and also says "Rapid advances in AI can increase the sophistication, speed and scale of cyber incidents."
- Ch. III, PDF p. 141: FSB's 2026 work programme gives AI a dedicated workstream, and IOSCO's AI Supervisory Toolkit covers third-party and outsourcing risk. These are international developments, reported by RBI rather than RBI's own conclusions.
- PDF p. 151, §III.3.1: "Evolution of Emerging Frontier AI Models" discusses frontier-AI cybersecurity implications for the Indian financial sector. PDF p. 148 notes SEBI's AI-powered Project SUDARSAN.

**FSR December 2025.** URL: https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/0FSRDEC25D1EB9AAEE5724BD5A3E068490996BAD5.PDF
- PDF p. 29: equity valuations "at the high end of the historical range, with stock prices of companies focused on AI particularly stretched and concentration within the stock index elevated".
- PDF p. 140, §3.24 (describing the FSB's October 2025 monitoring report): "addressing gaps in monitoring critical areas such as third-party dependencies, market correlations, and cyber risks will help to manage financial stability risks arising from increased AI adoption in the financial sector."
- PDF p. 140: "the adoption of AI by central banks has been challenging due to concerns about interpretability and explainability of the models" and "for generative AI models, the issue of explainability is compounded by the risk of hallucinations".
- PDF p. 142, §3.33: restates the FREE-AI recommendations.

**Herding (NOT-FOUND).** The word "herding" does not occur in either report, so any claim that the FSR flagged AI-driven herding is unsupported by these documents. The June 2026 pages I scanned were those that mention AI (pp. 5, 21, 29-31, 71, 141-151). The December 2025 report was also checked for "herding", with the same result. I did not read every page of either report line by line.

## 8. Early warning systems / red-flagging

**Document:** Master Directions on Fraud Risk Management in Commercial Banks (including Regional Rural Banks) and All India Financial Institutions, RBI/DOS/2024-25/118, DOS.CO.FMG.SEC.No.5/23.04.001/2024-25, 15 Jul 2024.
URL: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12702 (PDF: https://rbidocs.rbi.org.in/rdocs/notification/PDFs/118MDE97B8ED9A09B4B21BE7FDDE5F836CD09.PDF)

VERIFIED-PRIMARY (Chapter III):
- 3.1.1: "Banks shall have a framework for Early Warning Signals (EWS) and Red Flagging of Accounts (RFA) under the overall Fraud Risk Management Policy approved by the Board. A Red Flagged Account is one where suspicion of fraudulent activity is thrown up by the presence of one or more EWS indicators, alerting / triggering deeper investigation from potential fraud angle and initiating preventive measures by the banks."
- 3.1.3: the Risk Management Committee of the Board approves the EWS indicators. A turnaround time for examining EWS alerts, "preferably not more than 30 days", is prescribed.
- 3.2: the framework must provide, among others, "A system of robust EWS which is integrated with Core Banking Solution (CBS) or other operational systems" and effective use of CRILC and the Central Fraud Registry.
- 3.3.1: the EWS system "shall be comprehensive and designed to include both the quantitative and qualitative indicators", capturing "transactional data of accounts, financial performance of borrowers, market intelligence, conduct of the borrowers".
- 3.3.2: "Banks shall set up a dedicated Data Analytics and Market Intelligence (MI) Unit ... to enable an early detection and prevention of potentially fraudulent activities."
- 3.3.4: an account meeting the CRILC reporting threshold, once red flagged, "shall be reported to the Reserve Bank within seven days of being red flagged".
- 3.4.1: banks must also build EWS for non-credit transactions, and "the effectiveness of EWS system shall be tested periodically".
- The text contains no mention of AI or ML; the framework is technology-neutral. The commercial-banks Directions here are separate from the NBFC and co-operative bank versions issued the same day, which I did not read.
- **Possible newer version.** A search surfaced a mirror (lexsite.com) of an RBI document titled as "Commercial Banks - Fraud Risk Management Directions", dated 31 Jul 2026 (RBI/DoS/2026-27/412). It is an image-only PDF and I could not read it, so I do not know whether the 2024 Master Directions were replaced or whether the EWS paragraphs were renumbered. Check rbi.org.in before citing paragraph numbers.
- **Outcome data.** I found no RBI statistics on how many red flags were raised or how effective EWS is. The Annual Report lists "EWS" and "RFA" only in its abbreviations; the Annual Report 2025-26 mentions a thematic study on transaction-monitoring efficacy, with no findings published.

## Caveats for the CIS write-up
1. The 38% rule-based figure and any MuleHunter accuracy percentage are not in primary documents; drop them or flag them as unverified.
2. The Digital Lending Directions contain no AI or algorithm disclosure rule; the closest provision is mechanism documentation (Para 6(ii)).
3. The KYC Directions require liveness and spoof detection but do not mention deepfakes.
4. FY25 fraud numbers were revised from Rs 36,014 cr to Rs 32,803 cr, and FY26 is inflated by Rs 30,199 cr of re-classified older cases. Do not present the 2025-26 Rs 48,021 crore as new fraud.
5. I did not open the HyperVerge, MediaNama or other press pages beyond the snippets noted above, apart from the MediaNama RTI article.
