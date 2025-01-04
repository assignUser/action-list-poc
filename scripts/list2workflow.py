from pathlib import Path
from typing import Dict, Optional, TypedDict

import yaml


class RefDetails(TypedDict):
    expires_at: str
    keep: Optional[bool]


ActionRefs = Dict[str, RefDetails]


ActionsYAML = Dict[str, ActionRefs]


def load_list(list_path: Path) -> ActionsYAML:
    with open(list_path, "r") as file:
        actions: ActionsYAML = yaml.safe_load(file)
    return actions


def generate_workflow(actions: ActionsYAML) -> str:
    header = """name: Dummy Workflow

on:
  workflow_dispatch:

jobs:
  dummy:
    if: false
    runs-on: ubuntu-latest
    steps:
"""
    steps = []
    steps.extend(
        f"      - uses: {name}@{ref}"
        for name, refs in actions.items()
        for ref, details in refs.items()
        if not details.get("keep")  # Exclude refs with "keep"
    )

    return header + "\n".join(steps)
