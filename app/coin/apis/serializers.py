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
    coin = CoinSerializer()
    before_value = serializers.SerializerMethodField('debug_before_value')
    percent = serializers.SerializerMethodField('debug_calc_percent')

    def __init__(self, *args, **kwargs):
        self.cur_coin = kwargs.pop('cur_coin')
        super().__init__(*args, **kwargs)

    def debug_before_value(self, a):
        return list(CoinValue.objects.filter(coin=self.cur_coin))[-2].now_value

    def debug_calc_percent(self, a):
        today_start_value = CoinValue.objects.filter(coin=self.cur_coin, is_day_master=True).last().now_value
        current_value = CoinValue.objects.filter(coin=self.cur_coin).last().now_value
        percent = ((current_value - today_start_value) / 100)
        return percent

    class Meta:
        model = CoinValue
        fields = (
            'coin',
            'before_value',
            'now_value',
            'percent',
        )


class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = (
            'temperature',
            'created_at',
        )
