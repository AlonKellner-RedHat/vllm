# Attention Strategy Record

## Selected attention approach

- Selected strategy: `phase7-default-attention`
- Type: explicit strategy wrapper with runtime support checks and position/mask compatibility validation

## Selection rationale

- Keeps Phase 7 aligned with one-step-one-forward contracts.
- Provides clear fail-fast behavior for unsupported runtime environments.
- Enables deterministic capability-level conformance checks.

## Supported runtime conditions

- `gpu-linux`

## Fallback behavior

- Unsupported runtime -> fail fast with explicit error.

## Known limitations

- Current scaffold does not include production kernel/backend specialization.
- Additional real-weight and multi-runtime validation is expected in #25.
