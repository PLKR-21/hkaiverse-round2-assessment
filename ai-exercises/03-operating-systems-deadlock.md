# AI-assisted exercise — Operating Systems

- **Model:** ChatGPT GPT-6 (model label available in this conversation; exact backend build not exposed)
- **Date:** 2026-10-23
- **Evidence status:** Generated in this ChatGPT conversation; textbook/lecture-note verification still required.

## Exact prompt used

> Give a concise OS explanation of the four Coffman conditions for deadlock, then give a two-process/two-lock example and one prevention strategy. Clearly separate necessary conditions from the example.

## Output excerpt

The four necessary Coffman conditions are mutual exclusion, hold-and-wait, no preemption, and circular wait. Example: process P1 holds lock A and waits for B; process P2 holds lock B and waits for A. Each waits for a resource held by the other, creating a cycle. One prevention strategy is a global lock ordering: require every process to acquire A before B, so the circular-wait condition cannot arise if all code follows the same order.

## Verification notes

Check the four condition names and the lock-ordering prevention argument against the course textbook/lecture notes. The example is a conceptual trace, not an executed concurrency program. Candidate should add the exact course source consulted before claiming independent source verification.

## Verification source

https://pages.cs.wisc.edu/~remzi/OSTEP/ (use the synchronization/deadlock material available in the course text)

## Candidate review

Before submission, personally review the prompt/output, open the source, add any corrections you make, and do not claim a code/test was executed unless you execute it yourself. This record discloses AI assistance rather than attributing generated wording to independent candidate work.
