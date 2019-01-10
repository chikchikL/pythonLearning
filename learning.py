# input()返回的数据类型是 str name = input('输入名字')
# print("hello,world", 'gg', name)
print("1024 * 768= ", 1024 * 768)

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
print(a, b)  # XYZ ABC

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
print(ord('A'))  # 65
# chr()函数把编码转换为对应的字符
print(chr(65))  # A

# 如果要在网络上传输，或者保存到磁盘上，就需要把str 前加上b变为以字节为单位的 bytes
x = 'ABC'

# 编码为指定的 bytes,纯英文的 str 可以用 ASCII 编码为 bytes，内容是一样的，含有中文的 str
# 可以用 UTF-8 编码为 bytes
# \x表16进制 \u表unicode编码
y = x.encode('ascii')
z = '中文需要用utf-8编码'.encode('utf-8')
print(y)  # b'ABC'
print(z)

print(len(x))

# 格式化符号%
# %d 整数
print('%03d个人' % 5)  # 3表示数字前有几个空格，0表示空格补0
# %f 浮点数
print('%.2f' % 3.1415)  # .2表示保留两位有效数字
# %s 字符串 永远起作用，它会把任何数据类型转换为字符串
print('Age:%s name:%s' % (25, True))
# %x 十六进制

# 练习
s1 = 72
s2 = 85
r = (85 - 72) / 72
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


nums = [1, 2, 3]
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
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 当有缺省值，调用时可以不传入city参数
person('Jack', 24, job='Engineer')

# 任意函数，都可以通过类似 func(*args, **kw)的形式调用它
# 其中*args代表将一个tuple传入，**kw代表将一个dict传入


# 尾递归优化，python不支持尾递归优化
# 汉诺塔移动练习


# 切片操作符 L[-1]为倒数第一个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])

N = list(range(100))
print(N[:10])
# 每两个取一个0:10:2 每五个取一个::5 仅:表示取所有元素，因为没有指定范围
print(N[::5])

# 字符串切片
str1 = 'hashMap'
print(str1[:3])

# 迭代 for in
# 对于dict for k in d 或者for v in d.values()或者 for k,v in d.items
# 通过 collections 模块的 Iterable 类型判断是否可以迭代

from collections.abc import Iterable

bo = isinstance('abc', Iterable)
print(bo)

#  enumerate函数将iterable转换为索引-元素对
l = enumerate((1, 2, 3))
for i, v in l:
    print(i, v)

# 列表生成式
# 把要生成的元素 x * x 放到前面，后面跟 for 循环，for 循环后面还可以加上 if 判断
# 可以使用两层循环
xy = [(1, 2), (3, 4)]
l1 = [str(x) + '--' + str(y) for x, y in xy if x == 1]
print(l1)

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 生成器：generator
# 可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的 list，节省内存
# 与列表生成式区别仅在于最外层的[]和()，通过 next(g)函数获得 generator 的下一个值
l = list(range(5))
g = (x for x in l)
print(g)
print(next(g))


# generator isinstance iterable
# 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator
# 每次调用 next()的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
    return 'done'


o = odd()
print(next(odd()))
print(next(o))

# for h in odd():
#     print(h)
# 获取不到return返回值，需要捕获StopIteration异常
while True:
    try:
        print('g' + str(next(o)))
    except StopIteration as e:
        print(e.value)
        break


# 用生成器构造杨辉三角形
# 杨辉三角生成需要上一行的数据进行推算

def triangles():
    # 指定该行元素个数
    count = 1
    pre = [1]

    while True:
        if count == 1:
            count += 1
            yield pre
        else:
            # 初始化一个0数组
            L = [0 for i in range(count)]
            i = 0
            while i < count:
                # 需要注意加括号添加次序判定
                if (i == 0) | (i == count - 1):
                    L[i] = 1
                else:
                    L[i] = pre[i] + pre[i - 1]
                i += 1
            pre = L
            count += 1
            yield L


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# 可以被 next()函数调用并不断返回下一个值的对象称为迭代器Iterator
# 生成器都是 Iterator 对象,list、dict、str 虽然是 Iterable，但都不是Iterator
# Iterable 变成 Iterator 可以使用 iter()函数
from collections.abc import Iterator

print(isinstance(iter([]), Iterator))

# 函数式编程：允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# 高阶函数，函数名也是变量
# 高阶函数：一个函数就可以 接收另一个函数作为参数
# map()函数 ：map()传入的第一个参数是 f，即函数对象本身。由于结果 r 是一个Iterator 是惰性序列，
it = map(abs, [-1, -1])
# next()函数方式与for in方式遍历iterator中元素注意区别
for x in it:
    print(x)

# reduce函数，将前两个元素函数结果与下一个元素继续进行计算
from functools import reduce


def add(x, y):
    return x + y


re = reduce(add, [1, 2, 3])
print(re)


# 用 map 和 reduce 写一个str2int函数
# 思路:map对字符串每个字符转化成int类型，reduce将转换成的数字进行累加
def char2num(ch):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9}[ch]


def add2(x, y):
    return x * 10 + y


def str2int(str):
    return reduce(add2, map(char2num, str))


print(str2int("12345"))


# 将字符串变成首字母大写，其余小写
#
def normalize(s):
    pass


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
