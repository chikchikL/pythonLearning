import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 指定连接的服务端端口
s.connect(('127.0.0.1', 9999))
# 连接后接收的消息
print(s.recv(1024).decode('utf-8'))

for data in [b'tracy', b'kobe', b'harden']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()

