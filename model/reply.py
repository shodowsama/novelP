from common.database import db_conncect
from sqlalchemy import Table, func
from app.config.config import config
from app.setting import env

engine, dbsession, base = db_conncect()

class reply(base):
    __table__ = Table('reply', base.metadata, autoload_with=engine)

    # 查詢所有文章
    def find_reply(self,book_id):
        feedback_list = []
        feedbacks = self.find_reply_per(book_id).all()
        for f in feedbacks:
            feedback = self.find_re_reply_per(book_id=f.book_id, 
                                              replay_floor=f.floor_number).all()
            feedback_list.append({'floor':f,'floor_reply':feedback})
        return feedback_list


    def find_reply_per(self,book_id):
        return dbsession.query(reply).filter_by(
            book_id=book_id,
            replay_floor=0
        ).order_by(
            reply.floor_number.desc()
        )
    
    def find_re_reply_per(self,book_id, replay_floor):
        return dbsession.query(reply).filter_by(
            book_id=book_id,
            replay_floor=replay_floor
        ).order_by(
            reply.replay_sort.asc()
        )

    def add_reply(self, nickname, book_id, max_floor, content):
        new_reply = reply(
            username=nickname,
            book_id=book_id,
            floor_number=max_floor,
            replay_floor=0,
            replay_sort=0,
            content=content
        )
        dbsession.add(new_reply)
        dbsession.commit()
        return new_reply   
    
    def max_floor(self, book_id):
        return dbsession.query(func.max(reply.floor_number).label(
            'max_floor'
            )).filter_by(
            book_id=book_id
        ).one().max_floor
    
    def add_pre_reply(self, nickname, book_id,reply_floor , max_reply, content):
        new_reply = reply(
            username=nickname,
            book_id=book_id,
            floor_number=0,
            replay_floor=reply_floor,
            replay_sort=max_reply,
            content=content
        )
        dbsession.add(new_reply)
        dbsession.commit()
        return new_reply   
    
    def max_sort(self, book_id,reply_floor):
        return dbsession.query(func.max(reply.replay_sort).label(
            'max_replay'
            )).filter_by(
            book_id=book_id,
            replay_floor=reply_floor
        ).one().max_replay