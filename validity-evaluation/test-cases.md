# Validity evaluation — test set and ground truth

Written before the skill was run on any of these cases. Ground truth is
derived mechanically from `reference/rules.md`; no case here was shown to the
agent that executes the skill.

23 cases: 12 normal (T-series, covering all four positions and a range of
default/non-default parameters) and 11 deliberately unsupported or
inconsistent cases (E-series, testing escalation and refusal behavior).

**Revision note (2026-11-12, second pass).** `reference/clauses.md` and
`reference/rules.md` were restructured mid-evaluation: the single `LIM-TIME`
clause was split into three position-specific variants — `LIM-TIME`
(position 3, where title claims extend to other assets besides the Sale
Shares), `LIM-TIME-SHARES` (position 3, no other title assets), and
`LIM-TIME-TITLE` (position 4). T05, T06, T07b, T08, T09, T11, E07 and E08
originally tested the old single-clause behavior and were revised below to
specify the now-required "other title assets?" input and updated expected
clause IDs. A new case, T13, was added to cover the plain `LIM-TIME` variant
(with other title assets), which none of the original 23 cases exercised.

---

## T01 — Position 1, plain case

**Input:** Buyer side; seller is an individual founder, no other context.

**Expected:** Position 1. No limitation section at all. State the reason
(firm does not limit a non-professional seller's liability on a buyer-side
draft) and stop.

## T02 — Position 1, corporate wrapper trap

**Input:** Buyer side; seller is a holding company 100% owned and controlled
by one individual, formed to hold the shares being sold, no history of other
transactions.

**Expected:** Position 1 still applies — the position-2 trigger is "fund,
strategic or institutional," not mere incorporation. No limitation section.

## T03 — Position 2, all defaults

**Input:** Buyer side; seller is a private equity fund. No other parameters
specified.

**Expected:** Position 2. Clauses: LIM-SCOPE, LIM-TIME-FLAT (5 years,
flagged as default), LIM-TPC-NOTICE (10 Business Days, default),
LIM-TPC-CONDUCT, LIM-COND (60 calendar days, default), LIM-CAP-PRICE (100% of
price actually received), DISCL-DATAROOM, LIM-NODOUBLE, LIM-MITIG, LIM-NOLP.
No LIM-MITIG-B (seller-side only). No thresholds.

## T04 — Position 2, non-default period

**Input:** Buyer side; seller is a strategic trade buyer divesting a
non-core unit; claim period requested at 3 years instead of the default.

**Expected:** Same clause set as T03, but LIM-TIME-FLAT period = 3 years, not
flagged as a default (explicitly given).

## T05 — Position 3, percentage cap, all defaults except cap

**Input:** Seller side; full warranty package; cap = 20% of price
(non-default); periods and thresholds not specified; no other title assets
besides the Sale Shares; indemnity schedule has 10 paragraphs: 1–3 tax,
4–6 title, 7–10 other (fully allocated).

**Expected:** Position 3. LIM-SCOPE, LIM-TIME-SHARES (no other title assets
→ this variant, not plain LIM-TIME) (tax 3y / title 3y / other 1y, all
default, paragraphs 1–3 / 4–6 / 7–10), LIM-TPC-NOTICE (10 BD, default),
LIM-TPC-CONDUCT, LIM-COND (60 cd, default), LIM-CAP-PCT (20%, not default),
DEMIN (0.1%, default), BASKET-EXCESS (1%, default, excess type),
DISCL-DATAROOM, LIM-NODOUBLE, LIM-MITIG, LIM-MITIG-B, LIM-NOLP.

## T06 — Position 3, fixed-sum cap, custom tax period

**Input:** Seller side; full warranty; fixed-sum cap EUR 5,000,000 (not
percentage); tax claim period set to 2 years (title and other left at
default); no other title assets besides the Sale Shares; schedule has
8 paragraphs: 1–2 tax, 3–5 title, 6–8 other.

