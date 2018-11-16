import json

import requests
from django.shortcuts import render
from django.urls import reverse

def get_index(request):
    base_url = 'http://127.0.0.1:8000'
    btc_coinValue = requests.get(base_url+reverse('apis:apis_get_coinValue', kwargs={'pk': 1}))
    ten_coins = requests.get(base_url+reverse('apis:apis_get_ten_coin'))

    ten_coins_dict = json.loads(ten_coins.content)
    btc_coinValue_dict = json.loads(btc_coinValue.content)
    print(btc_coinValue_dict)

    context = {
        'ten_coins': ten_coins_dict,
        'btc_coinValue': btc_coinValue_dict,
    }

    return render(request, 'index.html', context=context)