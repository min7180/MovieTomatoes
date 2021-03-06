# MovieTomatoes Ver 0.1
# 내용:
#     1) 네이버 영화에서 영화 리뷰 수정
#     2) 수집된 리뷰 MongoDB 에 저장
#     3) MongoDB 에서 수집된 데이터 불러옴
#     4) 인공지능에 사용할 수 있게 전처리
#     5) 전처리된 데이터를 활용하여 인공지능 분석 시작
#     6) 분석 결과를 시각화
# 만든이: 고혜민
# 일자: 2021.11.09

import math
import requests
from bs4 import BeautifulSoup
import webcrawl.webCrawlService as wcs


###########################
# 1. 데이터 수집 및 저장 #
###########################

movie_code = '209496'  # 네이버 영화 code

# 1. 제목 수집

title = wcs.get_movie_title(movie_code)
print(title)

# 2.전체 페이지 수 계산

pages = wcs.calc_pages(movie_code)
print(pages)

# 3. 리뷰 수집
# wcs.get_reviews(movie_code, pages, title)

#########################
# 2. 인공지능 분석 #
#########################

#########################
# 3. 분석결과 시각화 #
#########################





















###########################
# 2. 인공지능 분석 #
###########################

###########################
# 3. 분석결과 시각화 #
###########################
