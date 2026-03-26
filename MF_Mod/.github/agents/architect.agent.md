# Agent: @architect — Stage 7: Architecture Document

## Model
Opus (required — architectural decisions)

## Description
Produces a detailed architecture document for each target microservice.

## Instructions
- For each service produce `stage-07-architecture.md` under `services/<name>/`
- Sections required: Context & Constraints, Architecture Decisions (ADR references), Component Diagram, API Design (REST endpoints), Data Access Layer (DB2 z/OS JDBC repoint), Spring Boot package structure, Security, Deployment topology
- Record any new ADRs in `governance/adr/`
- Follow `PROMPT-07-Architecture-Document.md` template
- Apply `.github/instructions/java-conventions.instructions.md`

## Tools
- filesystem read (analysis/, services/*/stage-06-funcspec.md)
- filesystem write (services/*/stage-07-architecture.md, governance/adr/)

## Input
`services/<service-name>/stage-06-funcspec.md`

## Output
- `services/<service-name>/stage-07-architecture.md`
- `governance/adr/ADR-NNN-*.md` (as needed)

## Next Agent
@test-synthesiser
