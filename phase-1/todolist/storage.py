"""
In-memory storage layer for the Todo application
"""

from typing import Dict, List, Optional
from .todo_data import Todo, TodoList, Priority

class InMemoryStorage:
    """Manages in-memory storage for Todo items"""

    def __init__(self):
        self.todo_list = TodoList()

    def add_todo(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM, tags: List[str] = None) -> Todo:
        """Add a new todo to storage"""
        return self.todo_list.add_todo(title, description, priority, tags)

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """Retrieve a todo by ID from storage"""
        return self.todo_list.get_todo_by_id(todo_id)

    def update_todo(self, todo_id: int, title: str = None, description: str = None,
                   priority: Priority = None, tags: List[str] = None) -> bool:
        """Update a todo in storage"""
        return self.todo_list.update_todo(todo_id, title, description, priority, tags)

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo from storage"""
        return self.todo_list.delete_todo(todo_id)

    def mark_completed(self, todo_id: int) -> bool:
        """Mark a todo as completed in storage"""
        return self.todo_list.mark_completed(todo_id)

    def mark_incomplete(self, todo_id: int) -> bool:
        """Mark a todo as incomplete in storage"""
        return self.todo_list.mark_incomplete(todo_id)

    def get_all_todos(self) -> List[Todo]:
        """Get all todos from storage"""
        return self.todo_list.get_all_todos()

    def get_completed_todos(self) -> List[Todo]:
        """Get completed todos from storage"""
        return self.todo_list.get_completed_todos()

    def get_pending_todos(self) -> List[Todo]:
        """Get pending todos from storage"""
        return self.todo_list.get_pending_todos()

    def search_todos(self, query: str) -> List[Todo]:
        """Search todos in storage"""
        return self.todo_list.search_todos(query)

    def filter_by_priority(self, priority: Priority) -> List[Todo]:
        """Filter todos by priority in storage"""
        return self.todo_list.filter_by_priority(priority)

    def filter_by_tag(self, tag: str) -> List[Todo]:
        """Filter todos by tag in storage"""
        return self.todo_list.filter_by_tag(tag)

    def sort_todos(self, key: str = "created_at", reverse: bool = False) -> List[Todo]:
        """Sort todos in storage"""
        return self.todo_list.sort_todos(key, reverse)

    def get_next_id(self) -> int:
        """Get the next available ID"""
        return self.todo_list.get_next_id()