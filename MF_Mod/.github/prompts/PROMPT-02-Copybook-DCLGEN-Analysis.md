# PROMPT-02: Copybook & DCLGEN Analysis

## Agent
@copybook-analyst

## Objective
Document all data structures defined in Copybooks and DCLGENs; produce Java type mappings.

## Input
- `analysis/stage-01/master-inventory.md`
- All files under `legacy-src/copybooks/` and `legacy-src/dclgens/`

## Instructions

### data-structures.md
For each Copybook / DCLGEN, document:
- File name and path
- Purpose (inferred from name and contents)
- Full hierarchical data structure (level numbers, field names, PICTURE clauses, USAGE)
- Reuse: list all programs that COPY this member

### type-mapping.md
Produce a flat mapping table:
| Copybook | Field Name | COBOL PIC | COBOL USAGE | Java Type | Notes |
|---------|-----------|-----------|------------|-----------|-------|

## Notes
- `COMP-3` (packed decimal) → `BigDecimal`
- `COMP` / `BINARY` → `int` / `long` depending on size
- `PIC X(n)` → `String` (note: trim trailing spaces at runtime)
- `PIC 9(m)V9(n)` → `BigDecimal` with scale n

## Output Files
- `analysis/stage-02/data-structures.md`
- `analysis/stage-02/type-mapping.md`
