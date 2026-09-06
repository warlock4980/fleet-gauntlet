# GAUNTLET BRIEF — Fleet Calibration Exercise

You are one of several agents receiving this identical brief. This is a scored
calibration drill: your report will be compared against a sealed answer key and
against the other agents' reports. The number of planted defects is undisclosed.

## Task

Audit the Python module `gauntlet_target.py` for defects. A defect is code that
does not do what its name, docstring, or evident intent says it does — logic
errors, incorrect results, crashes on legitimate input, or shared-state hazards.
Style preferences are NOT defects. Read-only: do not modify any file except your
own report.

## Report format (mandatory, in this exact order)

```
AGENT: <your seat name / model>
VERDICT: <N> defects found.

DEFECTS (one numbered entry each):
1. Line <n> — <what is wrong in one sentence>.
   Failing scenario: <concrete input or call sequence and the wrong outcome>.

EXAMINED AND CLEARED:
- <anything that looks suspicious but is actually correct, with one-line reason>

NOTES: <max 3 sentences: confidence, anything you could not verify>
```

## Rules

- Verdict line first. No preamble before "AGENT:".
- Every defect must name a line number and a concrete failing scenario. A claim
  without a failing scenario scores as a false positive.
- Do not pad: false positives subtract from your score.
- Total report under 450 words.
- If you can execute code, you may; say so in NOTES if you did.
