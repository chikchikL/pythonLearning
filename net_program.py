# 网络编程
# ipv4 32位2进制，分为4组8位显示即192.168.1.1这种
# ipv6 128位2进制

import socket

# param1：ipv4 param2：tcp流
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 用tuple指定域名和端口，连接
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html','wb') as f:
    f.write(html)