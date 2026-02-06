"""Task service for managing todo operations."""

from typing import List, Optional
from ..models.task import Task, Priority


class TaskService:
    """Service for managing tasks in memory."""

    def __init__(self):
        """Initialize the task service."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def create_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        tags: List[str] = None
    ) -> Task:
        """Create a new task."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            tags=tags or []
        )

        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self._tasks.copy()

    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return [task for task in self._tasks if task.completed]

    def get_pending_tasks(self) -> List[Task]:
        """Get all pending tasks."""
        return [task for task in self._tasks if not task.completed]

    def update_task(
        self,
        task_id: int,
        title: str = None,
        description: str = None,
        priority: Priority = None,
        tags: List[str] = None
    ) -> bool:
        """Update a task."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            task.update_title(title.strip() if title else "")
        if description is not None:
            task.update_description(description.strip() if description else "")
        if priority is not None:
            task.update_priority(priority)
        if tags is not None:
            task.tags = tags.copy()

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self._tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """Mark a task as complete."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.mark_complete()
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.mark_incomplete()
        return True

    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title or description."""
        query_lower = query.lower().strip()
        if not query_lower:
            return []

        return [
            task for task in self._tasks
            if query_lower in task.title.lower() or query_lower in task.description.lower()
        ]

    def filter_by_priority(self, priority: Priority) -> List[Task]:
        """Filter tasks by priority."""
        return [task for task in self._tasks if task.priority == priority]

    def filter_by_tag(self, tag: str) -> List[Task]:
        """Filter tasks by tag."""
        return [task for task in self._tasks if tag in task.tags]