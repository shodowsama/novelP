from common.database import db_conncect
from sqlalchemy import Table

engine, dbsession, base = db_conncect()

class User(base):
    __table__ = Table('novels', base.metadata, autoload_with=engine)

    def get_one(self):
        """
        獲取一個用戶
        :return: User object
        """
        return dbsession.query(User).first()