# Quickstart: Phase 7 Planning Validation

## Goal

Verify that Phase 7 planning artifacts for #12/#11 are complete and ready for task breakdown and implementation.

## 1) Confirm branch and artifact set

From repository root:

```bash
git branch --show-current
ls specs/001-llada2-phase7-spec
ls specs/001-llada2-phase7-spec/contracts
```

Expected:

- Current branch is `001-llada2-phase7-spec`
- `plan.md`, `spec.md`, `research.md`, `data-model.md`, `quickstart.md` exist
- Contracts directory contains five contract files

## 2) Validate scope boundaries

Review:

- `contracts/phase7-scope-and-milestones.md`
- `spec.md` requirements FR-011 to FR-014

Check that:

- #12 and #11 are explicit Phase 7 deliverables
- #25 is treated as downstream integration evidence owner

## 3) Validate conformance readiness

Review:

- `contracts/reference-conformance-contract.md`
- `data-model.md` (`ReferenceConformanceMatrix`, `ConformanceRow`)

Check that:

- Match-to-reference is default expectation
- Non-match requires rationale and owner
- Capability coverage is complete for in-scope work

## 4) Validate runtime contract continuity

Review:

- `contracts/runtime-contract-phase7.md`

Check that:

- Scheduler/worker ownership invariants are preserved
- One-step-one-forward remains intact
- Fail-fast behavior is required for incompatible states

## 5) Readiness decision

Proceed to `/speckit.tasks` only if all checks above pass and no unresolved clarifications remain.

## 6) #25 handoff procedure

1. Confirm `conformance-matrix.md` has explicit status for every in-scope capability.
2. Confirm pending/deviation rows include owner and resolution path.
3. Confirm `handoff-summary.md` and `evidence-index.md` are up to date.
4. Pass the full artifact set to #25 execution scope:
   - `conformance-matrix.md`
   - `attention-strategy-record.md`
   - `handoff-summary.md`
   - `evidence-index.md`
