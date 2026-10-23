# CampusFlow local prototype

Run from repository root:

```bash
pip install -r requirements.txt
streamlit run task-2-curriculum/app/app.py
```

Features:
- search and filter candidate-provided courses by semester/status/title/code;
- filter KEEP/UPDATE/REDUCE/ADD recommendations;
- calculate affected-credit share using the candidate-confirmed 172-credit baseline and 43-credit map (25.0%);
- calculate net workflow time savings under editable scenario assumptions;
- review five synthetic workflow test cases.

The tool uses local CSVs only. It has no authentication, database, live college integration or production workflow implementation. It must not be described as deployed or officially approved.
