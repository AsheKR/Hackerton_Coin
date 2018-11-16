# 한강 코인

## Installation

```bash
pipenv --python 3.6.6
pipenv install --dev
cd app
# Create Database
python3 manage.py migrate
# Add Data
python3 manage.py shell
    - from coin.cron import get_coin_info_1_minute
    - get_coin_info_1_minute()
    - get_coin_info_1_minute()
    - from river.cron import river_temper_cron
    - river_temper_cron()
    - exit()
# for automatic get coin, river
python3 manage.py crontab add
# runserver
python3 manage.py runserver
```
