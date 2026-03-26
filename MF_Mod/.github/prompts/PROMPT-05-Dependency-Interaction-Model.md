# PROMPT-05: Dependency & Interaction Model

## Agent
@dependency-modeller (Opus)

## Objective
Synthesise all Stage 4 analyses into a dependency graph and microservice boundary proposals.

## Input
All files under `analysis/stage-04/PROG-*.md`

## Instructions

### dependency-graph.md
- Directed graph in Mermaid `graph TD` syntax showing:
  - Program → Program (CALL dependencies)
  - Program → Copybook
  - Program → DB2 Table
  - JCL Job → Program
- Highlight shared nodes (copybooks or tables used by multiple programs)
- Identify clusters that naturally form service boundaries

### service-boundaries.md
Propose microservice boundaries:
| Service Name | Programs Included | DB2 Tables Owned | Shared Tables (read-only) | Rationale |
|-------------|------------------|-----------------|--------------------------|-----------|

#### Anti-patterns to flag
- God programs (> 2000 LOC, > 10 table accesses) — propose decomposition
- Circular dependencies between programs
- Shared mutable working storage patterns

## Output Files
- `analysis/stage-05/dependency-graph.md`
- `analysis/stage-05/service-boundaries.md`
