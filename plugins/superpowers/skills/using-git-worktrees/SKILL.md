---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification
---

# Using Git Worktrees

**Announce at start:** "I'm using the using-git-worktrees skill to set up an isolated workspace."

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

## Directory Selection Process

1. Check existing directories: `.worktrees/` then `worktrees/` (`.worktrees` wins if both exist)
2. Check CLAUDE.md for worktree directory preference
3. Ask user if neither found

## Safety Verification

For project-local directories, MUST verify directory is ignored before creating:
```bash
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

If NOT ignored: Add to .gitignore and commit before proceeding.

## Creation Steps

1. Detect project name: `project=$(basename "$(git rev-parse --show-toplevel)")`
2. Create worktree: `git worktree add "$path" -b "$BRANCH_NAME"`
3. Run project setup (npm install, cargo build, pip install, etc.)
4. Verify clean baseline (run tests)
5. Report location and test results

## Red Flags

**Never:**
- Create worktree without verifying it's ignored (project-local)
- Skip baseline test verification
- Proceed with failing tests without asking
- Assume directory location when ambiguous

**Always:**
- Follow directory priority: existing > CLAUDE.md > ask
- Verify directory is ignored for project-local
- Auto-detect and run project setup
- Verify clean test baseline
