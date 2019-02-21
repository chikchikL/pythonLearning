# 模拟往某个网址发送GET请求
from urllib import request

# GET请求
# with as的用法：返回的是个对象，该对象有__enter__与__exit__方法分别在with语句前执行和with语句后执行
# 这样不用考虑with语句内发生异常和
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 如果需要模拟iphone6请求移动端网页，需要使用Request对象，通过往Request对象添加Http头
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0
# like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0
# Mobile/10A5376e Safari/8536.25')


# POST请求，把参数data以bytes形式传入


# 通过Proxy访问网站