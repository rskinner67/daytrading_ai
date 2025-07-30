import random

def get_signals():
    return [
        {"symbol": "AAPL", "signal": "MACD Cross ↑", "confidence": random.randint(70, 95)},
        {"symbol": "TSLA", "signal": "VWAP Bounce", "confidence": random.randint(65, 90)},
    ]