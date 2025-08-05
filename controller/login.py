from flask import Blueprint,render_template, make_response, session
from flask import request
from flasgger import swag_from
from model.login import login_user
from common.utils import imagecode
import json
import hashlib

loginP = Blueprint('login', __name__)

@loginP.route('/vcode')
@swag_from('../swag/vcode.yml')
def vcode():
    image ,code = imagecode().get_image_code()
    response = make_response(image)
    # 設置響應頭
    response.headers['Content-Type'] = 'image/png'
    # 存儲內存
    session['verify_code'] = code
    return response



@loginP.route('/login',methods=['GET','POST'])
@swag_from('../swag/login.yml')
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        # 註冊
        if request.form.get('nickname') :
            username = request.form.get('nickname')
            email = request.form.get('email-input')
            psd = request.form.get('password-input')
            verify = request.form.get('verify-input')

            if verify != session.get('verify_code'):
                return render_template('login.html', message_error='驗證碼錯誤')              
            password = hashlib.md5(psd.encode()).hexdigest()
            user = login_user()

            if user.find_email(email):
                return render_template('login.html', message_error='信箱已存在')

            if user.find_nickname(username):
                return render_template('login.html', message_error='暱稱已存在')   

            user.register_user(username, email, password)

            session['is_login'] = True
            session['user_nickname'] = username

            res = make_response(render_template('home.html'))
            res.set_cookie('user_nickname', str(username), max_age=3600*24*7) 
            return res

        
        # 登入
        elif request.form.get('email-input-login'):
            email = request.form.get('email-input-login')
            psd = request.form.get('password-input-login')
            verify = request.form.get('verify-input-login')

            if verify != session.get('verify_code'):
                return render_template('login.html', message_error='驗證碼錯誤')   
            password = hashlib.md5(psd.encode()).hexdigest()
            user = login_user()

            user_info = user.find_email(email)
            if user_info:
                if user_info[0].userpsd == password:
                    session['is_login'] = True
                    session['user_nickname'] = user_info[0].username

                    res = make_response(render_template('home.html'))
                    res.set_cookie('user_nickname', str(user_info[0].username), max_age=3600*24*7) 
                    return res
                else:
                    return render_template('login.html', message_error='密碼錯誤')            
            else:
                return render_template('login.html', message_error='信箱不存在')
        else:
            return render_template('login.html')

@loginP.route('/logout')
@swag_from('../swag/logout.yml')
def logout():
    session.clear()
    res = make_response(render_template('home.html'))
    res.delete_cookie('user_nickname')
    return res