# Challenge Creation Guide

This guide defines how to create challenge packs for the Security Research Gym.

## Scope
- L1: source-visible flow-logic challenges.
- L2: disassembly/binary-oriented flow-logic challenges.

## Request-Driven Creation
Start from a user-supplied `CREATE_REQUEST.md` (see template at repo root).
Required knobs:
- `level`: L1 or L2
- `language`: for L1 (`python`, `c`, `rust`, `cpp`)
- `difficulty`: 1-5
- `code_poorness`: 1-5 (messy logic and guard quality)
- `chain_steps_min` / `chain_steps_max`
- flaw types
- flag format

## Standard Challenge Layout
Each challenge must live at `challenges/<challenge_id>/` and include:
- `CHALLENGE_INSTRUCTIONS.md`
- Source or disassembly files (depending on level)
- `runs/` directory
- `RUN_RESULT.template-explain.md`

Optional:
- `NOTES.md`, `HINTS.md`, `CONTEXT.md`

## Mandatory Instruction Clause
`CHALLENGE_INSTRUCTIONS.md` must instruct the solver to read `../../GENERAL_INSTRUCTIONS.md` first.

## Run Artifact Contract
Every solver run must create a new ordinal run folder `runs/<n>/` with:
- `RUN_DESCRIPTION.md`
- `STEP_*.md`
- `EXPLOIT_PATH.md`
- `RUN_RESULT.md`
- `RUN_RESULT.template-explain.md`

## Scratch Files Policy
Challenge authors must allow scratch experimentation under `runs/<n>/`.
The challenge must not require writes outside the run folder.

## Quality Bar
- Intended path should look valid.
- Unintended path must exist and be reproducible.
- Exploit chain depth must match request bounds.
- At least one plausible false path should exist.
- Logic/flow flaws should dominate over raw memory corruption in default configs.

## Deliverable Completeness Checklist
- [ ] Challenge files exist in expected locations.
- [ ] Unintended chain is present and documented in author notes.
- [ ] Flag format is consistent and verifiable.
- [ ] `RUN_RESULT.md` schema can be filled from real evidence.
- [ ] Challenge can be analyzed with markdown artifacts only.
