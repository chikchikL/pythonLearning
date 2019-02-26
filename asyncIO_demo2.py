# python3.5之后的async/await语法

# 两步替换
# 1. 把@asyncio.coroutine 替换为 async；
# 2. 把 yield from 替换为 await

import asyncio


async def hello():
    print('hello')
    r = await asyncio.sleep(1)
    print('hello again')


# coroutine不能直接调用，需要放到事件循环中
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()