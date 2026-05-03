import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 html 가져오기
url = "https://www.weather.go.kr/w/index.do/"

# 2. 페이지 가져오기
try:
    response = requests.get(url)
    
    # 3. 분석하기
    soup = BeautifulSoup(response.text, 'lxml')
    
    # 4. 결과 출력
    print("연결 성공!")
    print("사이트 제목:", soup.title.text)
    # print(soup.prettify())  # 전체 html을 가져온다

    # print(soup.title)  # title만 가져온다

    # print(soup.title.name)

    # print(soup.title.string)

    # print(soup.p)

    # print(soup.find_all('a')) # find_all(id="link3")

    # for link in soup.find_all('a'):
    #     print(link.get('href'))

    # print(soup.get_text())
    
except Exception as e:
    print(f"에러 발생: {e}")
