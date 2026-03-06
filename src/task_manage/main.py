from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.task_manage.database import get_db, engine

app = FastAPI(
    title="Week2-用户任务管理API",
    version="0.1.0",
    description="FastAPI+PostgreSQL基础版（极简连接验证）"
)

# 接口1：基础健康检查
@app.get("/")
def root():
    return {
        "msg": "FastAPI服务启动成功！",
        "下一步": "访问 /db/test 测试数据库连接"
    }

# 接口2：极简连接验证（核心！只验证能否获取数据库会话）
@app.get("/db/test")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        # 不执行任何SQL，只验证能否成功获取数据库会话
        # 能走到这一步，说明数据库连接已建立
        return {
            "msg": "数据库连接成功！✅",
            "database": "task_manage",
            "说明": "已成功建立数据库连接（绕开编码查询）",
            "status": "正常"
        }
    except Exception as e:
        # 只返回错误类型，不解析错误字符串（避开编码解码）
        return {
            "msg": "数据库连接失败！❌",
            "error_type": str(type(e)),
            "排查方向": "1.PostgreSQL服务是否启动 2.密码是否正确 3.库名是否存在"
        }