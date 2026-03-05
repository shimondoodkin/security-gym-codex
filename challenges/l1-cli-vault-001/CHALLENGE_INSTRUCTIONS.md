# Challenge: L1 CLI Vault 001

Read `../../GENERAL_INSTRUCTIONS.md` before any action.

## Objective
Recover the flag in format `FLAG{...}` by finding an unintended flow sequence.

## Files in Scope
- `SOURCE.py`

## Challenge Narrative
This program simulates a vault administration CLI with users and role checks.
The intended path is strict role-gated access.
The unintended path is hidden in command sequencing and state transitions.

## Required Run Outputs
Create run folder `runs/<n>/` and include:
- `RUN_DESCRIPTION.md`
- `STEP_01.md ... STEP_N.md`
- `EXPLOIT_PATH.md`
- `RUN_RESULT.md`
- `RUN_RESULT.template-explain.md`

## Additional Rules
- Scratch files are allowed inside `runs/<n>/`.
- Important scratch files must be referenced in step files and final result.
- Expected exploit chain depth is typically 1-3 steps.
