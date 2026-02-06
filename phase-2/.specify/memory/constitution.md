<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial constitution)
- Modified principles: N/A (new constitution)
- Added sections: All principles and sections based on project requirements
- Removed sections: N/A (new file)
- Templates requiring updates: ⚠ pending (.specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md)
- Follow-up TODOs: None
-->
# Hackathon II – Phase II Todo Full-Stack Web Application Constitution

## Core Principles

### Spec-Driven Development
Strict Spec-Driven Development using Claude Code + Spec-Kit Plus; No manual coding (all implementation generated from refined specs)

### Clean Separation of Concerns
Clean separation of concerns (frontend, backend, database, auth); Monorepo architecture for single Claude Code context

### Minimal Implementation
Minimal necessary implementation (no optional or advanced features); Implement only Basic Level features (Add, Delete, Update, View, Mark Complete)

### Secure Authentication
All API endpoints under /api/; All endpoints require JWT authentication; All database operations scoped to authenticated user

### Technology Standards
Backend follows FastAPI + SQLModel conventions; Frontend follows Next.js App Router patterns; Environment variables used for secrets (DATABASE_URL, BETTER_AUTH_SECRET)

### Phase II Scope Compliance
Phase II scope only (no chatbot, no Kubernetes, no Kafka); Persistent storage using Neon PostgreSQL; Authentication required using Better Auth + JWT

## Implementation Constraints

Monorepo structure as defined in hackathon documentation; No intermediate or advanced features; No additional endpoints beyond specified REST API

## Success Criteria

Multi-user web app with isolated user data; REST API secured with JWT verification; Tasks persist in Neon database; Responsive frontend connected to backend; All CRUD operations working through UI; Unauthorized requests return 401

## Governance

All features must reference specs in /specs directory; All implementations must comply with constitutional principles; Deviations require documented architectural approval

**Version**: 1.0.0 | **Ratified**: 2026-02-06 | **Last Amended**: 2026-02-06