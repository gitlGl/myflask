from flask import (Flask, render_template, redirect,
                   session, Blueprint,request,make_response)
from api import app as api
from datetime import timedelta

app = Flask(__name__)
# 注册 Blueprint 中定义的视图函数
main_bp = Blueprint('main', __name__)
app.register_blueprint(api)
app.config['SECRET_KEY'] = 'nemo'
app.permanent_session_lifetime = timedelta(seconds=10) # 设置会话过期时间为40s

#版本3
class Check():
    allowed_routes = ['/login', '/register','/api/adduser','/api/login']
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Check, cls).__new__(cls)
        return cls._instance
    
    def check(self,path):
        if path in self.allowed_routes:
            return False
        if path.startswith('/static'):
            return False
        
        return True
"""
版本2
class Check():
    allowed_routes = ['/login', '/register','/api/adduser','/api/login']
  
    def check(self,path):
        if path in self.allowed_routes:
            return False
        if path.startswith('/static'):
            return False
        
        return True
check = Check()

"""                      

"""
版本1
@app.before_request
def require_login():
    path = request.path
    allowed_routes = ['/login', '/register','/api/adduser','/api/login']
    if (not path in self.allowed_routes) and not path.startswith('/static')
        is_login  = session.get("is_login",None)
        if not is_login :
            # 用户未登录，重定向到登录页面
            return render_template('login.html')

"""

        
# 使用before_request钩子来检查用户是否登录，
# 该函数返回None则表示继续执行接下来的请求，但是返回值不能布尔值
@app.before_request
def require_login():
    check = Check()    
    # 定义不需要登录就可以访问的路径
    if check.check(request.path):
        is_login  = session.get("is_login",None)
        if not is_login :
            # 用户未登录，重定向到登录页面
            return render_template('login.html')
    return None

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')
    
  
@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/logout')
def logout():
    # 退出登录，清空session
    session.clear()
    return redirect('/')
   

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/show-cookies')
def show_cookies():
    # 读取所有cookies
    cookies = request.cookies
    cookies_str = '; '.join([f'{key}={value}' for key, value in cookies.items()])
    print(cookies_str)
    return f'Cookies received: {cookies_str}'

@app.route('/set-cookie')
def set_cookie():
    resp = make_response('Cookie is set')
    # 设置cookie到客户端
    resp.set_cookie('test_cookie', 'test_value')
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')