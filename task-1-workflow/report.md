# Task 1 — Investigate and redesign a small campus workflow

## Status and scope

The candidate has not supplied verified field observations for a current campus workflow. This report therefore uses a **hypothetical lab equipment fault-reporting walkthrough** to demonstrate a method and design. It does not claim that IFHE currently uses this workflow or that the process is manual.

If permitted access becomes available, replace or supplement the hypothesis with the actual observed process. If access is unavailable or declined, retain the hypothetical label and state that no current-state observations were collected.

## 1. Problem hypothesis

A fault report can become difficult to track if required details are missing, a duplicate is created, responsibility is unclear, or a notification/assignment step fails. This is a hypothesis to test, not a finding about the institution.

Questions for permitted investigation:
- Who may submit a request, and what fields are required?
- Who validates completeness and duplicate candidates?
- Which role can approve work, replacement or expenditure?
- How are status and closure communicated?
- What is the actual request volume, handling time and rework rate?
- Which delays are controllable by routing versus caused by external repair/approval capacity?

## 2. Hypothetical current-state walkthrough

```text
Requester notices an issue
  -> sends report through currently approved channel (to be confirmed)
  -> recipient checks required details
      -> missing: request clarification, then re-check
      -> complete: check possible duplicate
  -> authorized role reviews request
      -> out of scope/rejected: record reason and route appropriately
      -> approved: assign responsible role
  -> work progresses
      -> blocked/failed: record failure and use approved fallback
      -> resolved: requester/authorized role confirms and closes
```

This is a proposed model for investigation, not an observed map.

## 3. Evidence protocol

Use `evidence-log.csv` to record each evidence item with date, method, role only, summary, classification, sample count, permission status and limitations.

Classify each statement as:
- **Observed fact:** directly seen or stated in a permitted source/conversation.
- **Estimate:** measured or estimated quantity with method and sample size.
- **Assumption:** unverified premise used for design.

Ask permission before observing or interviewing. Do not collect names, student IDs, marks, fees, signatures, credentials or private messages. A refusal is a valid outcome and should not be bypassed.

## 4. Proposed future workflow

### Minimum request data
- generated request ID;
- location or asset category;
- concise issue description;
- urgency with defined criteria;
- submission timestamp;
- status and history;
- optional attachment only if institutional policy permits and privacy risks are reviewed.

### State model
`Submitted -> Needs information -> Validated -> Awaiting approval -> Assigned -> In progress -> Blocked/Failed -> Resolved -> Closed`

Other states: `Rejected`, `Cancelled`. Each transition should store timestamp, role responsible and reason. This proposal does not define real college permissions; an authorized owner must confirm them.

### Ownership and authorization
- Requester: submits and clarifies details; may confirm whether the issue appears resolved.
- Triage role: checks completeness and duplicate candidates; cannot approve actions outside delegated authority.
- Approver: only the role authorized by policy may approve repair, replacement or spending.
- Assigned role: updates progress and records blockers.
- Audit record: request ID, state history, role, timestamp, reason, retry count and closure outcome.

### Failure handling
A failed assignment or notification should not delete the request or silently bypass approval. Record the failure, preserve history, retry safely when appropriate, and use the approved manual fallback if the service is unavailable.

### Where AI is unnecessary
Ordinary validation rules can check required fields, state transitions and role permissions. AI must not grant authorization. If a future prototype uses AI to summarize a non-sensitive issue description, a human should verify the summary and original description should remain available.

## 5. Five synthetic test cases

The CSV in `test-cases.csv` covers normal, missing, duplicate, unauthorized and failed-step cases. These are synthetic tests, not evidence that a production system was tested. Record actual results after testing the prototype or manually walking through the acceptance rules.

## 6. Time-saving model

The calculator in `time-savings.csv` is an illustrative scenario, not a measurement from IFHE:
- monthly requests, N = 40;
- current handling = 12 minutes/request;
- proposed routine handling = 7 minutes/request;
- review overhead = 60 minutes/month;
- support overhead = 30 minutes/month.

Gross saving = `N × (current minutes − proposed minutes)` = 40 × (12 − 7) = 200 minutes/month.

Net saving = `gross saving − review overhead − support overhead` = 200 − 60 − 30 = **110 minutes/month**.

Sensitivity under the same illustrative assumptions:
- N = 20: 100 gross − 90 overhead = 10 net minutes/month.
- N = 60: 300 gross − 90 overhead = 210 net minutes/month.

Formula: `Net minutes/month = N × (baseline minutes/request − proposed minutes/request) − review minutes/month − support minutes/month`.

If actual net saving is zero or negative, the proposal is not justified by time savings alone. Traceability or service quality may still matter, but do not invent monetary value.

## 7. Risks and falsification

Risks include false duplicate flags, unauthorized state changes, poor adoption, inaccurate urgency labels, downtime, sensitive details in free text and incorrect assumptions about current practice.

**Observation that would change the design:** if permitted evidence shows most delays are caused by repair capacity or approval queues rather than missing details or routing, a request form alone will not solve the problem. The proposal should focus on capacity visibility and escalation rules instead.

## 8. Current evidence status

- Current workflow observed: **No evidence supplied**
- Fieldwork or voluntary conversations: **Not documented**
- Time values: **Illustrative assumptions**
- Five synthetic test cases: **Specified; execution results pending**
- Faculty/graduate feedback: **Not obtained in this draft**
- Production deployment/live college integration: **Not attempted**
