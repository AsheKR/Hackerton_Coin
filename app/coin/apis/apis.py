import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from river.models import River
from ..models import CoinValue, Coin
from .serializers import CoinValueSerializer, RiverSerializer


class CoinDetail(APIView):
    def get(self, request, pk, format=None):
        coin = Coin.objects.get(pk=pk)
        # 현재 값 가져오기
        coin_value_last = CoinValue.objects.filter(coin=coin).last()
        serializer = CoinValueSerializer(coin_value_last, cur_coin=coin)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RiverView(APIView):
    def get(self, request, format=None):
        river_temp = River.objects.last()
        serializer = RiverSerializer(river_temp)
        return Response(serializer.data, status=status.HTTP_200_OK)
