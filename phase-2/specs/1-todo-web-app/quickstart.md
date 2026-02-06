# Quick Start Guide: Todo Web Application

**Date**: 2026-02-06
**Feature**: 1-todo-web-app

## Prerequisites

- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL-compatible database (Neon recommended)
- Environment variables configured (see below)

## Environment Setup

### Environment Variables
Create a `.env` file in the project root with the following:

```bash
# Database Configuration
DATABASE_URL="postgresql://username:password@localhost:5432/todo_app"

# Authentication Secret
BETTER_AUTH_SECRET="your-super-secret-jwt-key-here"

# Application Configuration
APP_ENV="development"
PORT="8000"
```

## Project Structure

```
todo-app/
├── backend/
│   ├── src/
│   │   ├── models/
│   │   ├── services/
│   │   ├── api/
│   │   └── middleware/
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
├── specs/
│   └── 1-todo-web-app/
└── .env
```

## Installation & Setup

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m src.main  # to initialize database and start server
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Running the Application

### Development Mode
1. Start the backend server:
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

2. Start the frontend in a new terminal:
   ```bash
   cd frontend
   npm run dev
   ```

3. Access the application at `http://localhost:3000`

### Database Migrations
Run database migrations after initial setup or after model changes:
```bash
cd backend
python -c "from src.models import create_db_and_tables; create_db_and_tables()"
```

## API Endpoints

The application provides the following authenticated endpoints:

- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Authentication Flow

1. User registers/signs in via the frontend
2. Better Auth generates JWT token
3. Token is stored in browser session/local storage
4. Frontend attaches token to Authorization header for API requests
5. Backend validates token and extracts user_id for authorization

## Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Key Features

- User registration and authentication
- Task creation, reading, updating, and deletion (CRUD)
- Task completion toggling
- User data isolation (each user sees only their own tasks)
- Persistent data storage in Neon PostgreSQL
- Responsive Next.js frontend