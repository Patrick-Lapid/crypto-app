import requests
import json
import os
# Authentication using env variable
headers = {
    'X-CMC_PRO_API_KEY': os.environ.get("CMC_API_KEY"),
    'Accepts': 'application/json',
}
# API url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# Specify top 100 coins
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}
# Get json data of all 5 coins
data = requests.get(url, params=parameters, headers=headers).json()

time = data['status']['timestamp']
coins = data['data']



# Round each float to 2 decimal places
for coin in coins:
        coin['quote']['USD']['price'] = round(coin['quote']['USD']['price'], 2)
        coin['quote']['USD']['market_cap'] = round(coin['quote']['USD']['market_cap'], 2)
        coin['circulating_supply'] = round(coin['circulating_supply'], 2)
        print(coin['quote']['USD']['price'])

def displayCoinList():
    for coin in coins:
        coin['quote']['USD']['price'] = f"{float(coin['quote']['USD']['price']):,}"
        coin['quote']['USD']['market_cap'] = f"{float(coin['quote']['USD']['market_cap']):,}"
        coin['circulating_supply'] = f"{float(coin['circulating_supply']):,}"


def getPrice(ticker):
    for coin in coins:
        if coin['symbol'] == ticker.upper():
            return coin['quote']['USD']['price']
    print("Invalid Ticker")



