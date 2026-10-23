from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

def read_csv(rel):
    with (ROOT / rel).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def main():
    errors = []
    courses = read_csv("task-2-curriculum/data/curriculum.csv")
    changes = read_csv("task-2-curriculum/data/change-proposal.csv")
    jobs = read_csv("task-2-curriculum/data/job-descriptions.csv")
    ai = read_csv("task-2-curriculum/data/ai-verification-log.csv")
    cases = read_csv("task-1-workflow/test-cases.csv")
    sources = read_csv("evidence/source-register.csv")
    affected_map = read_csv("task-2-curriculum/data/affected-credit-map.csv")

    if len(courses) < 45: errors.append(f"Expected at least 45 curriculum rows; got {len(courses)}")
    if len(changes) != 12: errors.append(f"Expected 12 curriculum recommendations; got {len(changes)}")
    if len(ai) != 5: errors.append(f"Expected five AI exercise records; got {len(ai)}")
    if len(cases) != 5: errors.append(f"Expected five synthetic workflow test cases; got {len(cases)}")
    try:
        affected_total = sum(float(row["credits"]) for row in affected_map)
    except Exception:
        affected_total = -1
        errors.append("Affected-credit map contains invalid credits")
    if affected_total != 43: errors.append(f"Expected 43 distinct affected credits; got {affected_total}")
    if abs(100 * affected_total / 172 - 25.0) > 1e-9: errors.append("Affected-credit share should be 25.0% of the 172-credit baseline")
    dated = [j for j in jobs if j.get("posting_date") and j["posting_date"] != "Not shown on individual page at access"]
    if len(dated) < 3: errors.append(f"Expected at least three dated individual job descriptions; got {len(dated)}")
    if any(not s.get("source_url","").startswith("http") for s in sources if s.get("source_url","")):
        errors.append("At least one source URL is not HTTP(S)")
    for c in courses:
        try: credits = float(c["credits"])
        except Exception: errors.append(f"Invalid credits value for {c.get('course_title')}"); continue
        if credits < 0: errors.append(f"Negative credits for {c.get('course_title')}")
    # Check known semester arithmetic based on the candidate-provided record.
    totals = {}
    for c in courses:
        try: credits = float(c["credits"] or 0)
        except Exception: credits = 0
        totals[c["semester"]] = totals.get(c["semester"], 0) + credits
    expected = {"I":20, "II":24, "III":23, "IV":24, "ST-II":3, "V":21, "VI":21, "VII":16, "VIII":20}
    for sem, value in expected.items():
        if totals.get(sem) != value:
            errors.append(f"Semester {sem} credit sum expected {value}, got {totals.get(sem)}")
    if errors:
        print("VALIDATION FAILED")
        for e in errors: print(f"- {e}")
        return 1
    print("Structural validation passed.")
    print(f"Curriculum rows: {len(courses)}; recommendations: {len(changes)}; AI exercise records: {len(ai)}; synthetic cases: {len(cases)}.")
    print("Three or more dated individual job postings are recorded.")
    print("Semester sums match the candidate-confirmed official baseline arithmetic.")
    print(f"Affected-credit map: {affected_total:.0f}/172 = {100 * affected_total / 172:.1f}% (distinct courses counted once).")
    print("This script does not independently verify external source claims, fieldwork, or candidate review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
