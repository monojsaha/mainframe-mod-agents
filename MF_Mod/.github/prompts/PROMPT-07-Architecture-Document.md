# PROMPT-07: Architecture Document

## Agent
@architect (Opus)

## Objective
Produce the technical architecture document for a target microservice.

## Input
`services/<service-name>/stage-06-funcspec.md`

## Instructions
Produce `services/<service-name>/stage-07-architecture.md`:

### Structure
1. **Context & Constraints**: PoC scope, DB2 z/OS repoint constraint, cloud-native target
2. **Architecture Decisions**: Reference or create ADRs in `governance/adr/`
3. **Component Diagram**: Mermaid `C4Component` or `graph LR` showing layers
4. **API Design**: OpenAPI-style endpoint summary table
5. **Data Access Layer**: DB2 z/OS JDBC repoint strategy, connection pool, transaction boundaries
6. **Spring Boot Package Layout**: Exact package tree for `src/main/java/com/op/loan/<service>/`
7. **Security**: Authentication (JWT/OAuth2), authorisation (Spring Security), PII handling
8. **Deployment Topology**: Container image, environment variables, health checks
9. **Open Issues / Risks**: Items requiring human decision before Stage 9

## ADR Convention
Filename: `governance/adr/ADR-NNN-<short-title>.md`
Sections: Status | Context | Decision | Consequences

## Output Files
- `services/<service-name>/stage-07-architecture.md`
- `governance/adr/ADR-NNN-*.md` (as needed)
