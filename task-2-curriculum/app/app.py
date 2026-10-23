from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "task-2-curriculum" / "data"
COURSES_FILE = DATA / "curriculum.csv"
CHANGES_FILE = DATA / "change-proposal.csv"
TESTS_FILE = ROOT / "task-1-workflow" / "test-cases.csv"

st.set_page_config(page_title="CampusFlow | Curriculum & Workflow", page_icon="🎓", layout="wide")
st.title("CampusFlow")
st.caption("Curriculum audit and workflow-improvement prototype • local CSV data only")

@st.cache_data
def load_csv(path):
    return pd.read_csv(path, keep_default_na=False)

courses = load_csv(COURSES_FILE)
changes = load_csv(CHANGES_FILE)
test_cases = load_csv(TESTS_FILE)

st.warning(
    "Curriculum baseline: candidate-confirmed official course record supplied for this assignment (172 listed programme credits, including completed/current/planned components). "
    "Workflow data and time-saving values are illustrative. This is a local prototype, not a college system."
)

metric_cols = st.columns(3)
metric_cols[0].metric("Baseline programme credits", "172")
metric_cols[1].metric("Distinct affected credits", "43")
metric_cols[2].metric("Affected-credit share", "25.0%")
st.caption("Use the tabs below: explore the course map, inspect the 12 recommendations, review the credit-impact calculation, and test the illustrative workflow time-saving scenario.")

tab1, tab2, tab3, tab4 = st.tabs(["Curriculum explorer", "Change proposal", "Credit calculator", "Workflow scenario"])

with tab1:
    st.subheader("Course map")
    c1, c2, c3 = st.columns(3)
    semesters = sorted(courses["semester"].unique(), key=lambda x: (0, int(x)) if x.isdigit() else (1, x))
    chosen_semesters = c1.multiselect("Semester / period", semesters, default=semesters)
    statuses = sorted(courses["record_status"].unique())
    chosen_statuses = c2.multiselect("Record status", statuses, default=statuses)
    search = c3.text_input("Search course", placeholder="e.g. machine learning, CS206")
    view = courses[courses["semester"].isin(chosen_semesters) & courses["record_status"].isin(chosen_statuses)].copy()
    if search.strip():
        q = search.strip().casefold()
        view = view[view.apply(lambda r: q in str(r["course_code"]).casefold() or q in str(r["course_title"]).casefold(), axis=1)]
    view["credits"] = pd.to_numeric(view["credits"], errors="coerce")
    st.dataframe(view, use_container_width=True, hide_index=True)
    st.caption(f"{len(view)} course/period rows shown. Blank course codes are intentionally blank where not provided.")
    totals = courses.copy()
    totals["credits"] = pd.to_numeric(totals["credits"], errors="coerce").fillna(0)
    summary = totals.groupby(["semester", "record_status"], as_index=False)["credits"].sum()
    st.markdown("**Credit sum by listed period and status**")
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.info("The 172-credit baseline is the candidate-confirmed supplied official curriculum total across completed, current and planned components; it does not mean all 172 credits are already completed.")

with tab2:
    st.subheader("Proposed curriculum changes")
    decisions = sorted(changes["decision"].unique())
    chosen = st.multiselect("Decision", decisions, default=decisions)
    proposal_view = changes[changes["decision"].isin(chosen)]
    st.dataframe(proposal_view, use_container_width=True, hide_index=True)
    st.caption("Updates within existing courses do not automatically change credit totals. Conditional additions require regulation/faculty approval.")

with tab3:
    st.subheader("Affected-credit share")
    st.write("This calculator uses the candidate-confirmed official curriculum baseline supplied for this assignment. Count each affected credit once.")
    a, b = st.columns(2)
    total = a.number_input("Programme credits in supplied official baseline", min_value=1, value=172, step=1, help="Candidate-confirmed supplied curriculum total, including completed, current, and planned components.")
    affected = b.number_input("Distinct credits materially affected", min_value=0, value=43, step=1, help="Default comes from data/affected-credit-map.csv. Count a credit only once even if multiple recommendations touch it.")
    if affected > total:
        st.error("Affected credits cannot exceed the programme-credit denominator. Recheck your counting.")
    else:
        share = 100 * affected / total
        x, y, z = st.columns(3)
        x.metric("Affected share", f"{share:.1f}%")
        y.metric("20% threshold", f"{total * .20:.1f} credits")
        z.metric("25% threshold", f"{total * .25:.1f} credits")
        if 20 <= share <= 25:
            st.success("The entered figures fall within 20–25%. The current mapped proposal is 43/172 = 25.0%; verify the course map and approval conditions before reporting it.")
        else:
            st.info("The entered figures are outside 20–25%. Do not force the percentage; revise only with evidence and approval.")
    st.caption("Defaults come from the candidate-confirmed baseline and task-2-curriculum/data/affected-credit-map.csv. Count each course only once.")

with tab4:
    st.subheader("Illustrative workflow time-saving scenario")
    st.caption("All defaults are illustrative assumptions, not measured campus data. Replace them only with permitted observations or defensible estimates.")
    n = st.number_input("Requests per month", min_value=0, value=40, step=5)
    before = st.number_input("Current minutes per request", min_value=0.0, value=12.0, step=1.0)
    after = st.number_input("Proposed routine minutes per request", min_value=0.0, value=7.0, step=1.0)
    review = st.number_input("Review overhead minutes/month", min_value=0.0, value=60.0, step=5.0)
    support = st.number_input("Support/failure overhead minutes/month", min_value=0.0, value=30.0, step=5.0)
    gross = n * (before - after)
    net = gross - review - support
    a, b, c = st.columns(3)
    a.metric("Gross minutes saved", f"{gross:.0f}")
    b.metric("Net minutes saved", f"{net:.0f}")
    c.metric("Net hours saved", f"{net/60:.2f}")
    st.code("net = requests × (current minutes − proposed minutes) − review overhead − support overhead")
    if net <= 0:
        st.warning("Under these inputs, time savings alone do not justify the redesign.")
    st.dataframe(test_cases, use_container_width=True, hide_index=True)
    st.caption("Synthetic test cases are specified but not marked as passed until actual test runs are recorded.")
