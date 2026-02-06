"""Task model representing a todo item."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class Priority(str, Enum):
    """Priority levels for tasks."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    """Represents a todo task."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    tags: List[str] = None
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        """Initialize optional fields."""
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.updated_at = datetime.now()

    def update_title(self, title: str):
        """Update the task title."""
        self.title = title
        self.updated_at = datetime.now()

    def update_description(self, description: str):
        """Update the task description."""
        self.description = description
        self.updated_at = datetime.now()

    def update_priority(self, priority: Priority):
        """Update the task priority."""
        self.priority = priority
        self.updated_at = datetime.now()

    def add_tag(self, tag: str):
        """Add a tag to the task."""
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()

    def remove_tag(self, tag: str):
        """Remove a tag from the task."""
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()