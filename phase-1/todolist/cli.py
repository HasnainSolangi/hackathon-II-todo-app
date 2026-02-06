"""
Command-line interface for the Todo application
"""

import sys
from typing import List
from .storage import InMemoryStorage
from .todo_data import Todo, Priority


class TodoCLI:
    """Command-line interface for the Todo application"""

    def __init__(self):
        self.storage = InMemoryStorage()

    def display_menu(self):
        """Display the main menu"""
        print("\n=== Todo App ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print()

    def add_todo_interactive(self):
        """Interactive method to add a new todo"""
        title = input("Enter task title: ").strip()
        if not title:
            print("Title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()

        print("Select priority (1-low, 2-medium, 3-high): ", end="")
        priority_choice = input().strip()
        if priority_choice == "1":
            priority = Priority.LOW
        elif priority_choice == "3":
            priority = Priority.HIGH
        else:  # Default to medium for 2 or invalid input
            priority = Priority.MEDIUM

        tags_input = input("Enter tags separated by commas (optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []

        new_todo = self.storage.add_todo(title, description, priority, tags)
        print(f"Added task #{new_todo.id}: {new_todo.title}")

    def update_todo_interactive(self):
        """Interactive method to update a todo"""
        if not self.storage.get_all_todos():
            print("No tasks available to update.")
            return

        self.list_todos("")  # Show all tasks first
        try:
            todo_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        todo = self.storage.get_todo_by_id(todo_id)
        if todo is None:
            print(f"No task found with ID {todo_id}")
            return

        print(f"Updating task #{todo.id}: {todo.title}")
        print(f"Current description: {todo.description}")
        print(f"Current priority: {todo.priority.value}")
        print(f"Current tags: {', '.join(todo.tags) if todo.tags else 'None'}")

        new_title = input(f"New title (current: '{todo.title}', press Enter to keep current): ").strip()
        if not new_title:
            new_title = todo.title

        new_description = input(f"New description (current: '{todo.description}', press Enter to keep current): ").strip()
        if not new_description:
            new_description = todo.description

        print(f"Current priority: {todo.priority.value}")
        priority_input = input("New priority (1-low, 2-medium, 3-high, press Enter to keep current): ").strip()
        if priority_input == "1":
            new_priority = Priority.LOW
        elif priority_input == "3":
            new_priority = Priority.HIGH
        elif priority_input == "2":
            new_priority = Priority.MEDIUM
        else:
            new_priority = todo.priority

        tags_input = input(f"New tags (current: '{', '.join(todo.tags) if todo.tags else 'None'}, press Enter to keep current): ").strip()
        if tags_input:
            new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        else:
            new_tags = todo.tags

        success = self.storage.update_todo(todo_id, new_title, new_description, new_priority, new_tags)
        if success:
            print(f"Updated task #{todo_id}")
        else:
            print(f"Failed to update task #{todo_id}")

    def delete_todo_interactive(self):
        """Interactive method to delete a todo"""
        if not self.storage.get_all_todos():
            print("No tasks available to delete.")
            return

        self.list_todos("")  # Show all tasks first
        try:
            todo_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        success = self.storage.delete_todo(todo_id)
        if success:
            print(f"Deleted task #{todo_id}")
        else:
            print(f"No task found with ID {todo_id}")

    def complete_todo_interactive(self):
        """Interactive method to mark a todo as complete"""
        pending_todos = self.storage.get_pending_todos()
        if not pending_todos:
            print("No pending tasks to mark as complete.")
            return

        print("\nPending Tasks:")
        for todo in pending_todos:
            print(f"  #{todo.id} - {todo.title}")

        try:
            todo_id = int(input("Enter task ID to mark as complete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        success = self.storage.mark_completed(todo_id)
        if success:
            print(f"Marked task #{todo_id} as complete")
        else:
            print(f"No task found with ID {todo_id}")

    def incomplete_todo_interactive(self):
        """Interactive method to mark a todo as incomplete"""
        completed_todos = self.storage.get_completed_todos()
        if not completed_todos:
            print("No completed tasks to mark as incomplete.")
            return

        print("\nCompleted Tasks:")
        for todo in completed_todos:
            print(f"  #{todo.id} - {todo.title}")

        try:
            todo_id = int(input("Enter task ID to mark as incomplete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        success = self.storage.mark_incomplete(todo_id)
        if success:
            print(f"Marked task #{todo_id} as incomplete")
        else:
            print(f"No task found with ID {todo_id}")

    def run(self):
        """Start the command-line interface with menu"""
        print("Welcome to the Todo Application!")

        while True:
            try:
                self.display_menu()
                choice = input("Enter choice: ").strip()

                if choice == "1":
                    self.add_todo_interactive()
                elif choice == "2":
                    self.list_todos("")
                elif choice == "3":
                    self.update_todo_interactive()
                elif choice == "4":
                    self.delete_todo_interactive()
                elif choice == "5":
                    self.complete_todo_interactive()
                elif choice == "6":
                    self.incomplete_todo_interactive()
                elif choice == "7":
                    self.exit_app()
                else:
                    print("Invalid choice. Please enter 1-7.")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit(0)
            except EOFError:
                print("\nGoodbye!")
                sys.exit(0)

    def show_help(self, args: str = ""):
        """Display help information"""
        help_text = """
Available Commands:
  add <title> [description] [priority] [tags] - Add a new todo
  list [all|completed|pending] - List todos (default: all)
  view <id> - View details of a specific todo
  update <id> [title|description|priority|tags] [value] - Update a todo
  delete <id> - Delete a todo
  complete <id> - Mark a todo as complete
  incomplete <id> - Mark a todo as incomplete
  search <query> - Search todos by title or description
  filter <priority|tag> <value> - Filter todos
  sort <key> [asc|desc] - Sort todos (key: title, priority, created_at, updated_at, completed)
  help, h, ? - Show this help
  exit, quit, q - Exit the application

Examples:
  add "Buy groceries" "Need to buy milk and bread" high shopping
  list completed
  update 1 title "Updated title"
  filter priority high
  sort created_at desc
        """
        print(help_text)

    def add_todo(self, args: str):
        """Add a new todo"""
        if not args:
            print("Usage: add <title> [description] [priority] [tags]")
            return

        # Parse arguments - title is required, others are optional
        parts = args.split('" "')
        if len(parts) == 1 and '"' in args:
            # Handle case where arguments contain spaces
            parts = [part.strip('"') for part in args.split('"') if part.strip()]
        else:
            parts = args.split(' ', 3)  # Split into max 4 parts: title, description, priority, tags

        if len(parts) < 1:
            print("Usage: add <title> [description] [priority] [tags]")
            return

        title = parts[0].strip()
        description = parts[1].strip() if len(parts) > 1 else ""
        priority_str = parts[2].strip() if len(parts) > 2 else "medium"
        tags_str = parts[3].strip() if len(parts) > 3 else ""

        # Parse priority
        try:
            priority = Priority[priority_str.upper()]
        except KeyError:
            print(f"Invalid priority: {priority_str}. Valid options: low, medium, high")
            return

        # Parse tags
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]

        # Add the todo
        new_todo = self.storage.add_todo(title, description, priority, tags)
        print(f"Added todo #{new_todo.id}: {new_todo.title}")

    def list_todos(self, args: str = "all"):
        """List todos"""
        arg = args.strip().lower()

        if arg == "completed":
            todos = self.storage.get_completed_todos()
            print("\nCompleted Todos:")
        elif arg == "pending":
            todos = self.storage.get_pending_todos()
            print("\nPending Todos:")
        else:
            todos = self.storage.get_all_todos()
            print("\nAll Todos:")

        if not todos:
            print("  No todos found.")
            return

        # Sort by ID for consistent display
        todos = sorted(todos, key=lambda t: t.id)

        for todo in todos:
            status = "✓" if todo.completed else "○"
            priority = todo.priority.value.upper()
            tags = ", ".join(todo.tags) if todo.tags else "None"

            print(f"  [{status}] #{todo.id} - {todo.title}")
            print(f"      Description: {todo.description}")
            print(f"      Priority: {priority}")
            print(f"      Tags: {tags}")
            print(f"      Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"      Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print()

    def view_todo(self, args: str):
        """View details of a specific todo"""
        if not args:
            print("Usage: view <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        todo = self.storage.get_todo_by_id(todo_id)
        if todo is None:
            print(f"No todo found with ID {todo_id}")
            return

        status = "Completed" if todo.completed else "Pending"
        print(f"\nTodo #{todo.id}")
        print(f"  Title: {todo.title}")
        print(f"  Description: {todo.description}")
        print(f"  Status: {status}")
        print(f"  Priority: {todo.priority.value.upper()}")
        print(f"  Tags: {', '.join(todo.tags) if todo.tags else 'None'}")
        print(f"  Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    def update_todo(self, args: str):
        """Update a todo"""
        if not args:
            print("Usage: update <id> [title|description|priority|tags] [value]")
            return

        parts = args.split(' ', 2)
        if len(parts) < 3:
            print("Usage: update <id> [title|description|priority|tags] [value]")
            return

        try:
            todo_id = int(parts[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        field = parts[1].lower()
        value = parts[2]

        todo = self.storage.get_todo_by_id(todo_id)
        if todo is None:
            print(f"No todo found with ID {todo_id}")
            return

        if field == "title":
            self.storage.update_todo(todo_id, title=value)
            print(f"Updated title for todo #{todo_id}")
        elif field == "description":
            self.storage.update_todo(todo_id, description=value)
            print(f"Updated description for todo #{todo_id}")
        elif field == "priority":
            try:
                priority = Priority[value.upper()]
                self.storage.update_todo(todo_id, priority=priority)
                print(f"Updated priority for todo #{todo_id}")
            except KeyError:
                print(f"Invalid priority: {value}. Valid options: low, medium, high")
        elif field == "tags":
            tags = [tag.strip() for tag in value.split(',')]
            self.storage.update_todo(todo_id, tags=tags)
            print(f"Updated tags for todo #{todo_id}")
        else:
            print(f"Invalid field: {field}. Valid fields: title, description, priority, tags")

    def delete_todo(self, args: str):
        """Delete a todo"""
        if not args:
            print("Usage: delete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.delete_todo(todo_id):
            print(f"Deleted todo #{todo_id}")
        else:
            print(f"No todo found with ID {todo_id}")

    def complete_todo(self, args: str):
        """Mark a todo as complete"""
        if not args:
            print("Usage: complete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.mark_completed(todo_id):
            print(f"Marked todo #{todo_id} as complete")
        else:
            print(f"No todo found with ID {todo_id}")

    def incomplete_todo(self, args: str):
        """Mark a todo as incomplete"""
        if not args:
            print("Usage: incomplete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.mark_incomplete(todo_id):
            print(f"Marked todo #{todo_id} as incomplete")
        else:
            print(f"No todo found with ID {todo_id}")

    def search_todos(self, args: str):
        """Search todos by title or description"""
        if not args:
            print("Usage: search <query>")
            return

        query = args.strip()
        todos = self.storage.search_todos(query)

        if not todos:
            print(f"No todos found matching '{query}'")
            return

        print(f"\nSearch results for '{query}':")
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def filter_todos(self, args: str):
        """Filter todos by priority or tag"""
        if not args:
            print("Usage: filter <priority|tag> <value>")
            return

        parts = args.split(' ', 1)
        if len(parts) != 2:
            print("Usage: filter <priority|tag> <value>")
            return

        filter_type = parts[0].lower()
        value = parts[1]

        if filter_type == "priority":
            try:
                priority = Priority[value.upper()]
                todos = self.storage.filter_by_priority(priority)
                print(f"\nTodos with priority {value.upper()}:")
            except KeyError:
                print(f"Invalid priority: {value}. Valid options: low, medium, high")
                return
        elif filter_type == "tag":
            todos = self.storage.filter_by_tag(value)
            print(f"\nTodos with tag '{value}':")
        else:
            print(f"Invalid filter type: {filter_type}. Valid types: priority, tag")
            return

        if not todos:
            print("  No todos found.")
            return

        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def sort_todos(self, args: str):
        """Sort todos by a specific key"""
        if not args:
            print("Usage: sort <key> [asc|desc]")
            return

        parts = args.split()
        if len(parts) < 1 or len(parts) > 2:
            print("Usage: sort <key> [asc|desc]")
            return

        key = parts[0]
        order = parts[1].lower() if len(parts) > 1 else "asc"

        if order not in ["asc", "desc"]:
            print("Order must be 'asc' or 'desc'")
            return

        reverse = True if order == "desc" else False

        valid_keys = ["title", "priority", "created_at", "updated_at", "completed"]
        if key not in valid_keys:
            print(f"Invalid sort key: {key}. Valid keys: {', '.join(valid_keys)}")
            return

        todos = self.storage.sort_todos(key=key, reverse=reverse)
        print(f"\nTodos sorted by {key} ({order}):")
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def exit_app(self, args: str = ""):
        """Exit the application"""
        print("Goodbye!")
        sys.exit(0)


    def show_help(self, args: str = ""):
        """Display help information"""
        help_text = """
Available Commands:
  add <title> [description] [priority] [tags] - Add a new todo
  list [all|completed|pending] - List todos (default: all)
  view <id> - View details of a specific todo
  update <id> [title|description|priority|tags] [value] - Update a todo
  delete <id> - Delete a todo
  complete <id> - Mark a todo as complete
  incomplete <id> - Mark a todo as incomplete
  search <query> - Search todos by title or description
  filter <priority|tag> <value> - Filter todos
  sort <key> [asc|desc] - Sort todos (key: title, priority, created_at, updated_at, completed)
  help, h, ? - Show this help
  exit, quit, q - Exit the application

Examples:
  add "Buy groceries" "Need to buy milk and bread" high shopping
  list completed
  update 1 title "Updated title"
  filter priority high
  sort created_at desc
        """
        print(help_text)

    def add_todo(self, args: str):
        """Add a new todo"""
        if not args:
            print("Usage: add <title> [description] [priority] [tags]")
            return

        # Parse arguments - title is required, others are optional
        parts = args.split('" "')
        if len(parts) == 1 and '"' in args:
            # Handle case where arguments contain spaces
            parts = [part.strip('"') for part in args.split('"') if part.strip()]
        else:
            parts = args.split(' ', 3)  # Split into max 4 parts: title, description, priority, tags

        if len(parts) < 1:
            print("Usage: add <title> [description] [priority] [tags]")
            return

        title = parts[0].strip()
        description = parts[1].strip() if len(parts) > 1 else ""
        priority_str = parts[2].strip() if len(parts) > 2 else "medium"
        tags_str = parts[3].strip() if len(parts) > 3 else ""

        # Parse priority
        try:
            priority = Priority[priority_str.upper()]
        except KeyError:
            print(f"Invalid priority: {priority_str}. Valid options: low, medium, high")
            return

        # Parse tags
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]

        # Add the todo
        new_todo = self.storage.add_todo(title, description, priority, tags)
        print(f"Added todo #{new_todo.id}: {new_todo.title}")

    def list_todos(self, args: str = "all"):
        """List todos"""
        arg = args.strip().lower()

        if arg == "completed":
            todos = self.storage.get_completed_todos()
            print("\nCompleted Todos:")
        elif arg == "pending":
            todos = self.storage.get_pending_todos()
            print("\nPending Todos:")
        else:
            todos = self.storage.get_all_todos()
            print("\nAll Todos:")

        if not todos:
            print("  No todos found.")
            return

        # Sort by ID for consistent display
        todos = sorted(todos, key=lambda t: t.id)

        for todo in todos:
            status = "✓" if todo.completed else "○"
            priority = todo.priority.value.upper()
            tags = ", ".join(todo.tags) if todo.tags else "None"

            print(f"  [{status}] #{todo.id} - {todo.title}")
            print(f"      Description: {todo.description}")
            print(f"      Priority: {priority}")
            print(f"      Tags: {tags}")
            print(f"      Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"      Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print()

    def view_todo(self, args: str):
        """View details of a specific todo"""
        if not args:
            print("Usage: view <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        todo = self.storage.get_todo_by_id(todo_id)
        if todo is None:
            print(f"No todo found with ID {todo_id}")
            return

        status = "Completed" if todo.completed else "Pending"
        print(f"\nTodo #{todo.id}")
        print(f"  Title: {todo.title}")
        print(f"  Description: {todo.description}")
        print(f"  Status: {status}")
        print(f"  Priority: {todo.priority.value.upper()}")
        print(f"  Tags: {', '.join(todo.tags) if todo.tags else 'None'}")
        print(f"  Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Updated: {todo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    def update_todo(self, args: str):
        """Update a todo"""
        if not args:
            print("Usage: update <id> [title|description|priority|tags] [value]")
            return

        parts = args.split(' ', 2)
        if len(parts) < 3:
            print("Usage: update <id> [title|description|priority|tags] [value]")
            return

        try:
            todo_id = int(parts[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        field = parts[1].lower()
        value = parts[2]

        todo = self.storage.get_todo_by_id(todo_id)
        if todo is None:
            print(f"No todo found with ID {todo_id}")
            return

        if field == "title":
            self.storage.update_todo(todo_id, title=value)
            print(f"Updated title for todo #{todo_id}")
        elif field == "description":
            self.storage.update_todo(todo_id, description=value)
            print(f"Updated description for todo #{todo_id}")
        elif field == "priority":
            try:
                priority = Priority[value.upper()]
                self.storage.update_todo(todo_id, priority=priority)
                print(f"Updated priority for todo #{todo_id}")
            except KeyError:
                print(f"Invalid priority: {value}. Valid options: low, medium, high")
        elif field == "tags":
            tags = [tag.strip() for tag in value.split(',')]
            self.storage.update_todo(todo_id, tags=tags)
            print(f"Updated tags for todo #{todo_id}")
        else:
            print(f"Invalid field: {field}. Valid fields: title, description, priority, tags")

    def delete_todo(self, args: str):
        """Delete a todo"""
        if not args:
            print("Usage: delete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.delete_todo(todo_id):
            print(f"Deleted todo #{todo_id}")
        else:
            print(f"No todo found with ID {todo_id}")

    def complete_todo(self, args: str):
        """Mark a todo as complete"""
        if not args:
            print("Usage: complete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.mark_completed(todo_id):
            print(f"Marked todo #{todo_id} as complete")
        else:
            print(f"No todo found with ID {todo_id}")

    def incomplete_todo(self, args: str):
        """Mark a todo as incomplete"""
        if not args:
            print("Usage: incomplete <id>")
            return

        try:
            todo_id = int(args.strip())
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        if self.storage.mark_incomplete(todo_id):
            print(f"Marked todo #{todo_id} as incomplete")
        else:
            print(f"No todo found with ID {todo_id}")

    def search_todos(self, args: str):
        """Search todos by title or description"""
        if not args:
            print("Usage: search <query>")
            return

        query = args.strip()
        todos = self.storage.search_todos(query)

        if not todos:
            print(f"No todos found matching '{query}'")
            return

        print(f"\nSearch results for '{query}':")
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def filter_todos(self, args: str):
        """Filter todos by priority or tag"""
        if not args:
            print("Usage: filter <priority|tag> <value>")
            return

        parts = args.split(' ', 1)
        if len(parts) != 2:
            print("Usage: filter <priority|tag> <value>")
            return

        filter_type = parts[0].lower()
        value = parts[1]

        if filter_type == "priority":
            try:
                priority = Priority[value.upper()]
                todos = self.storage.filter_by_priority(priority)
                print(f"\nTodos with priority {value.upper()}:")
            except KeyError:
                print(f"Invalid priority: {value}. Valid options: low, medium, high")
                return
        elif filter_type == "tag":
            todos = self.storage.filter_by_tag(value)
            print(f"\nTodos with tag '{value}':")
        else:
            print(f"Invalid filter type: {filter_type}. Valid types: priority, tag")
            return

        if not todos:
            print("  No todos found.")
            return

        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def sort_todos(self, args: str):
        """Sort todos by a specific key"""
        if not args:
            print("Usage: sort <key> [asc|desc]")
            return

        parts = args.split()
        if len(parts) < 1 or len(parts) > 2:
            print("Usage: sort <key> [asc|desc]")
            return

        key = parts[0]
        order = parts[1].lower() if len(parts) > 1 else "asc"

        if order not in ["asc", "desc"]:
            print("Order must be 'asc' or 'desc'")
            return

        reverse = True if order == "desc" else False

        valid_keys = ["title", "priority", "created_at", "updated_at", "completed"]
        if key not in valid_keys:
            print(f"Invalid sort key: {key}. Valid keys: {', '.join(valid_keys)}")
            return

        todos = self.storage.sort_todos(key=key, reverse=reverse)
        print(f"\nTodos sorted by {key} ({order}):")
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"  [{status}] #{todo.id} - {todo.title}")

    def exit_app(self, args: str = ""):
        """Exit the application"""
        print("Goodbye!")
        sys.exit(0)


def main():
    """Main entry point for the CLI"""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()