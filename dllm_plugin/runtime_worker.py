"""Phase 7 runtime compatibility helpers."""

from __future__ import annotations

from typing import Any


def assert_phase7_runtime_compatibility(
    *,
    model_output: dict[str, Any],
) -> None:
    required = {"sampled_token_ids", "next_input_block"}
    missing = sorted(required.difference(model_output))
    if missing:
        raise ValueError(
            f"runtime compatibility failed; missing output keys: {missing}",
        )


def assert_position_mask_compatibility(
    *,
    position_ids: list[int],
    mask_shape: tuple[int, int],
) -> None:
    if len(position_ids) == 0:
        raise ValueError("position_ids cannot be empty")
    if mask_shape[0] <= 0 or mask_shape[1] <= 0:
        raise ValueError(f"invalid mask shape: {mask_shape}")


def assert_attention_contract_input(
    *,
    strategy_name: str,
    position_ids: list[int],
    mask_shape: tuple[int, int],
) -> None:
    if not strategy_name:
        raise ValueError("strategy_name is required")
    assert_position_mask_compatibility(position_ids=position_ids, mask_shape=mask_shape)
