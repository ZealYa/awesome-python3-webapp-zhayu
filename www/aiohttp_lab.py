import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    
    runner = web.AppRunner(app)
    await runner.setup()
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    site = web.TCPSite(runner,'*','9000')
    await site.start()
    print('Server started at http://127.0.0.1:9000...')
#     return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
