---
name: contract-clause-builder
description: Draft the limitation of liability section of a share purchase agreement under Russian law — scope, claim periods, third party claims, aggregate cap, no double recovery, mitigation — from deal parameters, selecting from a fixed set of firm-approved clause variants. Use when asked to prepare a limitation of liability section, claim periods or a liability cap for an SPA under Russian law, or to demonstrate the clause builder.
---

# SPA limitation of liability — clause builder (Russian law)

DEMONSTRATION VERSION. Covers the limitation of liability section only.
Governing law is Russian; the clause library and all output are in English.

Conduct the whole interaction in English by default — the questions, the
explanations, the drafted clauses, the closing note — regardless of the
language the user writes in. Do not switch language just to mirror the
user; the clause library itself only exists in English, so a conversation
in any other language would have to be translated back and forth around
it. Depart from English only if the user explicitly asks for a different
language.

The English wording is a rendering of the firm's Russian text. The whole
clause set was confirmed approved by the firm on 2026-11-12.

The clause set is closed. Every output is assembled from the variants in
`reference/clauses.md`, chosen according to `reference/rules.md`. Nothing is
drafted from scratch and nothing is adapted.

---

## Step 1 — Collect the inputs

Ask one question at a time and wait for the answer before asking the next.
Never combine two inputs into a single question — in particular, side and
seller type (or side and warranty scope) are always two separate questions,
never one. Where an input has a small fixed set of answers, offer them as
lettered options (e.g. "A) Buyer  B) Seller") rather than open text, so the
user can just pick one. If the user has supplied term sheet details that
answer a question before it is asked, propose that answer and ask for
confirmation instead of asking the question cold — but still one input at a
time, never several folded into one confirmation.

The inputs, in the order to ask them:

1. **Side** — buyer or seller? Ask this alone, first.
2. **Seller type** — buyer side only; once side is answered, ask next and
   alone: is the seller a professional seller (a fund, a strategic buyer, an
   institutional holder) or not?
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
10. **Purchase Price** — only if needed to compare a specific cap that counts
    toward the general cap where one cap is a fixed amount and the other is a
    percentage of the Purchase Price
11. **Buyer type** — for every position that produces a section, regardless of
    which side is acting; is the Buyer a professional/institutional party (a
    fund, a strategic acquirer, an institutional investor) or an individual/
    private buyer? This is independent of the Position table and does not
    change which position applies; it only decides whether
    LIM-BUYER-SOPHISTICATED is included. Not asked on position 1 drafts: they
    produce only the confirmatory LIM-NONE clause, not a limitation regime.

Do not ask about thresholds on a buyer-side draft, the third party claim notice
period, the conditional claim period, or which of the mitigation, lost profit
and disclosure clauses to include. Those follow from the position or are fixed,
and are set by `reference/rules.md`.

Ask for the disclosure date for every position that produces a limitation
section — but if it is not yet known (commonly the case: it is often still
being negotiated when this section is first drafted), do not block the
draft on it. Leave the `[DISCLOSURE DATE]` placeholder open in the output
and flag it clearly as unresolved, the same way other not-yet-known figures
are handled. Never invent a date. Position 1 produces only LIM-NONE, not a
limitation section, so do not ask for it once that position is established.

For a seller-side standard position, ask for other title assets before choosing
the claim-period variant. If there are none, select the no-other-title-assets
variant; never insert “none” into a clause placeholder. Do not ask this question
for the narrow seller position: its scope is limited to the Sale Shares.

Do not continue if the required indemnity schedule or its complete allocation
has not been supplied. Position 4 has no indemnity schedule.

Do not continue if a specific cap that counts toward the general cap cannot be
compared with it because one is expressed as a percentage and the other as a
fixed amount and the Purchase Price has not been supplied. Do not infer the
Purchase Price from a defined term or another deal figure.

Inputs 1 and 2, or 1 and 3, determine the position. Establish the position
before asking anything else — on position 1 the remaining questions do not
arise.

Never invent a figure or a period. Where one is unsettled, apply the default
from `reference/rules.md` and flag it in the output as a default.

## Step 2 — Select the clauses

Establish the position from the "Position" table in `reference/rules.md`.

**Position 1 produces only LIM-NONE, not a limitation section.** Select LIM-NONE
and nothing else. Give the reason — the firm does not limit a non-professional
seller's liability on a buyer-side draft — and stop before asking any of the
other inputs. That is the correct output, not a failure.

Otherwise start from the "Always included" list, then take what the selection
table gives for the position (including the applicable claim-period variant),
then add any specific caps asked for.

Do not choose between variants on judgment. The table decides.

**If the combination does not appear in the table, do not select the nearest
row.** State which combination has no entry, say that it falls outside the
approved clause set, and stop. Do not produce a partial draft.

## Step 3 — Assemble

**Position 1 is an exception to the rest of this step.** Output LIM-NONE
alone, under its own single heading (e.g. "10. No Limitation of Seller's
Liability") — not the numbered sub-heading structure below, which is for a
full limitation section only.

For positions 2-4, output as a numbered section, with these sub-headings, in
this order:

1. Scope
2. Periods for bringing claims — claim periods, third party claim notice,
   conduct of third party claims, conditional claims
3. Maximum aggregate liability of the Seller — general cap, then any specific
   caps
4. Thresholds — de minimis and basket, seller side only
5. Disclosure through the data room
6. No double recovery — positions 2 and 3 only
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
- In positions 2 and 3, does the cap clause retain the parenthesis covering
  property losses? In position 4, is that language absent? (consistency rule 2)
- Where a specific cap counts toward the general cap, has it been compared in
  the same unit of account?
- Is LIM-BUYER-SOPHISTICATED included if and only if the Buyer is
  professional/institutional? (consistency rule 10)

End the output in English with:

- the position taken, and why
- the clause IDs selected
- the defined terms the section relies on, to be checked against the agreement
- any paragraph of the indemnity schedule not allocated to a limitation period,
  where an indemnity schedule is required

## Step 5 — Offer an export (optional)

After delivering the output, ask once, as a single lettered-option question:
"Would you like this exported as a file — A) no, text is fine  B) Word
(.docx)  C) PDF  D) PowerPoint (.pptx)?" Do not export unless the user asks
for it here or later. The export uses a minimalistic HHL-branded template
(logo, yellow accent rule or frame, Verdana) — not firm letterhead, since
this is a demonstration deliverable, not a client-ready document.

If the user chooses B, C or D:

1. Write the exact assembled section plus its closing note (Steps 3-4's
   output, verbatim — nothing added, nothing paraphrased) to a temporary
   Markdown file.
2. Run `scripts/export.py <that file> <output path>`, with the output path
   ending `.docx`, `.pdf` or `.pptx` to match their choice.
3. Give the user the resulting file.

If PDF export fails because LibreOffice isn't available in this
environment, say so plainly and offer the Word file instead — do not retry
silently or fall back to pasting the text as a workaround.

Position 1's output is short (a single LIM-NONE clause), but still offer
the export — it is a real clause the user may want in Word or PDF form.
