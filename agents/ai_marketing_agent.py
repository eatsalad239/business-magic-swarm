"""
AI‑Powered Marketing Agent
==========================

This agent attempts to generate more creative marketing copy using an
open‑source transformer model when available.  It first tries to
instantiate a Hugging Face ``pipeline`` with a small GPT‑Neo model.
If the ``transformers`` library or model cannot be loaded (for
example, because it isn't installed or weights aren't available), it
falls back to the simple template‑based generator in
``marketing_agent``.

The default model used is ``EleutherAI/gpt‑neo‑125M``, which is
licensed under the MIT license and can be loaded via
``transformers.pipeline``.  You can replace ``MODEL_NAME`` with
another open‑source text generation model if desired.

Example usage::

    from agents.ai_marketing_agent import generate_marketing_copy

    description = generate_marketing_copy(
        "SuperWidget", ["fast", "easy to use", "durable"]
    )
    print(description)

The fallback ensures this function always returns a string even if
``transformers`` isn't installed.
"""

from typing import List

# Fallback import: we'll use the simple template generator if the
# transformer pipeline cannot be loaded.
from .marketing_agent import generate_marketing_copy as _simple_generate


MODEL_NAME = "EleutherAI/gpt-neo-125M"


def _load_generator():
    """Attempt to load a Hugging Face text generation pipeline.

    Returns a callable that takes a prompt and returns generated text
    or ``None`` if loading fails.
    """
    try:
        from transformers import pipeline  # type: ignore

        return pipeline("text-generation", model=MODEL_NAME)
    except Exception:
        # transformers not installed or model unavailable
        return None


_GENERATOR = _load_generator()



def generate_marketing_copy(product: str, features: List[str]) -> str:
    """Generate a marketing description for the given product.

    This function will use an AI model if available; otherwise it
    falls back to the simple template generator.
    """
    prompt = (
        f"Write a compelling, upbeat marketing description for a product called "
        f"{product}. Highlight the following features: {', '.join(features)}."
    )
    if _GENERATOR is not None:
        try:
            outputs = _GENERATOR(prompt, max_length=80, do_sample=True, num_return_sequences=1)
            text = outputs[0].get("generated_text", "").strip()
            # Trim the prompt from the beginning if present
            if text.lower().startswith(prompt.lower()):
                return text[len(prompt) :].lstrip()
            return text
        except Exception:
            # In case generation fails at runtime, fall back to simple version
            pass
    # Fallback
    return _simple_generate(product, features)
