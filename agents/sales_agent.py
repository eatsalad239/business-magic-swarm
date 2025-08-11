"""
Sales Agent
===========

This module contains a basic sales email generator.  It takes a
product name and an audience description and returns a friendly,
personalised email that highlights the value of the product and
encourages the reader to take the next step.
"""

from typing import List


def generate_sales_email(product: str, audience: str) -> str:
    """Generate a sales follow‑up email."""
    lines = [
        f"Hi {audience},",
        "",
        f"I hope you're doing well! I'm reaching out to share some exciting news about {product}.",
        f"This product has been designed with people like you in mind, helping you achieve more by providing –",
        f"a seamless experience and real value.",
        "",
        "I'd love to tell you more or answer any questions you might have. When would be a good time to connect?",
        "",
        "Best regards,",
        f"The {product} Team",
    ]
    return "\n".join(lines)
