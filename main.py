"""
Entry point for the Business Magic Swarm.  This script exposes a
collection of small agents through a simple command-line interface.

Usage examples::

    python main.py --task marketing_copy --product "SuperWidget" --features "fast,easy to use,durable"
    python main.py --task sales_email --product "SuperWidget" --audience "Technology enthusiast"
    python main.py --task build_website --product "SuperWidget" --features "fast,easy to use,durable"

The agents themselves live in the `agents` package.  To add new tasks
you can import your agent here and extend ``AGENT_MAP`` accordingly.
"""

import argparse
from pathlib import Path
from typing import Callable, Dict, List

# Import agent functions
from agents.marketing_agent import generate_marketing_copy
from agents.sales_agent import generate_sales_email
from agents.website_agent import build_website
# Try to import the AI-powered marketing agent.  If it fails, we'll add
# a placeholder later.
try:
    from agents.ai_marketing_agent import generate_marketing_copy as generate_ai_marketing_copy  # type: ignore
except Exception:
    generate_ai_marketing_copy = None  # type: ignore


# Map command names to agent callables and required arguments
AGENT_MAP: Dict[str, Callable[..., str]] = {
    "marketing_copy": generate_marketing_copy,
    "sales_email": generate_sales_email,
    "build_website": build_website,
    # AI-powered marketing copy using an open-source transformer model.  This
    # entry will be ignored if the import failed above.
    "ai_marketing_copy": generate_ai_marketing_copy,
}


def parse_features(features: str) -> List[str]:
    """Split a comma-separated string into a list, stripping whitespace."""
    return [f.strip() for f in features.split(",") if f.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a business magic task.")
    parser.add_argument(
        "--task",
        choices=list(AGENT_MAP.keys()),
        required=True,
        help=(
            "The task to run (marketing_copy, ai_marketing_copy, sales_email, build_website)"
        ),
    )
    parser.add_argument(
        "--product",
        type=str,
        required=True,
        help="Name of the product or service",
    )
    parser.add_argument(
        "--features",
        type=str,
        default="",
        help="Comma-separated list of product features (used by marketing and website tasks)",
    )
    parser.add_argument(
        "--audience",
        type=str,
        default="",
        help="Audience description (used by sales email task)",
    )
    args = parser.parse_args()

    # Dispatch to the selected agent
    func = AGENT_MAP[args.task]
    # If the function is ``None`` (e.g. missing optional dependency),
    # produce a user-friendly error.
    if func is None:
        parser.error(
            f"The selected task '{args.task}' is not available because the required dependencies are missing."
        )
    if args.task == "marketing_copy":
        if not args.features:
            parser.error("--features is required for marketing_copy task")
        result = func(args.product, parse_features(args.features))
        print(result)
    elif args.task == "sales_email":
        audience = args.audience or "Customer"
        result = func(args.product, audience)
        print(result)
    elif args.task == "ai_marketing_copy":
        if not args.features:
            parser.error("--features is required for ai_marketing_copy task")
        result = func(args.product, parse_features(args.features))
        print(result)
    elif args.task == "build_website":
        if not args.features:
            parser.error("--features is required for build_website task")
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        html = func(args.product, parse_features(args.features))
        out_path = output_dir / "website.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"Website generated at {out_path.resolve()}")
    else:
        parser.error(f"Unknown task: {args.task}")


if __name__ == "__main__":
    main()
