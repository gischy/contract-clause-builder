# Assignment revision log

## Submission-critical work remaining

This log distinguishes completed artefact changes from empirical work that
must be performed and documented before the paper can make a final claim.

### 1. Freeze and validate the skill

- Freeze the skill package, including the new Position 1 LIM-NONE behavior,
  Position 4's schedule-free design, buyer-type logic and export feature.
- Create a replacement, versioned ground-truth test set after the freeze.
- Re-run at least 20 cases against the frozen package, including normal,
  missing-input and deliberately unsupported cases.
- Record the exact model/environment, date, raw output, independent reviewer,
  pass/fail decision and error class for every case.
- Report accuracy, parameter correctness, consistency-rule correctness,
  escalation correctness and case-level pass rate using the final denominator.

### 2. Complete the quantitative model

The assignment requires a reproducible, parameterized, scenario-based model
with sensitivity analysis. Do not substitute assumed measurements for observed
ones.

- Measure input-preparation and lawyer review/correction time using a defined
  protocol, or disclose a clearly labelled expert-estimate method.
- Build conservative, central and aggressive scenarios using explicit adoption,
  input-preparation, review/correction and exception-rate assumptions.
- Report net time saved per transaction, annual hours released and the
  sensitivity of results to the principal assumptions.
- Attach the native spreadsheet or code and its output tables/charts.

### 3. Reconcile the paper before export

- Replace all historic 23/23 and 24/24 claims with the final re-test results.
- Update the Position 1 and Position 4 descriptions, Table 4, Table 5,
  Appendix B, Appendix C and the deployment verdict to the frozen skill.
- State that the library contains 25 clause variants and 11 consistency rules,
  if those remain the final counts at freeze.
- Replace every `[ ]`, `[timed test]`, `XX%` and model/version placeholder.
- Complete Appendix D with the actual AI systems, model/version, purpose and
  human verification performed.
- Update Word fields, citations, page numbers and the table of contents; then
  export and inspect the submission PDF.
