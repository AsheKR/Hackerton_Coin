import os
import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from river.models import River
from ..models import CoinValue, Coin
from .serializers import CoinValueSerializer, RiverSerializer, CoinSerializer


class GetTenCoinView(APIView):
    def get(self, request, format=None):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        return Response(serializer.data)

class CurrentCoinValueView(APIView):
    def get(self, request, pk, format=None):
        coin = Coin.objects.get(pk=pk)
        # 현재 값 가져오기
        coin_value_last = CoinValue.objects.filter(coin=coin).last()
        serializer = CoinValueSerializer(coin_value_last, cur_coin=coin)

        percent = serializer.data['percent']

        if percent < 0:
            dirname = 'down'
            if percent < -15:
                # -15보다 낮은것
                folder_name = '-20_-15'
            elif percent < -10:
                # -10보다 낮은것
                folder_name = '-15_-10'
            else:
                folder_name = '-10_0'
        else:
            dirname = 'up'
            if percent < 10:
                # 10보다 낮은 것
                folder_name = 'p0_10'
            elif percent < 15:
                # 15보다 낮은것
                folder_name = 'p10_15'
            else:
                folder_name = 'p15_20'

        dirpath = os.path.join(os.path.join(os.path.join(settings.STATIC_DIR, 'images'), dirname), folder_name)

        onlyfiles = [f for f in os.listdir(dirpath)]
        img_file = random.choice(onlyfiles)

        img_full_path = os.path.join(dirpath, img_file)
        img_rel_path = '../' + img_full_path.split('app/')[1]

        print(img_rel_path)

        data = serializer.data
        data['img_path'] = img_rel_path

        return Response(data, status=status.HTTP_200_OK)


class RiverView(APIView):
    def get(self, request, format=None):
        river_temp = River.objects.last()
        serializer = RiverSerializer(river_temp)
        return Response(serializer.data, status=status.HTTP_200_OK)
