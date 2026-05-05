# Contract: Reference Conformance

## Purpose

Define how local implementation is compared against designated LLaDA2 references.

## Designated Reference Baselines

- Hugging Face LLaDA2 reference implementation source.
- inclusionAI dInfer LLaDA2 implementation source.
- SGLang LLaDA2 model implementation source.

## Conformance Rules

1. Match is the default expectation for all in-scope capabilities.
2. Every capability must have deterministic comparison case IDs.
3. Every capability must have exactly one status: `matched`, `pending`, `deviation`, or `unsupported`.
4. Non-match statuses require explicit rationale and owner.

## Capability Coverage (minimum)

- Config/profile mapping semantics.
- Checkpoint/weight mapping semantics.
- Forward topology and output semantics.
- Attention and positional semantics.
- MoE routing/selection semantics.
- Runtime compatibility semantics at plugin boundary.

## #25 Handoff Rule

Matrix snapshot delivered at Phase 7 completion must be sufficient for #25 to continue without rediscovering capability definitions or comparison methodology.
