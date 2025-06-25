from flask import Blueprint

from model.user import User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_one_user():
    user = User()
    print( user.get_one())
    return 'ok'