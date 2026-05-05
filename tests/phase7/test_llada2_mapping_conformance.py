from tests.phase7.conformance_utils import ensure_case_id, has_matrix_row
from tests.phase7.reference_registry import CAPABILITY_MAP


def test_mapping_case_id_format() -> None:
    ensure_case_id("CASE-002")


def test_mapping_capability_row_exists() -> None:
    assert "C02" in CAPABILITY_MAP
    assert has_matrix_row("C02")
