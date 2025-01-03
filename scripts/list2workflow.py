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
    header = """
name: Dummy Workflow

on:
  workflow_dispatch:

jobs:
  dummy:
    if: false
    runs-on: ubuntu-latest
    steps:
"""
    steps = []

    for name, refs in actions.items():
        for ref, details in refs.items():
            print(ref)
            if 'keep' in details and details["keep"]:
                # this ref will be kept regardless of a new version
                continue
            steps.append(f"      - uses: {name}@{ref}")

    return header + "\n".join(steps)
