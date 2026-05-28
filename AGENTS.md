# Business Case System — Repository Agent Instructions

You are helping maintain a public-safe GitHub portfolio project called Business Case System.

## Role

Preserve this project as a structured, AI-assisted business case development system. It must help a human create better decision documents without pretending to make funding, governance, or executive decisions autonomously.

## Repository shape

Keep two layers distinct:

1. GitHub layer: README, examples, workflow diagrams, templates, local tooling, quality review, and public explanation.
2. ChatGPT Project runtime: the flat `chatgpt-project/` folder. This folder is the uploadable product.

Do not make users guess which files belong in ChatGPT. Runtime files must stay flat and self-contained.

## Boundaries

- Do not invent financial facts, stakeholder approvals, evidence sources, or ROI.
- State assumptions when evidence is missing.
- Preserve human accountability for decisions and final review.
- Do not duplicate the same operating logic across folders unless the second copy has a clearly distinct purpose.
- Keep root instructions compact. Put detailed workflow logic inside `chatgpt-project/`.

## Output expectations

Use plain enterprise prose. Avoid buzzwords. Favor decision clarity, scope control, financial discipline, risk honesty, and audience-aware review.
