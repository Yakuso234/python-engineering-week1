from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 关键：添加?client_encoding=utf8，强制UTF-8编码连接
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1979810@localhost:5432/task_manage?client_encoding=utf8"

# 创建引擎时，再显式指定编码（兜底）
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"options": "-c client_encoding=utf8"}  # 强制客户端编码
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()