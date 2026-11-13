# Rule table — SPA limitation of liability (Russian law)

---

## Position

The side alone does not decide. Four positions:

| # | Position | Trigger | Result |
|---|---|---|---|
| 1 | Buyer, non-professional seller | acting for buyer; seller is an individual or otherwise not a professional seller | **LIM-NONE only — a single clause confirming liability is not limited** |
| 2 | Buyer, professional seller | acting for buyer; seller is a fund, strategic or institutional | 100% of price, flat period |
| 3 | Seller, standard | acting for seller; full warranty package | capped, tiered periods, thresholds |
| 4 | Seller, narrow | acting for seller; title warranties only | liability for all other matters excluded |

Position 1 does not produce a full limitation section. It produces exactly
one clause, LIM-NONE, confirming that the Seller's liability is not limited
— no cap, no shortened claim periods, no thresholds, none of the other
limitation clauses. Select only LIM-NONE, give the reason, and stop. That is
the correct output, not a failure.

## Selection

| Position | Cap | Periods | Thresholds | Scope |
|---|---|---|---|---|
| 1 | — | — | — | — |
| 2 | LIM-CAP-PRICE | LIM-TIME-FLAT | none | LIM-SCOPE |
| 3 | LIM-CAP-PCT or LIM-CAP-FIXED | LIM-TIME, or LIM-TIME-SHARES where there are no other title assets | DEMIN + BASKET-EXCESS | LIM-SCOPE |
| 4 | LIM-CAP-PCT-TITLE or LIM-CAP-FIXED-TITLE | LIM-TIME-TITLE | DEMIN + BASKET-EXCESS | LIM-SCOPE-TITLE |

## Always included

Wherever a limitation section is produced at all (positions 2, 3 and 4):

LIM-TPC-NOTICE · LIM-TPC-CONDUCT · LIM-COND · LIM-MITIG · LIM-NOLP ·
DISCL-DATAROOM

Positions 2 and 3 additionally include LIM-NODOUBLE. Position 4 does not: it
has no indemnity schedule and therefore no schedule-based property-loss claims
to which LIM-NODOUBLE could apply.

Exclusion of loss of profit is always included and is not negotiated.

## Buyer type — asked on every position that produces a section

Positions 2, 3 and 4 all ask whether the Buyer is a professional/
institutional party (a fund, a strategic acquirer, an institutional
investor) or an individual/private buyer — regardless of which side is
acting. This is independent of the Position table above and does not change
which Position applies; it only decides whether LIM-BUYER-SOPHISTICATED is
included.

Not asked on Position 1 drafts: they produce only the confirmatory LIM-NONE
clause, not a limitation regime that LIM-BUYER-SOPHISTICATED could attach to.

| Buyer type | Result |
|---|---|
| Professional / institutional | LIM-BUYER-SOPHISTICATED included |
| Individual / private | LIM-BUYER-SOPHISTICATED omitted |

## Seller side only

Positions 3 and 4 additionally include LIM-MITIG-B.

## Separate caps for Representations and compensation of losses — alternative

Positions 2 and 3 only (position 4 has no compensation-of-losses track to
separate from). By default a single aggregate cap covers both tracks
(LIM-CAP-PRICE / LIM-CAP-PCT / LIM-CAP-FIXED). If the user explicitly wants
two separate caps instead, use LIM-CAP-REPS-ONLY and LIM-CAP-INDEMNITY-ONLY
together in place of the combined cap — never just one of them. See
consistency rule 12.

## Schedule-free deals — positions 2 and 3

Positions 2 and 3 assume an indemnity schedule (a compensation-of-losses
track under art. 406.1) exists, by default. If the user confirms this deal
has none at all:

- Position 2: use LIM-SCOPE-NOSCHED in place of LIM-SCOPE; omit LIM-NODOUBLE.
- Position 3: use LIM-SCOPE-NOSCHED in place of LIM-SCOPE and
  LIM-TIME-NOSCHED in place of LIM-TIME / LIM-TIME-SHARES; omit
  LIM-NODOUBLE; the cap clause must not include the property-losses
  parenthesis (word it as LIM-CAP-PCT-TITLE / LIM-CAP-FIXED-TITLE do).
  Consistency rule 1 (indemnity schedule allocation) does not apply — there
  is no schedule to allocate.

This replaces the former flat refusal for this combination. See consistency
rule 13.

## Security for Claims — escrow or retention

Optional, any position that produces a limitation section (2, 3, 4). If the
deal is backed by an escrow or retention arrangement, add
LIM-SECURITY-ESCROW alongside the cap clause(s) — it does not replace them.

## W&I insurance

