import os
import requests

OC = os.environ.get("LAW_API_OC")

if not OC:
    raise RuntimeError(
        "LAW_API_OC가 설정되어 있지 않습니다."
    )

url = "https://www.law.go.kr/DRF/lawService.do"

params = {
    "OC": OC,
    "target": "law",
    "MST": "268757",
    "type": "JSON",
}

response = requests.get(
    url,
    params=params,
    timeout=30
)

response.raise_for_status()

data = response.json()

print(data)
