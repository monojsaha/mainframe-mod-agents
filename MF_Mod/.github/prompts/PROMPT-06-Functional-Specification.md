# PROMPT-06: Functional Specification

## Agent
@funcspec-writer (Opus)

## Objective
Produce a functional specification for a target microservice.

## Input
- `analysis/stage-05/service-boundaries.md`
- Relevant `analysis/stage-04/PROG-*.md` files for the service

## Instructions
Produce `services/<service-name>/stage-06-funcspec.md`:

### Structure
1. **Document Header**: Service name, version, date, author (agent ID), source programs referenced
2. **Purpose & Scope**: What business capability this service delivers
3. **Functional Requirements**: Numbered list (FR-001, FR-002, …) — one requirement per business rule
4. **Business Rules**: Formal statement of each rule, cross-referenced to source COBOL program and paragraph
5. **Data Model**: Input and output data structures (reference `type-mapping.md` for types)
6. **API Operations**: For each operation — name, HTTP method/path (draft), inputs, outputs, error responses
7. **Error Handling**: Error codes, messages, retry behaviour
8. **Non-Functional Requirements**: Performance baseline (from CICS stats if available), auditability, idempotency

## Checkpoint
> **HUMAN APPROVAL REQUIRED** before writing to `services/`. Confirm scope with PoC lead.

## Output File
`services/<service-name>/stage-06-funcspec.md`
