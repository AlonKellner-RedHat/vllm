from dllm_plugin.models.llada2_profile import build_llada2_default_profile
from dllm_plugin.validation import assert_real_model_profile_config


def test_llada2_profile_has_required_fields() -> None:
    profile = build_llada2_default_profile()
    assert "hidden_size" in profile.required_fields
    assert "num_hidden_layers" in profile.required_fields


def test_profile_validation_fail_fast_on_missing_fields() -> None:
    profile = build_llada2_default_profile()
    bad = {"hidden_size": 2048}
    try:
        assert_real_model_profile_config(profile=profile, config=bad)
        assert False, "expected fail-fast validation"
    except ValueError as exc:
        assert "missing required fields" in str(exc)
