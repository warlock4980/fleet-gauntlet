# GAUNTLET SCORECARD — Fleet Calibration Drill, adjudicated 2026-08-26

Ground truth (now unsealed): **7 planted defects** — line 17 mutable default `tasks=[]` ·
line 50 `== "done" or "obsolete"` always-truthy (claim() can never succeed) · line 59
lexicographic priority sort (P10 outranks P2) · line 64 ZeroDivisionError on empty ledger
despite "Safe on any ledger" · line 69 pagination off-by-one (one item per page LOST, never
returned by any page) · line 74 pop-while-iterating-forward (consecutive obsoletes survive) ·
line 89 shallow snapshot (docstring promises independence, task dicts shared).
**2 traps** (correct code that looks wrong): line 32 `tags = tags or []` · lines 81–84
drop_done's reverse-iteration removal.

Formula: defects − false positives + 0.5 × traps explicitly cleared − format penalty (0/0.5/1). Max 8.0.

| Rank | Seat | Defects | FPs | Traps | Format | Score | Deliverable? |
|---|---|---|---|---|---|---|---|
| 1 | Baltazar (Codex/GPT-5) | 7/7 | 0 | 2/2 | 0 | **8.0** | Yes — exemplary |
| 1 | Sol (ChatGPT GPT-5) | 7/7 | 0 | 2/2 | 0 | **8.0*** | Yes — exemplary |
| 3 | Gaspar (Claude Code CLI) | 7/7 | 0 | 1/2 | 0 | **7.5** | Yes — exemplary |
| 4 | Melchor (Gemini CLI) | 7/7 | 0 | 1/2 | −0.5 | **7.0** | Yes — clean format, but ALL line numbers wrong |
| 5 | Nemotron Ultra 550B | 7/7 | 0 | 2/2 | −1 | **7.0†** | NO — leaked reasoning, wrong line numbers, truncated |
| 6 | Nemotron Super 120B | 7/7 | 0 | 2/2 | −1 | **7.0†** | NO — pure reasoning transcript, truncated pre-report |
| 7 | gemma4:12b (Ollama) | 5/7 | 0 | 1/2 | −1 | **4.5** | NO — no report, truncated, wrong line numbers |
| 8 | deepseek-coder 1.3B | 0/7 | 6 | 0 | −1 | **−7.0** | NO — vague prose, wrong claims, prescribed fixes |

## Seat-by-seat rulings

**Baltazar — 8.0, the only unqualified perfect run.** All seven with correct lines and
concrete counterexamples he EXECUTED and disclosed. Both traps explicitly cleared with the
right reasons (line 32 "creates a fresh list... avoiding a shared default tag list"; 81–83
"iterate backward, so deleting adjacent done tasks does not skip any"). Tightest report of
the fleet at 336 words. The re-brief out of advise-only took completely — the Skeptic seat
is confirmed operational for Friday. One nuance short of perfection: his pagination scenario
shows the short page but not that the dropped items are unreachable by ANY page.

**Sol — 8.0 with a timeline asterisk (*).** All seven, both traps, and the single sharpest
failing scenario of the drill: `page(0, size=1)` returns NOTHING — with size 1, every page
is empty and the whole ledger is unreachable. Chose static analysis to honor read-only
maximally and said so. The asterisk is procedural, not personal: Sol's dispatch (Aug 26,
20:25) happened ~22h after a collection summary enumerating the seven defects existed in
the Comandante's terminal. If the paste was brief+code only, the score stands clean;
recorded per anti-rubber-stamp doctrine because unrecorded gaps become unfalsifiable later.

**Gaspar — 7.5.** All seven, empirically verified by execution (disclosed), including the
best purge_obsolete evidence ("verified by execution"). Cleared the drop_done trap
explicitly; the tags trap only implicitly ("add_task — no defects found"), which misses the
half-point under the explicit-clearing rule. Verdict-first, in budget, zero waste. Builder
seat confirmed.

**Melchor (Gemini CLI) — 7.0, late entrant (Aug 26), the trinity completed.** Ran in a
clean-room copy (/tmp/gauntlet-arena) because the main folder held the unsealed scorecard
by then — blindness preserved. All seven defects with correct mechanisms and concrete
scenarios, execution-verified and disclosed, clean verdict-first format in budget, zero
false positives, drop_done trap cleared with the right reason. Deductions: missed the
tags-idiom trap entirely, and EVERY line number is systematically wrong (14/47/53/58/63/
69/83 vs true 17/50/59/64/69/74/89) — renumbered the file mentally instead of reading real
coordinates (−0.5). Council rule for his seat: reports must quote the offending line
verbatim beside the number. Byline self-reported "Gemini 1.5 Pro" — a training-era name;
seat identity verified by conduct, not by self-report. Auditor seat GRANTED, with the
quote-the-line harness.

**Nemotron Ultra — 7.0†, content excellent, delivery failed.** Found all seven and cleared
both traps — but shipped its chain-of-thought as the report: preamble, self-talk, a
placeholder "AGENT: <my identifier>", 1,066 words (2.4× budget), truncated mid-sentence
while trying to recount line numbers — which were WRONG throughout (it renumbered the file
from memory). In council terms: brilliant analyst, unusable report. † = score reflects
content; as a deliverable it fails the brief.

**Nemotron Super — 7.0†, same failure, one stage earlier.** All seven identified in
reasoning (including a careful, honest wrestle with the snapshot contract), both traps
cleared — but the output never left the thinking stage: no header, no numbered defects, cut
off mid line-numbering. Consistent with its audition truncation: these API models spend
their token budget reasoning aloud. Fixable with a system-prompt output contract + higher
max_tokens; unfixed, they cannot hold a reporting seat.

**gemma4:12b — 4.5.** Real analysis underneath: caught the claim bug, ZeroDivision, purge
skip, shallow snapshot, and reasoned its way to the priority-sort defect. But it MISSED the
mutable default (considered it, talked itself out), and — the worst single event of the
drill — examined the pagination bug and CLEARED it ("just returns a shorter list"). A
confident wrong "cleared" is more dangerous than a miss. No report format, wrong line
numbers, spinner artifacts, truncated. Triage duty only, always behind a verifier.

**deepseek-coder 1.3B — −7.0, cut from audit duty.** Ignored the format wholesale; six
vague or outright wrong claims (called claim()'s intended done/obsolete refusal a defect;
claimed drop_done doesn't work — it does; garbled snapshot into self-contradiction), zero
line numbers, zero scenarios, and prescribed fixes, which the house rules ban. Retired from
any review lane; at most autocomplete fodder.

## Fleet lessons for Friday

1. The three frontier chat/CLI seats (Gaspar, Baltazar, Sol) are report-discipline capable
   TODAY — identical ground truth found independently, zero false positives across all
   three, perfect format. The core council is battle-ready.
2. Raw-API models need an output contract (system prompt: "emit ONLY the final report") and
   generous max_tokens, or their reasoning IS their output. Do not seat them for reports
   without this harness.
3. Local bench: gemma4:12b = supervised triage only; deepseek-coder 1.3B = cut.
4. Process: the collector of reports should be a NON-entrant next time (a participant wrote
   the collection summary), and collection summaries must never enumerate findings while any
   seat is still outstanding — that is how the Sol asterisk happened.
5. Baltazar re-brief: CLOSED, confirmed by conduct under fire.
