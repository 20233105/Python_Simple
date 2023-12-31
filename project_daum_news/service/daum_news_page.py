# 다음 실시간 뉴스 목록(15개) 기사 [제목, 본문, 날짜] 수집기

import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

count = 0
url = "https://news.daum.net/breakingnews/digital"
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
