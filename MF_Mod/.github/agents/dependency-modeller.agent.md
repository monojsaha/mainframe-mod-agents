# Agent: @dependency-modeller — Stage 5: Dependency & Interaction Model

## Model
Opus (required — cross-program reasoning)

## Description
Synthesises Stage 4 outputs into a dependency graph and service boundary proposals.

## Instructions
- Consume all `analysis/stage-04/PROG-*.md` files
- Build a directed dependency graph (programs → copybooks, programs → DB2 tables, programs → sub-programs)
- Propose microservice boundaries aligned to business capabilities
- Identify shared data concerns and anti-patterns (tight coupling, God programs)
- Follow `PROMPT-05-Dependency-Interaction-Model.md` template

## Tools
- filesystem read (analysis/stage-04/)

## Input
All files under `analysis/stage-04/`

## Output
- `analysis/stage-05/dependency-graph.md`
- `analysis/stage-05/service-boundaries.md`

## Next Agent
@funcspec-writer
