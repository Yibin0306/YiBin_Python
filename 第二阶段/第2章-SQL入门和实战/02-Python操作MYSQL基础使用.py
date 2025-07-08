"""
安装第三方库：pip install pymysql
"""
from pymysql import Connection

# 获取到MySql数据库的链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='202306',
)

# 打印MySql数据库软件信息
print(conn.get_server_info())

# 执行非查询性质Sql
# cursor = conn.cursor() # 获取到游标对象
# conn.select_db('01-sql入门和实训') # 选择数据库
# cursor.execute('create table test(id int)')

# 执行查询性质Sql
cursor = conn.cursor() # 获取到游标对象
conn.select_db('world') # 选择数据库
cursor.execute('select * from city')
# 获得查询结果
result:tuple = cursor.fetchall()
for row in result:
    print(row)

# 关闭数据库的链接
conn.close()