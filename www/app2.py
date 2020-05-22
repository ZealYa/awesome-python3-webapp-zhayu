# !user/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Lanlan gets certificate of the teacher!</h1>',content_type='text/html')

#@asyncio.coroutine
async def init():
    app = web.Application()
    #app.router.add_route('GET', '/', index)
    app.add_routes([web.get('/',index)])
    #srv = yield from loop.create_server(app.make_handler(), 'localhost', 9000)
    
    #logging.info('server started at http://127.0.1.1:9000...')
    #return srv
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner,'*','9000')
    await site.start()
    print('服务器-127.0.1.1:9000-启动成功')

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
