# 内建模块使用
# datetime，从datetime模块引入datetime类
from datetime import datetime, timedelta

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

# 时间加减
print("加减前时间：", time)
newTime = time - timedelta(days=1)
print("加减后时间：", newTime)

# namedtuple命名元组,collections模块下的类
from collections import namedtuple

# 参数=名称，属性名集合
Name = namedtuple("hahah", ['x', 'y', 'z'])
name = Name(1, 2, 3)
print(name.x)

print(isinstance(name, Name))

# deque双向list,支持头尾快速插入与删除
from collections import deque

dq = deque(['a', 'b', 'c'])
dq.append('d')
print(dq)
dq.appendleft('e')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

# defaultdict 希望索取的key不存在时返回默认值
from collections import defaultdict

dd = defaultdict(lambda: "不存在的")
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# orderedDict key插入有序的dict,仅仅是插入有序，而不是key有序
from collections import OrderedDict

od = OrderedDict()
od['z'] = 1
od['x'] = 2
od['y'] = 3
print(od)
print(list(od.keys()))

# 计数器counter,实际是dict的子类
from collections import Counter

c = Counter()
for ch in "nihao":
    c[ch] = c[ch] + 1
print(c)

# 处理字节
# struct类，处理其他数据类型与bytes的转换
# pack函数将任意数据类型变成bytes
import struct

# I表示四字节无符号整数
pack = struct.pack('>I', 1024)
print(pack)

# unpack函数将bytes变成相应数据类型
unpack = struct.unpack('>I', b'\x00\x00\x04\x00')
print(unpack)

# 摘要算法：通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# 常见MD5，SHA1
# hashlib类
import hashlib

# 计算一个字符串的md5值
md5 = hashlib.md5()
md5.update("hello hello ha ha ha ha".encode('utf-8'))
print(md5.hexdigest())

db = {}


def calc_md5(content):
    # 注意这里如果不重置md5对象，会累加上一次update的结果
    md5 = hashlib.md5()
    md5.update(content.encode('utf-8'))
    return md5.hexdigest()


def register(username, password):
    db[username] = calc_md5(username + password + 'the-salt')


register('liuYang', 'uru123123')
print(db)


def login(username, password):
    md_ = calc_md5(username + password + 'the-salt')
    print(md_)
    if db[username] == md_:
        print("True")
    else:
        print("False")


login('liuYang', 'uru123123')

# itertools类生成指定类型迭代器，无限循环
import itertools

# 参数为指定起始位置
count = itertools.count(0)
for i in count:
    if (i <= 10):
        print(i)
    else:
        break

# cycle循环
# cycle = itertools.cycle('abc')
# for i in cycle:
#     print(i)


# repeat 指定重复次数
repeat = itertools.repeat('nihao', 3)
for i in repeat:
    print(i)

# chain 串联
chain = itertools.chain('abc', 'efg')
for x in chain:
    print(x)

# groupby 将相邻重复元素放在一起,第二个参数可以指定函数对元素修改
groupby = itertools.groupby('AaaBBbcCAAAa', lambda x: x.upper())
for key, group in groupby:
    print(key, list(group))


