# Agent: @acl-adapter — Stage 9J: DB2 z/OS JDBC Repoint Adapters

## Description
Generates the DB2 z/OS JDBC repoint (Anti-Corruption Layer) adapter classes, retaining the existing DB2 schema with no data migration.

## Instructions
- For each DB2 table accessed by the service (from `analysis/stage-04/` SQL extracts), generate a Spring Data JDBC repository and row-mapper
- Preserve original DB2 z/OS column names as-is; map to Java field names via `@Column` annotations
- Configure datasource properties for z/OS DB2 JDBC driver (type 4)
- Apply `.github/instructions/db2-zos-repoint.instructions.md`
- Output to `services/<name>/src/main/java/com/op/loan/infrastructure/db2/`
- **Requires human checkpoint before writing**

## Tools
- filesystem read (legacy-src/ddl/, analysis/stage-04/)
- filesystem write (services/*/src/main/java/com/op/loan/infrastructure/db2/)

## Input
- `legacy-src/ddl/` (schema reference)
- `analysis/stage-04/PROG-*.md` (SQL statements)

## Output
`services/<service-name>/src/main/java/com/op/loan/infrastructure/db2/`
