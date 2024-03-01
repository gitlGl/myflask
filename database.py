from Setting import connect_user
from pony.orm import Database,PrimaryKey,Required

db = Database()
db.bind(**connect_user)

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str,unique=True)
    password = Required(str, max_len=50)
# 生成数据表结构
db.generate_mapping(create_tables=True)

