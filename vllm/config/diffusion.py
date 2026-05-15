# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Configuration for discrete diffusion language models (dLLMs)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DiffusionConfig:
    """Configuration for block diffusion models like LLaDA2.

    Attributes:
        canvas_length: Number of tokens per diffusion block (e.g., 32).
            Maps to num_speculative_tokens for buffer sizing.
        mask_token_id: Token ID used for masked positions in the canvas.
        commit_threshold: Softmax probability threshold for committing
            a token position during iterative denoising.
        max_denoise_steps: Maximum denoising iterations per block before
            force-committing.
    """

    canvas_length: int = 32
    mask_token_id: int = 156895
    commit_threshold: float = 0.9
    max_denoise_steps: int = 64

    @property
    def num_speculative_tokens(self) -> int:
        """Canvas length maps to spec-decode buffer size."""
        return self.canvas_length
