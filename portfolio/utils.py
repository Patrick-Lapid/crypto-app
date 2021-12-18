import requests
import datetime as dt
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

# Get json data of top 100 coins
data = requests.get(url, params=parameters, headers=headers).json()

time = data['status']['timestamp']
coins = data['data']


# Round each float to 2 decimal places

def updateCoins():
    for coin in coins:
        price = coin['quote']['USD']['price'] 
        if (price < 0.01):
            coin['quote']['USD']['price'] = round(coin['quote']['USD']['price'], 8)
        else:
            coin['quote']['USD']['price'] = round(coin['quote']['USD']['price'], 2)
        coin['quote']['USD']['market_cap'] = round(
            coin['quote']['USD']['market_cap'], 2)  
        coin['circulating_supply'] = round(coin['circulating_supply'], 2)


# Grabs price based off of ticker
def getPrice(ticker):
    for coin in coins:
        if coin['symbol'] == ticker.upper():
            return coin['quote']['USD']['price']
    print("Invalid Ticker")


