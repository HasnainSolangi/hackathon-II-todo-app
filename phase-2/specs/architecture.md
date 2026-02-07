# System Architecture

## Overview

The system follows a modern full-stack architecture using Next.js for the frontend and FastAPI for the backend, communicating via REST API. Authentication is handled by Better Auth with JWT tokens properly verified by the backend.

## Components

### Frontend (Next.js)

- **Framework**: Next.js 16+ (App Router)
- **Styling**: Tailwind CSS
- **State Management**: React Hooks
- **Auth Client**: Better Auth React Client

### Backend (FastAPI)

- **Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Auth Middleware**: Custom dependency verifying Better Auth JWTs

## Data Flow

1. User logs in via Frontend (Better Auth).
2. JWT Token is issued and stored (Cookie/Storage).
3. Frontend attaches Token to API requests (Authorization: Bearer).
4. Backend verifies Token using Shared Secret.
5. Backend queries Database (Neon) for user-scoped data.
6. Response is returned to Frontend.
