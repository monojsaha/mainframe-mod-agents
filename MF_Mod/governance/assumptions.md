# Assumptions — MF App Modernisation PoC

| ID | Assumption | Impact if Wrong |
|----|-----------|----------------|
| A-01 | All COBOL source for the MF App is available in `legacy-src/` at PoC start | Stage 1 cannot complete; PoC blocked |
| A-02 | DB2 z/OS schema will not change during the PoC | Repoint adapters may need regeneration |
| A-03 | Java services will connect to the existing DB2 z/OS subsystem via JDBC (Type 4 driver) — no data migration | Architecture must be redesigned if not true |
| A-04 | IBM DB2 JDBC driver (JCC) licence is available for development use | Cannot generate or test DB2 adapters |
| A-05 | Target deployment platform supports outbound connectivity to z/OS DB2 port | Integration testing blocked |
| A-06 | GitHub Copilot Enterprise licence is available for all PoC team members | Agent-based workflow unavailable |
| A-07 | Opus model access is available for Stages 4–7 | Quality of analysis outputs may be reduced |
| A-08 | No new business requirements will be added to the MF App scope during the PoC | Funcspecs and architecture documents invalidated |
