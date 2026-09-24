# Testing

- Practice TDD: for any new feature or bug fix, write the failing test first, run it and confirm it fails for the expected reason, then write the implementation, then run the test again and confirm it passes. Do not write implementation code before the test exists.
- Every new function that touches `TaskStore` or `app/api.py` gets a matching test in `tests/`. No exceptions for "small" changes.
- After writing or changing a test, actually run `python -m pytest tests/ -q` and report the result. Don't just say a test "should pass."
- Test behavior, not implementation: assert on what a function returns or raises, not on internal calls it happens to make.
