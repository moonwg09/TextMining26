import NaverNewsCrawler as nnc
import streamlit as st

st.title("네이터 크롤링 결과")

keyword = st.text_input("검색할 키워드 : ")

# 1. 키워드가 입력되었을 때만 크롤링을 시작합니다.
if keyword:
    with st.spinner('뉴스 데이터를 가져오는 중...'):
        corpus = nnc.crawl_naver_news_all(keyword)
    if corpus:
        df = nnc.crawl_csv(corpus)
        st.success(f"'{keyword}'에 대한 결과를 찾았습니다.")
        st.json(corpus[:3])
        st.dataframe(df)

        if st.button("csv 저장"):
            df.to_csv("naver_news_results.csv", index=False, encoding='utf-8-sig')
            st.success("내 컴퓨터에 저장되었습니다.")
        
    else:
        st.warning("분석할 데이터가 없습니다.")
        
else:
    st.info("키워드를 입력해주세요.")


