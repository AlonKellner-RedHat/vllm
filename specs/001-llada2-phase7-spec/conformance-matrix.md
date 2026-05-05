# Reference Conformance Matrix

## Metadata

- Matrix ID: `phase7-initial-2026-05-05`
- Last Updated: `2026-05-05`
- Overall Status: `in_progress`

## Capability Rows

| Capability ID | Capability | Reference Sources | Comparison Case IDs | Status | Evidence | Deviation Rationale | Owner | Target Phase |
|---|---|---|---|---|---|---|---|---|
| C01 | Config/profile mapping semantics | HF, dInfer, SGLang | CASE-001 | matched | tests/phase7/test_llada2_profile_validation.py |  | phase7-maintainers | phase7 |
| C02 | Checkpoint/key mapping semantics | HF, dInfer, SGLang | CASE-002 | matched | tests/phase7/test_llada2_mapping_conformance.py |  | phase7-maintainers | phase7 |
| C03 | Real forward topology/output semantics | HF, dInfer, SGLang | CASE-003 | matched | tests/phase7/test_llada2_real_forward_runtime.py |  | phase7-maintainers | phase7 |
| C04 | Attention and positional semantics | HF, dInfer, SGLang | CASE-004 | matched | tests/phase7/test_attention_conformance.py |  | phase7-maintainers | phase7 |
| C05 | Fallback and failure behavior | HF, dInfer, SGLang | CASE-005 | matched | tests/phase7/test_attention_fallback_behavior.py |  | phase7-maintainers | phase7 |
| C06 | Runtime contract compatibility | plugin contracts + phase7 contracts | CASE-006 | pending | tests/phase7/test_phase7_docs_consistency.py | full real-weight integration proof deferred to #25 | issue25-maintainers | issue25 |

## Validation Section (SC-006 / SC-007)

- In-scope capability coverage: 6/6 rows defined.
- Rows with explicit status: 6/6.
- Rows in non-match state (`deviation` or `unsupported`): 0 (none yet).
- Rows deferred to #25 (`pending` with owner/rationale): 1 (C06).

## US1 Notes

- US1 baseline capabilities C01-C03 are marked `matched` based on deterministic scaffold checks.

## US2 Notes

- US2 attention capabilities C04-C05 are marked `matched` for supported runtime and fallback behavior checks.

## US3 Notes

- C06 remains `pending` with explicit #25 owner and rationale.
- No `deviation` rows currently exist.

## Unresolved / Deviation Owner Mapping

| Capability | Status | Owner | Resolution Path |
|---|---|---|---|
| C06 | pending | issue25-maintainers | Validate full runtime compatibility on real weights during #25 |
