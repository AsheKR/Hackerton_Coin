from datetime import datetime, timedelta, time

from .models import CoinValue, Coin
from .mixin import CoinMixin, GetTopTenCoinMixin


def get_coin_info_1_minute():
    CURRENCY_PAIR = GetTopTenCoinMixin.get_10_top_coins()

    for currency, __ in CURRENCY_PAIR:
        data = CoinMixin.coin_detail(currency)
        coin, created = Coin.objects.get_or_create(name=currency)
        now_value = int(data.get('last'))
        coinValue = CoinValue(
            coin=coin,
            now_value=now_value,
        )

        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        # 그날 만든 CoinValue 항목이 없다면 그날의 대표 값으로 지정
        if not CoinValue.objects.filter(created_at__lte=today_end, created_at__gte=today_start):
            coinValue.is_day_master = True

        coinValue.save()
