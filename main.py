import asyncio
import json
import websockets

from engine1.technical import TechnicalEngine


DERIV_WS = "wss://ws.derivws.com/websockets/v3?app_id=1089"


async def connect_deriv():

    async with websockets.connect(DERIV_WS) as ws:

        print("Connected to Deriv")

        request = {
            "ticks": "R_10"
        }

        await ws.send(json.dumps(request))

        engine1 = TechnicalEngine()

        while True:

            data = await ws.recv()

            tick_data = json.loads(data)

            print(tick_data)

            # hapa baadaye tutaunganisha engine 2 na engine 3

            if "tick" in tick_data:
                price = tick_data["tick"]["quote"]

                signal = engine1.analyze(price)

                print("Engine1:", signal)


async def main():

    await connect_deriv()


if __name__ == "__main__":
    asyncio.run(main())
