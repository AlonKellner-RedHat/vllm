from dllm_plugin.models.llada2 import Llada2Phase7Model
from dllm_plugin.runtime_worker import assert_phase7_runtime_compatibility


def test_real_forward_runtime_contract_shape() -> None:
    model = Llada2Phase7Model(model_id="inclusionAI/LLaDA2.0-mini")
    out = model.forward_step([1, 2, 3, 4])
    assert_phase7_runtime_compatibility(model_output=out)
    assert isinstance(out["sampled_token_ids"], list)
    assert isinstance(out["next_input_block"], list)
