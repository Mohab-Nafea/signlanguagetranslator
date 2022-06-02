import asyncio
import websockets
import signal
from random import randrange
import os

sentence = ['old', 'fine', 'are you ok', 'how are you', 'Hi', 'hello']
print("...")


async def echo(websocket):
    print("connect")
    index = randrange(6)
    await websocket.send(sentence[index])


async def main():
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
    async with websockets.serve(echo, host="", port=5000):
        await stop

asyncio.run(main())
