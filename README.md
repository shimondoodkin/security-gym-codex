# Security Research Gym (Instruction-Only)

This project is a benchmark workspace for testing whether LLM agents can act like security researchers and discover **flow/logic exploit chains** (not only static or memory bugs).

It is designed around:
- challenge packs with source or disassembly artifacts
- manager-driven investigation with sequential subagent steps
- reproducible run folders (`runs/<n>/`) containing evidence, exploit path notes, and final verdicts
- cross-run learning via `WHAT_WORKS.md`

Current status:
- v1 includes one L1 source example challenge (`l1-cli-vault-001`)
- framework is markdown/instruction-driven (no required harness yet)

## How to Run

This repository is currently an **instruction-driven gym**, not an executable harness.
You run challenges by giving the instruction files to an LLM manager agent and having it produce run artifacts.

## 1) Pick a Challenge
Example challenge:
- `challenges/l1-cli-vault-001/`

Core files:
- `GENERAL_INSTRUCTIONS.md`
- `challenges/<challenge_id>/CHALLENGE_INSTRUCTIONS.md`
- source/disasm files in that challenge folder

## 2) Start a Run
Tell your agent to:
1. Read `GENERAL_INSTRUCTIONS.md`.
2. Read `challenges/<challenge_id>/CHALLENGE_INSTRUCTIONS.md`.
3. Create next ordinal run folder: `challenges/<challenge_id>/runs/<n>/`.

Example for the included challenge:
- `challenges/l1-cli-vault-001/runs/0/`
- then `.../runs/1/`, etc.

## 3) Manager/Subagent Workflow
- Manager runs the overall investigation.
- Manager uses a **new subagent per step**, sequentially.
- Manager passes objective + hypothesis + links to prior evidence each step.

Suggested phases:
1. Recon
2. Capability mapping
3. Chain hypothesis
4. Exploit attempt
5. Verification + self-judgment

## 4) Allowed Workspace Writes
Inside the active run folder, the agent may create:
- required outputs
- scratch files and temporary scripts
- notes, extracted logs, and experiments

Important: key scratch files should be referenced in `STEP_*.md` and listed in `RUN_RESULT.md`.

## 5) Required Files Per Run
In `challenges/<challenge_id>/runs/<n>/` create:
- `RUN_DESCRIPTION.md`
- `STEP_01.md ... STEP_N.md`
- `EXPLOIT_PATH.md`
- `RUN_RESULT.md`
- `RUN_RESULT.template-explain.md` (copy from root or challenge)

Template source:
- `RUN_RESULT.template-explain.md`

## 6) Success/Failure Format
`RUN_RESULT.md` first line must be exactly:
- `RESULT: SUCCESS`
or
- `RESULT: FAIL`

Human review is final authority, even if the agent self-judges success.

## 7) Find Successful Runs
PowerShell:

```powershell
Get-ChildItem -Recurse -Filter RUN_RESULT.md | Select-String "RESULT: SUCCESS"
```

## 8) Create New Challenges
Use:
- `CREATE_REQUEST.template.md`
- `CHALLENGE_CREATION_GUIDE.md`
- `LEVEL_1_SOURCE_CREATION.md`
- `LEVEL_2_DISASM_CREATION.md`

Flow:
1. Copy `CREATE_REQUEST.template.md` to `CREATE_REQUEST.md`.
2. Fill level/language/difficulty/code_poorness/chain bounds.
3. Ask your creator agent to generate a new challenge pack under `challenges/<new_id>/` following the guides.

## 9) Update Learning Memory
After each run, append findings to:
- `WHAT_WORKS.md`

Include:
- challenge id/run id
- pattern name
- status (`confirmed working`, `promising`, `discarded`)
- links to key artifacts
