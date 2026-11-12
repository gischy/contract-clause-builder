# Rule table — SPA limitation of liability (Russian law)

---

## Position

The side alone does not decide. Four positions:

| # | Position | Trigger | Result |
|---|---|---|---|
| 1 | Buyer, non-professional seller | acting for buyer; seller is an individual or otherwise not a professional seller | **no limitation section at all** |
| 2 | Buyer, professional seller | acting for buyer; seller is a fund, strategic or institutional | 100% of price, flat period |
| 3 | Seller, standard | acting for seller; full warranty package | capped, tiered periods, thresholds |
| 4 | Seller, narrow | acting for seller; title warranties only | liability for all other matters excluded |

Position 1 produces nothing. Say so plainly, give the reason, and stop — that
is the correct output, not a failure.

## Selection

| Position | Cap | Periods | Thresholds | Scope |
|---|---|---|---|---|
| 1 | — | — | — | — |
| 2 | LIM-CAP-PRICE | LIM-TIME-FLAT | none | LIM-SCOPE |
| 3 | LIM-CAP-PCT or LIM-CAP-FIXED | LIM-TIME | DEMIN + BASKET-EXCESS | LIM-SCOPE |
| 4 | LIM-CAP-PCT or LIM-CAP-FIXED | LIM-TIME | DEMIN + BASKET-EXCESS | LIM-SCOPE-TITLE |

## Always included

Wherever a limitation section is produced at all (positions 2, 3 and 4):

LIM-TPC-NOTICE · LIM-TPC-CONDUCT · LIM-COND · LIM-NODOUBLE · LIM-MITIG ·
LIM-NOLP · DISCL-DATAROOM

Exclusion of loss of profit is always included and is not negotiated.

## Seller side only

Positions 3 and 4 additionally include LIM-MITIG-B.

## Specific caps — zero or more

A separate cap may be attached to a named breach or indemnity circumstance.
Asked for each one: which breach, what cap, and whether it counts toward the
general cap or sits outside it.

| Clause | Repeatable |
|---|---|
| LIM-CAP-SPECIFIC | yes, zero or more |

## Parameters

| Parameter | Position 2 | Positions 3 and 4 |
|---|---|---|
| Cap | 100% of price received | 25% of price, or a fixed sum |
| Flat claim period | 5 years from Closing | n/a |
| Tax claims | n/a | 3 years from Closing |
| Title claims | n/a | 3 years from Closing |
| Other claims | n/a | 1 year from Closing |
| De minimis | n/a | 0.1% of price |
| Basket | n/a | 1% of price |
| Basket type | n/a | excess — only the amount above the threshold is recoverable |
| Third party claim notice | 10 Business Days | 10 Business Days |
| Conditional claim period | 60 calendar days | 60 calendar days |

Flag every applied default in the output.

## Indemnity schedule allocation

Positions 3 and 4 only. LIM-TIME allocates each paragraph of the indemnity
schedule to a limitation tier. Every paragraph must be allocated to exactly one.

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
| LIM-TIME-FLAT | DEF-CLOSING-DATE, LIM-TPC-NOTICE |
| LIM-TPC-NOTICE | DEF-BUSINESS-DAY, DEF-COMPANY |
| LIM-TPC-CONDUCT | LIM-TPC-NOTICE |
| LIM-COND | LIM-TIME or LIM-TIME-FLAT, LIM-TPC-NOTICE, DEF-APPLICABLE-LAW |
| LIM-CAP-PRICE / PCT / FIXED | DEF-PRICE, DEF-CLAIM |
| LIM-CAP-SPECIFIC | a general cap clause |
| DEMIN | DEF-CLAIM |
| BASKET-EXCESS | DEF-CLAIM, DEMIN |
| LIM-NODOUBLE | DEF-SCHEDULE-LOSSES |
| LIM-MITIG-B | LIM-MITIG |
| DISCL-DATAROOM | DEF-REPS, DEF-DATA-ROOM |

## Consistency rules

1. **Indemnity schedule allocation.** Positions 3 and 4 only. Every paragraph
   of the indemnity schedule cited in LIM-TIME must be allocated to exactly one
   tier. Name any paragraph left unallocated or appearing twice, and stop.
2. **Cap must reach the indemnity.** The cap clause must expressly state that it
   covers compensation of property losses. A clause limiting only "liability" does
   not reach compensation under art. 406.1, which is not liability for breach.
3. **De minimis below basket.** The de minimis figure must be lower than the
   basket figure. If it is not, the section is incoherent — say so and stop.
4. **One cap only.** LIM-CAP-PRICE, LIM-CAP-PCT and LIM-CAP-FIXED are mutually
   exclusive. Exactly one appears.
5. **Specific caps.** Each LIM-CAP-SPECIFIC must state whether it counts toward
   or sits outside the general cap. If it counts toward it, its amount must not
   exceed it.
6. **Narrow scope.** In position 4, no clause in the output may create or assume
   liability for any matter other than title. Check LIM-TIME in particular — the
   tax and other tiers have nothing to attach to, so they are omitted.
7. **Cross-references.** LIM-COND and LIM-TIME refer to each other and to
   LIM-TPC-NOTICE by paragraph number. Every cross-reference must resolve.
8. LIM-MITIG-B requires LIM-MITIG.
9. Every DEF- dependency of every selected clause appears in the closing note.

## No match

If a combination of inputs does not appear above, state which combination is
missing and stop. Do not select the nearest row.

Deliberately not covered:

| Combination | Why excluded |
|---|---|
| Buyer-side de minimis or basket | Thresholds are used on seller-side drafts only |
| Separate caps for representations and for indemnity | A single aggregate cap covers both |
| Escrow, retention or other security for claims | Separate clause family, out of scope |
| Uplift of the cap for buyer contributions to the Company | Deal-specific, excluded from the set |
| W&I insurance structures | Not used |
| Deals with no indemnity schedule | LIM-SCOPE and LIM-TIME both assume one exists |
