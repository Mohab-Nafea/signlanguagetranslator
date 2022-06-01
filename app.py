import asyncio
import websockets
from random import randrange

sentence = ['old', 'fine', 'are you ok', 'how are you', 'Hi', 'hello']
print("...")


async def echo(websocket):
    index = randrange(6)
    await websocket.send(sentence[index])


async def main():
    async with websockets.serve(echo, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())