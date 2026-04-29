from wordcloud import WordCloud
import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


@st.cache_data
def change_text():
    text = st.title('텍스트가 변할 겁니다.')
    time.sleep(3)
    text = text.info('3초가 지났습니다.')

change_text()

with st.sidebar:
    st.header("설정")
    
    # 이름을 입력하세요 (text_input)
    user_name = st.text_input("이름을 입력하세요")
    
    # 나이 슬라이더 (slider)
    # min_value=0, max_value=120, default_value=25
    user_age = st.slider("나이", 0, 120, 25)
    
    # 좋아하는 색상을 선택하세요 (selectbox)
    user_color = st.selectbox(
        "좋아하는 색상을 선택하세요",
        ["빨강", "노랑", "초록", "파랑"]
    )

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    ["write", "magic Command", "text", "widget1", "widget2", "form", "matplotlib", "wordcloud"]
) 

with tab1:
    st.title("Hello, Streamlit World")
    st.header("Hello, Welcome to Streamlit world")
    name = "Woonggi"
    st.title(f"Hello, {name}~~~~ Welcome to Streamlit World!!!")

with tab2:
    df = pd.DataFrame({
        'A' : [1,2,3,4],
        'B' : [10,20,30,40]
    })
    df

with tab3:
    st.title('텍스트가 변할 겁니다.')

    placeholder = st.empty() # 내용을 갈아끼울 빈 칸 생성
    
    placeholder.info('2초가 지났습니다.')
    time.sleep(2)
    # placeholder.success('4초가 지났습니다.')
    # time.sleep(2)
    # placeholder.warning('6초가 지났습니다.')
    # time.sleep(2)
    # placeholder.error('8초가 지났습니다.')

with tab4:
    st.button("Reset", type="primary")
    if st.button("버튼"):
        st.success('clicked button')
    st.button("Go to gallery")

    genre = st.radio(
        "머신 러닝 방법",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        index=None,
    )
    # f-string을 사용하여 문자열을 하나로 합침
    st.info(f"나의 선택: {genre}")

    agree = st.checkbox("토큰화")
    if agree:
        st.write("성공")

with tab5:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
    )

    st.info(f"{option}")

    options = st.multiselect(
    "머신러닝 방법",
        ["Green", "Yellow", "Red", "Blue"],
        default=["Yellow", "Red"],
    )

    st.info(f"{options}")

    w = st.slider("가중치", 0, 20, 5)
    st.info(f"가중치: {w}")

with tab6:
    with st.form(key='user_input_form'):
        st.subheader("사용자 입력 폼")
        
        # 이름 입력 (text_input)
        name = st.text_input("이름", value="")
        
        # 나이 입력 (number_input)
        age = st.number_input("나이", min_value=1, max_value=100, value=24)
        
        # 약관 동의 (checkbox)
        agreed = st.checkbox("약관에 동의합니다", value=True)
        
        # 제출 버튼 (form_submit_button)
        submit_button = st.form_submit_button(label='제출')

    # 제출 버튼이 눌렸을 때의 동작
    if submit_button:
        # 이름과 나이 출력
        st.write(f"이름: {name}, 나이: {age}")
        
        # 약관 동의 여부에 따른 메시지
        if agreed:
            st.success("약관에 동의했습니다.")
        else:
            st.warning("약관에 동의하지 않았습니다.")
with tab7:
    # 1. 그래프에 들어갈 데이터 준비
    labels = ['A', 'B', 'C', 'D']
    values = [10, 40, 25, 30]

    # 2. Matplotlib 도화지(fig)와 축(ax) 만들기
    fig, ax = plt.subplots()

    # 3. 가로 막대 그래프 그리기
    ax.barh(labels, values, color='skyblue')

    # 4. 그래프 제목이나 라벨 설정 (선택 사항)
    ax.set_title("Matplotlib Chart")
    ax.set_xlabel("Values")
    ax.set_ylabel("Labels")

    # 5. Streamlit에 그래프 표시하기
    st.pyplot(fig)

with tab8:
    # 1. 앱 제목 설정
    st.title(":cloud: Streamlit 워드클라우드 시각화")

    # 2. 분석할 가짜 데이터 (텍스트) 준비
    # 원하는 텍스트로 자유롭게 바꿔보세요!
    text = """
    Streamlit is open-source Python library makes it easy to create and share beautiful custom web apps for machine learning and data science. In just minutes you can build and deploy powerful data apps. Streamlit is great for data visualization and interactive widgets like slider button selectbox. Making wordcloud in Streamlit is very simple using the wordcloud and matplotlib libraries. It helps to visualize word frequency in a beautiful way. Data scientists love Streamlit. Python is awesome for data analysis.
    """

    # 사이드바에서 설정 변경 기능 추가 (선택 사항)
    with st.sidebar:
        st.header("워드클라우드 설정")
        background_color = st.color_picker("배경색 선택", "#ffffff")
        colormap = st.selectbox("색상 테마 선택", ["viridis", "plasma", "inferno", "magma", "cividis", "rocket", "mako"])

        # 3. 워드클라우드 객체 생성 및 이미지 생성
        wc = WordCloud(
            width=800, 
            height=400, 
            background_color=background_color, 
            colormap=colormap,
            min_font_size=10,
            max_words=100
        ).generate(text)

        # 4. Matplotlib을 사용하여 시각화
        # Matplotlib 도화지(fig) 생성
        fig, ax = plt.subplots(figsize=(10, 5))

        # 생성된 워드클라우드 이미지를 축에 표시
        ax.imshow(wc, interpolation='bilinear')

        # 축(눈금) 숨기기 (워드클라우드는 축이 필요 없음)
        ax.axis("off")

        # 5. Streamlit에 Matplotlib 그래프 표시
        # 이전 답변처럼 st.pyplot(fig)를 사용합니다.
    st.pyplot(fig)

    


