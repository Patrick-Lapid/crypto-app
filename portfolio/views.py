from django.shortcuts import render
from . import utils

# Create your views here.


def home(request):

    return render(request, 'portfolio/home.html')


def about(request):
    if request.method == "GET":
        utils.updateCoins()
        coinlist = utils.coins
        # for s in range(len(utils.coins)):
        #     coinlist[s]['quote']['USD']['price'] = f"{utils.coins[s]['quote']['USD']['price']:,}"
        #     utils.coins[s]['quote']['USD']['price'] = utils.coins[s]['quote']['USD']['price'].strip(',')
        #     print(utils.coins[s]['quote']['USD']['price'])

        # for s in range(len(utils.coins)):
        #     coinlist[s]['quote']['USD']['price'] = f"{float(utils.coins[s]['quote']['USD']['price']):,}"
        #     coinlist[s]['quote']['USD'][
        #         'market_cap'] = f"{float(utils.coins[s]['quote']['USD']['market_cap']):,}"
        #     coinlist[s]['circulating_supply'] = f"{float(utils.coins[s]['circulating_supply']):,}"
        #     print(type(utils.coins[s]['quote']['USD']['price']))

        # for coin in utils.coins:
        #     coinlist['quote']['USD']['price'] = f"{coin['quote']['USD']['price']:,}"
        #     coinlist['quote']['USD']['market_cap'] = f"{coin['quote']['USD']['market_cap']:,}"
        #     coinlist['circulating_supply'] = f"{coin['circulating_supply']:,}"
    return render(request, 'portfolio/about.html', {'coins': coinlist})