Optional, seller-side positions (3 and 4) only. If the Buyer has taken out
warranty and indemnity insurance, use LIM-CAP-WI in place of the ordinary
general cap clause (it replaces, not supplements, the cap). See consistency
rule 14.

## Cap uplift for the Buyer's contributions — optional, seller-side positions only

Positions 3 and 4 only. If the Buyer plans contributions to the Company
before a Claim is resolved, add LIM-CAP-UPLIFT alongside the general cap
clause.

## Buyer-side thresholds — optional

Position 2 has no thresholds by default. If the Buyer explicitly requests a
de minimis and/or basket on a buyer-side draft anyway, include DEMIN and/or
BASKET-EXCESS as for the seller-side positions.

## Specific caps — zero or more

A separate cap may be attached to a named breach or indemnity circumstance in
any position that produces a limitation section. Ask for each one: which breach,
what cap, and whether it counts toward the general cap or sits outside it. In
position 4 (ground must be a title matter), or in a schedule-free position
2/3 deal, use LIM-CAP-SPECIFIC-TITLE instead of LIM-CAP-SPECIFIC — its
wording has no property-losses language to match the general cap it sits
alongside.

| Clause | Repeatable |
|---|---|
| LIM-CAP-SPECIFIC | yes, zero or more |
| LIM-CAP-SPECIFIC-TITLE | yes, zero or more; position 4 only |

## Parameters

| Parameter | Position 2 | Position 3 | Position 4 |
|---|---|---|---|
| Cap | 100% of price received | 25% of price, or a fixed sum | 25% of price, or a fixed sum |
| Flat claim period | 5 years from Closing | n/a | n/a |
| Tax claims | n/a | 3 years from Closing | omitted |
| Title claims | n/a | 3 years from Closing | 3 years from Closing |
| Other claims | n/a | 1 year from Closing | omitted |
| De minimis | n/a | 0.1% of price | 0.1% of price |
| Basket | n/a | 1% of price | 1% of price |
| Basket type | n/a | excess — only the amount above the threshold is recoverable | excess — only the amount above the threshold is recoverable |
| Disclosure date | ask; no default; leave open and flagged if not yet known | ask; no default; leave open and flagged if not yet known | ask; no default; leave open and flagged if not yet known |
| Purchase Price for cap comparison | ask only where required by consistency rule 5 | ask only where required by consistency rule 5 | ask only where required by consistency rule 5 |
| Third party claim notice | 10 Business Days | 10 Business Days | 10 Business Days |
| Conditional claim period | 60 calendar days | 60 calendar days | 60 calendar days |

Flag every applied default in the output.

## Indemnity schedule allocation

Position 3 only. The selected claim-period clause allocates each paragraph of
the indemnity schedule to a limitation tier. Every paragraph must be allocated
to exactly one. Position 4 has no indemnity schedule.

| Tier | Period | Paragraphs |
|---|---|---|
| Tax | 3 years | ask |
| Title | 3 years | ask |
| Other | 1 year | ask |

## Dependencies

| Clause | Requires |
|---|---|
| LIM-SCOPE | DEF-REPS, DEF-SCHEDULE-LOSSES, DEF-CLAIM |
| LIM-SCOPE-TITLE | DEF-REPS, DEF-CLAIM, DEF-SALE-SHARES |
| LIM-TIME | DEF-CLOSING-DATE, DEF-SCHEDULE-LOSSES, LIM-TPC-NOTICE |
| LIM-TIME-SHARES | DEF-CLOSING-DATE, DEF-SCHEDULE-LOSSES, LIM-TPC-NOTICE |
| LIM-TIME-TITLE | DEF-CLOSING-DATE, LIM-TPC-NOTICE, DEF-SALE-SHARES |
| LIM-TIME-FLAT | DEF-CLOSING-DATE, LIM-TPC-NOTICE |
| LIM-TPC-NOTICE | DEF-BUSINESS-DAY, DEF-COMPANY |
| LIM-TPC-CONDUCT | LIM-TPC-NOTICE |
| LIM-COND | one selected claim-period clause, LIM-TPC-NOTICE, DEF-APPLICABLE-LAW |
| LIM-CAP-PRICE / PCT | DEF-PRICE, DEF-CLAIM |
| LIM-CAP-FIXED | DEF-CLAIM |
| LIM-CAP-PCT-TITLE | DEF-PRICE, DEF-CLAIM |
| LIM-CAP-FIXED-TITLE | DEF-CLAIM |
| LIM-CAP-SPECIFIC | a general cap clause |
| LIM-CAP-SPECIFIC-TITLE | a general cap clause with no property-losses language |
| DEMIN | DEF-CLAIM |
| BASKET-EXCESS | DEF-CLAIM, DEMIN |
| LIM-NODOUBLE | DEF-SCHEDULE-LOSSES |
| LIM-MITIG-B | LIM-MITIG |
| DISCL-DATAROOM | DEF-REPS, DEF-DATA-ROOM |
| LIM-BUYER-SOPHISTICATED | DEF-REPS |
| LIM-NONE | DEF-REPS, DEF-APPLICABLE-LAW |
| LIM-SCOPE-NOSCHED | DEF-REPS, DEF-CLAIM |
| LIM-TIME-NOSCHED | DEF-CLOSING-DATE, LIM-TPC-NOTICE |
| LIM-CAP-REPS-ONLY | DEF-REPS, DEF-CLAIM |
| LIM-CAP-INDEMNITY-ONLY | DEF-SCHEDULE-LOSSES |
| LIM-SECURITY-ESCROW | DEF-PRICE |
| LIM-CAP-WI | DEF-CLAIM |

