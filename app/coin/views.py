import json
import os
import random

import requests
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

def get_index(request):
    base_url = 'http://127.0.0.1:8000'
    btc_coinValue = requests.get(base_url+reverse('apis:apis_get_coinValue', kwargs={'pk': 1}))
    ten_coins = requests.get(base_url+reverse('apis:apis_get_ten_coin'))
    river_temp = requests.get(base_url+reverse('apis:get_river'))

    ten_coins_dict = json.loads(ten_coins.content)
    btc_coinValue_dict = json.loads(btc_coinValue.content)
    river_temp = json.loads(river_temp.content)

    print(btc_coinValue_dict)

    context = {
        'ten_coins': ten_coins_dict,
        'btc_coinValue': btc_coinValue_dict,
        'river_temp': river_temp,
    }

    return render(request, 'index.html', context=context)