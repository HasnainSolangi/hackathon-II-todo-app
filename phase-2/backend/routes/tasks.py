from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from typing import List, Optional
from ..db import get_session
from ..models import Task, TaskCreate, TaskUpdate
from ..auth import get_current_user, UserPayload

router = APIRouter()

@router.get("/", response_model=List[Task])
async def read_tasks(
    task_status: Optional[str] = Query(None, pattern="^(all|pending|completed)$"),
    session: Session = Depends(get_session),
    user: UserPayload = Depends(get_current_user)
):
    query = select(Task).where(Task.user_id == user.id)
    
    if task_status == "pending":
        query = query.where(Task.completed == False)
    elif task_status == "completed":
        query = query.where(Task.completed == True)
    
    tasks = session.exec(query).all()
    return tasks

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    session: Session = Depends(get_session),
    user: UserPayload = Depends(get_current_user)
):
    try:
        new_task = Task.model_validate(task_data)
        new_task.user_id = user.id
        new_task.completed = False
        
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task
    except Exception as e:
        session.rollback()
        print(f"ERROR adding task: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not save task to database"
        )

@router.patch("/{task_id}/complete/", response_model=Task)
async def toggle_task_complete(
    task_id: int,
    session: Session = Depends(get_session),
    user: UserPayload = Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.completed = not task.completed
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.put("/{task_id}/", response_model=Task)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    session: Session = Depends(get_session),
    user: UserPayload = Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
        
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/{task_id}/")
async def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    user: UserPayload = Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return {"ok": True}