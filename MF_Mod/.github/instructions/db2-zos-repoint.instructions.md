---
applyTo: services/**/src/infrastructure/**
---

# DB2 z/OS JDBC Repoint Instructions

## Strategy
The PoC retains the existing DB2 z/OS schema with zero data migration. Java services connect via IBM DB2 Type 4 JDBC driver directly to the z/OS subsystem.

## Datasource Configuration
- Driver class: `com.ibm.db2.jcc.DB2Driver`
- Connection properties must include: `currentSchema`, `currentSQLID`, `fetchSize`
- Externalise credentials via Spring `application-{profile}.yml` + environment variables; NEVER hardcode
- Connection pool: HikariCP (Spring Boot default); set `maximumPoolSize` conservatively (max 10 for PoC)

## Column Mapping Rules
- Preserve original DB2 column names verbatim in `@Column(name = "...")` annotations
- Map DB2 `DECIMAL(p,s)` → Java `BigDecimal` (never `double` or `float`)
- Map DB2 `DATE` → `java.time.LocalDate`
- Map DB2 `TIMESTAMP` → `java.time.LocalDateTime`
- Map DB2 `CHAR(n)` → `String` (trim trailing spaces in row mapper)
- Map DB2 `SMALLINT` → `Integer`; `INTEGER` → `Integer`; `BIGINT` → `Long`

## Repository Pattern
- Use Spring Data JDBC `CrudRepository` where possible
- For complex queries with dynamic predicates, use `NamedParameterJdbcTemplate`
- No stored procedure calls unless explicitly listed in the funcspec

## Error Handling
- Catch `DataAccessException`; translate to domain exceptions in an `@Repository` `@Transactional` boundary
- Log SQLSTATE on failure at ERROR level

## Prohibited
- Do NOT use Hibernate / JPA — incompatible with DB2 z/OS ROWID and identity column conventions in this estate
- Do NOT issue DDL from application code
