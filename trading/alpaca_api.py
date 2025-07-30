import os
import requests

API_KEY = os.getenv("PKRCCUZQ8I3HJURZ1NAK")
SECRET_KEY = os.getenv("NqHypmqSC0TdH9ehPW6lp5JuYLcUtnjo8DW06m6d")
BASE_URL = os.getenv("https://paper-api.alpaca.markets/v2")

def get_quote(symbol):
    headers = {
        'APCA-API-KEY-ID': API_KEY,
        'APCA-API-SECRET-KEY': SECRET_KEY
    }
    url = f"{BASE_URL}/v2/stocks/{symbol}/quotes/latest"
    return requests.get(url, headers=headers).json()