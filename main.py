import asyncio
import json
import websockets

DERIV_WS = "wss://ws.derivws.com/websockets/v3?app_id=1089"


async def connect_deriv():
    async with websockets.connect(DERIV_WS) as ws:
        print("Connected to Deriv")

        request = {
            "ticks": "R_10"
        }

        await ws.send(json.dumps(request))

        while True:
            data = await ws.recv()
            tick = json.loads(data)

            print(tick)


if __name__ == "__main__":
    asyncio.run(connect_deriv())
