# Submission checklist

## Critical evidence
- [ ] Course details checked against the candidate-confirmed official curriculum copy; Semester VII course codes remain blank where not supplied.
- [ ] Candidate checks all course codes/titles/credits against source; Semester VII course codes and official “Human Computer Vision” title confirmed.
- [ ] Three dated individual job postings reopened; dates, requirements and experience caveats recorded.
- [ ] Workflow fieldwork recorded with permission, or hypothetical-only status retained.
- [ ] No personal/sensitive campus data included.
- [ ] Faculty/graduate feedback recorded only if actually obtained; otherwise state unavailable.

## Technical checks
- [ ] `pip install -r requirements.txt` succeeds.
- [ ] `python scripts/validate_project.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] `streamlit run task-2-curriculum/app/app.py` starts and all filters/calculators work.
- [ ] Five synthetic workflow tests actually walked through; results are recorded honestly.
- [ ] AI exercise outputs reviewed; source checks and any executable checks performed and described accurately.
- [ ] Credit calculator and `affected-credit-map.csv` reconcile: 43/172 = 25.0%, distinct courses counted once; no net credits added or removed by default.

## Submission mechanics
- [ ] Personal contribution and AI-use disclosure completed truthfully.
- [ ] `git status` reviewed; no `.env`, credentials, private portal screenshots or sensitive files.
- [ ] Final commit created and pushed.
- [ ] Named release created; release URL and full commit URL recorded in README.
- [ ] One repository URL submitted on portal.
- [ ] Saved receipt captured; remember receipt confirms URL submission, not review or access.
