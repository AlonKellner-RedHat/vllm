from pathlib import Path


def test_conformance_matrix_has_all_status_rows() -> None:
    text = Path("specs/001-llada2-phase7-spec/conformance-matrix.md").read_text(
        encoding="utf-8",
    )
    for capability in ("C01", "C02", "C03", "C04", "C05", "C06"):
        assert capability in text
    assert "Status" in text
