---
applyTo: analysis/stage-04/**
---

# COBOL Analysis Instructions

## Scope
These instructions apply when analysing COBOL source files and writing output to `analysis/stage-04/`.

## Analysis Standards
- Always identify the `PROGRAM-ID` as the canonical identifier
- Document all `EXEC SQL` blocks verbatim with table/column names extracted
- Document all `EXEC CICS` commands with their options
- List all `COPY` statements with resolved copybook names
- Flag any `PERFORM VARYING` or `EVALUATE` blocks as potential business-rule hotspots
- Note any use of `COMP-3`, `COMP`, `BINARY` for numeric precision concerns in Java

## Output Structure (per PROG-[ID].md)
1. Program Overview (ID, type, estimated LOC, purpose)
2. Data Division Summary (working storage groups, linkage section)
3. Business Logic Summary (paragraph-level narrative)
4. SQL Catalogue (statement type, tables, predicates)
5. CICS Command Catalogue
6. Called Modules / Sub-programs
7. Copybook Dependencies
8. Modernisation Risk Assessment (Low / Medium / High + rationale)
9. Recommended Java Equivalent Pattern

## Conventions
- Risk: **Low** = straightforward CRUD; **Medium** = complex logic or multiple tables; **High** = legacy patterns, GOTOs, or shared working storage
