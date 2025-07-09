from flask import Blueprint,render_template

# from model.home import home

homeP = Blueprint('home', __name__)

@homeP.route('/')
def home():
    
    return render_template('home.html')