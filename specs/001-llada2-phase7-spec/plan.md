# Implementation Plan: Phase 7 LLaDA2 Real Model and Attention

**Branch**: `001-llada2-phase7-spec` | **Date**: 2026-05-05 | **Spec**: [`spec.md`](./spec.md)  
**Input**: Feature specification from `/specs/001-llada2-phase7-spec/spec.md`

## Summary

Deliver Phase 7 planning for issue #12 (real LLaDA2 HF mapping + real model path) and issue #11 (attention strategy spike plus implementation) with explicit reference-conformance expectations. The plan preserves previously shipped scheduler/worker contracts from mock phases, defines required conformance artifacts for #25 handoff, and scopes implementation so #12/#11 completion is clearly separated from #25 integration evidence.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: vLLM runtime/plugin stack, PyTorch, transformers, LLaDA2 reference sources (HF, dInfer, SGLang)  
**Storage**: N/A (in-memory request/runtime state; no new persistence required)  
**Testing**: pytest-based unit/integration checks plus reproducible comparison artifacts for reference conformance  
**Target Platform**: Linux + GPU runtime environments currently used for dllm-plugin validation  
**Project Type**: Plugin/runtime integration feature planning for inference engine  
**Performance Goals**: Preserve one-step-one-forward semantics and existing batching behavior while adding real-model correctness and conformance evidence  
**Constraints**: No silent fallback from real-model path to mock behavior; explicit attention fallback contract; behavior match to designated references for in-scope capabilities unless documented deviation is approved  
**Scale/Scope**: Phase 7 design artifacts for #12/#11 plus #25 handoff matrix; no broad roadmap rewrite of earlier phases

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Pre-Design Gate | Post-Design Recheck |
|-----------|------------------|---------------------|
| I. Correctness First | PASS: plan requires explicit conformance matrix and mismatch tracking. | PASS: `research.md` and contracts require match/deviation evidence per capability. |
| II. Scheduler as Single Source of Truth | PASS: Phase 7 extends existing runtime contracts, not worker-owned state. | PASS: `runtime-contract-phase7.md` preserves scheduler-owned request progression. |
| III. Test-Driven Development | PASS: plan requires unit/integration plus deterministic conformance comparisons. | PASS: quickstart and contracts map required evidence artifacts before completion claims. |
| IV. One Step, One Forward | PASS: no change to step/forward contract; #12/#11 integrate within existing model step. | PASS: design explicitly keeps one-step-one-forward invariant and attention within it. |
| V. Backward Compatibility and Opt-In Behavior | PASS: real-model path is explicit and must not alter non-dLLM behavior. | PASS: fail-fast validation for unsupported configs/fallbacks documented in contracts. |
| VI. Performance and Batching | PASS: no planned bypass of continuous batching without explicit rationale. | PASS: quickstart and contracts include batching behavior checks and fallback notes. |

**Gate Result**: PASS (pre-design and post-design).

## Project Structure

### Documentation (this feature)

```text
specs/001-llada2-phase7-spec/
├── plan.md
├── spec.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── phase7-scope-and-milestones.md
│   ├── real-model-module-contract.md
│   ├── attention-strategy-contract.md
│   ├── reference-conformance-contract.md
│   └── runtime-contract-phase7.md
└── tasks.md  # Generated later by /speckit.tasks
```

### Source Code (repository root)

```text
dllm_plugin/
├── __init__.py
├── config.py
├── validation.py
├── runtime_worker.py
├── gpu_model_runner.py
├── worker.py
├── scheduler.py
├── remasking/
└── models/

tests/
├── test_two_phase_dllm.py
├── test_runtime_scheduler_draft_output.py
├── test_dllm_gpu_integration_semantics.py
└── fixtures/

tools/
├── e2e/
└── helm/dllm-plugin-gpu-test/
```

**Structure Decision**: Keep implementation in existing plugin/runtime directories and add Phase 7 planning artifacts under `specs/001-llada2-phase7-spec/`. Contract files isolate #12 and #11 boundaries while preserving linkage to existing runtime contracts and #25 handoff expectations.

## Complexity Tracking

No constitution violations require exceptions or special justification.

## Phase 6 Alignment Pass

- Verified plan alignment with updated conformance expectations (FR-011 to FR-014).
- Confirmed #12/#11 scope remains separate from #25 evidence ownership.
- Confirmed runtime ownership invariants remain unchanged in Phase 7 contracts.
