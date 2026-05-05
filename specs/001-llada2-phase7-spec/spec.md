# Feature Specification: Phase 7 LLaDA2 Real Model and Attention

**Feature Branch**: `001-llada2-phase7-spec`  
**Created**: 2026-05-05  
**Status**: Draft  
**Input**: User description: "Write a specification for issue #12 (real LLaDA2.0 HF mapping/model module) and issue #11 (attention path spike and implementation), using current dllm-plugin code, milestone #19, and external LLaDA2 implementation references."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Run real LLaDA2 model path (Priority: P1)

As a plugin maintainer, I want the plugin to support real LLaDA2 model configurations and real-weight forward execution so that Phase 7 moves from mock-only confidence to real-model capability.

**Why this priority**: This is the core Phase 7 outcome in issue #12 and the main dependency for real integration evidence.

**Independent Test**: Configure the plugin with a supported real LLaDA2 model identifier and real weights, run inference requests, and confirm the model loads and completes generation without relying on mock-only behavior and with direct behavior comparison against reference implementations.

**Acceptance Scenarios**:

1. **Given** a supported real LLaDA2 model identifier and valid model assets, **When** the operator starts the plugin stack, **Then** the runtime recognizes the model and initializes it as a real model path (not a mock fallback).
2. **Given** a running real-model stack, **When** inference requests are executed, **Then** the forward path produces valid outputs that respect existing plugin runtime contracts for scheduling and remasking handoff.
3. **Given** designated reference implementations, **When** maintainers execute agreed comparison cases, **Then** the plugin implementation records explicit per-capability match status and any justified divergence.

---

### User Story 2 - Select and ship a viable attention path (Priority: P1)

As a runtime maintainer, I want an explicit attention decision (recommended path and fallback limits) and an implemented attention behavior that is compatible with real LLaDA2 inference so that issue #11 is closed with clear operational expectations.

**Why this priority**: Attention behavior is a critical correctness dependency for real-model serving and must be settled before final integration evidence.

**Independent Test**: Use documented test cases that exercise the selected attention behavior on real-model requests and verify expected output validity across the supported run modes.

**Acceptance Scenarios**:

1. **Given** Phase 7 implementation work, **When** maintainers review the attention design artifact, **Then** it states the selected MVP attention approach, known limitations, and fallback behavior in concrete terms.
2. **Given** the selected attention implementation is enabled, **When** real-model inference executes under supported runtime conditions, **Then** requests complete with behavior consistent with the documented approach.

---

### User Story 3 - Preserve milestone contract clarity (Priority: P2)

As a milestone owner, I want #12 and #11 deliverables to be explicitly bounded against #19 so that teams can distinguish "Phase 7 implementation complete" from the later real-model integration evidence in #25.

**Why this priority**: Prevents scope drift and ambiguous release claims after prior mock-phase completion.

**Independent Test**: Review deliverable documentation and checklists and confirm they clearly identify what is complete in #12/#11 and what remains for #25.

**Acceptance Scenarios**:

1. **Given** the Phase 7 specification and implementation notes, **When** maintainers validate scope, **Then** #12 and #11 outputs are clearly marked as Phase 7 implementation deliverables and not conflated with full #25 completion.
2. **Given** downstream integration planning, **When** teams prepare real-weight validation, **Then** they can directly derive #25 tasks from documented #12/#11 outputs and known gaps.

---

### Edge Cases

