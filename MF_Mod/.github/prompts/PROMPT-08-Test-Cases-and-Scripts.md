# PROMPT-08: Test Cases & Scripts

## Agent
@test-synthesiser

## Objective
Derive a comprehensive test catalogue and generate JUnit 5 test class stubs.

## Input
- `services/<service-name>/stage-06-funcspec.md`
- `services/<service-name>/stage-07-architecture.md`
- Relevant `analysis/stage-04/PROG-*.md` (for parity test data)

## Instructions

### stage-08-test-cases.md
Produce a structured test catalogue:
| TC-ID | Category | Name | Pre-conditions | Steps | Expected Result | Source FR / COBOL Ref |
|-------|----------|------|---------------|-------|----------------|----------------------|

Categories: Unit, Integration, API, Parity

### JUnit 5 Stubs
For each test class, generate a stub with:
- Class annotation (`@Tag`, `@ExtendWith`)
- One `@Test` method per test case (body: `// TODO: implement`)
- Javadoc on each method referencing TC-ID and source COBOL

Apply `.github/instructions/test-standards.instructions.md`.

## Output Files
- `services/<service-name>/stage-08-test-cases.md`
- `services/<service-name>/src/test/java/com/op/loan/<service>/**/*Test.java`
