# input()返回的数据类型是 str name = input('输入名字')
# print("hello,world", 'gg', name)
import functools

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
    s1 = s.lower()
    # replace 替换所有指定字符，不一定是首位,采用切片的方法替换
    s2 = s1[0].upper() + s1[1:]
    return s2


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# sum函数，传入list求和
L = [1, 2, 3, 4]
print(sum(L))


# 写一个prod函数利用reduce()求积
def product(x1, x2):
    return x1 * x2


def prod(l):
    return reduce(product, l)


print(prod(L))


# 写一个str转float函数,map将数字和小数点字符转化为数字，reduce累加求和
def char2num(ch):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '.': -1}[ch]


def str2float(s):
    # 记录小数点后几位的变量
    point = 0

    def sum2sum(x, y):
        # point 记录y位于的小数点后位数，只有其大于0时才处理
        # 比如123.456 先走到3. x=123 y=-1 再走到.4 x=123.0 y=4
        # 用point记录遇到小数点前，正常累加求和
        # nonlocal声明point变量在整个大函数中都有效
        nonlocal point

        # 遇到小数点之后,改变求和方式，需要首先判断
        if y == -1:
            point = 1
            return x + 0.0

        if point == 0:
            return x * 10 + y
        else:
            # 每次进入该代码块代表向小数点后进了一位
            z = x + y / pow(10, point)
            point += 1
            return z

    return reduce(sum2sum, map(char2num, s))


print(str2float("0.99"))

# filter函数 filter()函数返回的是一个 Iterator
# 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素

# str.strip([chars])移除字符串头尾的指定字符序列，默认是空格和换行符
s = ' abc '
print(s and s.strip())


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


# 用埃式筛选法生成素数
# 除开2 ，从3开始的奇数序列生成器，返回序列第一个数，将剩余数字%，取不能整除的数字

# 从3开始奇数序列生成器
def odd_creator():
    n = 3
    while True:
        yield n
        n += 2


# 筛选函数,每次需要判断整除的数不固定，可以通过lambda生成不同的函数
def filter_method(n):
    return lambda x: x % n != 0


# 素数生成器
def primes():
    yield 2

    o = odd_creator()

    while True:
        # 取序列第一个元素
        n = next(o)
        yield n

        # 过滤惰性迭代器,filter函数返回的是新的iterator
        o = filter(filter_method(n), o)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


# filter过滤掉非回数
def reverse_judge(x):
    s = str(x)
    l = len(s) - 1
    i = 0
    while i < l:
        if s[i] == s[l]:
            i += 1
            l -= 1
            continue
        else:
            return True
    return False


print('------------filter---------------')
x = filter(reverse_judge, [121, 0, 100, 2002])

for n in x:
    print(n)

print('------------sorted函数---------------')

# key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)

# 忽略大小写并进行反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=lambda x: x[0])
print(L2)
L3 = sorted(L, key=lambda x: x[1])
print(L3)

print('------------闭包Closure---------------')
# 闭包就是内部函数引用外部变量，返回的函数保存了外部变量的值，最终调用返回的函数时，外部变量的值为最新值
# 牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量


print('------------装饰器（Decorator）---------------')
# 函数对象有一个__name__属性
print(abs.__name__)


# 无参数装饰器
def log(func):
    def a(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)

    return a


# 有参数装饰器，从上至下，依次传入@的文本，函数func，函数参数
def log(content):
    def a(func):
        # 加上这个注解，指定的函数属性就被复制到了func
        @functools.wraps(func)
        def b(*args, **kw):
            print('call %s--%s' % (func.__name__, content))
            return func(*args, **kw)

        return b

    return a


@log("卧佛了")
def now():
    print('2019-1-10')


now()
print(now.__name__)


# 请编写一个 decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log1(func):
    def wrapper(*args, **kw):
        print('begin call')
        func(*args, **kw)
        print('end call')

    return wrapper


@log1
def now2():
    print('2019-1-10')


now2()

print('------------偏函数partial function---------------')
# functools.partial 的作用就是，把一个函数的某些参数
# 给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数
# 会更简单

print(int('10', base=2))
# partial函数的入参为  函数  函数*args参数   函数**kw参数
# 相当于固定了base = 2关键字参数
int2 = functools.partial(int, base=2)
print(int2('10'))

# 相当于固定了100作为max *args入参之一
max2 = functools.partial(max, 100)
print(max2(*[10, 20, 30]))

# if __name__=='__main__':
# test()
# 这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

# xxx 和__xxx 这样的函数或变量就是非公开的（private），不应该被直接引用


# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 从清华镜像安装指定python库
from PIL import Image

print('------------OOP---------------')


# 第一个参数永远是 self，表示创建的实例本身,相当于java中的this
# 类名后面是父类
class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.__score__ = 100

    def print_info(self):
        print('姓名：%s 年龄：%s ' % (self.__name, self.age))


