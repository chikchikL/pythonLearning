# input()返回的数据类型是 str name = input('输入名字')
# print("hello,world", 'gg', name)
print("1024 * 768= ", 1024*768)

# Python 程序是大小写敏感的
# 1.23x109就是 1.23e9 0.000012 可以写成 1.2e-5

# 如果'本身也是一个字符，那就可以用""括起来 比如"I'm OK"
# 既包含'又包含"怎么办？可以用转义字符\来标识 'I\'m \"OK\"!' 表示I'm "OK
print("\"\\")
# r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# True、False 可以用and、or 和 not 运算
# 空值None

# 变量为英文_数字组合，可以重复赋值本身类型不固定的语言称之为动态语言

# 变量赋值，实际是指向了内存中的数据
a = 'ABC'
b = a
a = 'XYZ'
print(a, b) # XYZ ABC

# 全部大写的变量名表示常量
# /浮点除法 //整除 %取余数
# Python 的整数没有大小限制
# Python 的浮点数也没有大小限制，但是超出一定范围就直接表示为 inf（无限大）。



# 字符编码
# Unicode编码=两个字节表示一个字符 ASCII 编码是 1 个字节
# 如果把 ASCII 编码的 A 用 Unicode 编码，只需要在前面补0 就可以
# 在计算机内存中，统一使用 Unicode 编码，当需要保存到硬盘或者需要，传输的时候，就转换为 UTF-8 编码
# Python 3 版本中，字符串是以 Unicode 编码的


# ord()函数获取字符的整数表示
print(ord('A')) #65
# chr()函数把编码转换为对应的字符
print(chr(65)) #A

# 如果要在网络上传输，或者保存到磁盘上，就需要把str 前加上b变为以字节为单位的 bytes
x = 'ABC'

# 编码为指定的 bytes,纯英文的 str 可以用 ASCII 编码为 bytes，内容是一样的，含有中文的 str
# 可以用 UTF-8 编码为 bytes
# \x表16进制 \u表unicode编码
y = x.encode('ascii')
z = '中文需要用utf-8编码'.encode('utf-8')
print(y) #b'ABC'
print(z)


print(len(x))

# 格式化符号%
# %d 整数
print('%03d个人' % 5) # 3表示数字前有几个空格，0表示空格补0
# %f 浮点数
print('%.2f' % 3.1415) #.2表示保留两位有效数字
# %s 字符串 永远起作用，它会把任何数据类型转换为字符串
print('Age:%s name:%s' % (25, True))
# %x 十六进制

#练习
s1 = 72
s2 = 85
r = (85-72)/72
print('%.1f' % r + '%')



# list和tuple
chars = ['a', 'b', 'c']
# 可以用-1 做索引，直接获取最后一个元素
# 可变的有序表
chars.append('d')
chars.insert(1, 'e')
# 删除末尾一个元素
chars.pop()
# 删除指定位置元素
chars.pop(2)
# 替换=直接赋值
chars[2] = 'b'
# 元素的数据类型也可以不同,多维list，空list
L = []
len(L)

# tuple 初始化就不能修改
students = ('Michael', 'Bob', 'Tracy')
# 定义一个只有 1 个元素的 tuple,必须加一个逗号,，来消除歧义
t = (1,)
print(t)

# 可变tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)

# 条件判断语句
# elif 是 else if 的缩写
print(int('1000'))

# 循环 for in 和 while
# for in
for a in t:
    print(a)
# range()函数:range(5)生成的序列是从 0 开始小于 5 的整数
print(list(range(5)))


# dict 即java中的map，键值对形式,
# dict 内部存放的顺序和 key 放入的顺序是没有关系的
# 这种 key-value 存储方式，在放进去的时候，必须根据 key算出 value 的存放位置，
# 这样，取的时候才能根据 key 直接拿到 value,通过 key 计算位置的算法称为哈希算法（Hash）
# key 的对象必须保证不可变
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] = 90


# 避免key不存在报错
if 'Michael' in d:
    print(d['Michael'])
    # 如果 key 不存在，可以返回 None，或者自己指定的 value
    print(d.get('Michael', 100))
# 删除指定key-value
d.pop('Tracy')
print(d)


# Set 创建一个 set，需要提供一个 list 作为输入集合
# 也是一组 key 的集合,但不存储 value，因此不可重复，自动过滤重复元素
# 数学意义上的无序和无重复元素的集合
s = set([1, 2, 3, 5, 4])
s.add(6)
s.remove(6)
print(s)

# 做数学意义上的交集、并集等操作
s2 = set([1, 2])
print(s & s2)
print(s | s2)

# 同样不可以放入可变对象，因为无法判断两个可变对象是否相等，与dict一样需要通过hash生成其位置
# 不可变对象
a = 'abc'
b = a.replace('a', 'A')
print(a, b)

# 函数 abs()绝对值 max()最大值 int() float() str()转字符串 bool()布尔值
# 函数名赋给变量
a = abs
print(a(-20))
# hex()int转16进制
print(hex(255))

# 定义函数
# 没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-10))

# 空函数pass
def nop():
    pass

# 类型检查
print(isinstance(1, (int, float)))

# 返回多个值return x1，x2，返回值是一个 tuple
# 位置参数，power(x, n)传入的两个值按照位置顺序依次赋给参数 x 和 n


# 默认参数 def power(x, n=2): 必选参数在前，默认参数在后，与默认参数不符的参数需要赋值
def enroll(name, gender, age=6, city='Beijing'):
    pass
enroll('Bob', 'M', 7)
# 不按照顺序给默认参数赋值，需要指定参数名称
enroll('Adam', 'M', city='Tianjin')
# 默认参数必须指向不变对象

# 可变参数，参数 numbers 接收到的是一个 tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1,2,3]
print(calc(1, 2, 3, 4))
# Python允许你在list或tuple前面加一个*号,把list或tuple作为可变参数传进去
print(calc(*nums))

# 关键字参数
# 关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# person('Bob', 35, city='Beijing')
# 可以组装dict放入，extra =  {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)
# 关键字参数是拷贝，不会影响原来的extra dict

# 如果要限制关键字参数的名字，就可以用命名关键字参数,*后为命名关键字参数
# 必须传入参数名,可以有缺省值
def person(name, age, *, city = 'Beijing', job):
    print(name, age, city, job)
# 当有缺省值，调用时可以不传入city参数
person('Jack', 24, job='Engineer')


# 任意函数，都可以通过类似 func(*args, **kw)的形式调用它
# 其中*args代表将一个tuple传入，**kw代表将一个dict传入



# 尾递归优化，python不支持尾递归优化
# 汉诺塔移动练习


# 切片操作符







