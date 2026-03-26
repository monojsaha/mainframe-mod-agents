---
applyTo: services/**/src/test/**
---

# Test Standards

## Framework Stack
- JUnit 5 (`@Test`, `@ParameterizedTest`, `@ExtendWith`)
- Mockito for unit test mocking
- REST Assured for integration/API tests
- Testcontainers (if local DB2 container available; skip in PoC CI if not licensed)

## Test Categories
| Category | Annotation | Scope |
|----------|-----------|-------|
| Unit | `@Tag("unit")` | Domain + application layer; no I/O |
| Integration | `@Tag("integration")` | Infrastructure layer; real DB2 connection |
| API | `@Tag("api")` | Controller layer via REST Assured |
| Parity | `@Tag("parity")` | Numerical equivalence: COBOL output vs Java output |

## Parity Tests
- Parity tests are the highest priority in this PoC
- Reference the expected output from COBOL test data sets in `legacy-src/` or documented in `stage-08-test-cases.md`
- Use `BigDecimal` assertions with explicit scale for monetary calculations
- Document the source COBOL program and test data reference in the test Javadoc

## Naming Convention
```
<ClassUnderTest>Test            ← unit tests
<ClassUnderTest>IntegrationTest ← integration tests
<Feature>ParityTest             ← parity tests
```

## Assertions
- Use AssertJ (`assertThat`) — not JUnit `assertEquals`
- For monetary values: always assert scale and precision explicitly
