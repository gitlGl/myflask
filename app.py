from flask import Flask, render_template, redirect, session, Blueprint
from api import app as api
from datetime import timedelta

app = Flask(__name__)
# 注册 Blueprint 中定义的视图函数
main_bp = Blueprint('main', __name__)
app.register_blueprint(api)
app.config['SECRET_KEY'] = 'nemo'
app.permanent_session_lifetime = timedelta(seconds=40) # 设置会话过期时间为40s


@app.route('/')
@app.route('/index')
def index():
    if 'is_login' in session and session['is_login']:
        return render_template('index.html')
    
    return redirect('/login') 


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')