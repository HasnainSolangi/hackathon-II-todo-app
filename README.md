# Hackathon II: The Evolution of Todo

## Project Overview

This project is a submission for **Hackathon II: The Evolution of Todo – Mastering Spec-Driven Development & Cloud Native AI**. The goal is to build a progressively complex software system, evolving from a simple console application to a distributed, cloud-native AI system.

## Phases

### Phase I: In-Memory Python Console App (Completed)

- **Objective:** Build a command-line todo application storing tasks in memory.
- **Location:** `phase-1/`
- **Run:**

  ```bash
  python phase-1/src/main.py
  ```

### Phase II: Full-Stack Web Application (Ready)

- **Objective:** Transform the console app into a modern multi-user web application with persistent storage (Neon DB).
- **Location:** `phase-2/`
- **Stack:** Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL, Better Auth.
- **Setup & Run:**
  1. **Backend:**

     ```bash
     cd phase-2/backend
     python -m venv venv
     .\venv\Scripts\activate
     pip install -r requirements.txt
     # Ensure .env contains DATABASE_URL and NEON_API_KEY
     uvicorn main:app --reload
     ```

  2. **Frontend:**

     ```bash
     cd phase-2/frontend
     npm install
     npm run dev
     ```

- **API Documentation:**
  - `GET /api/tasks` - List tasks
  - `POST /api/tasks` - Create task
  - `PATCH /api/tasks/{id}/complete` - Toggle completion
  - `DELETE /api/tasks/{id}` - Delete task
  
### Phase III: AI-Powered Todo Chatbot (Planned)

- **Objective:** AI Chatbot with MCP.
- View spec: `phase-2/specs/features/chatbot.md`

### Phase IV & V (Planned)

- **Objective:** Cloud Native Deployment & Event Driven Architecture.

## Repository Structure

- `phase-1/src`: Python source code for the console app.
- `phase-2/frontend`: Next.js application.
- `phase-2/backend`: FastAPI application.
- `phase-2/specs`: Specifications for features, API, DB, and UI.
- `phase-2/.spec-kit`: Spec-Kit configuration.
