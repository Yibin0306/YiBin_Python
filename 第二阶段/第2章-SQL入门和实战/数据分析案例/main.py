from file_define import *
from data_define import *
from pymysql import Connection

text_file_reader = TextFileReader("D:/Download/可视化案例数据/面向对象案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/Download/可视化案例数据/面向对象案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.data_read()
feb_data: list[Record] = json_file_reader.data_read()

# 将两个月份的数据合并为一个list存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL的链接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='202306',
    autocommit=True #设置自动提交
)
# 获取到游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('01-sql入门和实训')
# 执行sql
for record in all_data:
    sql = f"insert into orders(order_data,order_id,money,province)" \
          f" values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)
# 关闭数据库的链接
conn.close()