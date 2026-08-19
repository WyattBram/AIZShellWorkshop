"""Data model for a single task."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """A single task with a title, tags, and optional due date."""

    id: int
    title: str
    tags: list = field(default_factory=list)
    done: bool = False
    due: datetime = None

    def is_overdue(self) -> bool:
        """Return True if the task has an unmet due date and isn't done."""
        if self.due is None or self.done:
            return False
        return self.due < datetime.now()
