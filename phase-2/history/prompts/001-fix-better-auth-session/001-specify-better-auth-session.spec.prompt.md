---
id: 1
title: Specify Better Auth Session
stage: spec
date: 2026-02-07
surface: agent
model: gpt-5
feature: 001-fix-better-auth-session
branch: 001-fix-better-auth-session
user: user
command: /sp.specify
labels: [specification, auth, session]
links:
  spec: ../specs/001-fix-better-auth-session/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/001-fix-better-auth-session/spec.md
  - ../specs/001-fix-better-auth-session/checklists/requirements.md
tests:
  - none
---

## Prompt

```
Update backend auth to validate Better Auth session tokens (opaque Authorization header) instead of JWT decoding.
Synchronize authentication between frontend and backend to resolve 401 Unauthorized caused by JWT decoding errors.
```

## Response snapshot

Created a new feature specification for Better Auth session validation, covering user stories, requirements, success criteria, and edge cases, plus a completed quality checklist.

## Outcome

- Impact: Created complete spec and requirements checklist
- Tests: Not applicable (spec-only)
- Files: Added spec.md and requirements checklist
- Next prompts: Ready for planning with /sp.plan
- Reflection: Scope stays focused on session validation and auth consistency

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to planning phase
