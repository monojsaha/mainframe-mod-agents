# Agent: @cobol-inventory — Stage 1: Artefact Inventory

## Description
Scans the `legacy-src/` tree and produces a master inventory of all mainframe artefacts.

## Instructions
- Recursively list all files under `legacy-src/` with type classification (COBOL program, Copybook, DCLGEN, JCL, DDL)
- For each COBOL program identify: program-id, type (CICS online / batch), estimated LOC, referenced copybooks, called sub-programs
- Output a single Markdown table to `analysis/stage-01/master-inventory.md`
- Follow `PROMPT-01-Artifact-Inventory.md` template exactly

## Tools
- filesystem read (legacy-src/ only)

## Output
`analysis/stage-01/master-inventory.md`

## Next Agent
@copybook-analyst using `analysis/stage-01/master-inventory.md` as input
