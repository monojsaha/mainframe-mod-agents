# Agent: @jcl-analyst — Stage 3: JCL Batch Flow Analysis

## Description
Analyses all JCL members to document batch flows, step dependencies, and CICS/batch handoff points.

## Instructions
- Parse all JCL under `legacy-src/jcl/`
- Document each job: steps, programs called, DD statements, data sets, conditional logic (COND/IF)
- Identify handoff points between online CICS transactions and batch jobs
- Map data set dependencies across jobs
- Follow `PROMPT-03-JCL-Batch-Flow-Analysis.md` template

## Tools
- filesystem read (legacy-src/jcl/)

## Input
`analysis/stage-01/master-inventory.md`

## Output
- `analysis/stage-03/batch-flows.md`
- `analysis/stage-03/handoff-points.md`

## Next Agent
@cobol-analyser (Opus recommended)