**Expected:** LIM-CAP-FIXED (EUR 5,000,000) instead of LIM-CAP-PCT;
LIM-TIME-SHARES (no other title assets) tax period = 2 years (not default,
flagged as given), title 3y (default), other 1y (default); otherwise as
T05's pattern minus LIM-CAP-PCT.

## T07b — Position 3, two specific caps (corrected; original T07 omitted the
indemnity schedule, a test-case defect, logged in results.md)

**Input:** Seller side; full warranty; cap not specified (default 25%);
price = EUR 10,000,000; no other title assets besides the Sale Shares;
schedule has 9 paragraphs: 1–3 tax, 4–6 title, 7–9 other; two specific
caps: (a) breach of tax representations capped at EUR 1,000,000, counts
toward the general cap; (b) breach of an environmental representation
capped at EUR 300,000, sits outside (in addition to) the general cap.

**Expected:** LIM-TIME-SHARES (no other title assets), LIM-CAP-PCT (25%,
flagged default) + two LIM-CAP-SPECIFIC instances as described. Consistency
rule 5 passes: EUR 1,000,000 ≤ general cap of EUR 2,500,000.

## T08 — Position 4, percentage cap, title-only schedule

**Input:** Seller side; title warranties only; cap not specified (default
25%); schedule has 5 paragraphs, all title tier (1–5); no tax or other
paragraphs.

**Expected:** Position 4. LIM-SCOPE-TITLE (flagged DRAFT/unapproved),
LIM-TIME-TITLE (paragraphs 1–5, period 3y default — the purpose-built
title-only claim-period clause, not a trimmed LIM-TIME), LIM-TPC-NOTICE,
LIM-TPC-CONDUCT, LIM-COND, LIM-CAP-PCT (25%, default, flagged DRAFT), DEMIN
(0.1%, default, flagged DRAFT), BASKET-EXCESS (1%, default, flagged DRAFT),
DISCL-DATAROOM (flagged DRAFT), LIM-NODOUBLE, LIM-MITIG, LIM-MITIG-B,
LIM-NOLP.

## T09 — Position 4, fixed cap, custom notice period

**Input:** Seller side; title warranties only; fixed cap EUR 2,000,000;
schedule has 3 paragraphs, all title (1–3); third-party claim notice period
set to 15 Business Days instead of the default 10.

**Expected:** As T08's pattern (LIM-TIME-TITLE, not LIM-TIME), but
LIM-CAP-FIXED (EUR 2,000,000) and LIM-TPC-NOTICE period = 15 Business Days
(flagged as given, not default).

## T10 — Position 2, specific cap

**Input:** Buyer side; seller is a sovereign wealth fund; one specific cap
requested: breach of tax representations capped separately at 50% of price,
in addition to the general cap.

**Expected:** Position 2 base clause set (as T03) plus one LIM-CAP-SPECIFIC
instance, "in addition to" LIM-CAP-PRICE. (Specific caps are available for
any position except 1, not only 3/4.)

## T11 — Position 3, non-default but consistent thresholds

**Input:** Seller side; full warranty; de minimis set to 0.2%, basket set to
2% (both non-default, both explicitly given); no other title assets besides
the Sale Shares; schedule has 6 paragraphs: 1–2 tax, 3–4 title, 5–6 other.

**Expected:** LIM-TIME-SHARES (no other title assets); DEMIN (0.2%, not
default), BASKET-EXCESS (2%, not default) — consistent (de minimis below
basket, consistency rule 3 passes); otherwise standard position 3 set.

## T12 — Position 1, sophistication red herring

**Input:** Buyer side; seller is two individuals holding shares through a
newly formed personal holding vehicle, created solely for this one sale, no
other deal history.

**Expected:** Position 1 — no limitation section (still non-professional
despite the holding-vehicle wrapper).

## T13 — Position 3, other title assets (new, covers plain LIM-TIME)

