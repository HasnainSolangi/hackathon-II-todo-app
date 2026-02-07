# Feature: Authentication

## Overview

Secure user authentication using Better Auth with JWT strategy to allow stateless backend verification. Includes support for social providers.

## User Stories

- As a user, I can sign up with email and password.
- As a user, I can sign in with email and password.
- As a user, I can sign in with Google or GitHub.
- As a user, I remain logged in across sessions.
- As a user, I can log out.

## Technical Requirements

### Frontend

- Use `better-auth/react` client.
- Implement `sign-in` and `sign-up` flows in `components/Auth.tsx`.
- Support OAuth providers: Google, GitHub.
- Handle session state with automatic token refresh.

### Backend

- Verify JWT token signature (`HS256`).
- Extract `sub` (User ID) from token claims.
- Protect API routes using `get_current_user` dependency.
- Return 401 Unauthorized for invalid/missing tokens.

### Security

- Tokens must be signed with `BETTER_AUTH_SECRET`.
- Secrets must be synchronized between Frontend and Backend.
- Client IDs/Secrets for Social Auth must be configured in `.env.local`.
