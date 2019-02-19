# 内建模块使用
# datetime，从datetime模块引入datetime类
from datetime import datetime
# 当前时间

print(datetime.now())
# 构造指定日期时间
time = datetime(2019, 2, 19, 17, 58)
print(time)

# timestamp = 1970至今的秒数float类型，与java和js不同
# 将datetime转化为timestamp类型
timestamp = time.timestamp()
print("时间戳秒数", timestamp)

# 将timestamp类型转化为datetime
fromtimestamp = datetime.fromtimestamp(timestamp)
print(fromtimestamp)

# str转化为datetime
strptime = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(strptime)

# datetime转化为str
strftime = time.strftime('%a, %b %d %H:%M')
print(strftime)