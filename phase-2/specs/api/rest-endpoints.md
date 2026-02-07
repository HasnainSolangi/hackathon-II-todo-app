# REST API Endpoints

## Base URL

- Development: <http://localhost:8000>
- Production: <https://api.example.com>

## Authentication

All endpoints require JWT token in header:
`Authorization: Bearer <token>`

## Endpoints

### GET /api/tasks

List all tasks for authenticated user.

Query Parameters:

- status: "all" | "pending" | "completed"
- sort: "created" | "title" | "due_date"

Response: Array of Task objects

### POST /api/tasks

Create a new task.

Request Body:

- title: string (required)
- description: string (optional)

Response: Created Task object

### PUT /api/tasks/{id}

Update a task's title or description.

Request Body:

- title: string (optional)
- description: string (optional)

Response: Updated Task object

### PATCH /api/tasks/{id}/complete

Toggle a task's completion status.

Response: Updated Task object

### DELETE /api/tasks/{id}

Delete a task.

Response: `{"ok": true}`
