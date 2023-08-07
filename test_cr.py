# requests와 BeautifulSoup 패키지를 불러옵니다.
import streamlit as st
import requests
from bs4 import BeautifulSoup

# 웹 사이트의 URL을 변수에 저장합니다.
url = "https://www.apple.com/kr/shop/refurbished/ipad"

# requests 모듈로 URL에 접근하고 HTML을 가져옵니다.
response = requests.get(url)

# BeautifulSoup으로 HTML을 파싱합니다.
soup = BeautifulSoup(response.text, "html.parser")

# HTML에서 텍스트만 추출합니다.
text = soup.get_text()

# 텍스트를 줄 단위로 나눕니다.
lines = text.split("\n")

# 특정 단어가 포함된 라인을 찾습니다.
keyword = "리퍼비쉬 iPad" # 찾고 싶은 단어를 입력하세요.
keyword2 = "₩"
keyword3 = "iPad Pro"

view=keyword
view

for line in lines:
    # 라인에 키워드가 있으면 출력합니다.
    if keyword in line:
       view=(line)
       view
    if keyword2 in line:
        view=(line)
        view
    if keyword3 in line:
        view=(line)
        view
          
       
