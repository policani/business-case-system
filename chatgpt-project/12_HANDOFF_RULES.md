# Handoff Rules

Use a handoff note when the business case creates downstream work. Do not make
the user re-explain context in the next module.

## Handoff note format

Source module: Business Case System
Recommended next module or human owner:
Work item:
Lifecycle stage:

Confirmed facts:
Assumptions:
Evidence gaps:
Decisions needed:
Risks, dependencies, or actions:
Value gate summary:
Measurement contract, if value is claimed:
Do not pass downstream:
Suggested first prompt:

## Common handoffs

| Condition | Handoff target | Pass downstream |
|---|---|---|
| Case is approved or selected for initiation | Project Charter Initiation Agent | Problem, recommendation, approved scope envelope, sponsor, constraints, expected outcomes, measurement contract, major risks, assumptions, open decisions |
| Multiple cases or initiatives need comparison | Portfolio Prioritization Scoring Agent | Initiative summary, value claim, measurement contract, cost/capacity estimate, risk level, urgency, sponsor, decision authority, evidence confidence |
| Benefit claims need follow-through after approval | Value Realization Governance Ledger | Value gate summary and measurement contract: benefit class, ROI eligibility, baseline availability, cost of doing nothing, assumptions, confidence, finance-validation status, expected outcome, benefit type, metric, baseline, target, actual if available, measurement period, source, measure owner, review cadence, validation need, realization risk, finance-sensitive flag, downstream route |
| Risks, decisions, actions, or blockers need operating follow-up | PMO Governance Operations Log | Action items, owners, due dates, open decisions, risks, dependencies, escalation candidates |
| Control, compliance, supplier, audit, financial, or operational exposure is material | Controls Exposure Governance Toolkit | Exposure statement, affected process/system/vendor, owner, evidence, remediation options, open authority questions |
| Sponsor or executive discussion is needed | Executive Portfolio Review Pack Builder | Executive summary, decision requested, options, tradeoffs, risks, assumptions, recommendation |

## Do not pass downstream

- Unsupported financial claims as facts.
- Private or sensitive source material not needed for the next decision.
- Draft alternatives that were rejected unless the rationale is decision-useful.
- Implied approvals, funding, or sponsor agreement not confirmed by the user.

## First-prompt examples

Charter: "Use this approved business-case handoff to develop a project charter. First confirm authorization basis, scope, sponsors, constraints, success measures, risks, dependencies, and open decisions."

Scoring: "Use this business-case summary as initiative metadata for portfolio scoring. Identify missing sponsor, owner, decision authority, cost, capacity, benefit, risk, and dependency fields before scoring."

Value ledger: "Use these approved value claims to create a value-realization ledger. Separate benefit hypotheses from measured outcomes and flag evidence gaps."

## Synthetic value handoff example

Source module: Business Case System
Recommended next module or human owner: Value Realization Governance Ledger
Work item: Customer onboarding workflow standardization
Lifecycle stage: Approved business case moving into benefit tracking

Confirmed facts: Sponsor approved the expected outcome of reducing onboarding cycle time for a synthetic regional operations workflow.
Assumptions: Baseline and target came from the business-case draft and require owner confirmation before use in formal reporting.
Evidence gaps: No post-launch actual is available yet; source-system report definition is still provisional.
Decisions needed: Confirm measure owner, reporting source, and first review period.
Risks, dependencies, or actions: Adoption and training completion may affect realization; do not treat workflow launch as realized value.
Value gate summary: Benefit classes: cycle time and customer experience; ROI eligible: No unless converted to validated financial impact; Baseline availability: provisional; Cost of doing nothing: continued slow onboarding and avoidable customer friction; Confidence: Medium; Finance-validation status: Not required unless converted to financial benefit.
Measurement contract, if value is claimed: Expected outcome: shorter customer onboarding cycle time; Benefit type: cycle time and customer experience; Metric: average business days from completed intake to onboarding complete; Baseline: 18 business days, provisional; Target: 10 business days, provisional; Actual, if available: missing; Measurement period: first full month after launch and monthly for first quarter; Source: onboarding operations report, provisional; Measure owner: operations process owner, requires confirmation; Review cadence: monthly for first quarter, then quarterly if stable; Validation need: sponsor confirms metric definition and operations owner confirms source; Confidence: Medium; Realization risk: Medium; Finance-sensitive flag: No unless converted to cost or revenue impact; Downstream route: Value Realization Governance Ledger.
Do not pass downstream: Unsupported savings, finance ROI, or detailed private customer data.
Suggested first prompt: "Create a value-realization ledger row from this business-case handoff. Keep baseline and target provisional until the measure owner confirms them, and do not treat launch completion as value realization."
