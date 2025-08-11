"""
Website Agent
=============

This module contains a very simple static website generator.  Given a
product name and a list of features it produces an HTML page that can
be viewed in any browser.  The page includes basic styling and a
bulleted list of features.
"""

from typing import List


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 2rem;
            background-color: #f9f9f9;
        }}
        h1 {{
            color: #333;
        }}
        ul {{
            list-style-type: disc;
            margin-left: 1.5rem;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            padding: 1rem;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{product}</h1>
        <p>Discover the benefits of {product}:</p>
        <ul>
            {features_list}
        </ul>
    </div>
</body>
</html>
"""


def build_website(product: str, features: List[str]) -> str:
    """Return an HTML page as a string for the given product."""
    items = [f"<li>{feature}</li>" for feature in features] or ["<li>Amazing benefits you have to see to believe</li>"]
    features_list = "\n            ".join(items)
    return HTML_TEMPLATE.format(product=product, features_list=features_list)
