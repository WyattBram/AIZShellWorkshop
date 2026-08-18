from app.models import Task
from app.config import MAX_TASKS


class TaskStore:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title: str, tags=None, due=None) -> Task:
        if len(self._tasks) >= MAX_TASKS:
            raise ValueError(f"task limit reached ({MAX_TASKS})")
        task = Task(id=self._next_id, title=title, tags=tags or [], due=due)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        return self._tasks.get(task_id)

    def complete(self, task_id: int) -> Task:
        task = self._tasks[task_id]
        task.done = True
        return task

    def by_tag(self, tag: str) -> list:
        return [t for t in self._tasks.values() if tag in t.tags]

    def all(self) -> list:
        return list(self._tasks.values())
