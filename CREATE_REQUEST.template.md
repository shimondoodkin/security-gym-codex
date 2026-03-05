---
request_id: "req-YYYYMMDD-001"
challenge_id: "l1-cli-vault-001"
level: "L1"
language: "python"
difficulty: 3
code_poorness: 3
chain_steps_min: 1
chain_steps_max: 3
required_flaw_types:
  - "state-confusion"
  - "missing-precondition"
optional_flaw_types:
  - "timing-sensitive-branch"
flag_format: "FLAG{...}"
include_hints: false
binary_target: ""
---

Goal:
Create a challenge pack that requires flow/logic reasoning to find unintended exploit paths.

Constraints:
- Must require reading GENERAL_INSTRUCTIONS.md first.
- Must include unintended exploit path in the requested chain-length bounds.
- Must support standardized run artifacts under runs/<n>/.
- Must allow scratch/intermediate files inside the run folder.
