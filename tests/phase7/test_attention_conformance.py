from dllm_plugin.models.llada2 import Llada2Phase7Model
from tests.phase7.conformance_utils import has_matrix_row


def test_attention_runtime_supported_path() -> None:
    model = Llada2Phase7Model(model_id="inclusionAI/LLaDA2.0-mini", runtime="gpu-linux")
    model.validate_attention_runtime()
    model.validate_positions_and_mask([0, 1, 2], (3, 3))


def test_attention_capability_row_exists() -> None:
    assert has_matrix_row("C04")
