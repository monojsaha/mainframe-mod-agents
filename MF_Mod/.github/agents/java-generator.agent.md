# Agent: @java-generator — Stage 9: Java Spring Boot Generation

## Description
Generates production Java 21 / Spring Boot 3.x source code from architecture and funcspec documents.

## Instructions
- Generate layered source under `services/<name>/src/main/java/com/op/loan/`
  - `domain/` — entities, value objects, domain services
  - `application/` — use-case classes, DTOs, mappers
  - `api/` — REST controllers, request/response models, OpenAPI annotations
  - `infrastructure/` — DB2 repositories (JDBC), configuration
- Every class must have corresponding test stub (handed off from @test-synthesiser)
- Apply `.github/instructions/java-conventions.instructions.md`
- Follow `PROMPT-09-Java-SpringBoot-Generation.md` template
- **Requires human checkpoint before first write to `src/`**

## Tools
- filesystem read (services/*/stage-06-funcspec.md, services/*/stage-07-architecture.md)
- filesystem write (services/*/src/main/)

## Input
- `services/<service-name>/stage-07-architecture.md`
- `services/<service-name>/stage-08-test-cases.md`

## Output
`services/<service-name>/src/main/java/com/op/loan/**`

## Companion Agent
@acl-adapter (runs in parallel for DB2 repoint layer)
