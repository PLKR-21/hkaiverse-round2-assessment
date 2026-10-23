# Task 2 — Audit and redesign the curriculum for work in 2030

## Executive summary

This proposal uses the candidate-confirmed official curriculum baseline supplied for the 2023 admission cohort, including completed/current/planned course components, plus dated employer job descriptions to identify skill signals. The candidate has instructed that the supplied curriculum is the official baseline for this assignment. The job-description sample remains small and purposive; it does not represent the entire labour market.

The candidate's course history already includes programming, data structures, algorithms, mathematics, data science, DBMS, software engineering, OS, networks, AI, ML, computer vision, big data and cloud computing. The strongest proposal is therefore not to replace fundamentals with a list of trendy tools. It is to check whether existing courses assess reproducible implementation, data quality, software testing, secure deployment and AI evaluation, and then fill only verified gaps.

## 1. Scope and baseline

- Programme context supplied by candidate: B.Tech Computer Science, IFHE/IcfaiTech Hyderabad, admission batch 2023.
- Source for course data: the candidate-confirmed official curriculum/grade-sheet baseline supplied for this assignment; current Semester VII and planned Semester VIII components are explicitly labelled in `data/curriculum.csv`.
- Institutional context: [IFHE/IcfaiTech B.Tech programme structure](https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure), accessed 2026-10-23. The supplied cohort curriculum is the controlling baseline for this proposal.

The baseline shows 136 cumulative credits through Semester VI, including Internship-I; 16 credits listed for current Semester VII; and a planned 20-credit Semester VIII internship. The programme baseline used in this assignment is therefore **172 credits** (136 + 16 + 20), including completed, current and planned components. The 20-credit internship is planned, not completed. See `data/curriculum-source-notes.md` for reconciliation.

## 2. Dated job-description sample and limitations

Four individual employer pages were opened on 2026-10-23; three have explicit posting dates and can satisfy the minimum dated-posting count after the candidate reopens and confirms the pages. They are a small purposive sample, not a statistically representative labour-market study.

