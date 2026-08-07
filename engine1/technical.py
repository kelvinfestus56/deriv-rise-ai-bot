class TechnicalEngine:
    def __init__(self):
        self.prices = []

    def add_tick(self, price):
        self.prices.append(price)

        # tunatunza ticks 300 za mwisho tu
        if len(self.prices) > 300:
            self.prices.pop(0)

    def analyze(self):
        if len(self.prices) < 10:
            return {
                "direction": "WAIT",
                "score": 0
            }

        recent = self.prices[-10:]

        start_price = recent[0]
        end_price = recent[-1]

        if end_price > start_price:
            direction = "UP"
            score = 70
        elif end_price < start_price:
            direction = "DOWN"
            score = 30
        else:
            direction = "SIDEWAYS"
            score = 50

        return {
            "direction": direction,
            "score": score
        }
