from pathlib import Path


def test_scope_and_handoff_docs_exist() -> None:
    required = [
        Path("specs/001-llada2-phase7-spec/handoff-summary.md"),
        Path("specs/001-llada2-phase7-spec/evidence-index.md"),
        Path("specs/001-llada2-phase7-spec/contracts/phase7-scope-and-milestones.md"),
    ]
    for item in required:
        assert item.exists(), f"missing required doc: {item}"
