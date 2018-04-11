from asyncio import sleep
from sanic import Sanic
from sanic.response import json

app = Sanic()

HOST = '0.0.0.0'
PORT = 8010
WORKERS = 1

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/sleep/<sleep_value:int>')
async def test(request, sleep_value):
	""" sleep_value : int """
    await sleep(sleep_value)
    return json({'sleep': sleep_value})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, workers=WORKERS)