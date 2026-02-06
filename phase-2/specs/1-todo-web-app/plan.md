# Implementation Plan: 1-todo-web-app

**Branch**: `1-todo-web-app` | **Date**: 2026-02-06 | **Spec**: [link](../specs/1-todo-web-app/spec.md)
**Input**: Feature specification from `/specs/1-todo-web-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of an authenticated multi-user Todo web application with persistent storage using a monorepo architecture. The system consists of a Next.js frontend with authentication and a FastAPI backend with SQLModel for database operations. All API endpoints are protected with JWT authentication and ensure users only access their own data.

## Technical Context

**Language/Version**: Python 3.11, Node.js 18+
**Primary Dependencies**: FastAPI, SQLModel, Better Auth, Next.js App Router
**Storage**: Neon PostgreSQL
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application (Linux/Mac/Windows)
**Project Type**: Web application monorepo
**Performance Goals**: Responsive UI with API response times under 1 second
**Constraints**: JWT authentication required, user data isolation, minimal feature set
**Scale/Scope**: Multi-user application supporting thousands of users

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Spec-Driven Development: All implementation must be generated from refined specs using Claude Code + Spec-Kit Plus (no manual coding)
- Clean Separation of Concerns: Architecture must maintain clean separation between frontend, backend, database, and auth layers
- Minimal Implementation: Implementation must focus only on Basic Level features (Add, Delete, Update, View, Mark Complete)
- Secure Authentication: All API endpoints must be under /api/ and require JWT authentication with user-scoped database operations
- Technology Standards: Must follow FastAPI + SQLModel for backend and Next.js App Router for frontend
- Phase II Scope Compliance: Must adhere to Phase II scope (no chatbot, no Kubernetes, no Kafka) with Neon PostgreSQL

## Project Structure

### Documentation (this feature)

```text
specs/1-todo-web-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── middleware/
│   │   └── jwt_auth.py
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
└── requirements.txt

frontend/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── client.ts
│   │   ├── auth/
│   │   │   ├── signin/
│   │   │   └── signup/
│   │   ├── tasks/
│   │   │   ├── page.tsx
│   │   │   └── components/
│   │   └── layout.tsx
│   ├── components/
│   └── lib/
├── public/
├── package.json
└── tsconfig.json

.env
README.md
```

**Structure Decision**: Selected web application monorepo structure with separate backend and frontend directories to maintain clean separation of concerns while enabling shared development in a single repository.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [No violations identified] | [All constitutional principles followed] |

## 1. Monorepo Setup

- **Frontend**: Next.js App Router + TypeScript, located in `/frontend`
- **Backend**: FastAPI + SQLModel, located in `/backend`
- **Specifications**: Structured by features, api, database, ui within `/specs`
- **Documentation**: Root `CLAUDE.md` and subfolder `CLAUDE.md` files for project-level and component-level instructions.

## 2. Database Layer

- **Model**: `Task` model defined using SQLModel.
- **Fields**:
  - `id`: Unique identifier for the task.
  - `user_id`: Identifier for the user who owns the task.
  - `title`: Title of the task.
  - `description`: Optional detailed description of the task.
  - `completed`: Boolean indicating if the task is completed.
  - `created_at`: Timestamp of task creation.
  - `updated_at`: Timestamp of last task update.
- **Connection**: Connect to Neon PostgreSQL using `DATABASE_URL` environment variable.
- **Indexes**: Create indexes on `user_id` and `completed` for efficient querying.

## 3. Authentication

- **Frontend**: Configure Better Auth with JWT plugin.
- **Shared Secret**: `BETTER_AUTH_SECRET` will be shared securely between frontend and backend for JWT signing and verification.
- **FastAPI Middleware**:
  - Extract `Authorization` header from incoming requests.
  - Verify JWT signature using the shared secret.
  - Decode user information from the JWT payload.
  - Reject requests with invalid or missing tokens with a `401 Unauthorized` status.

## 4. Backend API

- **Endpoints**: Implement REST endpoints as specified in `specs/1-todo-web-app/contracts/task-api.yaml`.
- **Authorization**: Enforce that the `user_id` extracted from the JWT matches the owner of the requested task.
- **Filtering**: All database queries will be filtered by the authenticated user's `user_id`.
- **Data Models**: Use Pydantic models for request and response validation and serialization.
- **Status Codes**: Use appropriate HTTP status codes for responses (e.g., 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 404 Not Found, 422 Unprocessable Entity).

## 5. Frontend

- **Authentication Pages**: Implement user sign-up and sign-in pages.
- **Task List Page**: Display a list of tasks for the authenticated user.
- **Create Task Form**: Allow users to create new tasks.
- **Update Task Functionality**: Enable editing of existing tasks.
- **Delete Task Button**: Provide a button to delete tasks.
- **Mark Complete Toggle**: Allow users to toggle the `completed` status of a task.
- **API Client**: Develop an API client that automatically attaches the JWT to request headers.

## 6. Validation & Error Handling

- **Title Validation**: Task title is required and must be between 1 and 200 characters.
- **Description Validation**: Task description is optional and has a maximum length of 1000 characters.
- **Authentication Errors**: Return `401 Unauthorized` for missing or invalid authentication tokens.
- **Not Found Errors**: Return `404 Not Found` for tasks that do not exist or do not belong to the authenticated user.

## Execution Order

1.  **Database schema**: Define and apply the SQLModel `Task` schema.
2.  **JWT middleware**: Implement and integrate the JWT authentication middleware in FastAPI.
3.  **CRUD API endpoints**: Develop the create, read, update, and delete API endpoints for tasks, ensuring authentication and authorization.
4.  **Frontend auth integration**: Integrate Better Auth into the Next.js frontend, including sign-up/sign-in flows.
5.  **Frontend task UI**: Build the user interface for displaying, creating, updating, and deleting tasks.
6.  **End-to-end testing**: Write and execute comprehensive tests to ensure all components work together correctly.

## Risks and Mitigation

1.  **Security Vulnerabilities (JWT)**: Ensure proper JWT secret management and robust token validation to prevent unauthorized access.
2.  **Database Performance**: Monitor database queries and add/optimize indexes as needed to maintain performance.
3.  **Frontend/Backend Integration Issues**: Implement clear API contracts and comprehensive integration tests to catch issues early.

## Next Steps

The next step is to generate tasks based on this plan.