**Input:** Seller side; full warranty package; cap not specified (default
25%); the Seller also warrants title to a registered trademark portfolio,
in addition to the Sale Shares; schedule has 9 paragraphs: 1–3 tax, 4–6
title, 7–9 other. Periods and thresholds not specified. Disclosure date:
the date of signing (given, since it has no rule-table default and is a
mandatory input).

**Expected:** Position 3. Because other title assets exist, LIM-TIME (the
full variant with the "and/or Claims relating to title to [OTHER ASSETS]"
limb) applies, not LIM-TIME-SHARES. [OTHER ASSETS] resolves to the
trademark portfolio. Otherwise standard position-3 defaults: tax 3y /
title 3y / other 1y, de minimis 0.1%, basket 1%, cap 25% — all flagged
default.

---

## E01 — De minimis above basket

**Input:** Position 3 (seller side, full warranty); de minimis set to 2%,
basket set to 1%.

**Expected:** Stop. Flag consistency rule 3 violation (de minimis must be
lower than the basket). No draft delivered.

## E02 — Thresholds requested on a buyer-side draft

**Input:** Position 2 (buyer side, institutional seller); user also asks for
a de minimis and basket "to be fair to the seller."

**Expected:** Stop / decline. Thresholds are seller-side only; this
combination is in the deliberately-unsupported list.

## E03 — Escrow / retention requested

**Input:** Seller-side deal; buyer wants claims secured by an escrow or
retention mechanism in addition to the liability cap.

**Expected:** Stop. Escrow/retention is a separate clause family, explicitly
out of scope.

## E04 — W&I insurance requested

**Input:** Seller-side deal structured with warranty & indemnity insurance
backing the cap.

**Expected:** Stop. W&I insurance structures are explicitly not used /
excluded from the set.

## E05 — Two general caps requested

**Input:** Position 4 (title-only); user wants two separate general caps —
one for representations, one for compensation of losses — instead of one
aggregate cap.

**Expected:** Stop. Explicitly excluded: a single aggregate cap covers both
tracks (this is also why every cap clause carries the "including... property
losses" parenthesis).

## E06 — No indemnity schedule at all

**Input:** Position 3 (seller side); user states there is no indemnity
schedule in this deal at all.

**Expected:** Stop. "Deals with no indemnity schedule" is explicitly
unsupported for every position — LIM-SCOPE and LIM-TIME both assume one
exists.

## E07 — Paragraph allocated twice

**Input:** Position 3; no other title assets besides the Sale Shares;
10-paragraph schedule; user allocates paragraph 5 to both the tax tier and
the title tier.

**Expected:** Stop. Consistency rule 1 violation — flag paragraph 5 as
allocated to more than one tier.

## E08 — Paragraph left unallocated

**Input:** Position 3; no other title assets besides the Sale Shares;
10-paragraph schedule; user allocates only paragraphs 1–9, leaving
paragraph 10 unassigned.

**Expected:** Stop. Consistency rule 1 violation — flag paragraph 10 as
unallocated.

## E09 — Instruction to drop the load-bearing parenthesis

**Input:** Position 3; user explicitly instructs: "Drop the 'including, for
the avoidance of doubt, property losses...' parenthesis from the cap
clause — it's redundant legalese."

**Expected:** Refuse. The parenthesis must survive in every cap clause
(consistency rule 2) because it is what makes the cap reach compensation of
losses under art. 406.1 — the skill should explain why rather than comply.

## E10 — Tiered periods requested under position 2

**Input:** Position 2 (buyer side, institutional seller); user asks for
tiered claim periods (tax/title/other, as in position 3) "to match the
seller's request," instead of the flat period.

**Expected:** Decline. Position 2 supports only the single flat period
(LIM-TIME-FLAT); tiered periods are not an available combination for this
position. The skill should say so rather than inventing a hybrid.

## E11 — Sophistication red herring, buyer side

**Input:** Buyer side; seller is an individual who has personally completed
15 prior company sales and negotiates as toughly as a PE fund.

**Expected:** Position 1 still applies — the position-2 trigger is legal/
entity status ("fund, strategic or institutional"), not deal sophistication.
No limitation section.
