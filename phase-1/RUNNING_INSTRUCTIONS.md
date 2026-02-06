# Running the Phase I Todo Application

## Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install the package in development mode:

```bash
pip install -e .
```

## Running the Application

### Method 1: Direct Python Module Execution
```bash
python -m todolist
```

### Method 2: Using the Installed CLI
```bash
todo-cli
```

## Available Commands

Once the application is running, you'll see a `>` prompt. Here are the available commands:

### Task Management
- `add <title> [description] [priority] [tags]` - Add a new todo
  - Examples:
    - `add "Buy groceries" "Milk and bread" medium shopping`
    - `add "Finish report" high work`
    - `add "Morning jog" "30 minutes in park"`

- `list [all|completed|pending]` - List todos (default: all)
  - Examples:
    - `list` - Show all todos
    - `list completed` - Show only completed todos
    - `list pending` - Show only pending todos

- `view <id>` - View details of a specific todo
  - Example: `view 1`

- `update <id> <field> <value>` - Update a todo's field
  - Fields: title, description, priority, tags
  - Examples:
    - `update 1 title "Updated title"`
    - `update 1 priority high`
    - `update 1 tags work,important`

- `delete <id>` - Delete a todo
  - Example: `delete 1`

- `complete <id>` - Mark a todo as complete
  - Example: `complete 1`

- `incomplete <id>` - Mark a todo as incomplete
  - Example: `incomplete 1`

### Search and Filtering
- `search <query>` - Search todos by title or description
  - Example: `search groceries`

- `filter <type> <value>` - Filter todos
  - Types: priority, tag
  - Examples:
    - `filter priority high`
    - `filter tag work`

- `sort <key> [asc|desc]` - Sort todos
  - Keys: title, priority, created_at, updated_at, completed
  - Examples:
    - `sort created_at desc`
    - `sort title asc`

### Help and Exit
- `help`, `h`, `?` - Show help information
- `exit`, `quit`, `q` - Exit the application

## Example Session

```
> add "Buy groceries" "Milk, bread, eggs" high shopping
Added todo #1: Buy groceries

> add "Complete project" "Submit by Friday" medium work
Added todo #2: Complete project

> list
All Todos:
  [○] #1 - Buy groceries
      Description: Milk, bread, eggs
      Priority: HIGH
      Tags: shopping
      ...

  [○] #2 - Complete project
      Description: Submit by Friday
      Priority: MEDIUM
      Tags: work
      ...

> complete 1
Marked todo #1 as complete

> list completed
Completed Todos:
  [✓] #1 - Buy groceries
      ...

> update 2 title "Complete project early"
Updated title for todo #2

> view 2
Todo #2
  Title: Complete project early
  Description: Submit by Friday
  Status: Pending
  Priority: MEDIUM
  Tags: work
  ...
```

## Important Notes

1. **In-Memory Storage**: All data is stored in memory only and will be lost when the application exits.

2. **Session-Based**: Each time you start the application, you begin with a fresh list of tasks.

3. **Unique IDs**: The application automatically assigns unique sequential IDs to each task.

4. **No Persistence**: This is by design for Phase I - no files or databases are used.

## Troubleshooting

- If you get a "command not found" error, make sure you installed the package with `pip install -e .`
- If the application crashes, check that you're using Python 3.8 or higher
- For malformed commands, the application will show an error message and continue running

## Exiting the Application

Press `Ctrl+C` or type `exit`, `quit`, or `q` to exit the application.