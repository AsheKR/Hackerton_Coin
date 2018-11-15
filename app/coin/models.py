from django.db import models

from .mixin import GetTopTenCoinMixin


class Coin(models.Model, GetTopTenCoinMixin):
    # korbit 에서 지원해주는 상위 10개의 비트코인을 가져와서 Choices로 만듬
    name = models.CharField(
        choices=GetTopTenCoinMixin.get_10_top_coins(),
        max_length=9,
        unique=True,
    )

    def __str__(self):
        return self.name


class CoinValue(models.Model):
    coin = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
    )
    now_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_day_master = models.BooleanField(default=False)