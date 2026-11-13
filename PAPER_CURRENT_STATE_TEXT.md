# Current-state replacement text for the paper

Use this text only after checking that it matches the final frozen package. It
is deliberately conservative: it does not convert unfinished re-testing or
unmeasured timing into positive findings.

## Replacement for Chapter 5.3 pending final re-test

### Current evidentiary status and deployment verdict

The historical evaluation results are not treated as validity evidence for the
current version of the prototype. Since the earlier evaluation wave, the rule
set and clause library have changed materially: Position 1 now produces a
confirmatory LIM-NONE clause; Position 4 is schedule-free and uses dedicated
title-only cap variants; buyer type determines whether a separate reliance
acknowledgment is included; and the skill now checks mixed-unit cap comparisons
using the Purchase Price. Each change affects the expected clause set, required
inputs or both. Applying earlier scores to the revised system would therefore
overstate what has been demonstrated.

Before submission, the frozen version of the skill must be evaluated against
the replacement protocol in Appendix B. The protocol contains 24 normal,
missing-input, inconsistent and deliberately unsupported cases. It tests every
current transaction position and every new decision path, including schedule-
free Position 4, buyer-type selection, Position 1's single-clause output and
mixed percentage/fixed-amount cap comparisons. For each case, the evaluation
will retain the verbatim input and output, expected and actual clause IDs,
parameter and dependency checks, escalation outcome, reviewer identity and
error classification. Reported rates will show their denominators and failed
cases will remain in the appendix.

Until this evaluation has been completed, the appropriate deployment verdict
is limited to prototype development and supervised demonstration. The system is
not validated for operational use on the current rule set. This is not a claim
that the revised logic is incorrect; it is a methodological conclusion that a
materially changed system requires fresh evidence before its reliability can be
asserted.

## Replacement for Table 5 pending final re-test

| Metric | Calculation | Current-version result |
|---|---|---|
| Variant-selection accuracy | Correct clause-ID decisions / all clause-ID decisions | Pending re-test of frozen package |
| Parameter accuracy | Correct inserted values / all parameter insertions | Pending re-test of frozen package |
| Consistency-rule correctness | Correctly applied rule checks / all triggered rule checks | Pending re-test of frozen package |
| Escalation correctness | Correctly stopped or requested input / all applicable cases | Pending re-test of frozen package |
| Case-level pass rate | Cases with no material error / all evaluated cases | Pending re-test of frozen package |
| Average lawyer review time | Mean minutes across complete generated outputs | Pending timed human review |

## Replacement for the quantitative-model caveat

The prototype's potential productivity effect cannot yet be stated as a
measured result. The model retains the baseline estimate of two current lawyer
hours for the in-scope task, but net saving depends on input preparation,
lawyer review and correction, exception handling and adoption. These inputs
will be measured through a documented timed review protocol or, where direct
measurement is infeasible, reported as explicitly labelled expert estimates.
The final model will present conservative, central and aggressive scenarios and
a sensitivity analysis rather than a single point estimate.

## Appendix-B lead-in

Appendix B reports the validity evaluation of the frozen current skill package.
The ground truth was versioned before execution and derived from the then-current
`SKILL.md`, `reference/rules.md` and `reference/clauses.md`. Historical results
from superseded versions are retained in the repository as an audit trail but
are not included in the final denominators. The complete protocol, raw outputs,
scoring decisions and error analysis are supplied with the submission.
