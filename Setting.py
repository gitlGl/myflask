import os,configparser

type_database = 'sqlite3' #sqlite3 'sqlite3' or 'mysql
file_name ="config.ini"

if not  os.path.exists(file_name):
      
    config = configparser.ConfigParser()    #实例化一个对象
    config['mysql'] = {
            'provider':'mysql',
            'host' : '127.0.0.1',
            'port' : '3306',
            'user' : 'user',
            'password' :'123456',
            'db' :'face_recognition',
            'charset' : 'utf8'
                    }
    
    config['sqlite3'] = {
        'provider':'sqlite',
        'filename':'db.db',
        'create_db':True
    }
    
    with open(file_name, "w", encoding="utf-8") as f:
        config.write(f)  
         
def configRead(filePath:str,type_database):
    cfg = configparser.ConfigParser() 
    connect_user = {}
    cfg.read(filePath)
    if type_database == "mysql":
        if "mysql" in cfg.sections():
            connect_user['provider'] = cfg.get('mysql','provider')
            connect_user['host'] = cfg.get('mysql','host')
            connect_user['port'] = cfg.getint('mysql','port')
            connect_user['user'] = cfg.get('mysql','user')
            connect_user['password'] = cfg.get('mysql','password')
            connect_user['db'] = cfg.get('mysql','db')
            connect_user['charset'] = cfg.get('mysql','charset')
        
            return connect_user
        else:
            return None
        
    if type_database == "sqlite3":
        if "sqlite3" in cfg.sections():
            connect_user['provider'] = cfg.get('sqlite3','provider')
            connect_user['filename'] = cfg.get('sqlite3','filename')
            connect_user['create_db'] = cfg.get('sqlite3','create_db')
            
        
            return connect_user
        else:
            return None
            
        
connect_user = configRead(file_name,type_database)
if connect_user is None:
    raise Exception("数据库配置文件错误")
else:
    connect_user = connect_user
        
        
