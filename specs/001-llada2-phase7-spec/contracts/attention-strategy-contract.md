# Contract: Attention Strategy (#11)

## Purpose

Define required outputs of the attention spike and implementation decision.

## Required Decision Artifact

The strategy record must include:

- Selected attention approach.
- Selection rationale.
- Supported runtime conditions.
- Fallback behavior when unsupported.
- Known limitations and operator guidance.

## Required Implementation Behaviors

1. Selected strategy must be implemented for real-model path.
2. Behavior must align with documented mask/position semantics used by the selected strategy.
3. Unsupported environments must follow explicit fallback policy (degrade safely or fail fast).

## Required Validation

- Deterministic comparison cases covering key attention semantics.
- Conformance status rows for attention-related capabilities in the matrix.
- Linked artifacts (tests/logs/checklists) proving supported-path behavior.
