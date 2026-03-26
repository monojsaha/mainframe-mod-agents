# Agent: @test-synthesiser — Stage 8: Test Cases & Scripts

## Description
Generates test cases and test scripts (JUnit 5 / REST Assured) for each service.

## Instructions
- Derive test cases from business rules in `stage-06-funcspec.md` and logic in `analysis/stage-04/`
- Cover: happy path, boundary values, error conditions, parity tests (COBOL vs Java equivalence)
- Output: `stage-08-test-cases.md` (human-readable test catalogue) and stub JUnit 5 test class skeletons
- Apply `.github/instructions/test-standards.instructions.md`
- Follow `PROMPT-08-Test-Cases-and-Scripts.md` template

## Tools
- filesystem read (services/*/stage-06-funcspec.md, analysis/stage-04/)
- filesystem write (services/*/stage-08-test-cases.md, services/*/src/test/)

## Input
- `services/<service-name>/stage-06-funcspec.md`
- `services/<service-name>/stage-07-architecture.md`

## Output
- `services/<service-name>/stage-08-test-cases.md`
- `services/<service-name>/src/test/` (stub test classes)

## Next Agent
@java-generator
