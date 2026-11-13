# Final re-test — option-2 expansion and regression checks

Written before any case was run. Covers the six new rule paths added
2026-11-13 (buyer-side thresholds, separate caps, cap uplift, escrow, W&I,
schedule-free deals), two new consistency-rule enforcement checks, and
three regression checks on the core flow (wizard one-question-at-a-time,
the disclosure-date dead-end fix, and a full integrated happy path).

## N01 — Buyer-side thresholds (position 2)

**Input:** Buyer side; seller is a professional/institutional fund.
Disclosure date: 1 April 2026. Buyer explicitly requests a de minimis
(0.1% of price) and basket (1% of price) be included anyway. Buyer type:
individual/private.

**Expected:** Position 2. LIM-SCOPE, LIM-TIME-FLAT (5y default), DEMIN
(0.1%, given, not default), BASKET-EXCESS (1%, given, not default),
LIM-TPC-NOTICE (10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd default),
LIM-CAP-PRICE (100%, default), DISCL-DATAROOM (1 Apr 2026, given),
LIM-NODOUBLE, LIM-MITIG, LIM-NOLP. No LIM-BUYER-SOPHISTICATED (individual
buyer).

## N02 — Separate Representations/indemnity caps (position 3)

**Input:** Seller side; full warranty; schedule exists, 6 paragraphs (1-2
tax, 3-4 title, 5-6 other); no other title assets; disclosure date 1 May
2026; wants separate caps instead of one combined cap: Representations
cap = 20% of price, compensation-of-losses cap = 10% of price; buyer type:
professional.

**Expected:** Position 3. LIM-SCOPE, LIM-TIME-SHARES, LIM-CAP-REPS-ONLY
(20%) and LIM-CAP-INDEMNITY-ONLY (10%) together — no LIM-CAP-PRICE/PCT/
FIXED. DEMIN (0.1% default), BASKET-EXCESS (1% default), LIM-TPC-NOTICE
(10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd default), DISCL-DATAROOM
(given), LIM-NODOUBLE, LIM-MITIG, LIM-MITIG-B, LIM-NOLP,
LIM-BUYER-SOPHISTICATED (professional buyer).

## N03 — Cap uplift for Buyer contributions (position 4)

**Input:** Seller side; title warranties only; cap not specified (default
25%); Buyer plans a EUR 500,000 contribution to the Company's charter
capital before any Claim is resolved, and wants the cap increased
accordingly; disclosure date 1 June 2026; buyer type: individual.

**Expected:** Position 4. LIM-SCOPE-TITLE, LIM-TIME-TITLE (3y default),
LIM-CAP-PCT-TITLE (25%, default) plus LIM-CAP-UPLIFT (EUR 500,000
contribution), DEMIN (0.1% default), BASKET-EXCESS (1% default),
LIM-TPC-NOTICE (10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd default),
DISCL-DATAROOM (given), LIM-MITIG, LIM-MITIG-B, LIM-NOLP. No LIM-NODOUBLE
(position 4 is always schedule-free). No LIM-BUYER-SOPHISTICATED
(individual buyer).

## N04 — Escrow security (position 3)

**Input:** Seller side; full warranty; schedule 4 paragraphs (1 tax, 2
title, 3-4 other); no other title assets; cap not specified (default 25%);
disclosure date 1 July 2026; deal backed by an escrow arrangement: Escrow
Agreement dated 1 August 2026 between the Parties and ABC Escrow LLC, EUR
1,000,000 of the Purchase Price withheld at Closing; buyer type:
professional.

**Expected:** Position 3 base set (LIM-SCOPE, LIM-TIME-SHARES, LIM-CAP-PCT
25% default, DEMIN, BASKET-EXCESS, LIM-TPC-NOTICE, LIM-TPC-CONDUCT,
LIM-COND, DISCL-DATAROOM, LIM-NODOUBLE, LIM-MITIG, LIM-MITIG-B, LIM-NOLP,
LIM-BUYER-SOPHISTICATED) **plus** LIM-SECURITY-ESCROW alongside the cap
(not instead of it), with the given escrow date/agent/amount inserted.

## N05 — W&I insurance (position 3)

**Input:** Seller side; full warranty; schedule 4 paragraphs (1 tax, 2
title, 3-4 other); no other title assets; disclosure date 1 September
2026; deal is W&I-insured, nominal cap agreed at EUR 50,000; buyer type:
professional.

**Expected:** Position 3 base set, but the general cap is LIM-CAP-WI (EUR
50,000 nominal) **instead of** LIM-CAP-PCT/LIM-CAP-FIXED — not alongside
it. Otherwise standard position-3 set (schedule-bearing, since a schedule
was confirmed to exist): LIM-SCOPE, LIM-TIME-SHARES, DEMIN, BASKET-EXCESS,
LIM-TPC-NOTICE, LIM-TPC-CONDUCT, LIM-COND, DISCL-DATAROOM, LIM-NODOUBLE,
LIM-MITIG, LIM-MITIG-B, LIM-NOLP, LIM-BUYER-SOPHISTICATED.

## N06 — Schedule-free deal (position 2)

