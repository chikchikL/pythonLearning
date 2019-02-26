# asyncio实现了tcp udp ssl等协议，aiohttp是基于asyncio实现的http框架
import asyncio
from aiohttp import web


# 编写一个http服务器处理以下url
#  / - 首页返回 b'<h1>Index</h1>'；
#  /hello/{name} - 根据 URL 参数返回文本 hello, %s!。
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    # 创建tcp服务
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)

    print('server started at http://localhost:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

