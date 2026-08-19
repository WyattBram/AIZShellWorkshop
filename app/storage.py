"""In-memory storage for tasks."""

from app.models import Task
from app.config import MAX_TASKS


class TaskStore:
    """Dict-backed store for tasks, with a hard cap on total count."""

    def __init__(self):
        """Initialize an empty store."""
        self._tasks = {}
        self._next_id = 1

    def add(self, title: str, tags=None, due=None) -> Task:
        """Create and store a new task, enforcing the MAX_TASKS cap."""
        if len(self._tasks) >= MAX_TASKS:
            raise ValueError(f"task limit reached ({MAX_TASKS})")
        task = Task(id=self._next_id, title=title, tags=tags or [], due=due)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        """Return the task with the given id, or None if it doesn't exist."""
        return self._tasks.get(task_id)

    def complete(self, task_id: int) -> Task:
        """Mark the task with the given id as done."""
        task = self._tasks[task_id]
        task.done = True
        return task

    def by_tag(self, tag: str) -> list:
        """Return all tasks that have the given tag."""
        return [t for t in self._tasks.values() if tag in t.tags]

    def all(self) -> list:
        """Return all tasks in the store."""
        return list(self._tasks.values())
