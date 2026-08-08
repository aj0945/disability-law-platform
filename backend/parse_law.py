import os
import requests


OC = os.environ.get("LAW_API_OC")

if not OC:
    raise RuntimeError("LAW_API_OC가 설정되어 있지 않습니다.")


# 교통약자의 이동편의 증진법
MST = "268757"

url = "https://www.law.go.kr/DRF/lawService.do"

params = {
    "OC": OC,
    "target": "law",
    "MST": MST,
    "type": "JSON",
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

law = data["법령"]


# 현재 법령의 조문 데이터
article_data = law["조문"]["조문단위"]


def as_list(value):
    """API에서 하나의 객체 또는 리스트로 오는 데이터를 리스트로 통일한다."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def print_articles(articles):
    for article in as_list(articles):

        # '전문'은 장·절 제목 등이다.
        if article.get("조문여부") != "조문":
            continue

        number = article.get("조문번호", "")
        title = article.get("조문제목", "")
        content = article.get("조문내용", "")

        print("=" * 80)
        print(f"제{number}조 {title}")
        print(content)

        # 항
        for paragraph in as_list(article.get("항")):
            paragraph_number = paragraph.get("항번호", "")
            paragraph_content = paragraph.get("항내용", "")

            print(f"  {paragraph_number} {paragraph_content}")

            # 호
            for item in as_list(paragraph.get("호")):
                item_number = item.get("호번호", "")
                item_content = item.get("호내용", "")

                print(f"    {item_number} {item_content}")

            # 목
            for subitem in as_list(paragraph.get("목")):
                subitem_number = subitem.get("목번호", "")
                subitem_content = subitem.get("목내용", "")

                print(f"      {subitem_number} {subitem_content}")


print_articles(article_data)
