"""Phase 7 validation helpers for real model path and attention behavior."""

from __future__ import annotations

from typing import Any

from dllm_plugin.models.llada2_profile import RealModelProfile


def assert_real_model_profile_config(
    *,
    profile: RealModelProfile,
    config: dict[str, Any],
) -> None:
    ok, missing = profile.validate_config(config)
    if not ok:
        raise ValueError(
            "real model profile config missing required fields: "
            + ", ".join(missing),
        )


def assert_no_mock_fallback(*, allow_mock_fallback: bool) -> None:
    if allow_mock_fallback:
        raise RuntimeError(
            "mock fallback is not allowed in Phase 7 real-model mode",
        )


def assert_attention_runtime_supported(
    *,
    strategy: str,
    runtime: str,
    supported_runtimes: set[str],
) -> None:
    if runtime not in supported_runtimes:
        raise RuntimeError(
            f"attention strategy {strategy!r} unsupported for runtime {runtime!r}",
        )


def fallback_action_for_unsupported_runtime(
    *,
    fallback_policy: str,
) -> str:
    if fallback_policy not in {"fail-fast", "degrade-safe"}:
        raise ValueError(f"unknown fallback policy: {fallback_policy}")
    return fallback_policy
