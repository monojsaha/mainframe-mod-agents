# PROMPT-01: Artefact Inventory

## Agent
@cobol-inventory

## Objective
Produce a complete, structured inventory of all mainframe artefacts in `legacy-src/`.

## Instructions
Scan the entire `legacy-src/` directory and produce `analysis/stage-01/master-inventory.md` with the following sections:

### 1. Summary Table
| Artefact Type | Count |
|--------------|-------|
| COBOL Online (CICS) | N |
| COBOL Batch | N |
| Copybooks (.cpy) | N |
| DCLGENs | N |
| JCL Members | N |
| DB2 DDL | N |

### 2. COBOL Program Inventory
For each program:
| Program ID | Type | Path | Est. LOC | Copybooks Referenced | Called Sub-programs | Notes |

### 3. Copybook Inventory
| Copybook Name | Path | Referenced By (Programs) | Purpose (inferred) |

### 4. JCL Job Inventory
| Job Name | Path | Steps | Programs Called | Notes |

### 5. DDL Inventory
| Table/View Name | Path | Notes |

## Output File
`analysis/stage-01/master-inventory.md`
