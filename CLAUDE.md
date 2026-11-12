# Project context

EMBA assignment ("Change Management and AI", HHL) on AI's impact on jobs.
Level chosen: discipline/individual — the first-draft process for SPA
limitation-of-liability clauses in an M&A law practice. Authors: Nikita
Butenko and Felix Kirchgeorg (joint submission, cleared with the professor).
Deadline: 2026-11-15.

## Structure

- `HHL_AI_SPA_Paper_v6.docx` — the paper. Components A (baseline), B
  (mechanisms) and E (change management) are complete. Component C
  (quantitative model) has correct logic but placeholder numbers. Component D
  (validity evaluation, Ch.5 + Appendix B) is the main open item: no test
  cases have been run yet.
- `contract-clause-builder/` — the Claude skill prototype (component D). See
  its `README.md` and `SKILL.md`.
- `SPA_Clause_Library_EN_review.xlsx` — tracks firm approval of the English
  clause wording per clause; every row is currently "To do".

## Outstanding work (as of 2026-11-12)

1. Build the quantitative-model spreadsheet (Appendix A) with live formulas,
   scenarios (conservative/central/aggressive) and sensitivity analysis.
2. Run ~20-24 test cases against the skill (normal + deliberately unsupported
   edge cases), score against the rule-table ground truth, and fill in the
   real numbers in paper Table 5/9 and Appendix B (currently "XX%" / "[ ]"
   placeholders) — deferred until the skill review/rename below was finished.
3. Fill Appendix D (AI-use disclosure) with the actual tools/versions used.
4. Confirm review-time / input-prep-time measurement approach (real timed
   trial vs. expert estimate) before building model inputs on top of it.

## Skill naming and design, already resolved

- Skill renamed from `spa-limitations` to `contract-clause-builder`
  (directory + SKILL.md `name:` + paper Appendix C references updated).
- Fixed: SKILL.md Step 3 sub-heading 8 was mislabeled "Limitation of the
  Parties' liability" — corrected to "Exclusion of lost profit" (the clause
  it actually covers, LIM-NOLP).
- Fixed: paper Appendix C wrongly called `clauses.md` "Russian-language" —
  it's the English rendering; corrected.
- Decision: everything stays in English (no Russian-language text added
  anywhere in the clause library, skill, or paper).
- Still open, not yet resolved: the clause-review spreadsheet flags a
  conflict between `LIM-SCOPE-TITLE` and `LIM-NODOUBLE` for position 4
  (title-only warranty deals may have no indemnity schedule at all, but
  `LIM-NODOUBLE` assumes one exists). See the xlsx `Instructions` sheet,
  "Open question for the reviewing lawyer".

## Working notes

- The working directory is on OneDrive sync; a hidden
  `.{GUID}` file at the root is a sync placeholder, not project content.
- `SPA_Clause_Library_EN_review.xlsx` is frequently open in Excel (file lock)
  — copy it elsewhere before reading with openpyxl/markitdown if locked.
