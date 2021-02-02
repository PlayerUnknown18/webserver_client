import asyncio
import websockets
import json
import time
from datetime import datetime


def open_as_json(path):
    with open(path,"r") as fin:
        json_data = json.loads(fin.read())
        return json_data["packets"],json_data["time"]



async def send_packets(uri):
    async with websockets.connect(uri) as websocket:
        json_data,time_to_send = open_as_json("playlist_4.jsonc")
        while True:
            if datetime.now().strftime("%d/%m/%Y %H:%M:%S") == time_to_send:
                break
            
        for i in range(len(json_data)):
            print(json_data[i])
            await websocket.send(json_data[i])
            print("Message sacssesfully sent!")
            for i in range(3):
                ack = await asyncio.wait_for(websocket.recv(),timeout=5)
                if "ack" == ack:
                    print("got an ack")
                    break
            
        

asyncio.get_event_loop().run_until_complete(
    send_packets('ws://localhost:3000'))




