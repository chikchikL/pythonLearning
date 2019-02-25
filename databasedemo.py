# 数据库
# python内置SQLite数据库
import sqlite3

# 连接到数据库,如果没有自动创建
# conn = sqlite3.connect('test.db')
# 创建cursor，cursor是对表操作的媒介
# cursor = conn.cursor()
# 创建user表
# cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# 创建一条user记录
# cursor.execute('insert into user (id,name) values (\'1\',\'michael\')')
# rowcount返代表影响的行数
# print(cursor.rowcount)

# 查询
# cursor.execute('select * from user where id=?', '1')
# 获取所有查询结果，是一个list，其中每条记录对应一个tuple
# values = cursor.fetchall()
# print(values)
# 关闭cursor，提交事务，关闭conn
# cursor.close()
# conn.commit()
# conn.close()


# 分数段练习
import os


# 初始数据
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table if not exists user2(id varchar(20) primary key, name varchar(20), score int)')
# cursor.execute(r"insert into user2 values ('A-001', 'Adam', 95)")
# cursor.execute(r"insert into user2 values ('A-002', 'Bart', 62)")
# cursor.execute(r"insert into user2 values ('A-003', 'Lisa', 78)")
# cursor.close()
# conn.commit()
# conn.close()

# 返回指定分数区间的名字，按分数从低到高排序
def get_score_in(low, high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name from user2 where score between ? and ? order by score', [low, high])
    values = []
    for x in cursor.fetchall():
        values.append(x[0])
    print(values)
    return values


assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Pass')
