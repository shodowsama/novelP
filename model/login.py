from common.database import db_conncect
from sqlalchemy import Table,or_
from app.config.config import config
from app.setting import env

engine, dbsession, base = db_conncect()

class login_user(base):
    __table__ = Table('users',base.metadata, autoload_with=engine)

    def find_email(self,email):
        return dbsession.query(login_user).filter_by(useremail = email).all()    

    def find_nickname(self,nickname):
        return dbsession.query(login_user).filter_by(username = nickname).all()    
    
    def register_user(self,nickname,email,psd):
        new_user = login_user(
            username = nickname,
            useremail = email,
            userpsd = psd
        )
        dbsession.add(new_user)
        dbsession.commit()
        return new_user
