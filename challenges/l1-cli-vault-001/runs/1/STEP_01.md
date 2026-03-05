# STEP 01 - Capability Recon

## Objective
Map commands, state transitions, and vault preconditions.

## Hypothesis
The CLI exposes commands that mutate auth state and maintenance mode independently.

## Findings
- `read` requires:
  - `current_user.role == admin`
  - `maintenance_mode == True`
- `ticket <username>` sets `pending_user` with no role check.
- `assume` switches `current_user` to `pending_user` with no auth check.
- `tz UTC+OPS` toggles `maintenance_mode = True` for any user.

## Evidence
- Source file: `../../SOURCE.py`
