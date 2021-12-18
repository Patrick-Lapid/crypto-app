from django.shortcuts import render
from . import utils

# Create your views here.


def home(request):

    return render(request, 'portfolio/home.html')


def about(request):
    if request.method == "GET":
        utils.updateCoins()
        coinlist = utils.coins
        
    return render(request, 'portfolio/about.html', {'coins': coinlist})
