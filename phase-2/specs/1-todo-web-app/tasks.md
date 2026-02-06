# Tasks: 1-todo-web-app

**Branch**: `1-todo-web-app` | **Date**: 2026-02-06 | **Plan**: [link](../specs/1-todo-web-app/plan.md)
**Input**: Implementation plan from `/specs/1-todo-web-app/plan.md`

**Note**: This template is filled in by the `/sp.tasks` command. See `.specify/templates/commands/tasks.md` for the execution workflow.

## Summary

This document outlines the detailed, actionable tasks required to implement the authenticated multi-user Todo web application, broken down into sequential phases. Each task is designed to be independently executable and testable, supporting an incremental development approach.

## Dependencies

The following outlines the recommended order of completing user stories:

1.  User Story 1: User Registration and Authentication (P1)
2.  User Story 2: Create Personal Tasks (P1)
3.  User Story 3: View Personal Tasks (P1)
4.  User Story 4: Update Personal Tasks (P2)
5.  User Story 5: Complete Personal Tasks (P2)
6.  User Story 6: Delete Personal Tasks (P2)

## Parallel Execution Examples

Tasks marked with `[P]` can be executed in parallel where indicated, across different files or components without direct dependencies on other `[P]` tasks within the same phase.

## Phase 1: Setup - Project Initialization & Structure

*   - [ ] T001 Create monorepo structure with `/backend` and `/frontend` directories
*   - [ ] T002 Initialize Python backend project in `backend/`
*   - [ ] T003 Initialize Next.js frontend project in `frontend/`
*   - [ ] T004 Create and configure `.env` file in project root
*   - [ ] T005 Install backend dependencies from `backend/requirements.txt`
*   - [ ] T006 Install frontend dependencies in `frontend/package.json`

## Phase 2: Foundational - Core Infrastructure

*   - [ ] T007 Create `backend/src/db.py` for Neon PostgreSQL connection
*   - [ ] T008 Define `Task` SQLModel in `backend/src/models/task.py`
*   - [ ] T009 Implement JWT verification dependency in `backend/src/services/auth.py`
*   - [ ] T010 Add JWT authentication middleware to FastAPI in `backend/src/middleware/jwt_auth.py`
*   - [ ] T011 [P] Setup Better Auth configuration in `frontend/src/app/auth/`
*   - [ ] T012 [P] Enable JWT plugin for Better Auth in `frontend/src/app/auth/`
*   - [ ] T013 [P] Create API client utility in `frontend/src/lib/api.ts` to attach JWT token to requests

## Phase 3: User Story 1 - User Registration and Authentication (P1)

**Goal**: Users can register and authenticate to receive a JWT token.
**Independent Test**: A user can register, log in, and receive a JWT token that authenticates subsequent API requests.

*   - [ ] T014 [US1] Implement user registration endpoint in `backend/src/api/auth.py`
*   - [ ] T015 [US1] Implement user login endpoint in `backend/src/api/auth.py`
*   - [ ] T016 [US1] Build user sign-up page in `frontend/src/app/auth/signup/page.tsx`
*   - [ ] T017 [US1] Build user sign-in page in `frontend/src/app/auth/signin/page.tsx`
*   - [ ] T018 [US1] Integrate authentication flow with API client in `frontend/src/lib/api.ts`

## Phase 4: User Story 2 - Create Personal Tasks (P1)

**Goal**: Authenticated users can create personal tasks.
**Independent Test**: An authenticated user can create a task that appears in their personal task list.

*   - [ ] T019 [US2] Implement POST `/api/{user_id}/tasks` endpoint in `backend/src/api/tasks.py`
*   - [ ] T020 [US2] Build create task form in `frontend/src/app/tasks/components/create-task-form.tsx`

## Phase 5: User Story 3 - View Personal Tasks (P1)

**Goal**: Authenticated users can view only their personal tasks.
**Independent Test**: An authenticated user can see only their personal tasks and not tasks belonging to other users.

*   - [ ] T021 [US3] Implement GET `/api/{user_id}/tasks` endpoint in `backend/src/api/tasks.py`
*   - [ ] T022 [US3] Implement GET `/api/{user_id}/tasks/{id}` endpoint in `backend/src/api/tasks.py`
*   - [ ] T023 [US3] Build task list page in `frontend/src/app/tasks/page.tsx` to display user's tasks

## Phase 6: User Story 4 - Update Personal Tasks (P2)

**Goal**: Authenticated users can modify their personal tasks.
**Independent Test**: An authenticated user can update their personal tasks through the UI.

*   - [ ] T024 [US4] Implement PUT `/api/{user_id}/tasks/{id}` endpoint in `backend/src/api/tasks.py`
*   - [ ] T025 [US4] Add update task functionality to task components in `frontend/src/app/tasks/components/`

## Phase 7: User Story 5 - Complete Personal Tasks (P2)

**Goal**: Authenticated users can mark their tasks as complete.
**Independent Test**: An authenticated user can mark their tasks as complete using the PATCH endpoint.

*   - [ ] T026 [US5] Implement PATCH `/api/{user_id}/tasks/{id}/complete` endpoint in `backend/src/api/tasks.py`
*   - [ ] T027 [US5] Add complete toggle to task components in `frontend/src/app/tasks/components/`

## Phase 8: User Story 6 - Delete Personal Tasks (P2)

**Goal**: Authenticated users can remove their personal tasks.
**Independent Test**: An authenticated user can delete their personal tasks through the UI.

*   - [ ] T028 [US6] Implement DELETE `/api/{user_id}/tasks/{id}` endpoint in `backend/src/api/tasks.py`
*   - [ ] T029 [US6] Add delete task button to task components in `frontend/src/app/tasks/components/`

## Phase 9: Polish & Cross-Cutting Concerns

*   - [ ] T030 Add proper error handling (401, 404, 400) to backend API endpoints (`backend/src/api/tasks.py`, `backend/src/api/auth.py`)
*   - [ ] T031 Handle loading and error states gracefully in frontend UI components (`frontend/src/app/tasks/`, `frontend/src/app/auth/`)
*   - [ ] T032 Verify data isolation: Ensure `user_id` in URL matches JWT user for all backend API calls (integration test/manual verification)
*   - [ ] T033 Test persistence after restart: Verify task data remains intact after backend server restarts (integration test/manual verification)
*   - [ ] T034 Validate no unauthorized access: Comprehensive testing of authentication and authorization flows (integration test/manual verification)
