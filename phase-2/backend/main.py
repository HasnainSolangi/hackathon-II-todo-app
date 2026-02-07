import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from dotenv import load_dotenv
from .db import engine, init_db
from .auth import get_current_user
from .routes import tasks

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # on_startup
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
extra_origins = [o.strip() for o in os.environ.get("CORS_ORIGINS", "").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=default_origins + extra_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"], include_in_schema=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
