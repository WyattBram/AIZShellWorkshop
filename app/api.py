from app.storage import TaskStore

store = TaskStore()


def create_task(title: str, tags=None, due=None):
    task = store.add(title, tags=tags, due=due)
    return {"id": task.id, "title": task.title, "done": task.done}


def complete_task(task_id: int):
    task = store.complete(task_id)
    return {"id": task.id, "done": task.done}


def get_task(task_id: int):
    task = store.get(task_id)
    if task is None:
        return {"error": "not found"}, 404
    return {"id": task.id, "title": task.title, "done": task.done}, 200


def list_by_tag(tag: str):
    return [t.title for t in store.by_tag(tag)]
