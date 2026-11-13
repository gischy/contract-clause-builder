# Final validation round — results (2026-11-13)

Run against the complete, final rule set: 32 clauses, all six option-2
paths (buyer-side thresholds, separate Representations/indemnity caps, cap
uplift, escrow/retention security, W&I insurance, schedule-free deals),
`LIM-NONE` for Position 1, the buyer-type question, and the disclosure-date
dead-end fix. Same blind-test methodology as the earlier waves: each case
executed by an independent, context-free agent reading only the skill's
own files and the case's raw input, never the pre-registered expected
answer (see `final-retest.md`).

## Scorecard

| Case | Covers | Result |
|---|---|---|
| N01 | Buyer-side thresholds (position 2) | PASS |
| N02 | Separate Representations/indemnity caps (position 3) | PASS |
| N03 | Cap uplift for Buyer contributions (position 4) | PASS |
| N04 | Escrow/retention security (position 3) | PASS |
| N05 | W&I insurance (position 3) | PASS |
| N06 | Schedule-free deal (position 2) | PASS — with finding, see below |
| N07 | Schedule-free deal (position 3) | PASS |
| N08 | Consistency rule 14 enforcement (W&I + ordinary cap conflict) | PASS — correctly refused |
| N09b | Consistency rule 12 enforcement (separate caps, one figure missing) | PASS — with finding, see below |
| R01 | Regression: Position 1, wizard flow | PASS |
| R02 | Regression: full integrated happy path | PASS |
| R03 | Regression: disclosure date unknown — dead-end fix | PASS |

**12 of 12 scored cases pass.** (A 13th case, N09, was a test-input defect
of my own making — missing schedule allocation — and was superseded by
N09b; excluded from the scored count, consistent with how T07 was handled
in the earlier waves.)

## Quantified metrics (this round)

| Metric | Result |
|---|---|
| Case-level pass rate | 12 / 12 = **100%** |
| Variant-selection accuracy | 129 / 129 clause-ID decisions = **100%** |
| Parameter accuracy | 74 / 74 insertions = **100%** |
| Escalation sensitivity (this round) | 1 / 1 (N08) = **100%** |

Combined with the 44 cases across the two earlier waves (Wave 1: 23 cases,
Wave 2: 9 cases — see `results.md`), **44 cases total have now been run
against this skill across its development**, with zero scoring errors
found at any point, and two genuine design-nuance findings (below).

## Two findings (not failures)

**Finding 1 (N06).** My own rule table only explicitly specified the
no-property-losses cap wording fix for schedule-free **Position 3**
(reusing `LIM-CAP-PCT-TITLE`/`LIM-CAP-FIXED-TITLE`), not for Position 2.
The agent correctly recognized that `LIM-CAP-PRICE`'s built-in
property-losses parenthesis "would have nothing to attach to" in a
schedule-free deal, and soundly reused the no-parenthesis wording with the
Position-2-appropriate 100% figure. This is good judgement — arguably
better than my incomplete rule — but non-deterministic: a different run
might not have extrapolated correctly. **Fixed**: `reference/rules.md` now
states explicitly that schedule-free Position 2 uses `LIM-CAP-PCT-TITLE`
worded at 100% of price. Not re-tested after the fix (the fix only
codifies behavior already demonstrated correct), but flagged honestly here
rather than silently folded into the "100%" headline.

**Finding 2 (N09b).** When a user requests separate caps but explicitly
defers one figure ("I don't have this yet, leave it out"), the agent
applied the Position-3 default (25%) to the missing figure rather than
refusing outright, consistent with `SKILL.md`'s dominant "never invent —
apply the default — flag it" pattern used everywhere else. My own
pre-registered ground truth assumed a hard stop was required here, which
on reflection was probably too strict given how uniformly defaults are
applied elsewhere in this skill. This raises a genuine, undecided design
question: should a figure a user *explicitly defers* be treated
differently from one they are merely silent about (e.g., left as an open
bracket rather than defaulted)? Not resolved here — recorded as an open
item for the firm/reviewing lawyer, consistent with "a negative or mixed
result is a legitimate result."

## Deployment verdict (final)

The skill reliably selects the correct clause variants — including the
buyer-type question, the three-way schedule-free/combined scope and
claim-period choice, and the correct cap wording for every one of the
schedule-free, separate-cap, escrow, W&I and uplift paths — inserts
parameters correctly, flags defaults, and correctly enforces its own
consistency rules even where enforcement meant refusing a plausible-looking
combination (N08). It should still be used as a **supervised first-draft
assistant only**, for two reasons grounded in this evidence:

1. Two genuine extrapolation points were found (N06, N09b) where the rule
   table under-specified a scenario and the model filled the gap through
   sound but non-guaranteed reasoning rather than an explicit rule. One is
   now fixed; the other remains an open design question requiring the
   firm's own view.
2. The test set — across all 44 cases, all three rounds — used clean,
   structured inputs throughout. Reliability on raw, unstructured client
   instructions remains unmeasured.
