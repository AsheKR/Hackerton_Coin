# 한강 코인

## Installation

```bash
pipenv install --dev
cd app
# 데이터 자동수집
python3 manage.py crontab add
```

## 시나리오

- 상승/하락 구간

구간 별 메세지를 사용자에게 랜덤으로 보여줌

20% ~ 15%
10% ~ 15%
0% ~ 10%
`상승`
--- 
`하락`
-10% ~ 0%
-15% ~ -10%
-20% ~ -15%