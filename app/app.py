from flask import Flask

def create_app():
    app = Flask(__name__,
                template_folder='../template', # 前端模板文件夾
                static_url_path= '/', 
                static_folder='../resource' # 靜態文件夾
                )

    from  controller.user import user
    app.register_blueprint(user)  


    return app