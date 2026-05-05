# Deterministic Comparison Cases

## Case Index

| Case ID | Purpose | Inputs | Expected Type |
|---|---|---|---|
| CASE-001 | Validate required profile fields and fail-fast checks | Synthetic config dictionaries | Validation pass/fail |
| CASE-002 | Validate key-mapping declarations for checkpoint loading | Synthetic key lists | Mapping status |
| CASE-003 | Validate real-forward scaffold output contract | Deterministic token/id input | Shape/field contract |
| CASE-004 | Validate selected attention strategy and position/mask checks | Deterministic position/mask settings | Strategy compatibility result |
| CASE-005 | Validate unsupported-environment fallback behavior | Unsupported runtime marker | Explicit fail/degrade behavior |
| CASE-006 | Validate documentation/runtime contract alignment | Contract docs + matrix rows | Completeness checks |

## Determinism Rules

- Use fixed seeds for synthetic inputs.
- Use explicit case IDs in all conformance rows.
- Attach evidence links for every executed case.
