from pydantic import BaseModel
from typing import Optional

# Task Create Schema
class TaskCreate(BaseModel):
    title: str
    time_to_complete: int
    description: str

# Task Response Schema
class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# Task Update Schema (optional for partial updates)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    time_to_complete: Optional[int] = None
    description: Optional[str] = None

# Task Status Create Schema
class TaskStatusCreate(BaseModel):
    task_id: int
    is_completed: bool
    completed_per: int

# Task Status Response Schema
class TaskStatusResponse(TaskStatusCreate):
    id: int

    class Config:
        orm_mode = True

# Task Status Update Schema (optional for partial updates)
class TaskStatusUpdate(BaseModel):
    is_completed: Optional[bool] = None
    completed_per: Optional[int] = None
