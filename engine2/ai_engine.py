class AIEngine:

    def __init__(self):
        self.history = []

    def analyze(self, technical_result):

        direction = technical_result["direction"]
        tech_score = technical_result["score"]

        if direction == "UP":
            ai_score = tech_score + 10

        elif direction == "DOWN":
            ai_score = tech_score - 10

        else:
            ai_score = 50


        if ai_score > 100:
            ai_score = 100

        if ai_score < 0:
            ai_score = 0


        return {
            "ai_score": ai_score,
            "analysis": self.get_message(ai_score)
        }


    def get_message(self, score):

        if score >= 80:
            return "Strong UP setup"

        elif score >= 60:
            return "Possible UP setup"

        elif score <= 30:
            return "Weak setup"

        else:
            return "Wait for better condition"
