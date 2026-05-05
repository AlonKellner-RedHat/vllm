"""Phase 7 root package scaffolding for local implementation tasks."""

from dllm_plugin.models.llada2 import Llada2Phase7Model

REGISTERED_MODELS = {
    "inclusionAI/LLaDA2.0-mini": Llada2Phase7Model,
    "inclusionAI/LLaDA2.0-flash": Llada2Phase7Model,
}


def register_llada2_models() -> dict[str, type[Llada2Phase7Model]]:
    return REGISTERED_MODELS
