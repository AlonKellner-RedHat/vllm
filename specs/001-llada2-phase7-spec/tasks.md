# Tasks: Phase 7 LLaDA2 Real Model and Attention

**Input**: Design documents from `/specs/001-llada2-phase7-spec/`  
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`

**Tests**: Included, because the spec requires reproducible validation and explicit conformance evidence.  
**Organization**: Tasks are grouped by user story so each story is independently testable and shippable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallelizable task (different files, no incomplete-task dependency)
- **[Story]**: User story label (`[US1]`, `[US2]`, `[US3]`)
- Every task includes a concrete file path

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create Phase 7 implementation scaffolding and shared validation locations.

- [X] T001 Create Phase 7 implementation tracker in `specs/001-llada2-phase7-spec/implementation-log.md`
- [X] T002 Create conformance matrix seed in `specs/001-llada2-phase7-spec/conformance-matrix.md`
- [X] T003 [P] Create deterministic comparison case index in `specs/001-llada2-phase7-spec/comparison-cases.md`
- [X] T004 [P] Create Phase 7 test package scaffold in `tests/phase7/__init__.py`
- [X] T005 [P] Create conformance utilities scaffold in `tests/phase7/conformance_utils.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build core prerequisites required by all user stories.

**CRITICAL**: No user story implementation starts before this phase completes.

- [X] T006 Define `RealModelProfile` schema and validation helpers in `dllm_plugin/models/llada2_profile.py`
- [X] T007 [P] Add fail-fast profile/config validation entrypoints in `dllm_plugin/validation.py`
- [X] T008 [P] Add runtime compatibility assertion helpers for Phase 7 in `dllm_plugin/runtime_worker.py`
- [X] T009 Create reference source registry and capability map in `tests/phase7/reference_registry.py`
- [X] T010 Create conformance row/status writer helper in `tests/phase7/conformance_writer.py`
- [X] T011 Add pytest marker/config for Phase 7 tests in `pytest.ini`
- [X] T012 Add Phase 7 test data fixture manifest in `tests/fixtures/phase7/cases_manifest.json`

**Checkpoint**: Foundation ready for independent user-story execution.

---

## Phase 3: User Story 1 - Run real LLaDA2 model path (Priority: P1) 🎯 MVP

**Goal**: Implement #12 real model mapping/forward path with direct reference conformance reporting.

**Independent Test**: Run real-model startup + forward checks and produce conformance rows for model mapping and forward capabilities.

### Tests for User Story 1

- [X] T013 [P] [US1] Add profile validation unit tests in `tests/phase7/test_llada2_profile_validation.py`
- [X] T014 [P] [US1] Add model mapping conformance test skeleton in `tests/phase7/test_llada2_mapping_conformance.py`
- [X] T015 [P] [US1] Add real forward compatibility integration test in `tests/phase7/test_llada2_real_forward_runtime.py`

### Implementation for User Story 1

- [X] T016 [US1] Implement real LLaDA2 model registration wiring in `dllm_plugin/__init__.py`
- [X] T017 [US1] Implement real LLaDA2 model module scaffold in `dllm_plugin/models/llada2.py`
- [X] T018 [P] [US1] Implement config-family mapping and required-field extraction in `dllm_plugin/models/llada2_profile.py`
- [X] T019 [US1] Implement fail-fast no-mock-fallback behavior in `dllm_plugin/validation.py`
- [X] T020 [US1] Wire real forward outputs into existing runtime contract path in `dllm_plugin/runtime_worker.py`
- [X] T021 [US1] Add checkpoint/key-mapping conformance capture hooks in `tests/phase7/conformance_utils.py`
- [X] T022 [US1] Record US1 capability statuses and evidence in `specs/001-llada2-phase7-spec/conformance-matrix.md`

**Checkpoint**: US1 is independently functional and validated for real-model path plus initial conformance evidence.

---

## Phase 4: User Story 2 - Select and ship a viable attention path (Priority: P1)

**Goal**: Implement #11 attention strategy with explicit fallback semantics and conformance checks.

**Independent Test**: Execute attention comparison cases under supported conditions and verify fallback/unsupported behavior is explicit.

### Tests for User Story 2

- [X] T023 [P] [US2] Add attention strategy decision artifact validation test in `tests/phase7/test_attention_strategy_record.py`
- [X] T024 [P] [US2] Add attention semantic conformance tests for selected cases in `tests/phase7/test_attention_conformance.py`
- [X] T025 [P] [US2] Add unsupported-environment fallback behavior test in `tests/phase7/test_attention_fallback_behavior.py`

### Implementation for User Story 2

- [X] T026 [US2] Implement attention strategy record for selected approach in `specs/001-llada2-phase7-spec/attention-strategy-record.md`
- [X] T027 [US2] Implement selected attention path integration in `dllm_plugin/models/llada2.py`
- [X] T028 [US2] Implement explicit fallback/unsupported handling in `dllm_plugin/validation.py`
- [X] T029 [US2] Add positional/mask compatibility checks for attention path in `dllm_plugin/runtime_worker.py`
- [X] T030 [US2] Record attention capability statuses and evidence in `specs/001-llada2-phase7-spec/conformance-matrix.md`

