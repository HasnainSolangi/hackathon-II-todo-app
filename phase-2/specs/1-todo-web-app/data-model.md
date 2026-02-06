# Data Model: Todo Web Application

**Date**: 2026-02-06
**Feature**: 1-todo-web-app

## Entity Definitions

### User
Represents registered application users with authentication data.

**Fields**:
- `id` (UUID/String) - Unique identifier for the user
- `email` (String, 255) - User's email address (unique, required)
- `username` (String, 50) - User's username (unique, required)
- `password_hash` (String) - Hashed password for authentication
- `created_at` (DateTime) - Timestamp of account creation
- `updated_at` (DateTime) - Timestamp of last update

**Relationships**:
- One-to-many: User → Tasks (via user_id foreign key)

### Task
Represents individual todo items with properties.

**Fields**:
- `id` (UUID/Integer) - Unique identifier for the task
- `user_id` (UUID/String) - Foreign key linking to User entity
- `title` (String, 200) - Task title (required, 1-200 characters)
- `description` (String, 1000) - Optional task description (max 1000 characters)
- `completed` (Boolean) - Completion status (default: false)
- `created_at` (DateTime) - Timestamp of task creation
- `updated_at` (DateTime) - Timestamp of last update

**Validation Rules**:
- Title must be 1-200 characters
- Description can be empty or 1-1000 characters
- user_id must reference an existing User
- completed defaults to false

**Indexes**:
- Primary key: id
- Foreign key: user_id (indexed for efficient filtering)
- Status index: completed (indexed for filtering by completion status)

## State Transitions

### Task State Transitions
- New → Active: When task is created
- Active ↔ Completed: When task completion status toggles
- Any state → Deleted: When task is deleted

## Data Relationships

### User-Tasks Relationship
- A User can have zero or many Tasks
- A Task belongs to exactly one User
- When a User is deleted, their Tasks should also be deleted (cascade delete)

## Data Access Patterns

### Query Patterns
1. Retrieve all tasks for a specific user (GET /api/{user_id}/tasks)
2. Retrieve specific task for a user (GET /api/{user_id}/tasks/{id})
3. Filter tasks by completion status (for future enhancement)
4. Update task fields (PUT /api/{user_id}/tasks/{id})
5. Toggle task completion status (PATCH /api/{user_id}/tasks/{id}/complete)
6. Delete a specific task (DELETE /api/{user_id}/tasks/{id})

### Security Constraints
- All queries must be filtered by user_id to ensure data isolation
- Users can only access their own tasks
- No cross-user task access is allowed