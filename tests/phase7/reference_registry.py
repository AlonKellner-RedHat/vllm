"""Reference source registry for Phase 7 conformance."""

from __future__ import annotations


REFERENCE_SOURCES = {
    "hf": "https://huggingface.co/inclusionAI/LLaDA2.0-mini/blob/main/modeling_llada2_moe.py",
    "dinfer": "https://github.com/inclusionAI/dInfer/blob/master/python/dinfer/model/modeling_llada2_moe.py",
    "sglang": "https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/llada2.py",
}


CAPABILITY_MAP = {
    "C01": "config/profile mapping semantics",
    "C02": "checkpoint/key mapping semantics",
    "C03": "forward topology/output semantics",
    "C04": "attention and positional semantics",
    "C05": "fallback and failure behavior",
    "C06": "runtime contract compatibility",
}
