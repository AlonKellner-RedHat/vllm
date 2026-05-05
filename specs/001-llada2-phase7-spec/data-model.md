# Data Model: Phase 7 LLaDA2 Real Model and Attention

## Entity: RealModelProfile

Represents a supported real LLaDA2 model family/configuration target for #12.

### Fields

- `profile_id` (string, required): Unique identifier for the supported profile.
- `model_identifiers` (list[string], required): Accepted model IDs/aliases mapped to this profile.
- `config_family` (string, required): Configuration class/family name expected for the profile.
- `required_fields` (list[string], required): Configuration fields that must exist for activation.
- `validation_rules` (list[string], required): Fail-fast checks applied before model activation.
- `status` (enum: `draft`, `supported`, `deprecated`, required): Lifecycle state.

### Validation Rules

- Must not activate when required fields are missing.
- Must not silently downgrade to mock behavior if validation fails.
- Must map to exactly one runtime behavior profile at activation.

## Entity: AttentionStrategyRecord

Captures the #11 selected attention path and operational constraints.

### Fields

- `strategy_id` (string, required): Identifier for the selected strategy.
- `selection_reason` (string, required): Why this strategy was chosen.
- `supported_runtime_conditions` (list[string], required): Explicit environments where strategy is supported.
- `fallback_policy` (string, required): What happens when strategy is unavailable.
- `known_limitations` (list[string], required): Declared unsupported or risky cases.
- `implementation_status` (enum: `planned`, `implemented`, `validated`, required).

### Validation Rules

- Must define fallback behavior; empty fallback is invalid.
- Must list at least one supported runtime condition.
- Must enumerate known limitations before declaring validated status.

## Entity: RuntimeCompatibilityContract

Represents compatibility assertions between real-model outputs and existing runtime contracts.

### Fields

- `contract_id` (string, required): Unique contract assertion set identifier.
- `upstream_contract_refs` (list[string], required): Referenced existing runtime contracts from prior phases.
- `required_output_semantics` (list[string], required): Expected semantics that must remain stable.
- `failure_mode_expectations` (list[string], required): Expected fail-fast behavior on incompatible outputs.
- `verification_artifacts` (list[string], optional): Tests/log references proving compatibility.

### Validation Rules

- Must include at least one upstream contract reference.
- Required output semantics cannot be empty.
- Verification artifacts required before status `validated`.

## Entity: ReferenceConformanceMatrix

Capability-level conformance ledger comparing local implementation to designated references.

### Fields

- `matrix_id` (string, required): Matrix version identifier.
- `capability_rows` (list[ConformanceRow], required): Full capability coverage entries.
- `overall_status` (enum: `in_progress`, `ready_for_25`, `closed`, required).
- `last_updated` (datetime, required).

### Validation Rules

- Must cover 100% of in-scope capabilities.
- Each row must have exactly one status and corresponding evidence or rationale.
- `ready_for_25` requires no unclassified non-match rows.

## Entity: ConformanceRow

One capability comparison row in the conformance matrix.

### Fields

- `capability_id` (string, required)
- `capability_name` (string, required)
- `reference_sources` (list[string], required)
- `comparison_case_ids` (list[string], required)
- `status` (enum: `matched`, `pending`, `deviation`, `unsupported`, required)
- `evidence_links` (list[string], optional)
- `deviation_rationale` (string, optional)
- `resolution_owner` (string, optional)
- `target_phase` (enum: `phase7`, `issue25`, required)

### Validation Rules

- `deviation_rationale` required when `status=deviation`.
- `resolution_owner` required when status is not `matched`.
- `target_phase=issue25` requires explicit handoff reason.

## Entity Relationships

- `RealModelProfile` 1..* -> `RuntimeCompatibilityContract`
- `AttentionStrategyRecord` 1..* -> `RuntimeCompatibilityContract`
- `ReferenceConformanceMatrix` 1..* -> `ConformanceRow`
- `ConformanceRow` *..1 -> `RealModelProfile` (by capability relevance)
- `ConformanceRow` *..1 -> `AttentionStrategyRecord` (for attention-related capabilities)

## State Transitions

### RealModelProfile

`draft` -> `supported` -> `deprecated`

- `draft` -> `supported` requires validation rules satisfied and runtime compatibility checks present.

### AttentionStrategyRecord

`planned` -> `implemented` -> `validated`

- `implemented` -> `validated` requires at least one reproducible validation artifact and fallback policy.

### ReferenceConformanceMatrix

`in_progress` -> `ready_for_25` -> `closed`

- `in_progress` -> `ready_for_25` requires full in-scope row coverage and no unclassified mismatches.
