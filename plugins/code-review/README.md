# Code Review Plugin

Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives.

## Overview

The Code Review Plugin automates pull request review by launching multiple agents in parallel to independently audit changes from different perspectives. It uses confidence scoring to filter out false positives, ensuring only high-quality, actionable feedback is posted.

## Commands

### `/code-review`

Performs automated code review on a pull request using multiple specialized agents.

**What it does:**
1. Checks if review is needed (skips closed, draft, trivial, or already-reviewed PRs)
2. Gathers relevant CLAUDE.md guideline files from the repository
3. Summarizes the pull request changes
4. Launches 5 parallel agents to independently review:
   - **Agent #1**: Audit for CLAUDE.md compliance
   - **Agent #2**: Scan for obvious bugs in changes
   - **Agent #3**: Analyze git blame/history for context-based issues
   - **Agent #4**: Read previous PRs touching same files
   - **Agent #5**: Check compliance with code comments
5. Scores each issue 0-100 for confidence level
6. Filters out issues below 80 confidence threshold
7. Posts review comment with high-confidence issues only

**Usage:**
```bash
/code-review
```

## Requirements

- Git repository with GitHub integration
- GitHub CLI (`gh`) installed and authenticated
- CLAUDE.md files (optional but recommended for guideline checking)

## Author

Boris Cherny (boris@anthropic.com)
