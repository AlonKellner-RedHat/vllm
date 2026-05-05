from pathlib import Path


def test_attention_strategy_record_contains_required_sections() -> None:
    path = Path("specs/001-llada2-phase7-spec/attention-strategy-record.md")
    text = path.read_text(encoding="utf-8")
    for required in (
        "Selected attention approach",
        "Supported runtime conditions",
        "Fallback behavior",
        "Known limitations",
    ):
        assert required in text
