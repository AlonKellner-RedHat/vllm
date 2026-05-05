import pytest

from dllm_plugin.models.llada2 import Llada2Phase7Model


def test_attention_unsupported_runtime_fails_fast() -> None:
    model = Llada2Phase7Model(
        model_id="inclusionAI/LLaDA2.0-mini",
        runtime="cpu-unsupported",
    )
    with pytest.raises(RuntimeError, match="unsupported"):
        model.validate_attention_runtime()
