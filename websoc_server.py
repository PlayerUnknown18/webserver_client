import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
           print("Got a message!")
           await websocket.send("hello")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 3000))
asyncio.get_event_loop().run_forever()
