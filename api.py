
from flask import request, session, flash, jsonify,abort,Blueprint
import sqlite3 
from function import *

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
            # sqlite3支持?占位符，通过绑定变量的查询方式杜绝sql注入
            sql = 'SELECT 1 FROM USER WHERE USERNAME=? AND PASSWORD=?'
            is_valid_user = cur.execute(sql, (username, password)).fetchone()

            # 拼接方式，存在sql注入风险, SQL注入语句：在用户名位置填入 1 or 1=1 --
            # sql = 'SELECT 1 FROM USER WHERE USERNAME=%s AND PASSWORD=%s' % (username, password)
            # print(sql)
            # is_valid_user = cur.execute(sql).fetchone()
        except:
            flash('用户名或密码错误！')
            return jsonify({'code': '400', 'msg': '用户名或密码错误！'}), 400
        finally:
            conn.close()

        if is_valid_user:
            # 登录成功后存储session信息
            session['is_login'] = True
            session['name'] = username
            return jsonify({'code': '200', 'msg': '登录成功！', 'newUser': username})
        else:
            flash('用户名或密码错误！')
            return jsonify({'code': '400', 'msg': '用户名或密码错误！'}), 400
        
        

@app.route('/api/adduser', methods=['GET', 'POST'])
def add_user():
    if request.json:
        username = request.json.get('username', '').strip()
        print(username)
        password = request.json.get('password')
        confirm_password = request.json.get('confirm')
        # 判断所有输入都不为空
        if username and password and confirm_password:
            if password != confirm_password:
                return jsonify({'code': '400', 'msg': '两次密码不匹配！'}), 400
            # 连接数据  库
            conn = sqlite3.connect('db.db')
            cur = conn.cursor()
            # 查询输入的用户名是否已经存在
            sql_same_user = 'SELECT 1 FROM USER WHERE USERNAME=?'
            same_user = cur.execute(sql_same_user, (username,)).fetchone()
            if same_user:
                return jsonify({'code': '400', 'msg': '用户名已存在'}), 400
            # 通过检查的数据，插入数据库表中
            sql_insert_user = 'INSERT INTO USER(USERNAME, PASSWORD) VALUES (?,?)'
            cur.execute(sql_insert_user, (username, hash_code(password)))
            conn.commit()
            sql_new_user = 'SELECT id,username FROM USER WHERE USERNAME=?'
            user_id, user = cur.execute(sql_new_user, (username,)).fetchone()
            conn.close()
            return jsonify({'code': '200', 'msg': '账号生成成功！', 'newUser': {'id': user_id, 'user': user}})
        else:

            return jsonify({'code': '404', 'msg': '请求参数不全!'})
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
