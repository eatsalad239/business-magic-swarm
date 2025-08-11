"""
Marketing Agent
===============

This module contains a simple marketing copy generator.  Given a
product name and a list of features, it returns a short piece of
copywriting designed to highlight the key benefits of the product.  The
implementation uses a handful of templates to keep things fresh.
"""

from typing import List
import random


TEMPLATES = [
    "Introducing {product}, the solution that {features_sentence}. Experience the difference today!",
    "Say hello to {product}! With its {features_sentence}, it's exactly what you need to stay ahead of the curve.",
    "Looking for a better way to work? {product} offers {features_sentence} — all in one powerful package.",
    "{product} combines {features_sentence} to deliver unparalleled performance and value.",
]


def _join_features(features: List[str]) -> str:
    """Convert a list of features into a human‑friendly sentence."""
    if not features:
        return "everything you need"
    if len(features) == 1:
        return features[0]
    return ", ".join(features[:-1]) + f" and {features[-1]}"


def generate_marketing_copy(product: str, features: List[str]) -> str:
    """Generate a marketing description for the given product."""
    features_sentence = _join_features(features)
    template = random.choice(TEMPLATES)
    return template.format(product=product, features_sentence=features_sentence)
