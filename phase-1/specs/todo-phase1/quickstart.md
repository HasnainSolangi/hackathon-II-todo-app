# Quickstart Guide - Phase I Todo Application

## Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies required

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install the package in development mode:
   ```
   pip install -e .
   ```

### Running the Application
```
python -m todolist
```

Or if installed via pip:
```
todo-cli
```

## Basic Commands

### Add a Task
```
add "Task title" "Optional description"
```

### List All Tasks
```
list
```

### Mark a Task Complete
```
complete 1
```

### Update a Task
```
update 1 title "New title"
```

### Delete a Task
```
delete 1
```

### Get Help
```
help
```

### Exit Application
```
exit
```

## Example Session
```
> add "Buy groceries" "Milk and bread"
Added task #1: Buy groceries

> list
All Tasks:
  [○] #1 - Buy groceries
      Description: Milk and bread

> complete 1
Task #1 marked as complete

> list completed
Completed Tasks:
  [✓] #1 - Buy groceries
      Description: Milk and bread

> exit
Goodbye!
```

## Architecture Overview

The application consists of three layers:
1. **Data Layer** (`todo_data.py`): Defines Todo entities
2. **Storage Layer** (`storage.py`): Handles in-memory operations
3. **Interface Layer** (`cli.py`): Processes commands and user interaction

This separation ensures clean architecture and maintainability.