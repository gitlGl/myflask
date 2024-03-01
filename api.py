
from flask import request, session, jsonify,abort,Blueprint
from function import *
from database import  User
from pony.orm import  db_session
app = Blueprint('main', __name__)

@app.route('/api/login', methods=['GET', 'POST'])
@db_session
def api_login():
   if request.method == 'POST':
        # 获取请求中的数据
        username = request.json.get('username')
        password = hash_code(request.json.get('password'))
       
        try:
            with db_session:
                user = User.get(username=username)
            if user and user.password == password:
                # 登录成功后存储session信息
                #用户登录相关的session与cookies由flask框架维护
                session.permanent = True  # 将会话设置为持久性会话
                
                #写session触发会话创建，并返回新cookies给客户端
                session['is_login'] = True
                session['name'] = username
                return jsonify({'code': 'ok', 'msg': '登录成功！', 'newUser': username})
            else:
               
                return jsonify({'code': 'error', 'msg': '用户名或密码错误！'})     
            
        except Exception as e:
            print(e)
           
     
@app.route('/api/adduser', methods=['GET', 'POST'])
@db_session
def add_user():
    if request.json:
        username = request.json.get('username', '').strip()
        print(username)
        password = request.json.get('password')
        confirm_password = request.json.get('confirm')
       
        user = User.get(username=username)
        
        if user :
            return jsonify({'code': '400', 'msg': '用户名已存在'}), 400
        
        User(username=username, password=hash_code(password))
        
        return jsonify({'code': 'ok', 'msg': '账号生成成功！',  'user':  username})
       
    else:
        abort(400)
        
        
@app.route("/radarChart")
def get_radar_charts():
    c = radar_base()
    return c.dump_options_with_quotes()


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()
