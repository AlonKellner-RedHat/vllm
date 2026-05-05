"""Helpers for Phase 7 conformance checks."""

from __future__ import annotations

from pathlib import Path


def conformance_matrix_path() -> Path:
    return Path("specs/001-llada2-phase7-spec/conformance-matrix.md")


def ensure_case_id(case_id: str) -> None:
    if not case_id.startswith("CASE-"):
        raise ValueError(f"invalid case id: {case_id}")


def has_matrix_row(capability_id: str) -> bool:
    text = conformance_matrix_path().read_text(encoding="utf-8")
    return capability_id in text


def capture_mapping_hook(checkpoint_keys: list[str]) -> dict[str, bool]:
    """Return simple key-presence flags for conformance reporting."""
    return {
        "has_gate_proj": any("gate_proj" in key for key in checkpoint_keys),
        "has_up_proj": any("up_proj" in key for key in checkpoint_keys),
        "has_down_proj": any("down_proj" in key for key in checkpoint_keys),
    }
