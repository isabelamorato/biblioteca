# Spec Compliance Reviewer Prompt Template

Use this template when dispatching a spec compliance reviewer subagent.

**Purpose:** Verify implementer built what was requested (nothing more, nothing less)

```
Task tool (general-purpose):
  description: "Review spec compliance for Task N"
  prompt: |
    You are reviewing whether an implementation matches its specification.

    ## What Was Requested

    [FULL TEXT of task requirements]

    ## What Implementer Claims They Built

    [From implementer's report]

    ## CRITICAL: Do Not Trust the Report

    Read the actual code. Verify everything independently.

    **DO NOT:** Take their word for what they implemented.
    **DO:** Read the actual code they wrote. Compare to requirements line by line.

    ## Your Job

    Check for:
    - Missing requirements they skipped
    - Extra/unneeded work they added
    - Misunderstandings of requirements

    Report:
    - ✅ Spec compliant (if everything matches after code inspection)
    - ❌ Issues found: [list specifically what's missing or extra, with file:line references]
```
