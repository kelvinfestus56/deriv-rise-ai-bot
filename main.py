from engine1.technical import TechnicalEngine
from engine2.ai_engine import AIEngine
from engine3.decision_engine import DecisionEngine

import asyncio
import json
import websockets


DERIV_WS = "wss://ws.derivws.com/websockets/v3?app_id=1089"


async def connect_deriv():

    technical_engine = TechnicalEngine()
    ai_engine = AIEngine()
    decision_engine = DecisionEngine()


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

                # ENGINE 1
                technical_engine.add_tick(price)

                technical_result = technical_engine.analyze()


                # ENGINE 2
                ai_result = ai_engine.analyze(
                    technical_result
                )


                # ENGINE 3
                decision = decision_engine.decide(
                    technical_result,
                    ai_result
                )


                print("---------------------")
                print("PRICE:", price)
                print("TECH:", technical_result)
                print("AI:", ai_result)
                print("FINAL:", decision)



asyncio.run(connect_deriv())
