---
id: 1
title: Update Project Constitution
stage: constitution
date: 2026-02-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

```
/sp.constitution

Project: Hackathon II – Phase II Todo Full-Stack Web Application

Core principles:
- Strict Spec-Driven Development using Claude Code + Spec-Kit Plus
- No manual coding (all implementation generated from refined specs)
- Clean separation of concerns (frontend, backend, database, auth)
- Minimal necessary implementation (no optional or advanced features)
- Monorepo architecture for single Claude Code context

Key standards:
- All features must reference specs in /specs directory
- Backend follows FastAPI + SQLModel conventions
- Frontend follows Next.js App Router patterns
- All API endpoints under /api/
- All endpoints require JWT authentication
- All database operations scoped to authenticated user
- Environment variables used for secrets (DATABASE_URL, BETTER_AUTH_SECRET)

Constraints:
- Phase II scope only (no chatbot, no Kubernetes, no Kafka)
- Implement only Basic Level features (Add, Delete, Update, View, Mark Complete)
- Persistent storage using Neon PostgreSQL
- Authentication required using Better Auth + JWT
- Monorepo structure as defined in hackathon documentation
- No intermediate or advanced features
- No additional endpoints beyond specified REST API

Success criteria:
- Multi-user web app with isolated user data
- REST API secured with JWT verification
- Tasks persist in Neon database
- Responsive frontend connected to backend
- All CRUD operations working through UI
- Unauthorized requests return 401
```

## Response snapshot

Updated the project constitution to reflect the specific requirements for the Hackathon II Todo application. Created a comprehensive constitution document that includes all the specified principles, constraints, and success criteria. Updated dependent template files to align with the constitutional requirements including authentication, security, and architectural guidelines.

## Outcome

- ✅ Impact: Created new constitution file and updated 3 dependent templates
- 🧪 Tests: No tests required for this configuration change
- 📁 Files: Updated .specify/memory/constitution.md and 3 template files
- 🔁 Next prompts: Can proceed with feature specification and planning
- 🧠 Reflection: Constitution now properly reflects project requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification