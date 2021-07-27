from django.http import HttpResponse
from django.shortcuts import render
from .forms import Userrequest
from django.contrib import messages
import random
import requests
from pycoingecko import CoinGeckoAPI
from .models import CoinRequest
# Create your views here.
def home(request):
    
    cg = CoinGeckoAPI()
    form = Userrequest(request.POST or None)
    if form.is_valid():
        try:
            cointst = form.cleaned_data.get('coin')
            price1 = cg.get_price(ids=cointst, vs_currencies='usd')
            price2 = price1.values()
            for p in price2:
                price = p.get('usd')
                link = random.randint(1111111, 9999999)
                query = CoinRequest.objects.create(coinPrice=price, coinLink=link)
                messages.info(request, link)
        except:
            form.add_error('coin', 'please dont edit this form')
    return render(request, 'home_file.html', {'form':form})

def show_price(request, *args, **kwargs):
    link = kwargs.get('link')
    price = CoinRequest.objects.get(coinLink=link)
    return HttpResponse(price.coinPrice)