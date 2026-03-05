# Level 2 Disassembly Creation Guide

L2 challenges hide source and expose binary/disassembly artifacts while still testing flow-logic reasoning.

## Inputs
Use `CREATE_REQUEST.md` with:
- `level: L2`
- optional target architecture/toolchain hints
- difficulty, chain depth, flaw families

## Output Requirements
Under `challenges/<challenge_id>/` include:
- `CHALLENGE_INSTRUCTIONS.md`
- binary/disasm artifacts
- lightweight context files (calling convention, runtime assumptions if needed)
- `RUN_RESULT.template-explain.md`
- `runs/`

## Design Constraints
- Keep primary exploitability tied to control/state flow, not only memory corruption.
- Ensure the unintended chain is inferable from provided artifacts.
- Include at least one misleading path.

## CHALLENGE_INSTRUCTIONS.md Essentials
- mandatory read of `../../GENERAL_INSTRUCTIONS.md`
- objective and flag format
- provided files and known constraints
- required run artifacts under `runs/<n>/`

## Author-Only Answer Key (private)
Maintain private documentation of:
- minimal exploit chain
- validating evidence points in disassembly
- expected false positives and dead ends
