import os
import requests

OC = os.environ["LAW_API_OC"]

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
