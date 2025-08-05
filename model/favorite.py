from common.database import db_conncect
from sqlalchemy import Table,or_
from model.ranking import Ranking
from app.config.config import config
from app.setting import env

engine, dbsession, base = db_conncect()

class favorite(base):
    __table__ = Table('favorite',base.metadata, autoload_with=engine)

    def update_status(self,nickname,book_id,checked=1):
        fdata = dbsession.query(favorite).filter_by(
            username = nickname,
            book_id = book_id
        ).first()
        if fdata:
            fdata.checked = checked
        else:
            new_favorite = favorite(
                username = nickname,
                book_id = book_id,
                checked = checked
            )
            dbsession.add(new_favorite)
        dbsession.commit()

    def find_favorite(self,nickname,book_id):
        return dbsession.query(favorite).filter_by(
            username = nickname,
            book_id = book_id
        ).first()
    
    def all_favorite(self):
        return dbsession.query(favorite,Ranking.book_name).join(
            Ranking,Ranking.book_id == favorite.book_id
        ).order_by(
            favorite.fid.desc()
        ).limit(5).all()
    
    def find_favorite_by_nickname(self,nickname):
        return dbsession.query(favorite,Ranking).join(
            Ranking,Ranking.book_id == favorite.book_id
        ).filter(
            favorite.username == nickname,
            favorite.checked == 1
        ).order_by(
            favorite.fid.desc()
        ).all()
    