---
name: contract-clause-builder
description: Draft the limitation of liability section of a share purchase agreement under Russian law — scope, claim periods, third party claims, aggregate cap, no double recovery, mitigation — from deal parameters, selecting from a fixed set of firm-approved clause variants. Use when asked to prepare a limitation of liability section, claim periods or a liability cap for an SPA under Russian law, or to demonstrate the clause builder.
---

# SPA limitation of liability — clause builder (Russian law)

DEMONSTRATION VERSION. Covers the limitation of liability section only.
Governing law is Russian; the clause library and all output are in English.

The English wording is a rendering of the firm's Russian text and is pending
firm approval. Say so once at the end of each output.

The clause set is closed. Every output is assembled from the variants in
`reference/clauses.md`, chosen according to `reference/rules.md`. Nothing is
drafted from scratch and nothing is adapted.

Clause variants marked DRAFT in `reference/clauses.md` have not been approved
by the firm and must be flagged in the output.

---

## Step 1 — Collect the inputs

Ask for these as a short numbered list. If the user has supplied term sheet
details, propose answers drawn from them and ask for confirmation.

1. **Side** — buyer or seller?
2. **Seller type** — buyer side only; is the seller a professional seller (a
   fund, a strategic buyer, an institutional holder) or not?
3. **Warranty scope** — seller side only; full warranty package, or title
   warranties only?
4. **Disclosure date** — the date by which information must have been made
   available in the Data Room for it to qualify as disclosed
5. **Cap** — seller side only; a percentage of the price, or a fixed sum, and
   the figure
6. **Claim periods** — where they differ from the defaults
7. **Other title assets** — seller, standard position only; identify assets
   other than the Sale Shares to which the title-claim period must apply, or
   confirm that there are none
8. **Indemnity schedule** — buyer-professional and standard seller positions
   only. A schedule is required: for the buyer-professional position, confirm
   that it exists; for the standard seller position, identify every paragraph
   and allocate it to the tax, title or other tier. The narrow seller position
   has no indemnity schedule.
9. **Specific caps** — for every position that produces a section, any named
   breach or circumstance with its own cap; for
   each, the breach, the amount, and whether it counts toward the general cap
10. **Buyer type** — for every position that produces a section, regardless of
    which side is acting; is the Buyer a professional/institutional party (a
    fund, a strategic acquirer, an institutional investor) or an individual/
    private buyer? This is independent of the Position table and does not
    change which position applies; it only decides whether
    LIM-BUYER-SOPHISTICATED is included. Not asked on position 1 drafts, since
    no section is produced at all.

Do not ask about thresholds on a buyer-side draft, the third party claim notice
period, the conditional claim period, or which of the mitigation, lost profit
and disclosure clauses to include. Those follow from the position or are fixed,
and are set by `reference/rules.md`.

Ask for the disclosure date for every position that produces a limitation
section. It is a required deal input: do not apply a default or leave the
`[DISCLOSURE DATE]` placeholder unresolved. Position 1 produces no section, so
do not ask for it once that position is established.

For a seller-side standard position, ask for other title assets before choosing
the claim-period variant. If there are none, select the no-other-title-assets
variant; never insert “none” into a clause placeholder. Do not ask this question
for the narrow seller position: its scope is limited to the Sale Shares.

Do not continue if the required indemnity schedule or its complete allocation
has not been supplied. Position 4 has no indemnity schedule.

Inputs 1 and 2, or 1 and 3, determine the position. Establish the position
before asking anything else — on position 1 the remaining questions do not
arise.

Never invent a figure or a period. Where one is unsettled, apply the default
from `reference/rules.md` and flag it in the output as a default.

## Step 2 — Select the clauses

Establish the position from the "Position" table in `reference/rules.md`.

**Position 1 produces no limitation section.** Say so, give the reason — the
firm does not limit a non-professional seller's liability on a buyer-side
draft — and stop. That is the correct output, not a failure.

Otherwise start from the "Always included" list, then take what the selection
table gives for the position (including the applicable claim-period variant),
then add any specific caps asked for.

Do not choose between variants on judgment. The table decides.

**If the combination does not appear in the table, do not select the nearest
row.** State which combination has no entry, say that it falls outside the
approved clause set, and stop. Do not produce a partial draft.

## Step 3 — Assemble

Output as a numbered section, with these sub-headings, in this order:

1. Scope
2. Periods for bringing claims — claim periods, third party claim notice,
   conduct of third party claims, conditional claims
3. Maximum aggregate liability of the Seller — general cap, then any specific
   caps
4. Thresholds — de minimis and basket, seller side only
5. Disclosure through the data room
6. No double recovery
7. Mitigation
8. Exclusion of lost profit
9. Buyer's acknowledgment of reliance — professional/institutional Buyer only

Insert the figures and periods from the rule table. Resolve every internal
cross-reference to the paragraph number it actually carries in the output.

## Step 4 — Check before delivering

Run every check in the "Consistency rules" section of `reference/rules.md`.
Rule 1, the indemnity schedule allocation, is the one most likely to fail — do
not skip it.

Then:

- Is every dependency of every selected clause present?
- Does every internal cross-reference resolve?
- Do the figures and periods match the rule table exactly?
- Are any defaults flagged as defaults?
- Are any DRAFT clauses flagged as unapproved?
- Does the cap clause retain the parenthesis covering property losses?
  (consistency rule 2)
- Is LIM-BUYER-SOPHISTICATED included if and only if the Buyer is
  professional/institutional? (consistency rule 10)
- Is it stated that the English wording is pending firm approval?

End the output in English with:

- the position taken, and why
- the clause IDs selected
- the defined terms the section relies on, to be checked against the agreement
- any paragraph of the indemnity schedule not allocated to a limitation period
