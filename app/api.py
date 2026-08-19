"""Thin API-layer functions wrapping the shared TaskStore."""

from app.storage import TaskStore

store = TaskStore()


def create_task(title: str, tags=None, due=None):
    """Create a new task and return its public representation."""
    task = store.add(title, tags=tags, due=due)
    return {"id": task.id, "title": task.title, "done": task.done}


def complete_task(task_id: int):
    """Mark a task as done and return its updated state."""
    task = store.complete(task_id)
    return {"id": task.id, "done": task.done}


def get_task(task_id: int):
    """Return a task by id, or a 404 error if it doesn't exist."""
    task = store.get(task_id)
    if task is None:
        return {"error": "not found"}, 404
    return {"id": task.id, "title": task.title, "done": task.done}, 200


def list_by_tag(tag: str):
    """Return the titles of all tasks that have the given tag."""
    return [t.title for t in store.by_tag(tag)]
