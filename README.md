# ASF Actions Allowlist Gateway

list.yml contains the data about allowlisted actions and their refs.
A workflow and `scripts/gateway.py` turns this into a dummy Github Actions workflow that is checked by Dependabot.
If Dependabot finds a new version it will open a PR against the workflow to update the ref.
Once the PR is merged a workflow will update list.yml with the new ref and set an expire date on previous refs and create `approved_patterns.yml` from the date which is in turn used to set the ASF org settings.
