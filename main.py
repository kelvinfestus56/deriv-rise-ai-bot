from engine1.technical import TechnicalEngine

import asyncio
import json
import websockets


DERIV_WS = "wss://ws.derivws.com/websockets/v3?app_id=1089"


async def connect_deriv():

    analyzer = TechnicalEngine()

    async with websockets.connect(DERIV_WS) as ws:

        print("Connected to Deriv")

        request = {
            "ticks": "R_10"
        }

        await ws.send(json.dumps(request))

        while True:

            data = await ws.recv()
            tick = json.loads(data)

            if "tick" in tick:

                price = tick["tick"]["quote"]

                analyzer.add_tick(price)

                analysis = analyzer.analyze()

                print(
                    "Price:",
                    price,
                    "| Direction:",
                    analysis["direction"],
                    "| Score:",
                    analysis["score"]
                )


asyncio.run(connect_deriv())
