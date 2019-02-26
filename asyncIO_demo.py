import asyncio


#
# @asyncio.coroutine
# def hello():
#     print('hello,world!')
#     # 异步调用,消息
#     r = yield from asyncio.sleep(1)
#     print('hello again')
#
#
# # 获取消息循环
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# 异步获取三个io首页的响应头内容
# 不要忘记注解，该方法将一个generator标记为协程coroutine
@asyncio.coroutine
def wget(host):
    print('wget %s....' % host)
    conn = asyncio.open_connection(host, 80)
    reader, writer = yield from conn
    # 这里的writer应该是指定请求头
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        # 这里应该是readline（）之后print，然后在第二次yield from处搁置，这时loop从队列中拿已经
        # 完成的异步操作消息继续下一步
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # 关闭socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
