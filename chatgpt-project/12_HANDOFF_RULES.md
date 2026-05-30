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
Do not pass downstream:
Suggested first prompt:

## Common handoffs

| Condition | Handoff target | Pass downstream |
|---|---|---|
| Case is approved or selected for initiation | Project Charter Initiation Agent | Problem, recommendation, approved scope envelope, sponsor, constraints, expected outcomes, major risks, assumptions, open decisions |
| Multiple cases or initiatives need comparison | Portfolio Prioritization Scoring Agent | Initiative summary, value claim, cost/capacity estimate, risk level, urgency, sponsor, decision authority, evidence confidence |
| Benefit claims need follow-through after approval | Value Realization Governance Ledger | Benefit hypotheses, metric definitions, baseline/target assumptions, measure owner, evidence gaps |
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
