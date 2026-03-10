from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.task_manage.database import Base, engine, get_db
from src.task_manage.models import Task

# 启动时自动建表（嵌入式SQLite无需手动建库）
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="任务管理API",
    version="0.2.0",
    description="FastAPI + 嵌入式SQLite任务管理系统"
)


# ---------- Pydantic 请求/响应模型 ----------

class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    model_config = {"from_attributes": True}


# ---------- 接口 ----------

@app.get("/")
def root():
    return {"msg": "任务管理API启动成功！", "docs": "/docs"}


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    """获取所有任务"""
    return db.query(Task).all()


@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    """创建新任务"""
    task = Task(title=task_in.title, description=task_in.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """获取单个任务"""
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db)):
    """更新任务"""
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    for field, value in task_in.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """删除任务"""
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    db.delete(task)
    db.commit()