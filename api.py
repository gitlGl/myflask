
from flask import request, session, jsonify,abort,Blueprint
import sqlite3 
from function import *
from database import database,PH
app = Blueprint('main', __name__)

@app.route('/api/login', methods=['GET', 'POST'])
def api_login():
   print("test2")
   if request.method == 'POST':
        # 获取请求中的数据
        username = request.json.get('username')
        password = hash_code(request.json.get('password'))
       

        # 连接数据库，判断用户名+密码组合是否匹配
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        try:
            # sqlite3支持PH占位符，通过绑定变量的查询方式杜绝sql注入
            sql = f'SELECT 1 FROM USER WHERE USERNAME={PH} AND PASSWORD={PH}'
            
            database.c.execute(sql, (username, password))
            is_valid_user = database.c.fetchone()

            
        except Exception as e:
            print(e)
           
            return jsonify({'code': '400', 'msg': '用户名或密码错误！'}), 400
        
        finally:
            conn.close()

        if is_valid_user:
            # 登录成功后存储session信息
            #用户登录相关的session与cookies由flask框架维护
            session.permanent = True  # 将会话设置为持久性会话
            session['is_login'] = True
            session['name'] = username
            return jsonify({'code': 'ok', 'msg': '登录成功！', 'newUser': username})
        
        else:
           
            return jsonify({'code': 'error', 'msg': '用户名或密码错误！'})
        
        
@app.route('/api/adduser', methods=['GET', 'POST'])
def add_user():
    if request.json:
        username = request.json.get('username', '').strip()
        print(username)
        password = request.json.get('password')
        confirm_password = request.json.get('confirm')
       
        
        # 查询输入的用户名是否已经存在
        sql_same_user = f'SELECT 1 FROM USER WHERE USERNAME={PH}'
        database.c.execute(sql_same_user, (username,))
        same_user = database.c.fetchone()
        if same_user:
            return jsonify({'code': '400', 'msg': '用户名已存在'}), 400
        
        # 通过检查的数据，插入数据库表中
        sql_insert_user = f'INSERT INTO USER(USERNAME, PASSWORD) VALUES ({PH},{PH})'
        database.c.execute(sql_insert_user, (username, hash_code(password)))
        
        sql_new_user = f'SELECT id,username FROM USER WHERE USERNAME={PH}'
        database.c.execute(sql_new_user, (username,))
        user_id, user = database.c.fetchone()
        
        return jsonify({'code': 'ok', 'msg': '账号生成成功！', 'newUser': {'id': user_id, 'user': user}})
       
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
