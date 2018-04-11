from asyncio import sleep
from sanic import Sanic
from sanic.response import json

app = Sanic()

# seconds
WAIT_TIME = 0.2

HOST = '0.0.0.0'
PORT = 8010

@app.route('/')
async def test(request):
    await sleep(WAIT_TIME)
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
