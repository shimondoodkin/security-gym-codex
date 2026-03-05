# General Instructions for Security Research Gym

You are operating as a security research manager for flow-logic CTF challenges.

## Inputs
- Challenge pack under `challenges/<challenge_id>/`
- Global framework files at repo root
- Current challenge source/disassembly artifacts

## Mandatory First Step
1. Read this file.
2. Read `challenges/<challenge_id>/CHALLENGE_INSTRUCTIONS.md`.
3. Create the next run folder: `challenges/<challenge_id>/runs/<n>/` where `<n>` is the next integer.

## Manager-Subagent Orchestration
- Use one manager process for the whole run.
- Use a **new subagent for each step**, sequentially.
- For each subagent step, provide:
  - step objective
  - current hypothesis
  - links/paths to relevant prior artifacts
  - required output file path in the current run folder
- Do not skip writing artifacts.

## Suggested Investigation Phases (manager may adapt)
1. Recon: identify commands, state variables, trust boundaries.
2. Capability Mapping: list actions, preconditions, and side effects.
3. Chain Hypothesis: propose unintended step sequences.
4. Exploit Attempt: test the best chain.
5. Verification + Judgment: verify flag/result and record final verdict.

## Run Workspace Policy (explicit)
- You may create any intermediate/scratch files under `challenges/<challenge_id>/runs/<n>/`.
- Scratch files are encouraged for experiments (e.g., `scratch/notes.md`, temp scripts, extracted outputs).
- Do not write outside the current run folder except updating root `WHAT_WORKS.md`.
- Important scratch files must be referenced in `STEP_*.md` and listed in `RUN_RESULT.md`.

## Required Artifacts per Run
Inside `challenges/<challenge_id>/runs/<n>/` create:
- `RUN_DESCRIPTION.md`
- `STEP_01.md ... STEP_N.md`
- `EXPLOIT_PATH.md`
- `RUN_RESULT.md`
- `RUN_RESULT.template-explain.md` (copy template or include equivalent guidance)

## RUN_RESULT Rules
- First line must be exactly one of:
  - `RESULT: SUCCESS`
  - `RESULT: FAIL`
- Include fields:
  - `CHALLENGE_ID`
  - `RUN_ID`
  - `MODEL`
  - `DATETIME_UTC`
  - `FLAG_FOUND`
  - `CHAIN_LENGTH`
  - `EXPLOIT_REPRO_STEPS`
  - `KEY_EVIDENCE_LINKS`
  - `SCRATCH_ARTIFACTS`
  - `CONFIDENCE` (0-100)
  - `SELF_JUDGMENT_RATIONALE`
  - `LIMITATIONS`
  - `NEXT_BEST_ACTION`

## Self-Judgment and Human Review
- You must self-judge each run in `RUN_RESULT.md`.
- Human review is final authority.

## Learning Loop
- After every completed run, append one concise entry to `WHAT_WORKS.md` with:
  - challenge id + run id
  - pattern name
  - status: confirmed working | promising | discarded
  - links to key artifacts

## Searchability
- Successful runs should be discoverable by searching for `RESULT: SUCCESS` in `RUN_RESULT.md` files.
