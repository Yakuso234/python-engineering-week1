"""任务管理API测试（SQLite嵌入式数据库）"""
import os
import tempfile

import pytest

# 使用mkstemp安全创建临时SQLite数据库文件
_fd, _TEST_DB = tempfile.mkstemp(suffix=".db")
os.close(_fd)  # 关闭文件描述符，让SQLite管理该文件
os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB}"

from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy.orm import sessionmaker  # noqa: E402

from src.task_manage.database import Base, engine, get_db  # noqa: E402
from src.task_manage.main import app  # noqa: E402

TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# 测试1：根路由返回成功消息
def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "msg" in resp.json()


# 测试2：初始任务列表为空
def test_list_tasks_empty(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json() == []


# 测试3：创建任务成功
def test_create_task(client):
    resp = client.post("/tasks", json={"title": "学习FastAPI", "description": "看文档"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "学习FastAPI"
    assert data["completed"] is False
    assert "id" in data


# 测试4：获取单个任务
def test_get_task(client):
    created = client.post("/tasks", json={"title": "测试任务"}).json()
    resp = client.get(f"/tasks/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "测试任务"


# 测试5：获取不存在任务返回404
def test_get_task_not_found(client):
    resp = client.get("/tasks/9999")
    assert resp.status_code == 404


# 测试6：更新任务标题和完成状态
def test_update_task(client):
    created = client.post("/tasks", json={"title": "旧标题"}).json()
    resp = client.put(
        f"/tasks/{created['id']}",
        json={"title": "新标题", "completed": True}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "新标题"
    assert data["completed"] is True


# 测试7：更新不存在任务返回404
def test_update_task_not_found(client):
    resp = client.put("/tasks/9999", json={"title": "无效"})
    assert resp.status_code == 404


# 测试8：删除任务成功
def test_delete_task(client):
    created = client.post("/tasks", json={"title": "待删任务"}).json()
    resp = client.delete(f"/tasks/{created['id']}")
    assert resp.status_code == 204
    # 确认已删除
    assert client.get(f"/tasks/{created['id']}").status_code == 404


# 测试9：删除不存在任务返回404
def test_delete_task_not_found(client):
    resp = client.delete("/tasks/9999")
    assert resp.status_code == 404


# 测试10：创建多个任务后列表数量正确
def test_list_tasks_multiple(client):
    client.post("/tasks", json={"title": "任务A"})
    client.post("/tasks", json={"title": "任务B"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.json()) == 2