**Checkpoint**: US2 attention strategy and implementation are independently validated and documented.

---

## Phase 5: User Story 3 - Preserve milestone contract clarity (Priority: P2)

**Goal**: Produce explicit #12/#11 completion boundary and #25-ready handoff artifacts.

**Independent Test**: Reviewers can map every Phase 7 capability and remaining #25 work from artifacts without additional discovery.

### Tests for User Story 3

- [X] T031 [P] [US3] Add docs consistency test for scope/handoff completeness in `tests/phase7/test_phase7_docs_consistency.py`
- [X] T032 [P] [US3] Add conformance row completeness test in `tests/phase7/test_conformance_matrix_completeness.py`

### Implementation for User Story 3

- [X] T033 [US3] Finalize #12/#11 versus #25 boundary summary in `specs/001-llada2-phase7-spec/handoff-summary.md`
- [X] T034 [US3] Populate unresolved/deviation owner mapping for #25 in `specs/001-llada2-phase7-spec/conformance-matrix.md`
- [X] T035 [US3] Produce Phase 7 evidence index linking tests/logs/docs in `specs/001-llada2-phase7-spec/evidence-index.md`
- [X] T036 [US3] Update operational quickstart with #25 handoff procedure in `specs/001-llada2-phase7-spec/quickstart.md`

**Checkpoint**: US3 produces independently reviewable boundary and handoff artifacts.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass across all stories.

- [X] T037 [P] Run and capture Phase 7 pytest suite results in `specs/001-llada2-phase7-spec/test-run-report.md`
- [X] T038 [P] Perform final contract/spec alignment pass in `specs/001-llada2-phase7-spec/plan.md`
- [X] T039 Validate conformance matrix statuses against SC-006/SC-007 in `specs/001-llada2-phase7-spec/conformance-matrix.md`
- [X] T040 Produce final implementation readiness summary in `specs/001-llada2-phase7-spec/implementation-readiness.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: Starts immediately.
- **Phase 2 (Foundational)**: Depends on Phase 1 and blocks all user stories.
- **Phase 3 (US1)**: Depends on Phase 2.
- **Phase 4 (US2)**: Depends on Phase 2; can run in parallel with late US1 tasks if contract interfaces are stable.
- **Phase 5 (US3)**: Depends on Phase 2 and requires US1/US2 artifacts to be meaningful.
- **Phase 6 (Polish)**: Depends on completion of targeted user stories.

### User Story Dependencies

- **US1 (P1)**: No dependency on other stories after foundational phase.
- **US2 (P1)**: No hard dependency on US1, but final conformance reporting reuses US1 matrix artifacts.
- **US3 (P2)**: Depends on outputs from US1 and US2 to build final #25 handoff.

### Parallel Opportunities

- Setup tasks T003-T005 can run in parallel.
- Foundational tasks T007-T010 can run in parallel after T006.
- US1 test tasks T013-T015 can run in parallel.
- US2 test tasks T023-T025 can run in parallel.
- US3 test tasks T031-T032 can run in parallel.
- Polish tasks T037-T038 can run in parallel.

---

## Parallel Example: User Story 1

```bash
Task: "T013 [US1] Add profile validation unit tests in tests/phase7/test_llada2_profile_validation.py"
Task: "T014 [US1] Add model mapping conformance test skeleton in tests/phase7/test_llada2_mapping_conformance.py"
Task: "T015 [US1] Add real forward compatibility integration test in tests/phase7/test_llada2_real_forward_runtime.py"
```

## Parallel Example: User Story 2

```bash
Task: "T023 [US2] Add attention strategy decision artifact validation test in tests/phase7/test_attention_strategy_record.py"
Task: "T024 [US2] Add attention semantic conformance tests for selected cases in tests/phase7/test_attention_conformance.py"
Task: "T025 [US2] Add unsupported-environment fallback behavior test in tests/phase7/test_attention_fallback_behavior.py"
```

## Parallel Example: User Story 3

```bash
Task: "T031 [US3] Add docs consistency test for scope/handoff completeness in tests/phase7/test_phase7_docs_consistency.py"
Task: "T032 [US3] Add conformance row completeness test in tests/phase7/test_conformance_matrix_completeness.py"
```

---

## Implementation Strategy

### MVP First (US1 only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1).
3. Validate real-model path + conformance rows for US1.
4. Stop for review before attention expansion.

### Incremental Delivery

1. Deliver US1 (#12 real-model baseline).
2. Deliver US2 (#11 attention strategy + implementation).
3. Deliver US3 (#25-ready boundary/handoff package).
4. Run polish phase and finalize readiness summary.

### Suggested MVP Scope

- **MVP scope**: Phase 1 + Phase 2 + Phase 3 (US1).
