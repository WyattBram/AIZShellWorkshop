"""Tests for the app.storage module."""

import pytest

from app.storage import TaskStore


def test_cancel_marks_task_cancelled():
    """Cancelling an existing task sets cancelled=True and returns it."""
    store = TaskStore()
    task = store.add("write slides")
    cancelled = store.cancel(task.id)
    assert cancelled.cancelled is True
    assert cancelled.id == task.id


def test_cancel_missing_task_raises_key_error():
    """Cancelling a task id that doesn't exist raises KeyError."""
    store = TaskStore()
    with pytest.raises(KeyError):
        store.cancel(999)


def test_cancel_already_cancelled_task_is_idempotent():
    """Cancelling a task twice does not raise and stays cancelled."""
    store = TaskStore()
    task = store.add("write slides")
    store.cancel(task.id)
    cancelled_again = store.cancel(task.id)
    assert cancelled_again.cancelled is True
