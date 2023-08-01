import websockets
import asyncio


async def listen():
    url = "ws://localhost:8000/ws"
    async with websockets.connect(url) as websocket:
        msg = await websocket.recv()
        print(msg)


asyncio.get_event_loop().run_until_complete(listen())
