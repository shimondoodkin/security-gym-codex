# Run Description

- Challenge ID: `l1-cli-vault-001`
- Run ID: `1`
- Objective: Recover `FLAG{...}` via unintended flow sequencing.
- Hypothesis: A normal user can chain `ticket -> assume -> tz UTC+OPS -> read` to satisfy both vault gate conditions without legitimate admin workflow.
