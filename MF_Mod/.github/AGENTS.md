# Copilot Coding Agent Instructions — MF App PoC

These instructions apply when GitHub Copilot runs background (autonomous) coding agents against this repository.

## Repository Layout
| Folder | Purpose | Agent write access |
|--------|---------|-------------------|
| `legacy-src/` | Original mainframe artefacts | **NEVER** |
| `analysis/` | AI-generated analysis outputs | Yes |
| `services/` | Generated Java source + docs | Yes (after checkpoint) |
| `governance/` | PoC governance docs | Yes |
| `ops/` | Pipeline state and CI | Yes |

## Stage Execution Order
Agents must execute stages in sequence. A stage is only started when the previous stage's output exists and has been committed.

1. `@cobol-inventory` → `analysis/stage-01/master-inventory.md`
2. `@copybook-analyst` → `analysis/stage-02/`
3. `@jcl-analyst` → `analysis/stage-03/`
4. `@cobol-analyser` → `analysis/stage-04/PROG-[ID].md`
5. `@dependency-modeller` → `analysis/stage-05/`
6. `@funcspec-writer` → `services/*/stage-06-funcspec.md`
7. `@architect` → `services/*/stage-07-architecture.md`
8. `@test-synthesiser` → `services/*/stage-08-test-cases.md`
9. `@java-generator` + `@acl-adapter` → `services/*/src/`

## Commit Convention
```
[STAGE-NN] <agent-name>: <short description>
```
Example: `[STAGE-04] cobol-analyser: deep analysis of NEWLNAPP`

## Agent Behaviour Rules
- Never delete or overwrite files in `legacy-src/`
- Always update `analysis/progress.md` with a dated entry
- Update `ops/pipeline-state.json` only after human review of outputs
- Raise a GitHub issue if a blocking ambiguity is found rather than guessing
