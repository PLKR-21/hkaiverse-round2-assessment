# AI-assisted exercise — Database Management Systems

- **Model:** ChatGPT GPT-6 (model label available in this conversation; exact backend build not exposed)
- **Date:** 2026-10-23
- **Evidence status:** Generated in this ChatGPT conversation; candidate review and local rerun recommended.

## Exact prompt used

> Explain whether an SQL INNER JOIN removes duplicate rows. Use synthetic tables Students(student_id, name) with (1, 'Asha') and Enrollments(student_id, course) with (1, 'DBMS'), (1, 'AI'). Show the query and exact result rows. Distinguish join multiplicity from SELECT DISTINCT.

## Output excerpt

Query: SELECT s.student_id, s.name, e.course FROM Students AS s INNER JOIN Enrollments AS e ON s.student_id = e.student_id;. Expected rows: (1, 'Asha', 'DBMS') and (1, 'Asha', 'AI'). An INNER JOIN returns one output row per matching pair; it does not automatically deduplicate rows. SELECT DISTINCT removes duplicate output tuples, but these two rows are not duplicates because course differs.

## Verification notes

The join cardinality follows the two matching enrollment records. The same behavior can be verified by running this query against SQLite with the two synthetic tables. No real student data is used.

## Verification source

https://www.sqlite.org/lang_select.html

## Candidate review

Before submission, personally review the prompt/output, open the source, add any corrections you make, and do not claim a code/test was executed unless you execute it yourself. This record discloses AI assistance rather than attributing generated wording to independent candidate work.
