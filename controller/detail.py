from flask import Blueprint,render_template,request
from model.detail import Detail
from flasgger import swag_from
from app.config.config import config
from app.setting import env

detail = Blueprint('detail',__name__)

@detail.route('/detail')
# @swag_from('/swag/detail.yml')
def detailP():

  book_id = request.args.get('book_id')

  result_detail,result_menu = Detail().find_detail(book_id)

  for k,v in config[env].book_type_map.items():
      if v == result_detail.book_type:
          typeID = k

  result_menu_5 = result_menu[:5]

  return render_template('detail.html',
                          resultD = result_detail,
                          resultM = result_menu_5,
                          typeID = typeID)