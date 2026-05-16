# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
from abc import ABC, abstractmethod
from typing import Any

import torch
import torch.nn as nn

from vllm.config import VllmConfig
from vllm.config.compilation import CUDAGraphMode
from vllm.tasks import GenerationTask
from vllm.v1.core.sched.output import NewRequestData
from vllm.v1.kv_cache_interface import KVCacheConfig
from vllm.v1.worker.gpu.input_batch import InputBatch
from vllm.v1.worker.gpu.mm.encoder_cache import EncoderCache
from vllm.v1.worker.gpu.states import RequestState
from vllm.v1.worker.utils import AttentionGroup


class ModelState(ABC):
    @abstractmethod
    def __init__(
        self,
        vllm_config: VllmConfig,
        model: nn.Module,
        encoder_cache: EncoderCache | None,
        device: torch.device,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_supported_generation_tasks(self) -> tuple[GenerationTask, ...]:
        raise NotImplementedError

    def add_request(self, req_index: int, new_req_data: NewRequestData) -> None:
        return None

    def apply_staged_writes(self) -> None:
        return None

    @abstractmethod
    def get_mm_embeddings(
        self,
        scheduled_encoder_inputs: dict[str, list[int]],
        input_batch: InputBatch,
        req_states: RequestState,
    ) -> torch.Tensor | None:
        raise NotImplementedError

    @abstractmethod
    def prepare_inputs(
        self, input_batch: InputBatch, req_states: RequestState
    ) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def prepare_dummy_inputs(self, num_reqs: int, num_tokens: int) -> dict[str, Any]:
        raise NotImplementedError

    def remove_request(self, req_id: str) -> None:
        """Clean up per-request state when a request finishes or aborts."""
        return None

    def custom_sampler(
        self,
        sampler: Any,
        config: Any,
    ) -> tuple[Any, Any] | None:
        """Wrap or replace the default sampler.

        Called after model loading. Return None to keep defaults,
        or (sampler, rejection_sampler | None) to override.
        """
        return None

    def before_step(
        self,
        scheduler_output: Any,
        dummy_run: bool = False,
    ) -> None:
        """Extract per-step metadata from scheduler output before forward pass."""
        return None

    def take_draft_token_ids(self) -> Any | None:
        """Produce next-step draft token IDs (e.g. for block diffusion)."""
        return None

    @property
    def num_bonus_tokens(self) -> int:
        """Number of bonus tokens prepended to draft sequences.

        AR models return 1 (last_sampled_token prepended by combine kernel).
        Diffusion models return 0 (canvas IS the full input).
        """
        return 1

    @abstractmethod
    def prepare_attn(
        self,
        input_batch: InputBatch,
        cudagraph_mode: CUDAGraphMode,
        block_tables: tuple[torch.Tensor, ...],
        slot_mappings: torch.Tensor,
        attn_groups: list[list[AttentionGroup]],
        kv_cache_config: KVCacheConfig,
        for_capture: bool = False,
    ) -> dict[str, Any]:
        raise NotImplementedError
