# 只需要知道对方的 IP 地址和端口号，就可以直接发数据包
import socket

# 与tcp相比，发送用sendto--send，接收用recvfrom获得数据和发送方地址
# 不需要listen监听连接，客户端也不需要connect进行连接，因为udp是面向无连接的
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('bind udp on 9999')

while True:
    data, addr = s.recvfrom(1024)
    print('received from %s:%s' % addr)
    s.sendto(b'hello,%s' % data, addr)