- What happens when a model claims to be LLaDA2-compatible but required configuration fields are missing or inconsistent? The system should fail fast with actionable model-compatibility errors.
- What happens when the preferred attention path is unavailable in a target environment? The documented fallback behavior must define whether operation degrades safely or is blocked.
- What happens when real-model outputs violate assumptions validated in the mock path (shape, token/block semantics, or remasking inputs)? The runtime must reject invalid data and surface clear diagnostics rather than silently continuing.
- What happens when #12 appears complete but #11 remains partial? The release process must explicitly prevent marking Phase 7 done until both responsibilities are satisfied.
- What happens when implementation behavior differs from reference implementations on a comparison case? The difference must be classified (bug, accepted deviation, or unsupported case), documented, and tracked to closure before declaring reference-match expectations met.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST support a real LLaDA2 model mapping path that recognizes and validates supported model identifiers and configuration families for Phase 7 operation.
- **FR-002**: The system MUST provide a real forward execution path for LLaDA2 that can run with real model assets and produce outputs consumable by existing plugin runtime contracts.
- **FR-003**: The system MUST retain compatibility with established scheduler/worker/remasking contracts from phases 3-6 when operating on real-model outputs.
- **FR-004**: The system MUST define an attention decision artifact for Phase 7 that includes selected approach, explicit rationale, operating limits, and fallback policy.
- **FR-005**: The system MUST implement the selected attention behavior for real-model inference in the supported runtime scope identified by the decision artifact.
- **FR-006**: The system MUST include tests and/or reproducible validation steps that confirm the selected attention behavior works with the real forward path.
- **FR-007**: The system MUST fail fast for unsupported or inconsistent real-model configurations instead of silently falling back to behavior that masks incompatibility.
- **FR-008**: The system MUST document Phase 7 scope boundaries so that #12 and #11 completion is clearly separated from #25 real-model integration evidence.
- **FR-009**: The system MUST identify known unsupported scenarios discovered during the #11 attention spike and communicate operator guidance for those scenarios.
- **FR-010**: The system MUST produce deliverables that are sufficient inputs for #25 re-validation planning (real-weight integration evidence), without requiring re-discovery of #12/#11 decisions.
- **FR-011**: The system MUST define an explicit reference conformance baseline for #12 using the designated source implementations and a deterministic set of comparison cases.
- **FR-012**: The system MUST compare the local LLaDA2 implementation directly against the designated reference source code behaviors for covered capabilities and record match results.
- **FR-013**: The system MUST treat match with the designated references as the expected outcome for covered capabilities; any non-match MUST be explicitly justified and tracked as unresolved work or approved deviation.
- **FR-014**: The system MUST produce a #25-ready conformance handoff artifact that maps each comparison capability to expected evaluation status (already matched, pending evaluation, or known divergence with rationale).

### Key Entities *(include if feature involves data)*

- **Real LLaDA2 Model Profile**: The validated set of model identifiers and configuration characteristics treated as supported real-model targets in Phase 7.
- **Attention Strategy Record**: The maintainers' decision artifact describing selected attention behavior, fallback behavior, constraints, and justification.
- **Runtime Compatibility Contract**: The expected shape and semantics alignment between real-model forward outputs and plugin runtime consumers.
- **Phase 7 Validation Evidence**: Test artifacts or reproducible checks demonstrating #12 and #11 outcomes and clearly separating remaining #25 work.
- **Reference Conformance Matrix**: A capability-by-capability comparison record between this repository's implementation and designated LLaDA2 references, including match status and rationale for any deviations.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Maintainers can run at least one real LLaDA2 model end-to-end through the plugin stack with reproducible setup documentation and no mock-only substitution.
- **SC-002**: 100% of required Phase 7 acceptance checks for #12 and #11 are mapped to explicit evidence artifacts (tests, logs, or checklists) that reviewers can verify.
- **SC-003**: At least one documented attention strategy is accepted and demonstrated working on real-model requests under supported runtime conditions.
- **SC-004**: Reviewers can identify Phase 7 scope boundaries in under 10 minutes using the produced docs, including explicit separation of remaining #25 responsibilities.
- **SC-005**: Validation runs report no silent compatibility fallbacks for unsupported model/attention combinations; failures are surfaced as explicit actionable errors.
- **SC-006**: A reference conformance matrix exists for all Phase 7 in-scope capabilities and reports explicit status for 100% of those capabilities.
- **SC-007**: Any capability marked as non-match includes tracked resolution path or approved deviation before #12/#11 are declared complete.

## Assumptions

- Phase 6 mock-stack contracts are the baseline, and Phase 7 extends them to real weights rather than redefining scheduler/worker ownership.
- #12 and #11 may be delivered through multiple PRs, but each PR must preserve the same acceptance boundaries defined here.
- #25 remains the formal owner of comprehensive real-model integration evidence after #12 and #11 implementation deliverables are complete.
- External implementation references are normative comparison baselines for in-scope capabilities; the default expectation is behavior match, with only explicit documented deviations allowed.
