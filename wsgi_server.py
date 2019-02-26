from wsgiref.simple_server import make_server

# 使用python内置的wsgi服务器进行测试
from wsgi_server_function import hello_wsgi

# ip地址，端口，处理函数
server = make_server('', 8000, hello_wsgi)
print('serving http on port 8000......')
server.serve_forever()
