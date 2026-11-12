# Changelog

All notable changes to this project (paper, clause library, and the
`contract-clause-builder` skill) are recorded here, newest first.

## 2026-11-12 (later)

### Buyer-type question added (new feature, not yet re-tested)

- Added a new Step 1 input, asked on every position that produces a section
  (2, 3, 4) regardless of which side is acting: is the Buyer professional/
  institutional, or an individual/private buyer? Independent of the
  Position table — does not change which position applies.
- Added `LIM-BUYER-SOPHISTICATED` (DRAFT, market-derived, not firm-sourced):
  a standard non-reliance/sophisticated-investor acknowledgment, included
  only when the Buyer is professional/institutional.
- Added consistency rule 10 (LIM-BUYER-SOPHISTICATED appears iff Buyer is
  professional/institutional) and a new Step 3 sub-heading.
- Rebuilt `contract-clause-builder.zip`.
- **Not yet re-tested.** The 24-case validity evaluation does not cover this
  new input at all; a further re-test is needed before any pass-rate claim
  in the paper can be considered to include it.

## 2026-11-12

### Skill rename and fixes

- Renamed the skill from `spa-limitations` to `contract-clause-builder`
  (directory `contract-skill/` → `contract-clause-builder/`, `SKILL.md`
  `name:` field, and the paper's Appendix C package-name reference).
- Fixed: `SKILL.md` Step 3's sub-heading 8 was mislabeled "Limitation of the
  Parties' liability" — it actually covers `LIM-NOLP`, "Exclusion of lost
  profit." Corrected.
- Fixed: `reference/clauses.md`'s dependency note for `LIM-COND` omitted the
  position-2 alternative (`LIM-TIME-FLAT`); `reference/rules.md` already had
  it correctly. Aligned both.
- Fixed: the paper's Appendix C wrongly described `reference/clauses.md` as
  containing "Russian-language" clause variants. It is the English
  rendering of the firm's Russian-law originals (pending approval).
  Corrected, consistent with the decision to keep the whole project in
  English.

### Design question resolved

- The clause-library spreadsheet (`SPA_Clause_Library_EN_review.xlsx`)
  flagged an open question: does a title-only warranty deal (Position 4)
  have an indemnity schedule at all, given `LIM-NODOUBLE` assumes one
  exists? Resolved per firm practice: yes, Position 4 always has a schedule
  (title tier only). Documented in `reference/rules.md` ("Indemnity
  schedule allocation") and in the spreadsheet itself (Instructions sheet
  and the `LIM-NODOUBLE` row's comment column).

### Repository and documentation

- Added `README.md` (project root and `contract-clause-builder/`),
  `CLAUDE.md` (project context and outstanding-work tracker), and
  `.gitignore`.
- Initialized git, pushed to
  [github.com/gischy/contract-clause-builder](https://github.com/gischy/contract-clause-builder)
  (public repository; confirmed acceptable given the clause library is a
  demonstration/pending-approval rendering with no client or counterparty
  names).
- Repository link added to the paper's Appendix C.

### Validity evaluation

- Pre-registered a 23-case test set with ground truth
  (`validity-evaluation/test-cases.md`), written before any case was run
  against the skill — 12 normal cases (all four positions, a mix of default
  and non-default parameters) and 11 deliberately unsupported or
  inconsistent cases.
- Ran all 23 cases through independent, context-free agents (each reads
  only the skill's own files and the case's raw input — no visibility into
  the pre-registered expected answer), to get a genuine blind test rather
  than self-graded output.
- Found and corrected a defect in test case T07's own input (it omitted the
  indemnity-schedule paragraph allocation needed to test specific-cap
  handling); re-run as T07b with a complete schedule.
- Result: 23 of 23 scored cases pass. 100% case-level pass rate, 100%
  variant-selection accuracy (111/111 clause-ID decisions), 100% parameter
  accuracy (59/59 insertions), 100% escalation sensitivity (11/11
  deliberately-unsupported cases correctly stopped). One genuine robustness
  finding despite the clean pass rate: inconsistent handling of an
  unspecified indemnity schedule across two otherwise-passing runs (T07
  original vs. E09) — a real gap in `reference/rules.md`, not random noise.
  Average review time not yet measured (needs a human timed trial or a
  labeled expert estimate).
- See `validity-evaluation/results.md` for the full scorecard, metrics and
  error analysis.

### Known in-flight change

- `SKILL.md` and `reference/rules.md` were updated (by a collaborator,
  concurrently with the validity evaluation above) to add a mandatory
  "Disclosure date" input: Step 1 now asks for it on every position that
  produces a limitation section, with no default — the `[DISCLOSURE DATE]`
  placeholder may no longer be left unresolved. All 23 test-set results in
  `validity-evaluation/results.md` were run and graded against the rules as
  they stood *before* this change (none of the graded outputs ask for or
  resolve a disclosure date). A supplementary check of the new
  disclosure-date behavior is a recommended follow-up, not yet done.
