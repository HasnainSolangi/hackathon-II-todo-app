"""Menu-driven CLI for the Todo application."""

from typing import Optional
from ..models.task import Task, Priority
from ..services.task_service import TaskService


class TodoCLI:
    """Menu-driven CLI interface for the todo application."""

    def __init__(self):
        """Initialize the CLI."""
        self.service = TaskService()

    def display_menu(self):
        """Display the main menu."""
        print("\n=== Todo App ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print()

    def get_user_choice(self) -> str:
        """Get and validate user choice."""
        while True:
            try:
                choice = input("Enter choice: ").strip()
                if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                    return choice
                else:
                    print("Invalid choice. Please enter 1-7.")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                return "7"

    def run(self):
        """Run the CLI application."""
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_view_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_mark_complete()
            elif choice == "6":
                self.handle_mark_incomplete()
            elif choice == "7":
                print("Goodbye!")
                break

    def handle_add_task(self):
        """Handle adding a new task."""
        print("\n--- Add Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()

        print("Select priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        priority_choice = input("Enter priority (1-3, default 2): ").strip()

        if priority_choice == "1":
            priority = Priority.LOW
        elif priority_choice == "3":
            priority = Priority.HIGH
        else:
            priority = Priority.MEDIUM

        tags_input = input("Enter tags (comma-separated, optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        try:
            task = self.service.create_task(title, description, priority, tags)
            print(f"Task added successfully! ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "✓" if task.completed else "○"
            priority = task.priority.value.upper()
            tags = ", ".join(task.tags) if task.tags else "None"

            print(f"{status} [{task.id}] {task.title}")
            print(f"    Description: {task.description}")
            print(f"    Priority: {priority}")
            print(f"    Tags: {tags}")
            print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print()

    def handle_update_task(self):
        """Handle updating a task."""
        print("\n--- Update Task ---")
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks available to update.")
            return

        print("Current tasks:")
        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"  {status} [{task.id}] {task.title}")

        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID.")
            return

        task = self.service.get_task_by_id(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return

        print(f"Updating task: {task.title}")
        new_title = input(f"New title (current: '{task.title}', Enter to keep): ").strip()
        new_description = input(f"New description (current: '{task.description}', Enter to keep): ").strip()

        print(f"Current priority: {task.priority.value}")
        print("Select new priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        print("4. Keep current")
        priority_choice = input("Enter choice (1-4): ").strip()

        if priority_choice == "1":
            new_priority = Priority.LOW
        elif priority_choice == "2":
            new_priority = Priority.MEDIUM
        elif priority_choice == "3":
            new_priority = Priority.HIGH
        else:
            new_priority = task.priority

        tags_input = input(f"New tags (current: '{', '.join(task.tags) if task.tags else 'None'}, Enter to keep): ").strip()
        if tags_input:
            new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        else:
            new_tags = task.tags

        # Use empty string instead of None to indicate no change
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description else None

        success = self.service.update_task(
            task_id,
            title=title_to_update,
            description=description_to_update,
            priority=new_priority,
            tags=new_tags
        )

        if success:
            print("Task updated successfully!")
        else:
            print("Failed to update task.")

    def handle_delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks available to delete.")
            return

        print("Current tasks:")
        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"  {status} [{task.id}] {task.title}")

        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID.")
            return

        success = self.service.delete_task(task_id)
        if success:
            print("Task deleted successfully!")
        else:
            print(f"No task found with ID {task_id}.")

    def handle_mark_complete(self):
        """Handle marking a task as complete."""
        print("\n--- Mark Task Complete ---")
        pending_tasks = self.service.get_pending_tasks()

        if not pending_tasks:
            print("No pending tasks to mark as complete.")
            return

        print("Pending tasks:")
        for task in pending_tasks:
            print(f"  [{task.id}] {task.title}")

        try:
            task_id = int(input("Enter task ID to mark complete: "))
        except ValueError:
            print("Invalid task ID.")
            return

        success = self.service.mark_task_complete(task_id)
        if success:
            print("Task marked as complete!")
        else:
            print(f"No task found with ID {task_id}.")

    def handle_mark_incomplete(self):
        """Handle marking a task as incomplete."""
        print("\n--- Mark Task Incomplete ---")
        completed_tasks = self.service.get_completed_tasks()

        if not completed_tasks:
            print("No completed tasks to mark as incomplete.")
            return

        print("Completed tasks:")
        for task in completed_tasks:
            print(f"  [{task.id}] {task.title}")

        try:
            task_id = int(input("Enter task ID to mark incomplete: "))
        except ValueError:
            print("Invalid task ID.")
            return

        success = self.service.mark_task_incomplete(task_id)
        if success:
            print("Task marked as incomplete!")
        else:
            print(f"No task found with ID {task_id}.")