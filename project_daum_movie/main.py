# SELENIUM

# pip install selenium
# pip install webdriver_manager

# ** Selenium 을 사용하는 이유?
#   - Requests 는 현재 URL 의 정적 페이지 소스코드만 수집 가능
#      -> "더보기" 버튼 클릭과 같이 동적인 정보는 수집 불가!
#   - Selenium 은 전용 브라우저를 사용해서 동작
#       -> 따라서 chrome 드라이버와 같은 브라우저 설정 반드시 필요 !
#       ※ Selenium 은 처음에 웹 브라우저 테스트 용으로 개발

# ** Selenium 사용 방법 2가지
# 1.직접 다운로드
#   -URL: https://sites.google.com/chromium.org/driver/downloads
# 2.실시간 (코드) 다운로드

from db.movie_dao import add_review
from datetime import datetime, timedelta
import math
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1.Selenium 전용 웹 브라우저 구동
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2.URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=169137"
driver.get(url)
time.sleep(2)

# 3.페이지 전체 코드 가져오기
doc_html = driver.page_source
# print(doc_html)

# 4.Selenium -> BeautifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5.영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print("=" * 100)
print(f" 영화 제목: {movie_title}")
print("=" * 100)

# 6.전체 리뷰 출력("평점 더보기" 클릭)
#   - 다음 영화 최초 페이지 -> 10개
#   - "평점 더보기" 클릭 -> 30개
#   ? "평점더보기" 몇 번 클릭 -> 전체 리뷰 출력

# ex) 전체 리뷰: 187개
# 수식: 올림 ((187-10) / 30)

# 6-1. 전체 리뷰 수집
total_review_cnt = doc.select("span.txt_netizen")[0].get_text()

# 6-2. 전체 리뷰에서 숫자만 추출
#   - 문자열 슬라이싱
#   - 예) (187명)
# print(total_review_cnt[1:-2])
# - 정규식 -> 숫자만 추출
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))  # 숫자가 아니면 공백으로 전환

# 6-3."평점 더보기" 클릭 횟수 계산(모든 리뷰 출력)
click_cnt = math.ceil((num_review - 10) / 30)

# 7.Selenium 을 통해서 "평점 더보기" 클릭
for i in range(click_cnt):
    # "평점 더보기" 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(0.2)

# 8.전체 소스 코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")  # li가 188개 있음
print(f"= 전체 리뷰: {len(review_list)}건")
print("=" * 100)
# item 리뷰 1건(평점, 리뷰, 작성자, 작성일자)
for item in review_list:
    review_score = item.select("div.ratings")[0].get_text()
    print(f" - 평점: {review_score} 점")
    review_content = item.select("p.desc_txt")[0].get_text()
    # \n = 한 줄 개행 -> \n을 제거
    review_content = re.sub("\n", "", review_content).strip()
    print(f" - 리뷰: {review_content}")
    review_writer = item.select("a.link_nick > span")[1].get_text()
    print(f" - 작성자: {review_writer}")
    review_date = item.select("span.txt_date")[0].get_text()
    # 24시간 이내에 작성 된 리뷰의 날짜 표기 -> 00시간 전 -> 다음 영화 날짜(20XX.00.00. 00:00)
    # 1.00시간 전으로 표기 되는 날짜 찾기
    if len(review_date) < 7:
        # 2."00시간" -> 숫자만 추출
        reg_hour = int(re.sub(r"[^~0-9]", "", review_date))
        # 3. 등록 일자 = 현재 시간 - 00
        # print(f"현재 시간: {datetime.now()}")   # 년 부터 나노초 까지
        review_date = datetime.now() - timedelta(hours=reg_hour)
        # print(f"등록 시간: {review_date}")
        # 4.계산된 등록일자 날짜 포맷 변경(다음 무비 양식으로)
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    print(f" - 작성 일자: {review_date}")
    print("=" * 100)

    # MariaDB 저장 (제목, 리뷰, 평점, 작성자, 작성 일자)
    data = {
        "title": movie_title,
        "review": review_content,
        "score": review_score,
        "writer": review_writer,
        "reg_date": review_date
    }
    add_review(data)
