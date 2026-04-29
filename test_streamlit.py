import time
import app as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt  # Altair은 시각화 라이브러리
from numpy.random import default_rng as rng

st.title('Hello, Streamlit World') # 일반 터미널에서 입력해야 정상적으로 작동합니다(streamlit run test_streamlit.py) , 옆에 생기는 섹션 앵커는 특정 부분으로 바로 이동할 수 있는 고유 주소를 복사하는 기능이에요.
st.set_page_config( # 페이지 타이틀 설정
    page_title="내 멋진 앱",
    page_icon="🔥"  # 여기에 원하는 이모지나 아이콘을 넣을 수 있습니다.
)

# 1. write and magic

# 1-1. write 

st.write("Hello, *World!* :sunglasses:") # ** : 텍스트 기울기, :sunglasses => 이모티콘

st.write(1234)   # 데이터 프레임

data_frame=pd.DataFrame(
        {
            "first column": [1,2,3,4],
            "second colunm": [10,20,30,40],
        }
    )
st.write(data_frame)

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")

df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)

# 1-2. write_stream : 
_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():    # 버튼을 누르면 관련 만들어둔 내용들이 나온다
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)

# 1-3. magic : streamlit의 기능으로 거의 모든 것을 작성할 수 있게 해준다
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 dataframe 생성

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# 대부분의 지원되는 차트 유형에서도 작동한다
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Matplotlib chart 그려준다

# 2. Text elements

# 2-1. subheader : 텍스트를 서브헤더 형식으로 표시
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)

# 2-2. markdown : markdown 형식으로 나열한 것
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

# 2-3. badge : 아이콘과 라벨이 있는 색상 배치를 표시
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# 2-4. caption: 작은 글씨로 텍스트 표현
st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")

# 2-5. code : 코드 블록 표시
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

# 2-6. divider : 수평선 표시
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  

st.write("This text is between the horizontal rules.")

st.divider() 

# 2-7. echo : 
with st.echo():
    st.write('This code will be printed')

# 2-8. latex:
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 2-9. text: 텍스트를 그대로 표현
st.text("This is text\n[and more text](that's not a Markdown link).")

# 2-10. html: html 형식으로 사용 가능
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

