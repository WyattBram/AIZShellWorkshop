from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    tags: list = field(default_factory=list)
    done: bool = False
    due: datetime = None

    def is_overdue(self) -> bool:
        if self.due is None or self.done:
            return False
        return self.due < datetime.now()
