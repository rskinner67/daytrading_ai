import requests
def send_alert(symbol, message):
    webhook_url = 'https://discord.com/api/webhooks/YOUR_WEBHOOK_ID'
    data = {"content": f"{symbol}: {message}"}
    requests.post(webhook_url, json=data)