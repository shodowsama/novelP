from common.database import db_conncect
from sqlalchemy import Table,or_
from app.config.config import config
from app.setting import env

engine, dbsession, base = db_conncect()

class Header(base):
    __table__ = Table('novels',base.metadata, autoload_with=engine)

    def key_search(self,keyward):
        result = dbsession.query(Header).filter(
            or_(Header.book_name.like('%'+keyward+'%'),
            Header.book_autor.like('%'+keyward+'%'))                
        ).order_by(
            Header.id.desc()
        ).limit(30).all()

        return result