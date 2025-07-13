from flask import Blueprint,render_template
from flasgger import swag_from

# from model.home import home

homeP = Blueprint('home', __name__)

@homeP.route('/')
@swag_from('../swag/home.yml')
def home():
    
    return render_template('home.html')