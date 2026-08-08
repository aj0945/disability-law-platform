import os
import requests

OC = os.environ.get("LAW_API_OC")

if not OC:
    raise RuntimeError(
        "LAW_API_OC가 설정되어 있지 않습니다. "
        "API 인증값을 환경변수로 설정해주세요."
    )

url = "https://www.law.go.kr/DRF/lawSearch.do"

params = {
    "OC": OC,
    "target": "law",
    "type": "JSON",
    "query": "교통약자의 이동편의 증진법",
    "display": 10,
    "page": 1,
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

print(data)
