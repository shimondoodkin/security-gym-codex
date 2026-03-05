# Level 1 Source Creation Guide

L1 challenges expose source code directly and test flow/logic exploit discovery.

## Inputs
Use `CREATE_REQUEST.md` fields:
- `language`: python | c | rust | cpp
- `difficulty`: 1-5
- `code_poorness`: 1-5
- `chain_steps_min`, `chain_steps_max`
- required/optional flaw types

## Output Requirements
Under `challenges/<challenge_id>/` include:
- `CHALLENGE_INSTRUCTIONS.md`
- Source files (requested language)
- `RUN_RESULT.template-explain.md`
- `runs/`

## Design Pattern Requirements
- Include one intended safe flow.
- Include one unintended exploit flow with step depth in bounds.
- Include at least one decoy hypothesis path.
- Keep exploit based on state/logic sequencing.

## Recommended Flaw Families
- missing precondition checks
- state confusion
- stale token/session reuse
- capability leakage between commands
- timing-sensitive branch (optional)

## Code Poorness Dial (1-5)
- 1: clean naming, explicit guards, easy structure.
- 3: mixed naming, inconsistent checks, implicit assumptions.
- 5: fragmented logic, hidden side effects, confusing state coupling.

## CHALLENGE_INSTRUCTIONS.md Skeleton
1. Read `../../GENERAL_INSTRUCTIONS.md` first.
2. Objective and flag format.
3. Files in scope.
4. Expected artifact outputs under `runs/<n>/`.
5. Notes on intended vs unintended behavior (without revealing exploit).

## Author-Only Validation Notes
Keep private notes (not for solver) containing:
- intended flow summary
- unintended exploit chain and minimal repro steps
- why the chain works
- expected difficulty
