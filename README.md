# CampusFlow — Workflow Improvement & Curriculum Audit

**HKAIVERSE Round 2 assessment project | Working final-draft package**  
**Deadline supplied by candidate:** 24 October 2026, 11:59 PM IST

CampusFlow contains two connected proposals:
1. **Task 1:** investigate and redesign a small workflow, using a hypothetical lab fault-reporting example until permitted field evidence is available.
2. **Task 2:** map the candidate's actual reported courses, compare selected dated job descriptions, and propose evidence-led curriculum improvements.

## Evidence integrity

This repository is a polished **draft package, not a claim that all external evidence has been independently verified**. It preserves important unresolved items:
- the candidate has not supplied current campus workflow observations;
- time-saving values are illustrative assumptions;
- job postings are a small sample, and some contain experience requirements that may not fit a 2027 graduate;
- the candidate must review AI-assisted exercise outputs and complete remaining source/execution checks;
- faculty/graduate feedback has not been obtained.

Do not remove these limitations unless the underlying evidence is actually obtained.

## Repository map

- `task-1-workflow/report.md` — hypothesis, proposed workflow, safety boundaries, scale model and limitations
- `task-1-workflow/evidence-log.csv` — evidence log with current hypothetical-only status
- `task-1-workflow/test-cases.csv` — five synthetic cases; execution pending
- `task-1-workflow/time-savings.csv` — low/base/high illustrative scenarios
- `task-1-workflow/proposed-workflow.md` — states, permissions, fallback and acceptance criteria
- `task-2-curriculum/report.md` — course audit, 12 recommendations, dated job sample, credit methodology and capstone proposal
- `task-2-curriculum/data/curriculum.csv` — candidate-provided grade-sheet courses plus separately labelled current/planned courses
- `task-2-curriculum/data/curriculum-source-notes.md` — credit reconciliation and source limitations
- `task-2-curriculum/data/job-descriptions.csv` — dated employer pages and fit caveats
- `task-2-curriculum/data/change-proposal.csv` — machine-readable KEEP/UPDATE/REDUCE/ADD proposal
- `task-2-curriculum/data/affected-credit-map.csv` — distinct affected courses and the 43-credit / 172-credit (25.0%) calculation
- `task-2-curriculum/data/ai-verification-log.csv` — five AI-assisted exercise records and pending candidate review
- `ai-exercises/` — prompts, output excerpts, verification notes and sources for five subjects
- `task-2-curriculum/app/app.py` — interactive curriculum explorer, recommendation filter, credit calculator and workflow scenario calculator
- `evidence/source-register.csv` — source URLs, access dates and verification status
- `evidence/contribution.md` — candidate contribution and AI-use disclosure
- `evidence/limitations.md` — material limitations
- `SUBMISSION_CHECKLIST.md` — final review checklist
- `scripts/validate_project.py` — structural/data validation; does not prove external claims
- `tests/test_project_logic.py` — local tests for credit and time-saving arithmetic

## Run locally

Use Python 3.10 or later.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run task-2-curriculum/app/app.py
```

In another terminal, run the checks:

```bash
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

The app reads only the local CSV files. It does not connect to college systems or submit data.

## Important credit arithmetic

For this assignment, the candidate confirms the supplied curriculum is the official baseline. It lists 136 credits through Semester VI including Internship-I, 16 current Semester VII credits, and a planned 20-credit Semester VIII internship, for a baseline of 172 credits including completed/current/planned components. The redesign materially affects 43 distinct credits (43/172 = 25.0%) while preserving the total at 172; see `task-2-curriculum/data/affected-credit-map.csv`.

## Before submission — do not skip

1. Confirm that the transcribed course details exactly match the candidate-confirmed official curriculum copy; semester VII codes remain blank where not supplied.
2. Reopen the three dated employer postings, check their requirements and retain the access date. Do not present the sample as representative of all employers.
3. Personally review all five AI-assisted exercise files. Run relevant local code/query tests and add exact source/chapter checks where required.
4. Conduct permitted workflow fieldwork if feasible. If access is unavailable or declined, keep the workflow hypothetical and state no observations were collected.
5. Record actual test results; do not change “Not tested” to “Pass” without running the tests.
6. Ask for voluntary faculty/graduate feedback if feasible; otherwise report unavailable.
7. Review `affected-credit-map.csv`: 43 distinct affected credits / 172 baseline credits = 25.0%; count each course once and keep the no-net-credit-change default.
8. Complete `evidence/contribution.md` truthfully.
9. Review the app and run both validation commands.
10. Create a final commit and named GitHub release. Add the release URL, full commit URL and submitted repository URL below only after they exist.

## Release record

- Release tag: `v1.0.0` (create after review)
- Release URL: `https://github.com/PLKR-21/hkaiverse-round2-assessment/releases/tag/v1.0.0`
- Full commit URL: `ADD AFTER FINAL COMMIT`
- Submitted repository URL: `ADD AFTER PORTAL SUBMISSION`
- Receipt/time: `ADD AFTER SUBMISSION`

## Sources

See `evidence/source-register.csv` and the relevant report sections. Official IFHE/IcfaiTech programme starting page: https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure

## Disclaimer

This is a student proposal and local prototype, not an official IFHE syllabus revision or a claim about a currently used campus process. It contains no production college data and no live college integration.
