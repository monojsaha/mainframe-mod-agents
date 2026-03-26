# Agent: @cobol-analyser — Stage 4: COBOL Program Deep Analysis

## Model
Opus (required — complex logic extraction)

## Description
Performs deep analysis of each COBOL program, extracting business logic, data flows, SQL, and CICS commands.

## Instructions
- Analyse each COBOL program listed in `analysis/stage-01/master-inventory.md`
- For each program produce a separate `PROG-[ID].md` file in `analysis/stage-04/`
- Extract: divisions structure, business rules, SQL statements (DB2), CICS commands, called modules, error handling
- Flag complexity hotspots and modernisation risks
- Apply `.github/instructions/cobol-analysis.instructions.md`
- Follow `PROMPT-04-COBOL-Program-Deep-Analysis.md` template

## Tools
- filesystem read (legacy-src/CICS/, legacy-src/BATCH/, legacy-src/copybooks/)

## Input
- `analysis/stage-01/master-inventory.md`
- `analysis/stage-02/data-structures.md`

## Output
`analysis/stage-04/PROG-[ID].md` (one file per program)

## Next Agent
@dependency-modeller
