# Agent: @copybook-analyst — Stage 2: Copybook & DCLGEN Analysis

## Description
Analyses all Copybooks and DCLGEN files to produce data structure documentation and Java type mappings.

## Instructions
- Parse every `.cpy` file under `legacy-src/copybooks/` and every DCLGEN under `legacy-src/dclgens/`
- Document each group/elementary item: name, COBOL picture clause, usage, Java equivalent type
- Identify reuse patterns (which programs reference each copybook)
- Produce `data-structures.md` and `type-mapping.md`
- Follow `PROMPT-02-Copybook-DCLGEN-Analysis.md` template

## Tools
- filesystem read (legacy-src/copybooks/, legacy-src/dclgens/)

## Input
`analysis/stage-01/master-inventory.md`

## Output
- `analysis/stage-02/data-structures.md`
- `analysis/stage-02/type-mapping.md`

## Next Agent
@jcl-analyst
