# AGENTS.md

## Purpose
This repository follows Spec-Driven Development (SDD). No agent may write or modify code unless a corresponding spec and task exist.

All agents must follow the lifecycle:
Specify -> Plan -> Tasks -> Implement

## Scope
This project is the Hackathon II "Evolution of Todo" with 5 phases. Current repo is a monorepo with:
- `frontend/` (Next.js)
- `backend/` (FastAPI)
- `specs/` (specs)
- `.spec-kit/` (Spec-Kit config)

## Source Of Truth
- Constitution: `speckit.constitution` (if present) or `specs/` rules referenced by the phase
- Requirements: `specs/overview.md` and relevant files in `specs/features/`, `specs/api/`, `specs/database/`, `specs/ui/`
- Architecture: `specs/architecture.md` and relevant `specs/api/`, `specs/database/`
- Tasks: `speckit.tasks` (or the project task file for the phase)

If a requirement is missing or unclear, stop and request a spec update. Do not invent features.

## Rules For Agents
1. Never generate code without a Task ID.
2. Never change architecture without updating the plan spec.
3. Never propose features without updating the requirement spec.
4. Never change principles without updating the constitution.
5. Keep changes scoped to the requested task. Do not modify unrelated files.

If conflict exists, follow this priority:
Constitution > Specify > Plan > Tasks > Code

## Implementation Protocol
When implementing, include a short reference in commit message or PR description (or in code comments if required by the task):
- Task ID
- Spec references (file + section)

Example:
[Task]: T-003
[From]: specs/features/task-crud.md#Create-Task, specs/api/rest-endpoints.md#POST-/api/tasks

## Spec-KitPlus Integration
If Spec-KitPlus commands or `.claude/commands/` are available, use them to generate or update:
- `speckit.specify`
- `speckit.plan`
- `speckit.tasks`

Do not proceed to implementation until tasks exist and are approved.

## Phase Guardrails
- Phase I: CLI only, in-memory storage, Python.
- Phase II: Full-stack web app, JWT auth, Neon DB.
- Phase III: Chatbot + MCP tools + Agents SDK.
- Phase IV: Local Kubernetes deployment.
- Phase V: Cloud deployment + Kafka + Dapr.

Only implement features required by the current phase unless explicitly asked to expand.
