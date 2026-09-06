# Fleet Gauntlet — a planted-defect calibration drill for AI agents

Before trusting an AI agent with real work, I make it walk the Gauntlet:
a code-audit exam with a **sealed answer key**, **false-positive traps**,
and a **deterministic scoring formula**. In August 2026 I ran eight systems
through it — two frontier coding CLIs, a desktop assistant, a CLI from a
third vendor, two large API-only models, and two small local models — and
the results calibrated exactly which seat each one earned on my team.

## How it works

- `gauntlet_target.py` — a small task-ledger module with **7 planted
  defects** (mutable default sharing, an always-true guard that kills the
  core operation, lexicographic priority sorting, a division-by-zero that
  violates its own docstring, an off-by-one that silently loses data,
  pop-while-iterating, and a shallow copy that breaks a documented
  contract) plus **2 traps** — correct code that *looks* wrong, to separate
  reasoners from pattern-matchers.
- `BRIEF_GAUNTLET.md` — the identical exam brief every agent receives:
  mandatory verdict-first format, line numbers + concrete failing scenario
  required per claim, false positives subtract, defect count undisclosed.
- The answer key stayed sealed (off-disk) during all runs; it is published
  in `GAUNTLET_SCORECARD.md` now that the drill is complete.
- Score = defects − false positives + ½·(traps explicitly cleared) −
  format penalty.

## What it caught

- Two large API-only models found **every defect** — and shipped raw
  chain-of-thought instead of reports, with **fabricated line numbers**,
  because their output budget was consumed by reasoning. Content ≠
  deliverable.
- A 12B local model confidently **cleared a real bug** ("just returns a
  shorter list") — a wrong "verified safe" is more dangerous than a miss.
- A tiny code model produced six vague claims, five of them wrong, and
  prescribed forbidden fixes. Cut.
- The top three (two frontier CLIs and a desktop assistant) independently
  converged on the identical 7/7 ground truth with zero false positives —
  which is what earned them autonomous roles on subsequent projects.

Raw graded reports from every entrant are in `reports/` — including the
leaked reasoning transcripts, kept unedited as evidence.

## Why this matters

Benchmarks tell you what a model can do on someone else's test. A gauntlet
with a sealed key, traps, and a format contract tells you what an agent will
do **on your work, under your rules** — including whether it follows
instructions, respects constraints, and knows what it doesn't know. Ten of
the most useful evaluation dollars I've ever spent were the API calls in
this repo.

*Ismael Rodriguez — Magpie Studios LLC*
