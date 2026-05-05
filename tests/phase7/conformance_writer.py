"""Write small conformance status snippets for Phase 7 tests."""

from __future__ import annotations

from pathlib import Path


MATRIX_PATH = Path("specs/001-llada2-phase7-spec/conformance-matrix.md")


def append_test_note(note: str) -> None:
    text = MATRIX_PATH.read_text(encoding="utf-8")
    if note in text:
        return
    with MATRIX_PATH.open("a", encoding="utf-8") as f:
        f.write(f"\n- Test note: {note}\n")
