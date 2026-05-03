import requests
from bs4 import BeautifulSoup

#실행 할때 터미널에서 python my_crawling_test.py로 실행

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
    
    # # find & find_all : 특정 태그를 찾는다. find는 첫 번째 매칭되는 태그만, find_all은 모두 찾는다.
    # print(soup.find("span"))
    # print(soup.find_all("span"))

    # select: css 선택자를 사용해 요소를 찾는다.
    # print(soup.select(".title"))

    # stripped_strings : 모든 텍스트를 공백을 제거한 상태로 하나씩 반환한다.
    # for string in soup.stripped_strings:
    #     print(repr(string))

    # string : 요소 내에서 직접 포함된 텍스트를 반환한다.
    # print(soup.span.string)
    
    # find_parents : 현재 태그의 모든 부모 요소를 리스트 형태로 반환한다.
    # print(soup.p.find_parents())

    # find_parend : 첫번째 부모 요소만 반환한다.
    # print(soup.p.find_parent)

    # find_next_siblings : 현재 태그 이후에 나오는 모든 형제를 가져온다.
    # print(soup.p.find_next_siblings())

    # find_previous_siblings : 현재 태그 이전에 있는 형재 요소들을 반환한다.
    # print(soup.p.find_previous_siblings())

    # find_next : 현재 요소 이후에 나오는 첫 번째 요소를 반환한다.
    # print(soup.p.find_next())

    # extract : 요소를 트리에서 제거하고 반환한다.
    # p_tag = soup.p.extract()
    # print(soup)

    # insert_before : 선택한 요소 앞에 새 요소를 삽입한다.
    # new_tag = soup.new_tag('p')
    # new_tag.string = 'Hello'
    # soup.p.insert_before(new_tag)
    # print(soup)

    # replact_with : 요소를 트리에서 제거하고 반환한다.
    # soup.span.replace_with("통보기준")
    # print(soup)

    # contents : 요소의 직속 자식들을 리스트 형태로 반환한다.
    print(soup.div.contents)

    # unwrap : 요소를 제거하고 그 내부 내용을 상위 요소에 병합한다.
    # soup.span.unwrap()
    # print(soup)

    # decompost : 요소를 트리에서 제거하고 완전히 삭제한다.
    # soup.span.decompost()
    # print(soup)

    # append : 기존 태그의 마지막 자식 요소로 새 요소를 추가할 때 유용하다.
    # new_tag = soup.new_tag("span")
    # new_tag.string = "메시지3"
    # soup.span.append(new_tag)
    # print(soup)

    # extend : 리스트나 여러 요소를 한꺼번에 추가할 수 있다.
    # new_tag1 = soup.new_tag("p")
    # new_tag1.string = "First"
    # new_tag2 = soup.new_tag("p")
    # new_tag2.string = "Second"
    # soup.span.extend([new_tag1, new_tag2])
    # print(soup)

    # clear : 요소의 모든 자식들을 제거한다.
    soup.span.clear()
    print(soup)


except Exception as e:
    print(f"에러 발생: {e}")
