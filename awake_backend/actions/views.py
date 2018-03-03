from django.shortcuts import render
from django.http import HttpResponse

from time import sleep

import asyncio
import zmq
from jsonrpcclient.zeromq_async_client import ZeroMQAsyncClient

# Create your views here.

def test(request):
    asyncio.set_event_loop(zmq.asyncio.ZMQEventLoop())
    asyncio.get_event_loop().run_until_complete(commu())
    return HttpResponse("done")


async def commu():
    client = ZeroMQAsyncClient('tcp://localhost:5000')
    response = await client.request("hi_yoko")
    return response
