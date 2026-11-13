# Current validity-evaluation protocol

## Status and version control

This protocol replaces the superseded historical test set. Complete it only
after the clause library, rules and run instructions are frozen. Record the
Git commit of the frozen package, execution date, model and version, skill
host, reviewer and scorer before any case is run. Do not amend a case or its
expected result after observing an output; log any needed change as a new
version of this protocol.

## Validity standard

For a supported input, a passing output selects only the prescribed clause IDs,
uses every supplied value and every applicable default correctly, includes all
dependencies, resolves cross-references, flags each DRAFT clause, and identifies
the applicable position and defined terms. For unsupported, incomplete or
inconsistent inputs, a passing output stops without drafting a partial section,
identifies the reason, and requests the missing required input where applicable.

The system is evaluated as a supervised first-draft assistant, not as an
autonomous legal decision-maker. A lawyer remains responsible for the inputs,
legal review and approval of every output.

## Execution convention

Unless a case tests a missing input, use these common values where needed:

- Disclosure date: 15 January 2026.
- Buyer type: professional/institutional.
- Closing Date, Business Day, Company, Applicable Law, Purchase Price, Sale
  Shares and Data Room: present as defined terms in the agreement.
- The required Schedule exists in Positions 2 and 3; it does not exist in
  Position 4.

For every case, save the verbatim input and output. Score clause selection,
parameter handling, dependencies, cross-references, DRAFT/default flags and
escalation independently before recording an overall case result.

## Test cases and ground truth

| ID | Input focus | Expected result |
|---|---|---|
| T01 | Position 1; individual seller | LIM-NONE only; no other clause or further intake. |
| T02 | Position 1; personal holding vehicle | LIM-NONE only; corporate form alone does not make the seller professional. |
| T03 | Position 2; professional seller; professional Buyer | LIM-SCOPE, LIM-TIME-FLAT, LIM-CAP-PRICE, common clauses, LIM-NODOUBLE and LIM-BUYER-SOPHISTICATED; defaults flagged. |
| T04 | Position 2; professional seller; private Buyer | T03 clause set without LIM-BUYER-SOPHISTICATED. |
| T05 | Position 2; specific cap stated as EUR amount, counts toward the 100%-of-price cap; Purchase Price supplied | Include LIM-CAP-SPECIFIC; compare the two caps using the supplied Purchase Price. |
| T06 | Position 3; percentage cap; no other title assets; complete allocation | LIM-TIME-SHARES, LIM-CAP-PCT, thresholds, LIM-NODOUBLE and LIM-BUYER-SOPHISTICATED. |
| T07 | Position 3; fixed cap; other title asset identified; complete allocation | LIM-TIME and LIM-CAP-FIXED; other-title-assets wording resolves to the supplied asset. |
| T08 | Position 3; fixed specific cap counts toward percentage general cap; Purchase Price supplied | Correct comparison under consistency rule 5; draft only if the specific cap does not exceed the general cap. |
| T09 | Position 3; custom tax period and custom thresholds, internally consistent | Given values used and not labelled defaults. |
| T10 | Position 4; percentage cap; professional Buyer; no schedule | LIM-SCOPE-TITLE, LIM-TIME-TITLE, LIM-CAP-PCT-TITLE, thresholds, common clauses, LIM-MITIG-B and LIM-BUYER-SOPHISTICATED; no LIM-NODOUBLE. |
| T11 | Position 4; fixed cap; private Buyer; no schedule | T10 pattern with LIM-CAP-FIXED-TITLE and no LIM-BUYER-SOPHISTICATED. |
| T12 | Position 4; title-specific cap, counts toward general cap | LIM-CAP-SPECIFIC-TITLE; title ground and cap relationship stated. |
| E01 | Position 2; de minimis or basket requested | Stop: buyer-side thresholds are unsupported. |
| E02 | Position 3; de minimis at or above basket | Stop: consistency rule 3. |
| E03 | Position 3; schedule paragraph allocated twice | Stop: consistency rule 1; identify the duplicated paragraph. |
| E04 | Position 3; schedule paragraph unallocated | Stop: consistency rule 1; identify the unallocated paragraph. |
| E05 | Position 2; no indemnity schedule | Stop: unsupported combination. |
| E06 | Position 3; no indemnity schedule | Stop: unsupported combination. |
| E07 | Position 3; other title assets not supplied | Request the missing input; do not choose a period variant. |
| E08 | Position 3; mixed-unit specific/general caps that count toward each other; Purchase Price missing | Request Purchase Price; do not perform the comparison or draft. |
| E09 | Position 4; specific cap concerns a non-title matter | Stop: position-4 specific caps cover title matters only. |
| E10 | Any supported position; disclosure date missing | Request the mandatory disclosure date; no assembled draft. |
| E11 | Position 2–4; Buyer type missing | Request Buyer type; do not decide whether to include LIM-BUYER-SOPHISTICATED. |
| E12 | Escrow, retention or W&I insurance requested | Stop: unsupported clause family/structure. |

## Reporting template

For each case, record: expected clause IDs; actual clause IDs; supplied and
defaulted parameters; expected and actual escalation; dependency and
cross-reference result; DRAFT/default-flag result; reviewer minutes; overall
pass/fail; and a concise error classification. Report denominators beside every
percentage, retain failed outputs, and distinguish missing-input requests from
unsupported-combination refusals.
