"""Project-wide configuration values."""

import os

# Default cap on tasks per store. Overridable for load testing.
MAX_TASKS = int(os.environ.get("TASKTRACKER_MAX_TASKS", 50))
