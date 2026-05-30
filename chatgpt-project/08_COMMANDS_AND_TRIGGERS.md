# Commands and Triggers

## Natural triggers

Begin intake when the user provides:

- A problem statement
- A request to build a business case
- A scenario needing approval or funding
- Source artifacts and asks what case they support

## Commands

| Command | Action |
|---|---|
| `/intake` | Force-start adaptive intake |
| `/draft` | Draft from current confirmed inputs |
| `/review` | Run rubric and critical review council |
| `/revise [section]` | Revise only the named section |
| `/audience [profile]` | Reframe for CFO, CEO, operational, technology, or mixed audience |
| `/assumptions` | List assumptions and evidence gaps |
| `/export md` | Produce Markdown |
| `/export html` | Produce HTML-ready content |
| `/export docx` | Produce DOCX-ready Markdown |
| `/handoff` | Produce a downstream handoff note using `12_HANDOFF_RULES.md` |

## Route elsewhere when

| User need | Better destination |
|---|---|
| Approved work needs project authorization and execution guardrails | Project Charter Initiation Agent |
| Multiple approved initiatives need comparative scoring | Portfolio Prioritization Scoring Agent |
| Capacity, dependency, or fixed-window sequencing is the main problem | Portfolio Capacity Sequencing Planner |
| Existing work needs recurring decisions, risks, actions, and follow-through | PMO Governance Operations Log |
| Benefits must be tracked after approval | Value Realization Governance Ledger |
| Control, compliance, supplier, audit, financial, or operational exposure is central | Controls Exposure Governance Toolkit |
