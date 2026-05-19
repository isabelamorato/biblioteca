---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## The Four Phases

### Phase 1: Root Cause Investigation

1. **Read Error Messages Carefully** - stack traces, line numbers, error codes
2. **Reproduce Consistently** - exact steps, every time
3. **Check Recent Changes** - git diff, recent commits, new dependencies
4. **Gather Evidence in Multi-Component Systems** - add diagnostic instrumentation at each component boundary
5. **Trace Data Flow** - where does bad value originate? trace up until you find source

### Phase 2: Pattern Analysis

1. Find Working Examples - similar working code in same codebase
2. Compare Against References - read reference implementation COMPLETELY
3. Identify Differences - list every difference, however small
4. Understand Dependencies - what other components, settings, environment

### Phase 3: Hypothesis and Testing

1. Form Single Hypothesis - "I think X is the root cause because Y"
2. Test Minimally - SMALLEST possible change, one variable at a time
3. Verify Before Continuing - worked? Phase 4. Didn't? Form NEW hypothesis. Don't add more fixes on top.

### Phase 4: Implementation

1. Create Failing Test Case
2. Implement Single Fix - address root cause, ONE change at a time
3. Verify Fix - test passes, no other tests broken
4. **If Fix Doesn't Work** - STOP, count attempts. If 3+: question the architecture.

## Red Flags - STOP and Follow Process

| Excuse | Reality |
|--------|--------|
| "Issue is simple" | Simple bugs have root causes too. |
| "Emergency, no time" | Systematic debugging is FASTER than guess-and-check. |
| "Just try this first" | First fix sets the pattern. Do it right. |
| "Multiple fixes at once" | Can't isolate what worked. Causes new bugs. |
| "One more fix attempt" (after 2+) | 3+ failures = architectural problem. |

## Supporting Techniques

- **`root-cause-tracing.md`** - Trace bugs backward through call stack
- **`defense-in-depth.md`** - Add validation at multiple layers after finding root cause
- **`condition-based-waiting.md`** - Replace arbitrary timeouts with condition polling
