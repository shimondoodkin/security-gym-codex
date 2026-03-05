# STEP 02 - Chain Construction

## Objective
Build the shortest viable exploit sequence.

## Hypothesis
Escalate identity to `ops` via ticket/assume, then enable maintenance via timezone bug, then read vault.

## Planned Chain
1. `ticket ops`
2. `assume`
3. `tz UTC+OPS`
4. `read`

## Why It Should Work
- Step 1+2 sets `current_user` to admin (`ops`).
- Step 3 enables maintenance mode globally.
- Step 4 now passes both read preconditions.
