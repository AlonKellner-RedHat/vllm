"""Phase 7 real-model profile schema and validation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class RealModelProfile:
    profile_id: str
    model_identifiers: tuple[str, ...]
    config_family: str
    required_fields: tuple[str, ...]
    validation_rules: tuple[str, ...]
    status: str = "draft"

    def validate_config(self, config: dict[str, Any]) -> tuple[bool, list[str]]:
        missing = [field for field in self.required_fields if field not in config]
        ok = not missing
        return ok, missing


def build_llada2_default_profile() -> RealModelProfile:
    return RealModelProfile(
        profile_id="llada2-default",
        model_identifiers=("inclusionAI/LLaDA2.0-mini", "inclusionAI/LLaDA2.0-flash"),
        config_family="LLaDA2MoeConfig",
        required_fields=(
            "hidden_size",
            "num_hidden_layers",
            "num_attention_heads",
            "num_key_value_heads",
            "vocab_size",
        ),
        validation_rules=(
            "fail-fast-on-missing-required-fields",
            "no-silent-mock-fallback",
        ),
        status="supported",
    )


def extract_required_field_values(
    config: dict[str, Any],
    profile: RealModelProfile,
) -> dict[str, Any]:
    ok, missing = profile.validate_config(config)
    if not ok:
        raise ValueError(f"missing required config fields: {missing}")
    return {field: config[field] for field in profile.required_fields}
