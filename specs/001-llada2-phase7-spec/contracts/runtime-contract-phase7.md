# Contract: Runtime Compatibility (Phase 7)

## Purpose

Ensure #12/#11 integrate into established runtime contracts from prior phases without ownership drift.

## Contract References

- `specs/001-dllm-integration/contracts/dllm-step-contract.md`
- `specs/002-dllm-plugin/contracts/dllm-step-contract-ref.md`
- `specs/002-dllm-plugin/contracts/plugin-registration-contract.md`

## Required Runtime Invariants

1. Scheduler remains source of truth for per-request progression state.
2. Worker/model output semantics remain compatible with existing update/apply flow.
3. One scheduler step maps to at most one model forward per batch.
4. Invalid real-model/attention states fail fast and explicitly.

## Compatibility Checks

- Real-model outputs satisfy required shape/semantic assumptions already used by runtime consumers.
- Attention path does not violate declared scheduler/worker contracts.
- Any contract-affecting deviation is recorded and linked in conformance matrix.

## Non-Goals

- Redefining core runtime ownership model.
- Introducing hidden fallback paths that obscure compatibility failures.
