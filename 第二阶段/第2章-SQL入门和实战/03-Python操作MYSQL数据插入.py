from pymysql import Connection

# 获取到MySql数据库的链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='202306',
    autocommit=True #设置自动提交
)

# 执行查询性质Sql
cursor = conn.cursor() # 获取到游标对象
conn.select_db('01-sql入门和实训') # 选择数据库

# 执行sql
cursor.execute('insert into test values (1)')

# 通过commit确定
conn.commit()

# 关闭数据库的链接
conn.close()