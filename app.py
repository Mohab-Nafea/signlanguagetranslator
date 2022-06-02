import asyncio
import websockets
from random import randrange
import os

sentence = ['old', 'fine', 'are you ok', 'how are you', 'Hi', 'hello']
print("...")


async def echo(websocket):
    print("connect")
    index = randrange(6)
    await websocket.send(sentence[index])


async def main():
    async with websockets.serve(echo, host="0.0.0.0", port=5000):
        await asyncio.Future()

asyncio.run(main())