**Input:** Buyer side; seller is a professional/institutional strategic
buyer. User confirms there is no indemnity schedule of any kind in this
deal. Disclosure date 1 October 2026. Buyer type: individual.

**Expected:** Position 2. LIM-SCOPE-NOSCHED (not LIM-SCOPE), LIM-TIME-FLAT
(5y default — unaffected, it never referenced a schedule), LIM-TPC-NOTICE
(10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd default), LIM-CAP-PRICE
(100% default), DISCL-DATAROOM (given), LIM-MITIG, LIM-NOLP. No
LIM-NODOUBLE (omitted per consistency rule 13). No LIM-BUYER-SOPHISTICATED
(individual).

## N07 — Schedule-free deal (position 3)

**Input:** Seller side; full warranty; user confirms there is no indemnity
schedule of any kind in this deal. Cap: fixed sum, EUR 3,000,000.
Disclosure date 1 November 2026. Buyer type: professional.

**Expected:** Position 3. LIM-SCOPE-NOSCHED, LIM-TIME-NOSCHED (three tiers
by Representation category — tax/title/other — all periods default: 3y/
3y/1y), LIM-CAP-FIXED-TITLE (EUR 3,000,000 — the no-property-losses
wording, not ordinary LIM-CAP-FIXED), DEMIN (0.1% default), BASKET-EXCESS
(1% default), LIM-TPC-NOTICE (10 BD default), LIM-TPC-CONDUCT, LIM-COND
(60cd default), DISCL-DATAROOM (given), LIM-MITIG, LIM-MITIG-B, LIM-NOLP,
LIM-BUYER-SOPHISTICATED (professional). No LIM-NODOUBLE. No
indemnity-schedule-allocation check (consistency rule 1 doesn't apply —
there is no schedule).

## N08 — Consistency rule 14 enforcement: W&I + ordinary cap both requested

**Input:** Seller side; full warranty; schedule exists (4 paragraphs: 1
tax, 2 title, 3-4 other); deal is W&I-insured (nominal cap EUR 50,000),
but the user also asks for a 25% percentage cap "just in case," on top of
the W&I nominal cap.

**Expected:** The skill should not silently combine both. LIM-CAP-WI
replaces, not supplements, any other general cap (consistency rule 14) —
it should flag this combination as inconsistent/not permitted and ask the
user to choose one, rather than drafting both caps together or silently
picking one.

## N09 — Consistency rule 12 enforcement: separate caps, only one figure given

**Input:** Seller side; full warranty; schedule exists. User wants separate
caps (Representations + compensation-of-losses) instead of one combined
cap, gives the Representations-only figure (20%), but does not give a
figure for the compensation-of-losses cap and says they don't have one
yet.

**Expected:** The skill should not proceed with only LIM-CAP-REPS-ONLY
alone. Consistency rule 12 (both-or-neither) — it should say both figures
are required before this alternative can be assembled, and should not
invent the missing figure or silently fall back to the combined cap
either.

## R01 — Regression: Position 1, new wizard flow

**Input:** Buyer side; seller is an individual (non-professional).

**Expected:** Position 1. LIM-NONE only, correct reasoning given, stop
before any further questions arise. (Also confirms side and seller-type
were asked as two separate questions, not combined — report whether the
agent's own process did this correctly if observable from its reasoning.)

## R02 — Regression: full integrated happy path, position 3

**Input:** Seller side; full warranty; schedule exists, 10 paragraphs (1-3
tax, 4-6 title, 7-10 other); no other title assets; cap 20% of price;
disclosure date 15 December 2026 (given); buyer type: professional; no
specific caps, no escrow, no W&I, no cap uplift, no separate caps (uses
the combined cap).

**Expected:** Standard full Position 3 draft: LIM-SCOPE, LIM-TIME-SHARES,
LIM-CAP-PCT (20%, given), DEMIN (0.1% default), BASKET-EXCESS (1%
default), LIM-TPC-NOTICE (10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd
default), DISCL-DATAROOM (15 Dec 2026, given), LIM-NODOUBLE, LIM-MITIG,
LIM-MITIG-B, LIM-NOLP, LIM-BUYER-SOPHISTICATED (professional). Confirms
the full chain of new Step-1 questions (schedule-exists, cap structure,
buyer type, etc.) still produces a coherent, correct draft end to end.

## R03 — Regression: disclosure date not known, position 2

**Input:** Buyer side; seller is a professional/institutional investor.
Disclosure date is not yet known/not supplied. Buyer type: individual.

**Expected:** Position 2. A full draft IS produced (not blocked) — this is
the dead-end fix: DISCL-DATAROOM is included with `[DISCLOSURE DATE]` left
as an open, clearly flagged bracket, not a refusal. Otherwise standard
defaults: LIM-SCOPE, LIM-TIME-FLAT (5y default), LIM-CAP-PRICE (100%
default), LIM-TPC-NOTICE (10 BD default), LIM-TPC-CONDUCT, LIM-COND (60cd
default), LIM-NODOUBLE, LIM-MITIG, LIM-NOLP. No LIM-BUYER-SOPHISTICATED
(individual).
