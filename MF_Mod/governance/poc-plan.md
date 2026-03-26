# 12-Week PoC Schedule — MF App Modernisation

## Phases

| Week | Phase | Stages | Key Deliverables | Checkpoint |
|------|-------|--------|-----------------|-----------|
| 1 | Setup | — | Repo provisioned, `legacy-src/` populated, team onboarded | — |
| 2 | Analysis Sprint 1 | 1, 2 | `master-inventory.md`, `data-structures.md`, `type-mapping.md` | Review inventory completeness |
| 3 | Analysis Sprint 2 | 3 | `batch-flows.md`, `handoff-points.md` | Review batch flow accuracy |
| 4–5 | Deep Analysis | 4 | `PROG-*.md` (all programs) | SME review of each PROG-*.md |
| 6 | Dependency Modelling | 5 | `dependency-graph.md`, `service-boundaries.md` | Architecture team sign-off on boundaries |
| 7 | Specification | 6 | `stage-06-funcspec.md` × 3 services | **Human Checkpoint: Product Owner approval** |
| 8 | Architecture | 7 | `stage-07-architecture.md` × 3, initial ADRs | Architecture board review |
| 9 | Test Design | 8 | `stage-08-test-cases.md` × 3, test stubs | QA Lead sign-off |
| 10–11 | Code Generation | 9 | Generated Java source, DB2 adapters | **Human Checkpoint: Architect code review** |
| 12 | Parity & PoC Closure | — | Parity test results, risk register update, Go/No-Go decision | PoC Lead + Product Owner |

## Definition of Done (PoC)
- All 9 stages complete for at least one service (loan-origination-service)
- Parity tests pass for all monetary calculations
- Architecture Decision Records signed off
- Go/No-Go recommendation documented in `governance/poc-plan.md`
