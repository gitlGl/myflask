import os,configparser

type_database = 'sqlite3' #sqlite3 'sqlite3' or 'mysql
file_name ="config.ini"

if not  os.path.exists(file_name):
      
    config = configparser.ConfigParser()    #实例化一个对象
    config['sql'] = {
            'host' : '127.0.0.1',
            'port' : '3306',
            'user' : 'user',
            'password' :'123456',
            'db_name' :'face_recognition',
            'charset' : 'utf8'
                    }
  
    with open(file_name, "w", encoding="utf-8") as f:
        config.write(f)  
         
def configRead(filePath:str):
    cfg = configparser.ConfigParser() 
    connect_user = {}
    cfg.read(filePath)
    if "sql" in cfg.sections():
        connect_user['host'] = cfg.get('sql','host')
        connect_user['port'] = cfg.getint('sql','port')
        connect_user['user'] = cfg.get('sql','user')
        connect_user['password'] = cfg.get('sql','password')
        connect_user['db'] = cfg.get('sql','db_name')
        connect_user['charset'] = cfg.get('sql','charset')
       
        return connect_user
    else:
        return None

if type_database == 'sqlite3':
    connect_user = "db.db"
else:
    connect_user = configRead(file_name)
    if connect_user is None:
        raise Exception("数据库配置文件错误")
    else:
        connect_user = connect_user
        
        
