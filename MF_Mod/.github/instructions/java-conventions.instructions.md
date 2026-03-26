---
applyTo: services/**/src/**
---

# Java Coding Conventions

## Target Stack
- Java 21 (use records, sealed classes, pattern matching where appropriate)
- Spring Boot 3.x
- Spring Data JDBC (not JPA — DB2 z/OS compatibility)
- Maven (not Gradle)

## Package Structure
```
com.op.loan.<service-short-name>/
  domain/          ← pure business logic, no framework dependencies
  application/     ← use cases, DTOs, MapStruct mappers
  api/             ← REST controllers, OpenAPI annotations
  infrastructure/  ← DB2 repositories, external integrations
```

## Naming Conventions
- Domain entities: `LoanApplication`, `LoanAssessment` (PascalCase nouns)
- Use-case classes: `SubmitLoanApplicationUseCase`, `AssessLoanRiskUseCase`
- REST controllers: `LoanApplicationController`
- Repositories: `LoanApplicationRepository` (interface), `Db2LoanApplicationRepository` (impl)

## Code Style
- No field injection (`@Autowired`) — constructor injection only
- All public API methods must have Javadoc
- Use `Optional<T>` rather than returning `null`
- Validation via Jakarta Bean Validation (`@NotNull`, `@Size`, etc.)
- Exceptions: domain exceptions extend `RuntimeException`; map to HTTP status in `@ControllerAdvice`

## Logging
- SLF4J + Logback; structured JSON in production profile
- Log at INFO on entry/exit of use-case execute methods
- Log at DEBUG for SQL parameter binding

## OpenAPI
- Annotate all controller methods with `@Operation`, `@ApiResponse`
- Use `springdoc-openapi` 2.x
