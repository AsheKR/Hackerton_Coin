import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

"""
    Coin Model 확장을 위한 Mixin Classes
"""


class GetTopTenCoinMixin:
    CURRENCY_PAIR = []

    @classmethod
    def get_10_top_coins(cls):
        """
        korbit에서 지원하는 상위 10개의 코인을 가져와서 Choices 형태로 저장

        :return: CURRENT_PAIR ('<Bitcoin Real Name>', '<BitCoin Full Name>')
        """
        if not cls.CURRENCY_PAIR:
            url = 'https://coinmarketcap.com/exchanges/korbit/'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            trs = soup.select_one('table').find_all('tr')[1:]
            for tr in trs:
                currency = tr.select_one('.link-secondary').text
                pair = tr.find('a', href='https://www.korbit.co.kr/').text
                pair_name = re.sub(r'(\w+)/(\w+)', r'\g<1>_\g<2>', pair.lower())
                cls.CURRENCY_PAIR.append((pair_name, currency))
        return tuple(cls.CURRENCY_PAIR)


class CoinMixin:

    @staticmethod
    def coin_detail(coin):
        def message(data):
            """
            json 파일을 받아 다음과 같이 사용하면 아래 내용을 가져올 수 있다.
            """
            last_price = int(data.get('last'))
            high_price = int(data.get('high'))
            low_price = int(data.get('low'))
            bid_price = int(data.get('bid'))
            ask_price = int(data.get('ask'))
            timestamp = datetime.fromtimestamp(int(data.get('timestamp') / 1000))

            # for Debug
            return '''
                현재가: {:,}
                최근 24시간 최고가: {:,}
                최근 24시간 최저가: {:,}
                매수 호가: {:,}
                매도 호가: {:,}
                최종 체결 시각: {}
                '''.format(last_price, high_price, low_price, bid_price, ask_price, timestamp)

        base_url = 'https://api.korbit.co.kr/v1/ticker/detailed'
        url = '{}?currency_pair={}'.format(base_url, coin)
        response = requests.get(url)
        msg = message(response.json())
        return response.json()
