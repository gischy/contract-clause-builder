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
2. Selects the clause variants the rule table assigns to that position.
3. Inserts the parameters.
4. Runs ten consistency checks before producing output.
5. Refuses to improvise and stops if the input combination isn't covered by
   the approved rule set — the correct result in that case, not a failure.
   (On a buyer-side draft against a non-professional seller, the correct
   result is a single short clause, LIM-NONE, confirming liability is not
   limited — not a full section, but not silence either.)
6. Optionally exports the result as a Word (.docx) or PDF file.

## Files

- `SKILL.md` — the skill definition: the workflow Claude follows (collect
  inputs, select clauses, assemble, check).
- `reference/clauses.md` — the clause library: 19 variants, English wording
  (a rendering of the firm's Russian-law originals, pending firm approval).
- `reference/rules.md` — the rule table: the four positions, clause
  selection and dependencies, parameter defaults, consistency rules, and the
  combinations deliberately left unsupported.
- `scripts/export.py` — converts the assembled section to `.docx` or `.pdf`
  (PDF requires LibreOffice/`soffice` on PATH; falls back to a clear error,
  not a crash, if it isn't available).

## How to run it

This is a Claude skill package (Markdown instructions, a reference clause
library, and one export script). To use it:

1. Copy this folder into wherever Claude skills are loaded in your
   environment (for Claude Code: `~/.claude/skills/contract-clause-builder/`).
2. Ask Claude to prepare the limitation-of-liability section of an SPA, or
   invoke the skill by name.
3. Answer the structured questions the skill asks (side, seller type, cap,
   claim periods, indemnity-schedule allocation, specific caps).
4. Review the generated section together with the closing note: the position
   taken and why, the clause IDs selected, the defined terms to check against
   the rest of the agreement, any defaults applied, and any indemnity-schedule
   paragraph left unallocated.

## Status

Demonstration prototype built for an EMBA assignment on AI's impact on jobs
(Change Management and AI, HHL). Not approved for production use: several
clause variants are explicitly marked DRAFT / not yet approved by the firm,
and the skill is deliberately scoped to one section of one document type. See
the accompanying paper for the validity evaluation and deployment verdict.
