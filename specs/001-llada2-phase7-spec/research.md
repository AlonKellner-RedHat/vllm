# Phase 0 Research: Phase 7 LLaDA2 Real Model and Attention

## Decision 1: Treat designated LLaDA2 sources as normative conformance baselines

- **Decision**: Use the designated LLaDA2 references (HF model source, dInfer implementation, and SGLang model implementation) as normative baselines for in-scope capability matching in #12/#11.
- **Rationale**: The feature spec explicitly requires direct comparison and expectation to match. A normative baseline prevents ambiguous "close enough" claims.
- **Alternatives considered**:
  - Treat references as guidance only: rejected because it conflicts with FR-011 to FR-014.
  - Compare only generated text outputs: rejected because hidden contract mismatches can still exist.

## Decision 2: Use a capability-level conformance matrix

- **Decision**: Track conformance by capability (config mapping, checkpoint loading rules, embedding path, decoder topology, MoE routing, attention math, RoPE/positions, runtime output contract) instead of a monolithic pass/fail.
- **Rationale**: Capability-level rows allow explicit status for each behavior and create a clean #25 handoff artifact.
- **Alternatives considered**:
  - Single aggregate "reference parity" result: rejected because it hides partial gaps.
  - Per-file textual diff only: rejected because structural similarity does not prove runtime behavior.

## Decision 3: Strict-match default, explicit-deviation exception path

- **Decision**: Default expectation is strict behavior match for in-scope capabilities. Any non-match must be categorized as bug, accepted deviation, or unsupported case, with owner and closure path.
- **Rationale**: Aligns with the updated spec and constitution correctness-first governance.
- **Alternatives considered**:
  - Loose tolerance without formal deviation tracking: rejected due to auditability gaps.
  - Blanket acceptance of backend/runtime differences: rejected because some differences can change semantics.

## Decision 4: Keep Phase 7 scope and #25 evidence ownership separate

- **Decision**: #12/#11 must produce implementation and initial conformance evidence, while #25 remains owner of comprehensive real-weight integration re-validation and expanded matrix execution.
- **Rationale**: Matches issue #19 phase gates and avoids inflating #12/#11 into indefinite validation work.
- **Alternatives considered**:
  - Merge #25 obligations into #12/#11: rejected as scope drift.
  - Delay all conformance work to #25: rejected because #12/#11 completion would be under-defined.

## Decision 5: Preserve existing runtime contracts from mock phases

- **Decision**: Real-model work must preserve existing scheduler/worker/remasking ownership contracts from phases 3-6, including one-step-one-forward and scheduler-owned request progression.
- **Rationale**: Constitution requires backward compatibility and contract stability for new inference modes.
- **Alternatives considered**:
  - Introduce a new worker-owned state model for Phase 7: rejected as a high-risk contract fork.
  - Rework scheduler semantics during #12/#11: rejected because not required for stated scope.

## Decision 6: Define attention strategy as explicit contract artifact

- **Decision**: #11 deliverable includes a concrete attention strategy contract specifying selected path, supported environments, fallback behavior, and known unsupported cases.
- **Rationale**: Attention behavior is the highest-risk semantic area and requires explicit governance for operators and reviewers.
- **Alternatives considered**:
  - Capture attention decisions only in PR descriptions: rejected as non-discoverable and non-durable.
  - Delay strategy decision until #25: rejected because #11 requires implementation in Phase 7.

## Decision 7: Conformance comparison should include deterministic cases

- **Decision**: Comparison matrix rows must map to deterministic case definitions (input shape/seed/config/mask setup) and artifact links.
- **Rationale**: Deterministic reproducibility is required for review and future regression checks.
- **Alternatives considered**:
  - Ad hoc manual comparisons: rejected as non-repeatable.
  - Environment-dependent benchmark traces only: rejected because they can blur correctness vs performance.

## Capability Set for Reference Conformance Matrix

1. Supported configuration family mapping and validation
2. Checkpoint key mapping and weight loading rules
3. Embedding path behavior (discrete and any declared blended path)
4. Decoder block ordering and sparse/dense layer gating
5. MoE routing/top-k behavior and combine semantics
6. Attention projection/splitting and head semantics
7. RoPE and positional handling behavior
8. Attention mask semantics and selected backend behavior contract
9. Runtime output compatibility with existing remasking/worker contracts
10. Operator-visible fallback and failure behavior

## Phase 0 Outcome

All prior technical unknowns are resolved for planning. No `NEEDS CLARIFICATION` entries remain.
