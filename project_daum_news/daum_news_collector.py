# 카테고리별 실시간 다음 뉴스 수집기 ver 1.0
# - 작성자: 20233105
# - 2023.11.08
# - 라이브러리: requests, Beautifulsoup4, pymongo
# - 프로세스
#   1) 수집 가능한 뉴스 카테고리 출력
#   2) 사용자로부터 원하는 카테고리 입력
#   3) 입력 된 카테고리 다음 실시간 뉴스 수집(제목, 본문, 날짜)
#   4) 수집 된 뉴스 데이터 데이터베이스에 저장

# 도메인 지식: 내가 개발하고자 하는 분야의 전문지식
# ex) 은행 프로그램 -> 도메인 지식(은행 로직)
# ex) 인사 프로그램 -> 도메인 지식(노동법)
# ex) 회계 프로그램 -> 도메인 지식(회계)

import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

news_category = {
    "사회": "society",
    "정치": "politics",
    "경제": "economic",
    "국제": "foreign",
    "문화": "culture",
    "연예": "entertain",
    "스포츠": "sports",
    "IT": "digital",
}
print("=" * 100)
print("뉴스 카테고리 목록")
for i, item in enumerate(news_category):
    print(f" {i+1}.{item}")
print("MSG: 수집하고 싶은 뉴스 카테고리를 입력해주세요.")

while True:
    news = input(" => 카테고리: ")
    if news in list(news_category.keys()):
        break
    else:
        print("= MSG: 올바른 카테고리를 입력하세요")
    print(list(news_category.keys()))
    exit()
print(news_category[news])
# 다음 실시간 뉴스 목록(15개) 기사 [제목, 본문, 날짜] 수집기



count = 0
url = f"https://news.daum.net/breakingnews/{news_category[news]}?page={page}"
result = requests.get(url)

if result.status_code == 200:
    print("URL 접속 성공 => 데이터를 수집합니다.")
    doc = BeautifulSoup(result.text, "html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")


    for url, in url_list:
        count += 1
        print(f"{count}", "=" * 100)
        get_news(url["href"])
else:
    print("잘못된 URL 경로 입니다. 다시 한 번 확인해 주세요")

print(result)
