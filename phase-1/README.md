# Todo CLI Application

A menu-driven CLI application for managing todo tasks.

## Features

- Add tasks with title, description, priority, and tags
- View all tasks with status indicators
- Update task details
- Delete tasks by ID
- Mark tasks as complete/incomplete

## Setup

1. Ensure you have Python 3.11+ installed
2. Install dependencies: `uv sync` (if using uv) or `pip install -e .`

## Usage

Run the application:

```bash
python main.py
# or if installed as a package
todo-cli
```

## Functionality

The application provides a menu-driven interface with the following options:

1. **Add Task** - Create a new todo task
2. **View All Tasks** - List all tasks with status indicators
3. **Update Task** - Modify existing task details
4. **Delete Task** - Remove a task by ID
5. **Mark Task Complete** - Mark a pending task as complete
6. **Mark Task Incomplete** - Mark a completed task as incomplete
7. **Exit** - Close the application

## Architecture

The application follows a clean architecture pattern:

- `src/models/` - Data models (Task class)
- `src/services/` - Business logic (TaskService)
- `src/cli/` - User interface (TodoCLI)
- `src/__main__.py` - Application entry point