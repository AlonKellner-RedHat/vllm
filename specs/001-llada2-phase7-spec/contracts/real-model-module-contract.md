# Contract: Real Model Module (#12)

## Purpose

Specify behavioral contract for real LLaDA2 model mapping and forward execution.

## Required Inputs

- Supported real model identifier mapped to a declared `RealModelProfile`.
- Configuration object containing all required profile fields.
- Real model assets compatible with the selected profile.

## Required Behaviors

1. Validate profile and configuration before runtime activation.
2. Fail fast on missing/invalid profile requirements.
3. Execute real forward path and emit outputs compatible with existing runtime contracts.
4. Record conformance comparison status against designated references for covered capabilities.

## Non-Functional Contract

- No silent fallback to mock behavior.
- No behavior regression for non-dLLM stacks.
- Preserve one-step-one-forward and scheduler-owned request progression contracts.

## Evidence Requirements

- At least one reproducible real-model run artifact.
- Capability-level conformance entries for model mapping and forward behavior.
