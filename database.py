from Setting import type_database,connect_user

if type_database == 'sqlite3':
    print('sqlite3 loaded')
    import sqlite3
    PH = '?'
    Auto = 'AUTOINCREMENT'
   
elif type_database == 'mysql':
    print('mysql  loaded')
    import pymysql
    PH = '%s'
    Auto = 'AUTO_INCREMENT'
  
#######


class Database():
    def __init__(self):
        def dictFactory(cursor, row):#重定义row_factory函数查询返回数据类型是字典形式
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        if type_database == 'sqlite3':
            sqlite3.enable_callback_tracebacks(True)
            self.conn = sqlite3.connect(connect_user, isolation_level = None,
                                        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,check_same_thread=False)
            self.conn.row_factory = dictFactory
            self.c = self.conn.cursor()
            
        elif type_database == 'mysql':
            self.conn = pymysql.connect(**connect_user,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.conn.autocommit(True)
            self.c = self.conn.cursor()

        
    def creatble(self):#528 李回复 2018035144217
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS user
       ( id INTEGER PRIMARY KEY {Auto},
        username       CHAR(50)    NOT NULL,
        password        CHAR(50)    NOT NULL
                 );''')
        
    def __del__(self):
        self.conn.close()
        
database = Database()

database.creatble()
