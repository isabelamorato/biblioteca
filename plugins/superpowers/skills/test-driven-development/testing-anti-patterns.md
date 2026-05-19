# Testing Anti-Patterns

**Load this reference when:** writing or changing tests, adding mocks, or tempted to add test-only methods to production code.

## The Iron Laws

```
1. NEVER test mock behavior
2. NEVER add test-only methods to production classes
3. NEVER mock without understanding dependencies
```

## Anti-Pattern 1: Testing Mock Behavior

Verifying the mock exists instead of testing real component behavior. Fix: test real component or don't mock it.

## Anti-Pattern 2: Test-Only Methods in Production

Adding methods to production classes only used by tests. Fix: put in test utilities instead.

## Anti-Pattern 3: Mocking Without Understanding

Mocking methods without knowing their side effects. Fix: understand dependencies first, mock at correct level.

## Anti-Pattern 4: Incomplete Mocks

Partial mocks that only include fields you think you need. **Iron Rule:** Mock the COMPLETE data structure as it exists in reality.

## Anti-Pattern 5: Integration Tests as Afterthought

Writing tests after implementation. Fix: TDD cycle - write failing test first.

## Quick Reference

| Anti-Pattern | Fix |
|--------------|-----|
| Assert on mock elements | Test real component or unmock it |
| Test-only methods in production | Move to test utilities |
| Mock without understanding | Understand dependencies first, mock minimally |
| Incomplete mocks | Mirror real API completely |
| Tests as afterthought | TDD - tests first |

## The Bottom Line

**Mocks are tools to isolate, not things to test.**

If TDD reveals you're testing mock behavior, you've gone wrong.
