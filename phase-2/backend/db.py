from sqlmodel import create_engine, SQLModel, Session
import os

# Use environment variable or default to a local file for dev
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./todo.db")

# For parsing Neon connection string if needed later (e.g. replacing postgres:// with postgresql://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
