# PROMPT-04: COBOL Program Deep Analysis

## Agent
@cobol-analyser (Opus)

## Objective
Produce a comprehensive analysis document for a single COBOL program.

## Input
- The COBOL source file (specified by caller)
- `analysis/stage-02/data-structures.md`
- `analysis/stage-02/type-mapping.md`

## Instructions
Produce `analysis/stage-04/PROG-[PROGRAM-ID].md` with the following sections:

### 1. Program Overview
- Program ID, source path, type (CICS/Batch), estimated LOC, inferred purpose

### 2. Division & Section Summary
- Brief description of ENVIRONMENT, DATA, and PROCEDURE divisions
- Key WORKING-STORAGE groups

### 3. Business Logic Narrative
- Paragraph-by-paragraph walkthrough of PROCEDURE DIVISION
- Identify the main processing flow and key decision points

### 4. SQL Catalogue
| Statement # | Type (SELECT/INSERT/UPDATE/DELETE) | Tables | Key Predicates | Notes |

### 5. CICS Command Catalogue
| Command | Options | Purpose |

### 6. Module Dependencies
- CALL statements (static and dynamic)
- COPY members used

### 7. Modernisation Risk Assessment
- Risk Level: Low / Medium / High
- Risk Factors (GOTOs, ALTER, shared WORKING-STORAGE, COMP-3 arithmetic, etc.)
- Recommended Java Pattern (e.g., REST endpoint + service class, batch job step, domain service)

### 8. Suggested Java Class Skeleton
Brief pseudo-code or class outline only — full generation is Stage 9.

## Output File
`analysis/stage-04/PROG-[PROGRAM-ID].md`
