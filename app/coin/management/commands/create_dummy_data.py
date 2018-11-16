from django.core.management import BaseCommand

from coin.models import CoinValue, Coin

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('percent', nargs='+', type=int)

    def handle(self, *args, **options):
        percent = options.get('percent')[0]
        print(percent)
        if not percent:
            percent = 9

        percent = percent / 100

        coin = Coin.objects.get(pk=1)
        first_value = CoinValue.objects.filter(is_day_master=True)[0].now_value

        # 0.9퍼 오른거
        now_value = first_value + (first_value * percent)

        CoinValue.objects.create(
            coin=coin,
            now_value=now_value
        )