# Branching Notes

This document explains the Git workflow used in this repository.

## Branches

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready code. Never commit directly here. |
| `develop` | Integration branch where finished features are merged and tested. |
| `feature/<name>` | New features, e.g. `feature/add-calculator`. Created from `develop`. |
| `bugfix/<name>` | Fixes for non-urgent bugs. Created from `develop`. |
| `hotfix/<name>` | Urgent fixes for production. Created from `main`. |

## Workflow

1. Create a branch from `develop`:
   `git checkout develop && git checkout -b feature/my-feature`
2. Make small, focused commits.
3. Push the branch and open a Pull Request into `develop`.
4. After review and passing tests, merge the PR.
5. When `develop` is stable, merge it into `main` and tag a release (e.g. `v1.0.0`).

## Commit Message Convention

Use a short prefix followed by a clear description:

- `feat:` a new feature
- `fix:` a bug fix
- `docs:` documentation changes
- `test:` adding or updating tests
- `chore:` maintenance (config, .gitignore, etc.)

Example: `feat: add divide function with zero check`

## Rules

- Never force-push to `main` or `develop`.
- Keep branches short-lived; delete them after merging.
- Every change must be tested before merging.
