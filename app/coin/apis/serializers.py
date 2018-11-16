from rest_framework import serializers

from coin.models import Coin, CoinValue
from river.models import River


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = (
            'id',
            'name',
        )


class CoinValueSerializer(serializers.ModelSerializer):
    coin_id = CoinSerializer()

    class Meta:
        model = CoinValue
        fields = (
            'id',
            'now_value',
            'created_at',
            'is_day_master',
            'coin_id',
        )


class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = (
            'temperature',
            'created_at',
        )
