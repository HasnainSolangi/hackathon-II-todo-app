# Feature Specification: Better Auth Session Validation

**Feature Branch**: `001-fix-better-auth-session`  
**Created**: 2026-02-07  
**Status**: Draft  
**Input**: User description: "Update backend auth to validate Better Auth session tokens (opaque Authorization header) instead of JWT decoding"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Access Tasks With Session Token (Priority: P1)

As a signed-in user, I can call task APIs using my existing session token so my tasks load without authorization errors.

**Why this priority**: This unblocks the core product by allowing authenticated users to access their own tasks.

**Independent Test**: Can be fully tested by making an authenticated request with a valid session token and verifying a successful tasks response.

**Acceptance Scenarios**:

1. **Given** a user has a valid active session, **When** they request their tasks with that session token, **Then** the API returns the task list successfully.
2. **Given** a user has a valid active session, **When** they create a task using that session token, **Then** the task is created and returned successfully.

---

### User Story 2 - Reject Invalid Sessions (Priority: P2)

As a system owner, I need invalid or expired session tokens to be rejected so unauthorized access is blocked.

**Why this priority**: Protects user data and ensures only valid sessions can access the API.

**Independent Test**: Can be fully tested by sending an invalid or expired session token and verifying a 401 response.

**Acceptance Scenarios**:

1. **Given** an invalid or expired session token, **When** a request is made to a protected endpoint, **Then** the API returns a 401 unauthorized response.

---

### Edge Cases

- What happens when the Authorization header is missing or empty?
- How does the system handle a session token that exists but is revoked?
- What happens when the client sends extra whitespace or a malformed token value?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST treat the Authorization header value as an opaque session token, not a structured JWT.
- **FR-002**: System MUST validate session tokens against the authoritative session store before granting access.
- **FR-003**: System MUST return 401 status for requests with missing, invalid, expired, or revoked session tokens.
- **FR-004**: System MUST scope all task operations to the authenticated user associated with the session.
- **FR-005**: Client requests to task APIs MUST not require automatic redirects to succeed.

### Key Entities *(include if feature involves data)*

- **Session**: Represents an authenticated session with state (active, expired, revoked) and a token value.
- **User**: Represents the authenticated account associated with the session.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95%+ of authenticated task API requests using valid session tokens succeed without authorization errors.
- **SC-002**: 100% of requests with invalid or expired session tokens are rejected with a 401 response.
- **SC-003**: Users can load their task list on first attempt after signing in without manual retries.

## Assumptions & Dependencies

- The system already issues session tokens at sign-in and maintains an authoritative session store.
- Task endpoints already exist and require authentication for access.
