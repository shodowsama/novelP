from common.database import db_conncect
from sqlalchemy import Table

from model.ranking import Ranking

engine, dbsession, base = db_conncect()

class Detail(base):
    __table__ = Table('novelscontent',base.metadata, autoload_with=engine)

    def find_detail(self,book_id):

        novel_detail = dbsession.query(Ranking).filter(
            Ranking.book_id == book_id 
        ).first()

        novel_menu = dbsession.query(Detail).filter(
            Detail.book_id == book_id 
        ).all()

        return novel_detail,novel_menu


    def find_menu(self,book_id):
        novel_menu = dbsession.query(Detail).filter(
            Detail.book_id == book_id 
        ).all()

        return novel_menu
