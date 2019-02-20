# \d一个数字 \w一个字母或者数字 \s一个空格或者tab空白符
# .匹配任意字符 *任意个字符 +表至少一个字符 ？0或者1个字符 {n}n个字符 {n,m}表示n-m个字符
# \d{3}\s+\d{3,8} 三个数字，至少一个空格，3-8个数字
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线，\_表示转义
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}前面 1 个字符+后面最多 19 个字符
# [P|p]ython 可以匹配'Python'或者'python'
# ^表示行的开头，^\d 表示必须以数字开头
# $表示行的结束，\d$表示必须以数字结束
import re

content = input("输入电话号码")
# 返回的是Match对象
if re.match(r'^\d{3}-\d{3,8}$', content):
    print('match success')
else:
    print('fail')

# 正则表达式切分字符串
# 切分空格或者逗号分割的字符串
a = re.split(r'[\s\，]+', "a,  b  c     d")
if isinstance(a, list):
    print(a)

# 分组group，用（）表示分组
m = re.match(r'^(\d{3})-(\d{3,8})$', content)
# 打印子串
print(m.groups())
# 原始字符串
print(m.group(0))

# 贪婪匹配规则,匹配结果为('102300', '')，前一组匹配了所有字符串
m2 = re.match(r'^(\d+)(0*)$', '102300')
print(m2.groups())

# 预编译一个正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
h = re_telephone.match(content).groups()
print(h)

# 练习：验证email地址
re_email = re.compile(r'^(\w+)(\.{0,1})(\w*)@(\w+)(\.com)$')
if re_email.match("someone@gmail.com"):
    print(re_email.match("someone@gmail.com").groups())