bart = Student('李四', 20)
# print(bart.__name) 类所绑定的属性前加上__，则表示权限为private，外部不可以访问
# 单下划线_xx可以访问但是希望被视为private的
# 不能直接访问__name 是因为 Python 解释器对外把__name 变量改成了_Student__name
print(bart._Student__name)
# __xx__特殊变量是可以直接访问的，不是 private 变量
print(bart.__score__)

bart.age = 30
bart.print_info()


# 多态
class Animal(object):
    def run(self):
        print("animal is running")


class Cat(Animal):
    def run(self):
        print("cat is running")


class Dog(Animal):
    def run(self):
        print("dog is running")


def sth_run(animal):
    animal.run()


dog1 = Dog()
cat1 = Cat()
sth_run(dog1)
sth_run(cat1)


# 鸭子类型,只要实现了run方法就可以实现多态，继承不是必须的
class Sth(object):
    def run(self):
        print('sth is running')


sth1 = Sth()
sth_run(sth1)

print('------------判断数据类型---------------')
# type()函数
print(type(sth1))
print(type([]))

# 判断是否函数
import types

print(type(sth_run) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# isinstance()函数
print(isinstance(dog1, Animal))
print(isinstance(dog1, (Animal, Sth)))

# dir()函数，列出对象所有属性和方法
d = dir(Animal)
print(d)

# getattr()获取指定对象某属性、setattr()设置属性、hasattr()判断是否有属性
age = getattr(bart, "age")
print(age)

# 获取不存在的属性值，返回default值
print(getattr(bart, 'name', "not found"))
setattr(bart, "age", 13)
print(bart.age)
print(hasattr(bart, "age"))

# getattr()也可以用于获取方法
pr = getattr(bart, "print_info")
pr()


# 类属性和实例属性的区别
class Person(object):
    name = '我是个人'

    def __init__(self):
        self.name = '具体人名字'


# 当类属性与实例属性同名，实例属性优先级高于类属性
print(Person.name)
p = Person()
print(p.name)

# 删除实例属性
del p.name
print(p.name)

print('------------OOP高级---------------')


# 给Air类的实例动态绑定一个方法
class Air(object):
    pass


def dynamic_method(self, age1):
    self.age = age1
    print("实例的动态绑定方法----" + str(age1))


air = Air()

from types import MethodType

# 绑定方法到指定实例
air.dy_meth = MethodType(dynamic_method, air)
air.dy_meth(20)
print(air.age)

# 给Air类动态绑定方法，以使得所有实例都可调用
Air.meth = MethodType(dynamic_method, air)
air2 = Air()
air2.meth(100)


# __slot__变量限制该类的实例能够定义的属性
class Net(object):
    __slots__ = ['name', 'money']


net = Net()
# 不能绑定slots中没有指定的属性
net.name = '网络'
net.money = '无限'


# net.slim = '瘦子'


# @property装饰器，回忆装饰器中的@log
# @property注解的相当于getter方法，@属性名.setter相当于setter方法
class Stu(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


stu = Stu()
stu.score = 11  # 调用setter方法，并进行参数合法性判断
print(stu.score)  # 相当于调用getter方法


# 多重继承 = MixIn设计

# __str__作用 改变print(obj)打印的信息
class Obj1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name = %s age = %s' % (self.name, self.age)


obj_ = Obj1("张三", 130)
print(obj_)


# 如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实现一个__iter__()方法
# for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
# 利用__iter__和__next__写一个斐波那契数列生成器
class Fib(object):
    # 无参数构造器
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a

    # 使得Fib实例能够用索引获取元素,n为传入的索引值
    # __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
for fib in f:
    print(fib)

print(f[4])
print(f[0:5])


# 在没有找到属性的情况下，才调用__getattr__，任意调用则返回None
class Obj3(object):

    def __getattr__(self, item):
        if item == 'name':
            return lambda: 'nickname'


obj_1 = Obj3()
print(obj_1.name())
print(obj_1.age)


# 实现一个链式调用
class Chain(object):
    # 需要将前一个对象的path传入进行初始化
    def __init__(self, path=''):
        self.__path = path

    def __str__(self):
        return self.__path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self.__path, item))

    def __call__(self, *args, **kwargs):
        print('obj is called')


ch = Chain().user.name.age.score
print(ch)

# __call__函数，使得对象能直接调用，模糊了对象和函数的界限
ch()
# 判断一个对象是否可以被调用
print(callable(ch))

print('-------------枚举-----------------')
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value是默认从1开始自动分配的值
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 继承Enum类自定义枚举类型
from enum import unique


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问方式
print(Week.Mon)
print(Week.Thu.value)
print(Week['Mon'])
# 通过value获取
print(Week(1))

print('-----------------元类-----------------')
# from 是py文件名字 import 后是类名
from hi import Hello

# import之后就可以像普通对象一样
h = Hello()
h.hello()
print(type(Hello), type(h))


def hello(self, name='world'):
    print('Hello, %s.' % name)


# 使用type()函数返回一个对象的类型，也可以创建一个新的类型
# 参数 1.类名 2.多重继承的tuple 3.函数与方法名绑定
GG = type('GG', (object,), dict(f=hello))
GG().f()


# metaclass 元类-->类-->实例 允许对类进行修改和创建

