# ASF Actions Allowlist Gateway

- actions.yml contains the data about allowlisted actions and their refs
- a workflow and `scripts/gateway.py` turns this into a dummy Github Actions workflow that is checked by Dependabot
- if Dependabot finds a new version it will open a PR against the workflow to update the ref
- once the PR is merged a workflow will update actions.yml with the new ref and set an expire date on previous refs and create `approved_patterns.yml` from the data which is in turn used to set the ASF org settings
- a cron job removes expired refs and actions with no refs from `actions.yml`
