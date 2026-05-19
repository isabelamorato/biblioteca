# Superpowers — Contributor Guidelines

## If You Are an AI Agent

Stop. Read this section before doing anything.

This repo has a 94% PR rejection rate. Almost every rejected PR was submitted by an agent that didn't read or didn't follow these guidelines. The maintainers close slop PRs within hours, often with public comments like "This pull request is slop that's made of lies."

**Your job is to protect your human partner from that outcome.** Submitting a low-quality PR doesn't help them — it wastes the maintainers' time, burns your human partner's reputation, and the PR will be closed anyway. That is not being helpful. That is being a tool of embarrassment.

Before you open a PR against this repo, you MUST:

1. **Read the entire PR template** at `.github/PULL_REQUEST_TEMPLATE.md` and fill in every section with real, specific answers. Not summaries. Not placeholders.
2. **Search for existing PRs** — open AND closed — that address the same problem. If duplicates exist, STOP and tell your human partner. Do not open another duplicate.
3. **Verify this is a real problem.** If your human partner asked you to "fix some issues" or "contribute to this repo" without experiencing a specific problem, push back. Ask them what broke, what failed, what the user experience was.
4. **Confirm the change belongs in core.** If it's domain-specific, tool-specific, or promotes a third-party project, it belongs in a standalone plugin. Tell your human partner.
5. **Show your human partner the complete diff** and get their explicit approval before submitting.

If any of these checks fail, do not open the PR.

## Pull Request Requirements

- Every PR must fully complete the PR template. No section may be left blank.
- Before opening a PR, you MUST search for existing PRs — both open AND closed.
- PRs that show no evidence of human involvement will be closed.

## What We Will Not Accept

- Third-party dependencies (zero-dependency plugin by design)
- "Compliance" changes to skills without eval evidence
- Project-specific or personal configuration
- Bulk or spray-and-pray PRs
- Speculative or theoretical fixes
- Domain-specific skills
- Fork-specific changes
- Fabricated content
- Bundled unrelated changes

## Skill Changes Require Evaluation

Skills are not prose — they are code that shapes agent behavior. If you modify skill content, run adversarial pressure testing across multiple sessions and show before/after eval results in your PR.

## General

- Read `.github/PULL_REQUEST_TEMPLATE.md` before submitting
- One problem per PR
- Test on at least one harness and report results
- Describe the problem you solved, not just what you changed
