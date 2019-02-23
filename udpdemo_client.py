import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 不用connect直接发送和接收数据
for data in [b'tracy',b'kobe',b'cater']:
    sock.sendto(data,('127.0.0.1',9999))
    print(sock.recv(1024).decode('utf-8'))
sock.close()