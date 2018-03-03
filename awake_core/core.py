import asyncio
import aiozmq
import zmq
from jsonrpcserver.aio import methods
from jsonrpcserver.response import NotificationResponse

import time

@methods.add
async def ping():
    return 'pong'

@methods.add
async def hi_yoko():
    time.sleep(3)
    return '洋子你好！'

@methods.add
async def awake(**kargs):
    print("### should wake up now!")
    return "awake."

async def main():
    rep = await aiozmq.create_zmq_stream(zmq.REP, bind='tcp://*:5000')
    while True:
        request = await rep.read()
        for block in request:
            response = await methods.dispatch(block.decode())
            if not response.is_notification:
                rep.write((str(response).encode(),))

if __name__ == '__main__':
    asyncio.set_event_loop_policy(aiozmq.ZmqEventLoopPolicy())
    asyncio.get_event_loop().run_until_complete(main())
