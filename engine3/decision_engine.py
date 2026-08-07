class DecisionEngine:

    def __init__(self):
        self.minimum_confidence = 75


    def decide(self, technical, ai):

        technical_score = technical["score"]
        ai_score = ai["ai_score"]


        confidence = (
            technical_score + ai_score
        ) / 2


        if confidence >= self.minimum_confidence:
            decision = "BUY RISE"

        else:
            decision = "WAIT"


        return {
            "decision": decision,
            "confidence": round(confidence, 2)
        }
