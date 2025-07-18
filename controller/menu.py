from flask import Blueprint,render_template,request
from model.detail import Detail
from flasgger import swag_from

Menu = Blueprint('menu',__name__)

@Menu.route('/menu')
@swag_from('../swag/menu.yml')
def MenuP():
    book_id = request.args.get('book_id')
    
    result_menu = Detail().find_menu(book_id)

    return render_template('menu.html',
                        resultM = result_menu)