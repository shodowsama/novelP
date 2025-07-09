from flask import Blueprint,render_template,request,redirect,url_for
from model.header import Header

Nheader = Blueprint('header',__name__)

@Nheader.route('/header')
def search():
    keyward = request.args.get('search_key')

    if keyward == '':
        db_result = {}
    elif keyward is not None:
        db_result = Header().key_search(keyward)
    else:
        db_result = {}

    return render_template('search.html',
                           result = db_result,
                           keyward = keyward)