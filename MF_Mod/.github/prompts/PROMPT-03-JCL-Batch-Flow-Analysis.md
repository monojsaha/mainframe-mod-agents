# PROMPT-03: JCL Batch Flow Analysis

## Agent
@jcl-analyst

## Objective
Document all batch job flows, step dependencies, and CICS↔batch handoff points.

## Input
- `legacy-src/jcl/`
- `analysis/stage-01/master-inventory.md`

## Instructions

### batch-flows.md
For each JCL job:
- Job name, purpose, schedule (if determinable)
- Step-by-step breakdown: step name, program, key DD statements, data sets
- Conditional logic (COND parameters or IF/THEN/ELSE constructs)
- Return code handling
- Estimated runtime characteristics (if EXEC TIME or comments indicate)

### handoff-points.md
Document all integration points between online (CICS) and batch:
| Handoff ID | Direction | CICS Program | JCL Job | Mechanism (file/queue/DB2) | Data Set / Table | Notes |

## Output Files
- `analysis/stage-03/batch-flows.md`
- `analysis/stage-03/handoff-points.md`
