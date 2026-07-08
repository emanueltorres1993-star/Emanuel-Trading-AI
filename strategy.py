from config import PAIRS

class Strategy:

    def __init__(self):
        self.signals_today = 0

    def analyze(self):

        if self.signals_today >= 8:
            return None

        signal = {
            "pair": PAIRS[0],
            "direction": "CALL",
            "confidence": 90
        }

        self.signals_today += 1

        return signal
