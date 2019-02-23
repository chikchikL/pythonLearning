import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听的端口(服务端可能有多张网卡)，这里本机同时模仿服务端
s.bind(('127.0.0.1', 9999))
# 等待连接的最大数量
s.listen(5)
print('等待连接...')


# 每个线程单独处理的连接
def tcplink(sock, addr):
    print('接收了新的连接，来自：%s:%s' % addr)
    # 发送welcome给客户端
    sock.send(b'welcome')
    # 循环接收消息,且如果客户端发送了exit或者空消息，停止接收
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data).encode('utf-8'))
        # 将客户端发送来的消息添加hello发回去

    sock.close()
    print('来自%s:%s的连接关闭了' % addr)


while True:
    # 接收新连接
    sock, addr = s.accept()
    # 创建新线程处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    # 启动线程
    t.start()
