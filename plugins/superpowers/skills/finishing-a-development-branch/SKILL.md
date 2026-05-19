---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
---

# Finishing a Development Branch

**Announce at start:** "I'm using the finishing-a-development-branch skill to complete this work."

**Core principle:** Verify tests → Present options → Execute choice → Clean up.

## The Process

1. **Verify Tests** - Run project test suite. If failing, STOP.
2. **Determine Base Branch** - Find merge base from main/master.
3. **Present exactly these 4 options:**
   ```
   1. Merge back to <base-branch> locally
   2. Push and create a Pull Request
   3. Keep the branch as-is (I'll handle it later)
   4. Discard this work
   ```
4. **Execute Choice** per selected option
5. **Cleanup Worktree** for Options 1, 2, 4 only

## Red Flags

**Never:**
- Proceed with failing tests
- Merge without verifying tests on result
- Delete work without confirmation (require typed "discard")
- Force-push without explicit request

**Always:**
- Verify tests before offering options
- Present exactly 4 options
- Get typed confirmation for Option 4
- Clean up worktree for Options 1 & 4 only
