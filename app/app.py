from flask import Flask
from flasgger import Swagger
import os

def create_app():
    app = Flask(__name__,
                template_folder='../template', # 前端模板文件夾
                static_url_path= '/', 
                static_folder='../resource' # 靜態文件夾
                ) 
    Swagger(app)

    from  controller.home import homeP
    app.register_blueprint(homeP)  
    from  controller.ranking import rank
    app.register_blueprint(rank) 
    from  controller.header import Nheader
    app.register_blueprint(Nheader) 
    from controller.detail import detail
    app.register_blueprint(detail)   
    from controller.menu import Menu
    app.register_blueprint(Menu)    
    from controller.login import loginP
    app.register_blueprint(loginP)  

    app.config['SECRET_KEY'] = os.urandom(24)  # 設置密鑰，用於session加密

    return app