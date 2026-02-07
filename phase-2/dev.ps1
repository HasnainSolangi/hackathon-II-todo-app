$ErrorActionPreference = "Stop"

Start-Process powershell -WindowStyle Normal -ArgumentList @(
    "-NoExit",
    "-Command",
    "cd f:\hackathon-II-todo-app\phase-2; python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000"
)

Start-Process powershell -WindowStyle Normal -ArgumentList @(
    "-NoExit",
    "-Command",
    "cd f:\hackathon-II-todo-app\phase-2\frontend; npm run dev"
)
