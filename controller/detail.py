from flask import Blueprint,render_template,request,session,make_response,redirect
from model.detail import Detail
from model.favorite import favorite
from model.ranking import Ranking
from model.reply import reply
from flasgger import swag_from
from app.config.config import config
from app.setting import env
from random import sample

import json

detail = Blueprint('detail',__name__)

@detail.route('/detail')
# @swag_from('/swag/detail.yml')
def detailP():
  # 小說詳情
  book_id = request.args.get('book_id')

  result_detail,result_menu = Detail().find_detail(book_id)

  for k,v in config[env].book_type_map.items():
      if v == result_detail.book_type:
          typeID = k

  result_menu_5 = result_menu[:5]

  # 連載小說
  db_result = Ranking().find_novel_online()

  if len(db_result) > 5:
    result_online = sample(db_result, 5)
  else:
    result_online = db_result

  # 發燒
  result_hot = favorite().all_favorite()
  
  # 收藏
  is_favorite = 0
  if session.get('is_login'):
      nickname = session.get('user_nickname')
      is_favorite = favorite().find_favorite(nickname, book_id)
      if is_favorite:
          is_favorite = is_favorite.checked
      else:
          is_favorite = 0

  # 回覆
  result_reply = reply().find_reply(book_id)
  

  return render_template('detail.html',
                          resultD = result_detail,
                          resultM = result_menu_5,
                          result_hot = result_hot,
                          typeID = typeID,
                          result_online = result_online,
                          is_favorite = is_favorite,
                          result_reply = result_reply)


@detail.route('/favorite/update',methods=['POST'])
# @swag_from('/swag/favorite.yml')
def favoriteP():
  res_data = json.loads(request.data)
  nickname = session.get('user_nickname')

  if nickname is None:
    return make_response({'status': 500})
  else:
    book_id = res_data.get('book_id')
    checked = res_data.get('checked')
    favorite().update_status(nickname, book_id, checked)
    return make_response({'status': 200})


@detail.route('/post/reply',methods=['POST','GET'])
def replyP():
  if not session.get('is_login'):    
    return render_template('login.html')
  else:
    res_data = request.form.to_dict()
    nickname = session.get('user_nickname')

    for key, value in res_data.items():
      book_id = key.split('_')[0]
      floornumber = key.split('_')[1]
      
      if int(floornumber) == 0:
          # 留言
        max_floor = reply().max_floor(book_id)
        if max_floor is None:
          max_floor = 1
        else:
          max_floor += 1
        reply().add_reply(nickname,book_id,max_floor,value)
      else:
        # 回覆
        max_reply = reply().max_sort(book_id, floornumber)
        if max_reply is None:
          max_reply = 1
        else:
          max_reply += 1
        reply().add_pre_reply(nickname,book_id,floornumber,max_reply,value)

    return redirect('/detail?book_id=' + book_id)
  