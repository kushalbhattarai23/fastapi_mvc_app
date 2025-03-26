from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    time_to_complete = Column(Integer)
    description = Column(String)

    status = relationship("TaskStatus", back_populates="task", uselist=False)

class TaskStatus(Base):
    __tablename__ = "task_status"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    is_completed = Column(Boolean, default=False)
    completed_per = Column(Integer, default=0)

    task = relationship("TaskModel", back_populates="status")
