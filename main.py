import asyncio
import json
import websockets

DERIV_WS = "wss://ws.derivws.com/websockets/v3?app_id=1089"


async def connect_deriv():
    async with websockets.connect(DERIV_WS) as ws:
        print("Connected to Deriv")

        await ws.send(json.dumps({
            "ticks": "R_10"
        }))

        while True:
            data = await ws.recv()
            print(data)


asyncio.run(connect_deriv())
