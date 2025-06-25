from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session,declarative_base
from app.config.config import config
from app.setting import env

def db_conncect():
    # 創建連接數據庫引擎，echo=True表示打印所有SQL語句
    engine = create_engine(config[env].db_url,echo=True)
    # 實例化會話配置(在一次請求時被創建一個綁定引擎的session)
    session = sessionmaker(engine)
    # 使用scoped_session來管理會話(可以避免session衝突)
    dbsession = scoped_session(session)
    # 創建基類
    base = declarative_base()

    return engine,dbsession, base