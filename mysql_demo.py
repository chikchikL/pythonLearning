# 导入mysql驱动
import mysql.connector

# 连接
conn = mysql.connector.connect(user='root', password='password',database='testdb')
cursor = conn.cursor()
# 建表
cursor.execute('create table if not exists user (id varchar(20) primary key,'
               'name varchar(20))')
# 插入记录,sqlite占位符为？，mysql占位符为%s
for i in range(5):
    cursor.execute('insert into user (id,name) values (%s,%s)', [str(i), 'someone' + str(i)])
print(cursor.rowcount)

# 增删改查之后需要提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
