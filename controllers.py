from sqlalchemy.orm import Session
import models, schemas

# Get all tasks
def get_tasks(db: Session):
    return db.query(models.TaskModel).all()

# Create a new task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get a specific task by ID
def get_task(db: Session, task_id: int):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not task:
        raise ValueError("Task not found")
    return task

# Update an existing task by ID
def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not task:
        raise ValueError("Task not found")

    # Update the task fields based on the provided update
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.time_to_complete is not None:
        task.time_to_complete = task_update.time_to_complete
    if task_update.description is not None:
        task.description = task_update.description

    db.commit()
    db.refresh(task)
    return task

# Delete a task by ID
def delete_task(db: Session, task_id: int):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not task:
        raise ValueError("Task not found")
    
    db.delete(task)
    db.commit()
    return task

# Create a new task status
def create_task_status(db: Session, task_status: schemas.TaskStatusCreate):
    # Ensure task_id has not been used for a task status before
    existing_status = db.query(models.TaskStatus).filter(models.TaskStatus.task_id == task_status.task_id).first()
    if existing_status:
        raise ValueError(f"Task ID {task_status.task_id} has already been used for Task Status.")
    
    db_status = models.TaskStatus(**task_status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

# Get a specific task status by ID
def get_task_status(db: Session, status_id: int):
    status = db.query(models.TaskStatus).filter(models.TaskStatus.id == status_id).first()
    if not status:
        raise ValueError("Task Status not found")
    return status

# Update a task status by ID
def update_task_status(db: Session, status_id: int, status_update: schemas.TaskStatusUpdate):
    status = db.query(models.TaskStatus).filter(models.TaskStatus.id == status_id).first()
    if not status:
        raise ValueError("Task Status not found")

    # Update the status fields based on the provided update
    if status_update.is_completed is not None:
        status.is_completed = status_update.is_completed
    if status_update.completed_per is not None:
        status.completed_per = status_update.completed_per

    db.commit()
    db.refresh(status)
    return status

# Delete a task status by ID
def delete_task_status(db: Session, status_id: int):
    status = db.query(models.TaskStatus).filter(models.TaskStatus.id == status_id).first()
    if not status:
        raise ValueError("Task Status not found")

    db.delete(status)
    db.commit()
    return status
