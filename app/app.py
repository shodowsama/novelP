from flask import Flask

def create_app():
    app = Flask(__name__,
                template_folder='../template', # 前端模板文件夾
                static_url_path= '/', 
                static_folder='../resource' # 靜態文件夾
                )

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


    return app