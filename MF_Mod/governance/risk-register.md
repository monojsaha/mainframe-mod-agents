# Risk Register — MF App Modernisation PoC

| ID | Risk | Probability | Impact | Severity | Mitigation | Owner |
|----|------|------------|--------|----------|-----------|-------|
| R-01 | DB2 z/OS JDBC connectivity unavailable in PoC environment | Medium | High | High | Provision JDBC test credentials in sprint 1; mock layer as fallback | Java Architect |
| R-02 | COBOL source incomplete or missing members | Low | High | Medium | Verify inventory in Stage 1 before proceeding; flag blockers early | Mainframe SME |
| R-03 | Business rule misextraction (agent hallucination) | Medium | High | High | Human review of every PROG-*.md before Stage 6; parity tests in Stage 8 | PoC Lead |
| R-04 | Generated Java does not achieve numerical parity with COBOL | Medium | High | High | Parity test suite in Stage 8; `BigDecimal` for all monetary calculations | QA Lead |
| R-05 | Scope creep beyond MF App | Low | Medium | Medium | copilot-instructions.md scope lock; change control via Product Owner | PoC Lead |
| R-06 | Data migration requirement surfaces during analysis | Low | High | High | DB2 repoint constraint is fixed; escalate to Product Owner if migration needed | Java Architect |
