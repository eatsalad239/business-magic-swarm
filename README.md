# Business Magic Swarm

**Business Magic Swarm** is a minimal open source toolkit that bundles
several small agents into a single command‑line application.  The goal
is to provide "magic button" functionality for common business tasks
without requiring any proprietary services or API keys.  Each agent
encapsulates a specific workflow, and the main entry point (`main.py`)
allows you to select which workflow to run.

## Features

Currently the repository includes three example agents:

| Task                      | Description |
|--------------------------|-------------|
| Marketing copy generator | Takes a product name and a list of features and produces a short, upbeat marketing description. |
| Sales email generator    | Composes a friendly follow‑up email to a potential customer, highlighting the product and inviting the reader to take action. |
| Website builder          | Generates a simple static web page (`output/website.html`) showcasing the product and its features, using clean HTML and CSS. |

These agents are intentionally lightweight and operate on local
resources only.  They demonstrate how you can structure a project so
that adding new functionality is as simple as creating another agent
module and wiring it up in `main.py`.

## Getting started

1. Ensure you have Python 3.8+ installed.  No external dependencies are
   required—everything uses the Python standard library.
2. Clone this repository or copy the `business_magic_swarm` directory
   into your own project.
3. From the `business_magic_swarm` directory, run one of the following
   commands:

   ```bash
   # Generate marketing copy
   python main.py --task marketing_copy --product "SuperWidget" --features "fast,easy to use,durable"

   # Generate a sales email
   python main.py --task sales_email --product "SuperWidget" --audience "Technology enthusiast"

   # Build a simple website
   python main.py --task build_website --product "SuperWidget" --features "fast,easy to use,durable"
   ```

4. Check the console output or open the generated HTML file in the
   `output/` directory to see the result.

## Extending the swarm

To add new business tasks, simply create another module under the
`agents/` package exposing a single function.  Then update the
`AGENT_MAP` dictionary in `main.py` to register your new agent with
an associated command‑line task.
