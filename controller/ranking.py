from flask import Blueprint, render_template,request,session
from model.ranking import Ranking
from model.favorite import favorite
from app.config.config import config
from app.setting import env
import logging
from flasgger import swag_from

rank = Blueprint('ranking', __name__)

@rank.route('/ranking')
@swag_from('../swag/ranking.yml')
def ranking():
    page = request.args.get('page')

    # 取得參數(url)
    # 連載/完本
    ranking_status = request.args.get('ranking_status')
    # 推薦/新書
    # ranking_info = request.args.get('ranking_info')
    # 玄幻/魔法
    ranking_type = request.args.get('ranking_type')

    # # 日誌
    logging.debug('page:' + str(page))
    logging.debug('ranking_status:' + str(ranking_status))
    # logging.debug('ranking_info:' + ranking_info)
    logging.debug('ranking_type:' + str(ranking_type))

    if page is None or int(page) < 1:
        page = 1
    if ranking_type is None:
        ranking_type = 1
    # if ranking_info is None:
    #     ranking_info = 'hot'
    if ranking_status is None:
        ranking_status = 1

    # 查詢數據
    db_result = Ranking().find_novels(page, ranking_status ,ranking_type)

    return render_template('ranking.html',
                           book_status_map = config[env].book_status_map,
                           book_type_map = config[env].book_type_map,  
                           result = db_result,
                           reply_type = ranking_type,
                           reply_status=ranking_status,
                           page = page)



@rank.route('/bookshelf')
# @swag_from('../swag/bookshelf.yml')
def bookshelf():
    if not session.get('is_login'):    
        return render_template('login.html')
    else:
        nickname = session.get('user_nickname')
        db_results = []
        db_result = favorite().find_favorite_by_nickname(nickname)
        if not db_result:
            db_result = [] 
        else:
            for i_data in db_result:
                db_results.append(i_data[1])

        return render_template('search.html',
                           result = db_results,
                           keyward = nickname)