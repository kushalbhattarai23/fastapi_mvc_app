from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, controllers
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return controllers.get_tasks(db)

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return controllers.create_task(db, task)

@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = controllers.get_task(db, task_id)
        if task is None:
            raise ValueError("Task not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return task

@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    try:
        task = controllers.update_task(db, task_id, task_update)
        if task is None:
            raise ValueError("Task not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = controllers.delete_task(db, task_id)
        if task is None:
            raise ValueError("Task not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Task deleted"}

# Task Status Endpoints
used_task_ids = set()

@router.post("/task_status", response_model=schemas.TaskStatusResponse)
def create_status(task_status: schemas.TaskStatusCreate, db: Session = Depends(get_db)):
    try:
        if task_status.task_id in used_task_ids:
            raise ValueError("Task ID has already been used in Task Status")
        used_task_ids.add(task_status.task_id)
        return controllers.create_task_status(db, task_status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/task_status/{status_id}", response_model=schemas.TaskStatusResponse)
def read_status(status_id: int, db: Session = Depends(get_db)):
    try:
        status = controllers.get_task_status(db, status_id)
        if status is None:
            raise ValueError("Task Status not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return status

@router.put("/task_status/{status_id}", response_model=schemas.TaskStatusResponse)
def update_status(status_id: int, status_update: schemas.TaskStatusUpdate, db: Session = Depends(get_db)):
    try:
        status = controllers.update_task_status(db, status_id, status_update)
        if status is None:
            raise ValueError("Task Status not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return status

@router.delete("/task_status/{status_id}")
def delete_status(status_id: int, db: Session = Depends(get_db)):
    try:
        status = controllers.delete_task_status(db, status_id)
        if status is None:
            raise ValueError("Task Status not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Task Status deleted"}
