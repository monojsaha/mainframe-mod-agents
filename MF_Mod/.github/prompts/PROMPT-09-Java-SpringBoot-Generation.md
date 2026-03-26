# PROMPT-09: Java Spring Boot Generation

## Agent
@java-generator + @acl-adapter

## Objective
Generate production-ready Java 21 / Spring Boot 3.x source code for the target microservice.

## Input
- `services/<service-name>/stage-07-architecture.md`
- `services/<service-name>/stage-08-test-cases.md`
- `legacy-src/ddl/` (for @acl-adapter)

## CHECKPOINT
> **HUMAN APPROVAL REQUIRED** — confirm architecture document is signed off before proceeding.

## Instructions (@java-generator)
Generate source under `services/<service-name>/src/main/java/com/op/loan/<service>/`:

### domain/
- One entity/record per aggregate root identified in funcspec
- Value objects for monetary amounts (`Money`), identifiers
- Domain service interfaces

### application/
- One use-case class per functional requirement group
- DTOs (Java records preferred)
- MapStruct mapper interfaces

### api/
- `@RestController` per bounded context
- OpenAPI annotations (`@Operation`, `@ApiResponse`)
- Global exception handler (`@ControllerAdvice`)

### infrastructure/
- Delegated to @acl-adapter for DB2 layer
- `application.yml` with profile-based DB2 datasource config

## Instructions (@acl-adapter)
Generate under `services/<service-name>/src/main/java/com/op/loan/<service>/infrastructure/db2/`:
- One `Repository` interface + `Db2*Repository` impl per DB2 table accessed
- `RowMapper` implementations preserving original column names
- `application-{profile}.yml` datasource stanzas (no credentials — placeholders only)

Apply `.github/instructions/java-conventions.instructions.md` and `.github/instructions/db2-zos-repoint.instructions.md`.

## Output
`services/<service-name>/src/main/java/com/op/loan/<service>/**`
