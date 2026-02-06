# Claude Code Instructions

This project is a menu-driven CLI todo application built with Python.

## Project Structure

- `src/models/task.py` - Task data model with priority enum
- `src/services/task_service.py` - In-memory task management service
- `src/cli/todo_cli.py` - Menu-driven command-line interface
- `src/__main__.py` - Package entry point
- `main.py` - Direct execution entry point
- `pyproject.toml` - Project configuration and dependencies
- `README.md` - Usage instructions

## Functionality

The application provides a console menu with these options:

1. Add Task - Create tasks with title, description, priority, tags
2. View All Tasks - Display all tasks with status indicators (✓/○)
3. Update Task - Modify existing task details
4. Delete Task - Remove tasks by ID
5. Mark Task Complete - Update task completion status
6. Mark Task Incomplete - Mark completed tasks as pending
7. Exit - Close application

## Architecture

- Models: Data classes with validation
- Services: Business logic in memory
- CLI: Interactive menu interface
- Clean separation of concerns