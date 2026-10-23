# AI-assisted exercise — Software Engineering and Testing

- **Model:** ChatGPT GPT-6 (model label available in this conversation; exact backend build not exposed)
- **Date:** 2026-10-23
- **Evidence status:** Generated in this ChatGPT conversation; candidate review and executable tests recommended.

## Exact prompt used

> Design a compact test matrix for a function that accepts a request description as a non-empty trimmed string of at most 200 characters. Include normal, whitespace-only, empty, 200-character boundary, 201-character boundary, and wrong-type cases. State expected outcomes and avoid pretending tests were run.

## Output excerpt

Expected cases: 'pump issue' -> accept; '   ' -> reject after trimming; '' -> reject; exactly 200 characters -> accept; 201 characters -> reject; None/non-string -> reject with a controlled validation error. The implementation should trim before checking length, reject non-strings safely, and return a clear error rather than crashing.

## Verification notes

These cases cover valid input, normalization, empty input, both sides of the length boundary, and type validation. They can be executed as unit tests against the actual implementation; this prompt/output alone does not prove a program passed.

## Verification source

https://docs.python.org/3/library/unittest.html

## Candidate review

Before submission, personally review the prompt/output, open the source, add any corrections you make, and do not claim a code/test was executed unless you execute it yourself. This record discloses AI assistance rather than attributing generated wording to independent candidate work.
