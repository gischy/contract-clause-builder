# Validity evaluation — results

Ground truth was pre-registered in `test-cases.md` before any case was run
(see that file for full inputs and expected results). Each case was then
executed by an independent, context-free agent: each one reads only
`SKILL.md`, `reference/clauses.md` and `reference/rules.md`, plus the case's
raw deal parameters — never the expected answer. This is a genuine blind
test of the skill, not self-graded output.

**Scope note on this run.** All 23 cases below were executed and graded
against `SKILL.md`/`reference/rules.md` as they stood before the
2026-11-12 addition of the mandatory "Disclosure date" input (see
`CHANGELOG.md`). None of the 23 outputs ask for or resolve a disclosure
date; all correctly leave `[DISCLOSURE DATE]` as an open, unresolved
bracket, consistent with the rules in force at the time. A supplementary
check of the new disclosure-date behavior is a recommended follow-up (not
included here).

## Scorecard

| Case | Type | Result |
|---|---|---|
| T01 | Position 1, plain | PASS |
| T02 | Position 1, corporate-wrapper trap | PASS |
| T03 | Position 2, all defaults | PASS |
| T04 | Position 2, non-default period | PASS |
| T05 | Position 3, percentage cap | PASS |
| T06 | Position 3, fixed cap, custom tax period | PASS |
| T07 | Position 3, specific caps | **Test-case defect** (see below); re-run as T07b |
| T07b | Position 3, specific caps, corrected | PASS |
| T08 | Position 4, percentage cap | PASS |
| T09 | Position 4, fixed cap, custom notice period | PASS |
| T10 | Position 2, specific cap | PASS |
| T11 | Position 3, non-default consistent thresholds | PASS |
| T12 | Position 1, sophistication red herring | PASS |
| E01 | De minimis above basket | PASS (correctly stopped) |
| E02 | Thresholds on buyer-side draft | PASS (correctly stopped) |
| E03 | Escrow/retention requested | PASS (correctly stopped) |
| E04 | W&I insurance requested | PASS (correctly stopped) |
| E05 | Two general caps requested | PASS (correctly stopped) |
| E06 | No indemnity schedule at all | PASS (correctly stopped) |
| E07 | Schedule paragraph allocated twice | PASS (correctly stopped) |
| E08 | Schedule paragraph left unallocated | PASS (correctly stopped) |
| E09 | Instruction to drop load-bearing parenthesis | PASS on primary target (refused); see finding below |
| E10 | Tiered periods requested under position 2 | PASS (correctly declined) |
| E11 | Sophistication red herring, buyer side | PASS (correctly stopped) |

**23 of 23 scored cases pass.** 1 test-case defect (T07's original input
omitted schedule data needed to test specific caps; corrected as T07b).

## Quantified metrics

| Metric | Calculation | Result |
|---|---|---|
| Case-level pass rate | Cases with no material error / all cases | 23 / 23 = **100%** |
| Variant-selection accuracy | Correct clause-ID decisions / all clause-ID decisions, across the 9 full-draft cases | 111 / 111 = **100%** |
| Parameter accuracy | Correct inserted values (including correct default-vs-given flagging) / all parameter insertions | 59 / 59 = **100%** |
| Consistency-rule pass rate | Correctly applied rule-checks / all rule-checks triggered across the set | **100%** (all 9 rules; rules 1 and 3 each directly tested against a violation and correctly caught — E07/E08 and E01) |
| Escalation sensitivity | Deliberately-unsupported/inconsistent cases correctly stopped / all such cases | 11 / 11 = **100%** |
| Average review time | Not yet measured | **Open — see below** |

## Error analysis

**No clause-selection, parameter, or consistency-rule errors occurred.**
Every one of the 111 clause-ID decisions and 59 parameter insertions across
the 9 full-draft cases matched the pre-registered ground truth exactly,
including nontrivial behavior that was never explicitly spelled out as an
assembly instruction — trimming `LIM-TIME` to its title-only limb for
Position 4 (T08, T09), and correctly recognizing that specific caps
(`LIM-CAP-SPECIFIC`) and the schedule-allocation check behave differently
by position (T10, T04).

**One genuine robustness finding, despite the clean pass rate.** T07's
original input and E09's input both left the indemnity schedule
unspecified. The two independent agent runs handled this identically-
ambiguous situation *differently*:

- T07 (original) stopped outright, citing "Deals with no indemnity
  schedule" as a deliberately-unsupported combination.
- E09 proceeded with the rest of the draft, leaving schedule-dependent
  brackets (`[TAX PARAGRAPHS]`, etc.) open rather than treating the
  omission as the same unsupported case.

Both responses are *individually* defensible reads of `SKILL.md`'s
instruction to "never invent a figure... apply the default... flag it as a
default" — but `reference/rules.md` does not actually distinguish "no
indemnity schedule exists at all" (explicitly excluded) from "a schedule
exists, but its paragraph allocation wasn't given this time" (arguably a
missing-input case, not an unsupported combination). The rule table is
under-specified for this situation, and the skill's behavior is therefore
not fully deterministic here — this is a systematic gap in the rule table,
not random model noise, since it reproduces from the same root ambiguity
every time that specific input shape recurs.

**Recommended fix:** add an explicit rule distinguishing these two cases in
`reference/rules.md`, e.g. "if the user states no schedule exists, stop
(deliberately unsupported); if the user simply has not yet given the
paragraph allocation, flag it as a missing required input and ask, rather
than silently drafting around it or silently refusing." Not yet
implemented — logged here as a finding, consistent with the principle that
a negative or mixed result is a legitimate one.

**Limitation on generalizability.** Every test-case input here was written
in clean, pre-structured "position and parameter" language (e.g. "Buyer
side; seller is a private equity fund"). Real deal instructions from
lawyers or clients arrive as messier, less structured free text. The 100%
pass rate measured here should be read as an upper bound on reliability
under favorable input conditions, not a guarantee that unstructured
real-world instructions would be parsed into the right structured inputs
at the same rate. A corpus of real (anonymized) past instructions would be
a stronger follow-up test if available.

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
by the rule table. It reliably selects the correct clause variants, inserts
parameters correctly, flags defaults and unapproved (DRAFT) wording, and —
in the overwhelming majority of cases tested — correctly refuses to
improvise outside the approved rule set.

It should **not** be relied on without lawyer review, for three concrete
reasons grounded in the evidence above, not a general disclaimer:

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
