"""
Todo data structures for the in-memory console application
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass, field

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class Todo:
    """Represents a single todo item"""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        # Ensure updated_at is set to current time when created
        if self.updated_at == self.created_at:
            self.updated_at = datetime.now()

    def mark_completed(self):
        """Mark the todo as completed and update timestamp"""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the todo as incomplete and update timestamp"""
        self.completed = False
        self.updated_at = datetime.now()

    def update_title(self, new_title: str):
        """Update the title and update timestamp"""
        self.title = new_title
        self.updated_at = datetime.now()

    def update_description(self, new_description: str):
        """Update the description and update timestamp"""
        self.description = new_description
        self.updated_at = datetime.now()

    def update_priority(self, new_priority: Priority):
        """Update the priority and update timestamp"""
        self.priority = new_priority
        self.updated_at = datetime.now()

    def add_tag(self, tag: str):
        """Add a tag to the todo and update timestamp"""
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()

    def remove_tag(self, tag: str):
        """Remove a tag from the todo and update timestamp"""
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()

@dataclass
class TodoList:
    """Manages a collection of Todo items in memory"""
    todos: List[Todo] = field(default_factory=list)
    _next_id: int = 1

    def add_todo(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM, tags: List[str] = None) -> Todo:
        """Add a new todo to the list"""
        if tags is None:
            tags = []

        new_todo = Todo(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags.copy()
        )

        self.todos.append(new_todo)
        self._next_id += 1
        return new_todo

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """Retrieve a todo by its ID"""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: str = None, description: str = None,
                   priority: Priority = None, tags: List[str] = None) -> bool:
        """Update a todo's properties"""
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return False

        if title is not None:
            todo.update_title(title)
        if description is not None:
            todo.update_description(description)
        if priority is not None:
            todo.update_priority(priority)
        if tags is not None:
            todo.tags = tags.copy()
            todo.updated_at = datetime.now()

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """Remove a todo from the list"""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_completed(self, todo_id: int) -> bool:
        """Mark a todo as completed"""
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_completed()
            return True
        return False

    def mark_incomplete(self, todo_id: int) -> bool:
        """Mark a todo as incomplete"""
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_incomplete()
            return True
        return False

    def get_all_todos(self) -> List[Todo]:
        """Get all todos"""
        return self.todos.copy()

    def get_completed_todos(self) -> List[Todo]:
        """Get all completed todos"""
        return [todo for todo in self.todos if todo.completed]

    def get_pending_todos(self) -> List[Todo]:
        """Get all pending (not completed) todos"""
        return [todo for todo in self.todos if not todo.completed]

    def search_todos(self, query: str) -> List[Todo]:
        """Search todos by title or description"""
        query_lower = query.lower()
        return [
            todo for todo in self.todos
            if query_lower in todo.title.lower() or query_lower in todo.description.lower()
        ]

    def filter_by_priority(self, priority: Priority) -> List[Todo]:
        """Filter todos by priority"""
        return [todo for todo in self.todos if todo.priority == priority]

    def filter_by_tag(self, tag: str) -> List[Todo]:
        """Filter todos by tag"""
        return [todo for todo in self.todos if tag in todo.tags]

    def sort_todos(self, key: str = "created_at", reverse: bool = False) -> List[Todo]:
        """Sort todos by specified attribute"""
        if key == "title":
            return sorted(self.todos, key=lambda x: x.title, reverse=reverse)
        elif key == "priority":
            return sorted(self.todos, key=lambda x: x.priority.value, reverse=reverse)
        elif key == "created_at":
            return sorted(self.todos, key=lambda x: x.created_at, reverse=reverse)
        elif key == "updated_at":
            return sorted(self.todos, key=lambda x: x.updated_at, reverse=reverse)
        elif key == "completed":
            return sorted(self.todos, key=lambda x: x.completed, reverse=reverse)
        else:
            return self.todos.copy()

    def get_next_id(self) -> int:
        """Get the next available ID"""
        return self._next_id