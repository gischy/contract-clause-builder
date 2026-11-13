# Changelog

All notable changes to this project (paper, clause library, and the
`contract-clause-builder` skill) are recorded here, newest first.

## 2026-11-13 (later)

### DOCX export layout fixed

- The DOCX template relied on python-docx's built-in defaults (1in/2.54cm
  margins, 0.5in header distance, inherited paragraph spacing), which read
  as cramped once a logo sat in the header next to the yellow rule.
  Set explicit, consistent values: 2.5cm margins all around, 1.25cm header/
  footer distance, explicit heading/paragraph spacing (space before/after),
  and a symmetric 1cm left/right indent with spacing on clause quote blocks
  (previously left-indent only, no right indent or spacing).
- Rebuilt `contract-clause-builder.zip`.

## 2026-11-13

### Whole clause set confirmed approved; disclosure-date dead end fixed

- At the user's explicit direction, the clause library's "DRAFT / pending
  firm approval" status is removed: all 11 previously-DRAFT clauses
  (LIM-NONE, LIM-SCOPE-TITLE, LIM-TIME-TITLE, LIM-CAP-PCT,
  LIM-CAP-PCT-TITLE, LIM-CAP-FIXED-TITLE, LIM-CAP-SPECIFIC-TITLE, DEMIN,
  BASKET-EXCESS, DISCL-DATAROOM, LIM-BUYER-SOPHISTICATED) are now labeled
  **APPROVED (confirmed 2026-11-12)**. Updated `clauses.md`, `SKILL.md`,
  `README.md`, and the clause-library spreadsheet's Status column (all 19
  rows, "To do" → "Done — approved by firm 2026-11-12").
  **Important for the paper:** this is a simplifying assumption adopted for
  the deployment-verdict exercise, not a record of an actual firm legal
  review having taken place. Updated the two paper passages (Appendix C)
  that stated DRAFT status as fact; flagged and fixed the
  `validity-evaluation/results.md` deployment verdict, which cited
  unapproved DRAFT wording as a reason for lawyer oversight (no longer
  applies; down to two reasons).
- Dead-end audit (requested): found and fixed one unintended dead end — the
  mandatory disclosure-date input blocked *every* normal Position 2/3/4
  draft outright, not just edge cases, even though in practice this date is
  often still being negotiated when the section is first drafted. Reverted
  to: ask for it, but if unknown, leave `[DISCLOSURE DATE]` open and
  flagged rather than refusing to draft — consistent with how every other
  not-yet-known figure is handled. All other "stop" paths audited and
  confirmed as deliberate, genuine scope exclusions (escrow, W&I insurance,
  separate reps/indemnity caps, buyer-side thresholds, no-indemnity-schedule
  deals), not bugs.
- Rebuilt `contract-clause-builder.zip`.
- **Still open, explicitly deferred to a follow-up**: giving every
  remaining refusal case (escrow, W&I, separate caps, buyer-side
  thresholds, etc.) a fallback drafted clause instead of stopping. This
  would mean inventing new clause content for scenarios the firm has no
  real position on — scoped as a distinct task, not done in this entry.
- Not yet re-tested against the validity-evaluation set.

## 2026-11-12 (yet later still)

### HHL-branded export template + PPTX support

- Bundled the HHL logo (`assets/hhl_logo.png`) into the skill package so
  export works standalone, without depending on the hhl-branding skill or
  any machine-specific path.
- `scripts/export.py` rewritten: now supports `.pptx` in addition to
  `.docx`/`.pdf`, and applies a minimalistic HHL-branded template to all
  three — logo, a single yellow (#FAAA00) accent (a rule under the DOCX
  title block, a thin frame on PPTX slides), Verdana (the official
  Office-theme fallback font, chosen over the corporate Gotham font for
  portability to machines that don't have it installed).
- PPTX export splits one slide per sub-clause (splitting on `###`, not the
  section's single top-level heading), with a title slide carrying the
  overall section heading.
- Updated `SKILL.md` Step 5 to offer the PowerPoint option too.
- Rebuilt `contract-clause-builder.zip`.
- Carried forward an unrelated `reference/rules.md` refinement (made
  directly by Felix/Nikita, not by me): comparing a fixed-amount specific
  cap against a percentage-based general cap now explicitly requires
  asking for the Purchase Price first, rather than silently assuming a
  unit of account.
- Not yet re-tested against the validity-evaluation set.

## 2026-11-12 (yet later)

- Fixed: the skill was mirroring the user's language (observed: it asked
  the first question in German because the user wrote in German). Added an
  explicit instruction to conduct the whole interaction in English by
  default, departing only if the user explicitly asks for another
  language — consistent with the clause library itself only existing in
  English. Rebuilt `contract-clause-builder.zip`.

## 2026-11-12 (still later)

### Position 1 now produces a confirmatory clause (LIM-NONE)

- Position 1 (buyer side, non-professional seller) previously produced no
  output at all. User feedback from a live run: this read as the skill
  "stopping" rather than completing. Added `LIM-NONE` (DRAFT, new — not yet
  firm-reviewed): a single clause confirming the Seller's liability is not
  limited. The firm's substantive position is unchanged; this only makes it
  visible in the document instead of omitting Section 10 silently.
  Consistency rule 11 ensures LIM-NONE is the *only* clause Position 1
  produces — explicitly considered and rejected: actually capping
  non-professional sellers' liability, which would reverse a real,
  documented firm position (see the alternative recorded in this entry's
  discussion, not implemented).
- Updated `SKILL.md` Steps 1-5 and `reference/rules.md` accordingly.
- Rebuilt `contract-clause-builder.zip`.
- **Paper + validity evaluation now inconsistent with this change** — paper
  §5.1 and Table 3/4 still describe Position 1 as producing "no limitation
  section at all," and T01/T02/T12/E11 in the validity evaluation currently
  score "no section produced" as the passing answer. Both need updating
  before submission; not yet done.

## 2026-11-12 (even later)

### Wizard-flow fix and export feature

- Fixed: `SKILL.md` Step 1 said "ask for these as a short numbered list,"
  which a live run (reported by the user) followed literally — asking side
  and seller type as one combined question instead of two. Rewrote Step 1
  to require one question at a time, never combined, with lettered options
  offered for fixed-choice inputs. The Position 1 output itself (no section,
  reason given) was confirmed correct in that same run.
- Added `scripts/export.py`: converts the assembled section to `.docx`
  (always available, python-docx) or `.pdf` (needs LibreOffice/`soffice` on
  PATH; fails with a clear message, not a crash or silent fallback, if it
  isn't available). Added Step 5 to `SKILL.md` offering this export once,
  after delivering the drafted section.
- Rebuilt `contract-clause-builder.zip`.

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
