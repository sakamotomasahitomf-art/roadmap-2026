from fastapi import APIRouter, HTTPException
from typing import List
from .models import Task, TaskCreate

router = APIRouter()

# メモリに簡易保存（学習用）
_TASKS: List[Task] = []
_NEXT_ID = 1

def _next_id() -> int:
    global _NEXT_ID
    val = _NEXT_ID
    _NEXT_ID += 1
    return val

@router.get("/tasks", response_model=List[Task])
def list_tasks():
    return _TASKS

@router.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    task = Task(id=_next_id(), **payload.model_dump())
    _TASKS.append(task)
    return task

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in _TASKS:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global _TASKS
    before = len(_TASKS)
    _TASKS = [t for t in _TASKS if t.id != task_id]
    if len(_TASKS) == before:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
