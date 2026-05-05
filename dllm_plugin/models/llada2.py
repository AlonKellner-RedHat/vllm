"""Phase 7 real model scaffold and attention integration hooks."""

from __future__ import annotations

from dataclasses import dataclass

from dllm_plugin.runtime_worker import (
    assert_phase7_runtime_compatibility,
    assert_position_mask_compatibility,
)
from dllm_plugin.validation import assert_attention_runtime_supported
from dllm_plugin.validation import fallback_action_for_unsupported_runtime


@dataclass(slots=True)
class AttentionStrategy:
    name: str = "phase7-default-attention"
    supported_runtimes: frozenset[str] = frozenset({"gpu-linux"})
    fallback_policy: str = "fail-fast"


class Llada2Phase7Model:
    def __init__(self, model_id: str, runtime: str = "gpu-linux") -> None:
        self.model_id = model_id
        self.runtime = runtime
        self.attention = AttentionStrategy()

    def validate_attention_runtime(self) -> None:
        try:
            assert_attention_runtime_supported(
                strategy=self.attention.name,
                runtime=self.runtime,
                supported_runtimes=set(self.attention.supported_runtimes),
            )
        except RuntimeError:
            action = fallback_action_for_unsupported_runtime(
                fallback_policy=self.attention.fallback_policy,
            )
            if action == "degrade-safe":
                return
            raise

    def forward_step(self, input_block: list[int]) -> dict[str, list[int]]:
        self.validate_attention_runtime()
        out = {
            "sampled_token_ids": input_block[:1],
            "next_input_block": input_block[-1:] + input_block[:-1],
        }
        assert_phase7_runtime_compatibility(model_output=out)
        return out

    def validate_positions_and_mask(
        self,
        position_ids: list[int],
        mask_shape: tuple[int, int],
    ) -> None:
        assert_position_mask_compatibility(
            position_ids=position_ids,
            mask_shape=mask_shape,
        )
