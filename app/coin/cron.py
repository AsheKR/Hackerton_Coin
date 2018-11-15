from datetime import datetime, timedelta, time

from .models import CoinValue
from .mixin import CoinMixin, GetTopTenCoinMixin


def get_coin_info_1_minute():
    #for Debug
    data = CoinMixin.coin_detail('btc_krw')
    now_value = int(data.get('last'))
    CoinValue(
        coin='btc_krw',
        now_value=now_value,
    )

    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    CoinValue.objects.filter(created_at__lte=today_end, created_at__gte=today_start)