| Employer / role | Posting date | Useful skill signals | Eligibility caveat |
|---|---|---|---|
| [DXC Luxoft — Junior AI/ML Engineer, Hyderabad](https://career.luxoft.com/jobs/junior-aiml-engineer-28443) | 2026-10-21 | Python, SQL, Git, RAG, agents, embeddings/vector DBs, LLM evaluation, FastAPI, ML evaluation | No years stated; expects an early-career engineer who already builds LLM agents. |
| [Wipro — AI Engineer L1, Hyderabad](https://careers.wipro.com/job/AI-ENGINEER-L1/208281-en_US/) | 2026-10-12 | Python/Java/C++, deep learning, computer vision/OpenCV, model evaluation, cloud and data platforms | Not clearly graduate-level; page includes 2–5 and 3–5 years experience wording. |
| [Amgen — Associate Software Engineer, Hyderabad](https://careers.amgen.com/en/job/hyderabad/associate-software-engineer/87/100307758640) | 2026-09-07 | Python, FastAPI/Django, React, LLM/RAG workflows, GitHub review, SQL/NoSQL, vector search, reliability | Overview says early-career, but basic qualification asks for 2–5 years relevant experience. |
| [Amazon — Software Dev Engineer I, University Talent Acquisition](https://www.amazon.jobs/en/jobs/10517917/software-dev-engineer-i-amazon-university-talent-acquisition) | Date not shown on page at access | CS fundamentals, data structures, algorithms, programming, distributed systems, databases | Explicitly intended for 2025/2026 graduates, so not an eligibility match for a 2027 graduate; included only as a comparative signal, not one of the three dated roles. |

The sample suggests that course outcomes should connect foundations to demonstrable work: programming, data structures, SQL, Git, API development, testing, cloud/operational reliability, model evaluation and safe LLM integration. These are signals from these pages, not a claim that every employer requires every skill.

## 3. What the current course map already covers

The candidate-provided record contains relevant existing foundations:

- Programming and algorithms: CS101, CS102, CS203, CS201, CS303.
- Mathematics and theory: MA101, MA102, MA201, MA202, CS202.
- Data management and analytics: CS206, DS203, DS307.
- Software and systems: CS304, CS302, CS306, CS307, CS205.
- AI/ML: DS101, DS201, DS304, CS305, plus current Deep Learning and NLP.
- Security: CS301 and current Ethical Hacking.
- Project / practical experience: DS202, IP201, SP301, planned Internship.

These course names, codes and credits are taken from the candidate-confirmed official baseline. Detailed course learning outcomes and assessment rubrics were not part of the supplied course/credit table, so recommendations call for reviewing those materials before claiming a gap.

## 4. Twelve KEEP / UPDATE / REDUCE / ADD recommendations

The full machine-readable proposal is `data/change-proposal.csv`. The 12 recommendations retain fundamentals, target assessment quality, and make new lab/module content embedded in existing credits by default. A standalone credit change would require formal reallocation and approval.

| # | Decision | Course area | Proposed action and rationale |
|---:|---|---|---|
| 1 | KEEP | CS102 Data Structures; CS203 DAA | Retain foundations; assess implementation, edge cases and complexity reasoning. |
| 2 | KEEP / AUDIT | CS304 project workflow (counted once with recommendation 4) | Retain existing programming foundations; audit Git, code review, debugging and reproducible setup, and assess these through the already-counted CS304 project only where gaps exist. |
| 3 | UPDATE | CS206 DBMS | Add practical SQL, joins, query plans, transactions, migrations and data-quality checks where gaps exist. |
| 4 | UPDATE | CS304 Software Engineering | Use requirements, issues, code review, CI checks and release notes in a graded team project. |
| 5 | UPDATE | CS302 OS; CS306 Networks | Use applied labs for concurrency, APIs, timeouts, retries and failure recovery while preserving systems theory. |
| 6 | UPDATE | CS307 Cloud Computing | Assess deployment, logs, secrets hygiene, monitoring and rollback using safe free/local environments. |
| 7 | UPDATE | DS304 ML; DS201 AI; Semester VII Deep Learning | Require baselines, leakage-safe splits, error analysis, reproducibility and limitations. |
| 8 | UPDATE | Semester VII Human Computer Vision | Assess context variation, failure cases, usability and human override. CS305 Computer Vision is not included in this change unless a separate evidence-based change is approved. |
| 9 | ADD (conditional) | Data engineering workflow lab embedded in CS307 Cloud Computing / DS307 Big Data Systems | Embed ingestion, validation, transformation, lineage and idempotency within existing coursework by default; no net credits added. |
| 10 | ADD (conditional) | AI evaluation, privacy and human review embedded in DS201, DS304 and Semester VII Deep Learning | Embed dataset provenance, leakage, evaluation sets, privacy and human review within the already-counted AI/ML courses; no net credits added by default. |
| 11 | REDUCE (conditional) | Only proven duplicated demonstrations | Reduce only documented repetition after a full syllabus/contact-hour map; no specific course is named for reduction yet. |
| 12 | KEEP | Mathematics, theory, OS, networks and cryptography | Preserve foundations; count material assessment updates only in the explicitly listed affected-credit map, and do not double-count overlapping recommendations. |

### How the recommendations are evaluated

Each recommendation should be checked against: (a) official course learning outcomes, (b) actual assessment/rubric, (c) the dated job-description sample, (d) prerequisites and contact hours, and (e) student/faculty feedback where available. Do not claim an existing course is deficient merely because a new tool is popular.

## 5. Credit impact and 20–25% target

For this assignment, the candidate-confirmed official programme baseline supplied is **172 credits**, including 136 completed through Semester VI, 16 current Semester VII credits, and a planned 20-credit Semester VIII internship. The proposed redesign materially affects **43 distinct credits**, counted once per course/period in `data/affected-credit-map.csv`.

\`Affected-credit share = distinct credits materially affected ÷ baseline programme credits × 100\`

\`43 ÷ 172 × 100 = 25.0%\`

The proposal therefore sits at the upper boundary of the requested 20–25% affected-credit band. The affected credits are CS102 (4), CS203 (3), CS206 (4), CS304 (3), CS302 (4), CS306 (4), CS307 (4), DS304 (4), DS201 (3), Deep Learning (4), Human Computer Vision (3), and DS307 Big Data Systems (3). Each course is counted once even where multiple recommendations touch it. See `data/affected-credit-map.csv` for the course-level rationale and recommendation links.

**Balanced credit plan:** the default proposal changes learning outcomes/assessed practice within existing courses and embeds the conditional workflow/data-engineering and AI-evaluation modules. No net credits are added or removed, so the baseline total remains **172 credits**. The `credits_changed` column in `change-proposal.csv` is zero for this default design. A standalone new module is an alternative only if the programme formally reallocates existing credits and approves the change; it must not be added on top of the baseline without reconciliation.

This is an affected-credit share, not a claim that 25% of credits are deleted or newly added. Course owners should check learning outcomes, assessment rubrics, prerequisites and workload before adopting the proposal.

## 6. Five AI-assisted exercises

Five transparent exercise records are in `../../ai-exercises/`:
1. DSA — hash-map Two Sum and duplicate values.
2. DBMS — join multiplicity versus `DISTINCT`.
3. OS — deadlock conditions and lock ordering.
4. Software testing — input-validation boundary cases.
5. ML — leakage-safe preprocessing and split strategy.

The prompt and output excerpts were generated in this ChatGPT conversation on 2026-10-23 using the model label GPT-6; the exact backend build is not exposed. The log discloses that assistance. These are not represented as five independent experiments or as proof of execution. Candidate review, source checks, and executable tests where applicable remain required. The AI log marks candidate review as pending.

## 7. Task 1 workflow converted into a lab/capstone

**Proposed title:** CampusFlow — Auditable Request Workflow and Reliability Lab.

- **Possible host:** Software Engineering (CS304), Special Project (SP301), or another approved practical course. Exact host and credit allocation require faculty/programme approval.
- **Prerequisites:** programming, DBMS, basic web/API development, Git and testing.
- **Learning outcomes:** map a process with permission; implement required-field validation and role boundaries; maintain an audit trail; test duplicate, incomplete, unauthorized and failed requests; quantify effort with transparent assumptions.
- **Synthetic data only:** fabricated request IDs, asset categories, timestamps and statuses.
- **Milestones:** evidence plan; current-state map; prototype; five test cases; measurement and limitations; demonstration and review.
- **Acceptance criteria:** the five synthetic cases have recorded outcomes; unauthorized actions are blocked; failures preserve state/history; calculations can be reproduced.
- **AI boundary:** AI may summarize a non-sensitive issue description only with human review; it must not authorize, approve or infer permission.

The proposed lab remains a design proposal. Task 1 fieldwork has not been documented, so no current campus process or benefit is claimed.

## 8. Feedback, falsification and limitations

Faculty/graduate feedback has not been obtained in the materials available for this draft. If it cannot be obtained before submission, report that honestly and include questions for future validation.

**Falsifiable claim:** integrated practical assessment of data quality, testing, cloud reliability and AI evaluation may improve work readiness. The claim would be weakened if existing assessments already measure these outcomes well, employers prioritize different gaps, or the added work displaces essential foundations.

## 9. Submission checklist

- [ ] Use the candidate-confirmed official curriculum baseline supplied for this assignment; verify transcription against the candidate’s source copy before submission.
- [ ] Recheck all three dated individual job pages and retain access dates.
- [ ] Candidate reviews the five AI exercise records and completes source checks/local tests.
- [ ] Keep Semester VII course-code fields blank where no code was supplied; preserve the title “Human Computer Vision” exactly as supplied.
- [ ] Record actual workflow evidence or clearly retain the hypothetical-only limitation.
- [ ] Ask for voluntary faculty/graduate feedback if feasible; never invent a response.
- [ ] Recheck the 43/172 = 25.0% affected-credit map; count distinct credits once and preserve the no-net-credit-change default.
- [ ] Test the Streamlit app and validation script locally.
- [ ] Complete the personal contribution statement truthfully.
