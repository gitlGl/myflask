from flask import Flask, render_template, redirect, session, Blueprint
from api import app as api
from datetime import timedelta
app = Flask(__name__)
# 注册 Blueprint 中定义的视图函数
main_bp = Blueprint('main', __name__)
app.register_blueprint(api)
app.config['SECRET_KEY'] = 'nemo'
app.permanent_session_lifetime = timedelta(minutes=30)  # 设置会话过期时间为30分钟



@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/logout')
def logout():
    # 退出登录，清空session
    session.pop('username', None)
    return redirect('/')
   

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')