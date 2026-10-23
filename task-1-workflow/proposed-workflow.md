# Proposed workflow and controls

## Goal
Demonstrate how a small request workflow could improve traceability and failure recovery without assuming any particular institution's current process.

## Status transitions
`Submitted -> Needs information -> Validated -> Awaiting approval -> Assigned -> In progress -> Blocked/Failed -> Resolved -> Closed`

Also allow `Rejected` and `Cancelled` with a reason. Each transition records request ID, prior/new status, timestamp, role and reason.

## Role boundaries
- Requester can submit and clarify.
- Triage can check completeness and duplicate candidates.
- Only a formally authorized role can approve restricted work, spending or closure.
- Assigned worker records progress and blockers.
- Audit history is append-only in the intended design; real deployment would require authenticated access controls and retention policy.

## Minimum data
Generated ID, asset/location category, concise description, urgency category with criteria, timestamp, status and event history. Avoid names and unnecessary personal data in the prototype.

## Failure behavior
- Incomplete request: move to `Needs information`.
- Duplicate candidate: flag for human review; never silently delete.
- Unauthorized action: deny and record the attempt.
- Assignment/notification failure: preserve the request and log; retry idempotently or use an approved manual fallback.

## AI boundary
Rules, not AI, should enforce permissions, required fields and status transitions. Any AI summary must be optional, non-sensitive, human-reviewed and linked to the original text. AI must never approve work or infer authorization.

## Acceptance checks
Run all five synthetic cases in `test-cases.csv`. Record actual result, pass/fail, date and test environment. Until run, the cases are specified but not tested.
