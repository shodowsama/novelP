from common.database import db_conncect
from sqlalchemy import Table
from app.config.config import config
from app.setting import env

import logging

engine, dbsession, base = db_conncect()

class Ranking(base):
    __table__ = Table('novels', base.metadata, autoload_with=engine)

    # 查詢所有文章
    def find_novels(self,page,ranking_status=1,ranking_type=1):

        count = int(page) * config[env].page_count
        per_count = (int(page)-1) * config[env].page_count

        try:
            type_name = config[env].book_type_map[str(ranking_type)]
        except:
            ranking_type = 1
            type_name = config[env].book_type_map[str(ranking_type)]

        try:
            status_name = config[env].book_status_map[str(ranking_status)]
        except:
            ranking_status = 1
            status_name = config[env].book_status_map[str(ranking_status)]
            

        if (int(ranking_type) != 1) & (int(ranking_status) != 1) :
            result = dbsession.query(Ranking).filter(
                Ranking.book_type == type_name,
                Ranking.book_status == status_name,                
            ).order_by(
                Ranking.id.desc()
            ).offset(per_count).limit(config[env].page_count).all()

        elif int(ranking_status) != 1:
            result = dbsession.query(Ranking).filter(
                Ranking.book_status == status_name,                
            ).order_by(
                Ranking.id.desc()
            ).offset(per_count).limit(config[env].page_count).all()   

        elif int(ranking_type) != 1:
            result = dbsession.query(Ranking).filter(
                Ranking.book_type == type_name,               
            ).order_by(
                Ranking.id.desc()
            ).offset(per_count).limit(config[env].page_count).all()  

        else:
            result = dbsession.query(Ranking).order_by(
                Ranking.id.desc()
            ).offset(per_count).limit(config[env].page_count).all()    

        return result
    
    def find_novel_online(self):
        result = dbsession.query(Ranking).filter(
            Ranking.book_status == '连载',
        ).order_by(
            Ranking.id.desc()
        ).all()

        return result
