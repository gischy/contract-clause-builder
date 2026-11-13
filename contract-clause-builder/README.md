# contract-clause-builder

A Claude skill that drafts the limitation-of-liability section of a share
purchase agreement (SPA) governed by Russian law, by selecting from a closed,
firm-approved library of clause variants rather than drafting freely.

## What it does

Given a handful of structured deal parameters (buyer/seller side, seller type,
warranty scope, buyer type, cap, claim periods, indemnity-schedule
allocation, any specific caps), collected one question at a time rather than
as a batch, the skill:

1. Establishes which of four transaction "positions" applies.
2. Selects the clause variants the rule table assigns to that position,
   including optional add-ons when relevant: separate Representations/
   indemnity caps, schedule-free deals, escrow/retention security, W&I
   insurance, cap uplift for the Buyer's contributions, and buyer-side
   thresholds.
3. Inserts the parameters.
4. Runs fourteen consistency checks before producing output.
5. Refuses to improvise and stops only for genuinely novel combinations not
   anticipated by any rule — every combination that used to be a flat
   refusal (buyer-side thresholds, separate caps, escrow, W&I, cap uplift,
   schedule-free deals) now has a real clause path instead. (On a buyer-side
   draft against a non-professional seller, the correct result is a single
   short clause, LIM-NONE, confirming liability is not limited — not a full
   section, but not silence either.)
6. Optionally exports the result as a Word (.docx), PDF or PowerPoint (.pptx)
   file, on a minimalistic HHL-branded template (yellow accent, logo,
   Verdana).

## Files

- `SKILL.md` — the skill definition: the workflow Claude follows (collect
  inputs, select clauses, assemble, check).
- `reference/clauses.md` — the clause library: 32 variants, English wording
  (a rendering of the firm's Russian-law originals; the whole set was
  confirmed approved by the firm on 2026-11-12).
- `reference/rules.md` — the rule table: the four positions, clause
  selection and dependencies, parameter defaults, consistency rules, and the
  (now very short) list of combinations still genuinely unsupported.
- `scripts/export.py` — converts the assembled section to `.docx`, `.pdf` or
  `.pptx`, on a minimalistic HHL-branded template (PDF requires LibreOffice/
  `soffice` on PATH; falls back to a clear error, not a crash, if it isn't
  available).
- `assets/hhl_logo.png` — the HHL logo, bundled so the export works
  standalone without depending on anything outside this package.

## How to run it

This is a Claude skill package (Markdown instructions, a reference clause
library, and one export script). To use it:

1. Copy this folder into wherever Claude skills are loaded in your
   environment (for Claude Code: `~/.claude/skills/contract-clause-builder/`).
2. Ask Claude to prepare the limitation-of-liability section of an SPA, or
   invoke the skill by name.
3. Answer the structured questions the skill asks (side, the relevant seller
   type or warranty scope, disclosure date, cap, buyer type, claim periods,
   other title assets, indemnity-schedule allocation where required, and any
   specific caps).
4. Review the generated section together with the closing note: the position
   taken and why, the clause IDs selected, the defined terms to check against
   the rest of the agreement, any defaults applied, and any indemnity-schedule
   paragraph left unallocated.

## Status

Demonstration prototype built for an EMBA assignment on AI's impact on jobs
(Change Management and AI, HHL). The clause set is confirmed approved by the
firm (2026-11-12); the skill is still deliberately scoped to one section of
one document type. See the accompanying paper for the validity evaluation
and deployment verdict.
