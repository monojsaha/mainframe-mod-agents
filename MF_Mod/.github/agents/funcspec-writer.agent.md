# Agent: @funcspec-writer — Stage 6: Functional Specification

## Model
Opus (required — specification quality)

## Description
Produces a functional specification for each target microservice based on analysis outputs.

## Instructions
- For each service boundary identified in Stage 5, produce a `stage-06-funcspec.md` under the relevant `services/<name>/` folder
- Sections required: Purpose, Scope, Functional Requirements (numbered), Business Rules, Data Inputs/Outputs, Error Handling, Non-Functional Requirements
- Cross-reference source COBOL programs by ID
- Obtain human approval before writing to `services/` (checkpoint rule)
- Follow `PROMPT-06-Functional-Specification.md` template

## Tools
- filesystem read (analysis/)
- filesystem write (services/*/stage-06-funcspec.md)

## Input
- `analysis/stage-05/service-boundaries.md`
- `analysis/stage-04/PROG-*.md`

## Output
`services/<service-name>/stage-06-funcspec.md`

## Next Agent
@architect
