# AI-assisted exercise — Data Structures and Algorithms

- **Model:** ChatGPT GPT-6 (model label available in this conversation; exact backend build not exposed)
- **Date:** 2026-10-23
- **Evidence status:** Generated in this ChatGPT conversation; candidate review and local rerun recommended.

## Exact prompt used

> You are helping with a data-structures lab. Explain a hash-map solution to Two Sum. Use nums = [2, 7, 11, 15] and target = 9, return indices, give time and auxiliary-space complexity, and include a duplicate-value test nums = [3, 3], target = 6. Do not claim code was executed unless you execute it.

## Output excerpt

Maintain a map from value to index. For each value x at index i, compute complement = target - x; if complement is already in the map, return [map[complement], i]. Otherwise store x -> i. For [2, 7, 11, 15], target 9, the result is [0, 1]. For [3, 3], target 6, the first 3 is stored at index 0 and the second finds complement 3, producing [0, 1]. Expected time is O(n) average with a hash map; auxiliary space is O(n).

## Verification notes

The two examples were manually traced against the algorithm. The duplicate case confirms the complement lookup occurs before inserting the current value. Candidate should run the included validation script before submission.

## Verification source

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

## Candidate review

Before submission, personally review the prompt/output, open the source, add any corrections you make, and do not claim a code/test was executed unless you execute it yourself. This record discloses AI assistance rather than attributing generated wording to independent candidate work.
