import requests
import json
import os
# Authentication
headers = {
    'X-CMC_PRO_API_KEY': os.environ.get('CMC_API_KEY'),
    'Accepts': 'application/json',
}
# API url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# Specify top 5 coins
parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}
# Get json data of all 5 coins
data = requests.get(url, params=parameters, headers=headers).json()

coins = data['data']


def getPrice(ticker):
    for coin in coins:
        if coin['symbol'] == ticker.upper():
            return coin['quote']['USD']['price']
    print("Invalid Ticker")


btc = getPrice("btec")

print(btc)