## Consistency rules

1. **Indemnity schedule allocation.** Position 3 only. Every paragraph
   of the indemnity schedule cited in the selected claim-period clause must be allocated to exactly one
   tier. Name any paragraph left unallocated or appearing twice, and stop.
2. **Cap must reach the indemnity.** In positions 2 and 3, the cap clause must
   expressly state that it covers compensation of property losses. A clause
   limiting only "liability" does not reach compensation under art. 406.1, which
   is not liability for breach. Position 4 is schedule-free and must not refer to
   property losses.
3. **De minimis below basket.** The de minimis figure must be lower than the
   basket figure. If it is not, the section is incoherent — say so and stop.
4. **One cap only.** LIM-CAP-PRICE, LIM-CAP-PCT, LIM-CAP-FIXED,
   LIM-CAP-PCT-TITLE and LIM-CAP-FIXED-TITLE are mutually exclusive. Exactly
   one appears.
5. **Specific caps.** Each LIM-CAP-SPECIFIC or LIM-CAP-SPECIFIC-TITLE must state
   whether it counts toward or sits outside the general cap. If it counts toward
   it, its amount must not exceed it. Where the two caps use different units
   (a fixed amount and a percentage), obtain the Purchase Price and calculate
   both amounts before applying this check. In position 4, it must cover title
   only.
6. **Narrow scope.** In position 4, no clause in the output may create or assume
   liability for any matter other than title. Check LIM-TIME-TITLE in particular:
   it must not refer to an indemnity schedule, property losses, tax or other tiers.
7. **Cross-references.** LIM-COND and LIM-TIME refer to each other and to
   LIM-TPC-NOTICE by paragraph number. Every cross-reference must resolve.
8. LIM-MITIG-B requires LIM-MITIG.
9. Every DEF- dependency of every selected clause appears in the closing note.
10. **Buyer sophistication.** LIM-BUYER-SOPHISTICATED appears if and only if
    the Buyer is professional/institutional. Never include it for an
    individual/private Buyer, and never omit it for a professional/
    institutional Buyer.
11. **Position 1 is LIM-NONE alone.** Position 1's output is exactly one
    clause, LIM-NONE. No cap, period, threshold, disclosure, mitigation,
    buyer-type or other limitation clause may appear alongside it.
12. **Separate caps are both-or-neither.** LIM-CAP-REPS-ONLY and
    LIM-CAP-INDEMNITY-ONLY must appear together or not at all. Never select
    one without the other, and never combine either with the ordinary
    combined cap (LIM-CAP-PRICE / LIM-CAP-PCT / LIM-CAP-FIXED).
13. **Schedule-free deals.** If LIM-SCOPE-NOSCHED is selected,
    LIM-NODOUBLE must not appear, and the cap clause must not include the
    property-losses parenthesis. If LIM-TIME-NOSCHED is selected, do not
    run the indemnity-schedule-allocation check (rule 1) — there is nothing
    to allocate.
14. **W&I replaces, not supplements.** LIM-CAP-WI may not appear alongside
    any other general cap clause (LIM-CAP-PRICE / LIM-CAP-PCT /
    LIM-CAP-FIXED / LIM-CAP-REPS-ONLY / LIM-CAP-INDEMNITY-ONLY). It may
    still appear alongside LIM-CAP-SPECIFIC, LIM-CAP-UPLIFT and
    LIM-SECURITY-ESCROW.

## No match

If a combination of inputs does not appear above, state which combination is
missing and stop. Do not select the nearest row.

As of 2026-11-13, every combination previously listed here as deliberately
unsupported now has a path (see the sections above): buyer-side thresholds,
separate representations/indemnity caps, escrow/retention security, cap
uplift for Buyer contributions, W&I-insured deals, and schedule-free
deals for positions 2 and 3. This section now covers only genuinely novel
combinations not anticipated by any rule above — name the missing
combination and stop; still do not select the nearest row or guess.
