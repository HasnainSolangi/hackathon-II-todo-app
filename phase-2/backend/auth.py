# backend/auth.py
import os
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from sqlmodel import Session, select
from .db import engine 
from .models import User 
# Import the actual Session model from your models file (likely named 'Session' or 'BetterSession')
# Ensure it doesn't conflict with the 'Session' from sqlmodel
from .models import Session as BetterSession 

security = HTTPBearer()

class UserPayload(BaseModel):
    id: str
    email: str
    name: Optional[str] = None

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> UserPayload:
    token = credentials.credentials

    with Session(engine) as db_session:
        # Better Auth stores the session secret in 'token' or 'sessionToken'
        # Check your database - if using Neon/Postgres, it's usually 'token'
        statement = select(BetterSession).where(BetterSession.token == token)
        user_session = db_session.exec(statement).first()

        if not user_session:
            # If token lookup fails, try checking if the token is actually the session ID
            statement = select(BetterSession).where(BetterSession.id == token)
            user_session = db_session.exec(statement).first()

        if not user_session:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session not found in database",
            )

        # Retrieve user
        statement_user = select(User).where(User.id == user_session.user_id)
        user = db_session.exec(statement_user).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

        return UserPayload(
            id=str(user.id),
            email=user.email,
            name=user.name
        )