import streamlit as st

st.set_page_config(
    page_title="스마트 홈 대시보드 - 류지현",
    layout="wide"
)

st.header("스트림릿 베포 테스트중")
st.write("스트림릿 베포 해보기 - 류지현")

st.write("스트림릿 베포 내용 추가합니다")

# 페이지 등록
# st.page("파일경로", title='메뉴이름', icon="아이콘")
# 1. 홈 화면
home = st.Page("pages/home.py", title = "홈")
# 2. 센서 화면
sensors = st.Page("pages/sensors.py", title="센서 현황")
# 3. 전력 화면
power = st.Page("pages/power.py", title="전력 현황")

# 네이게이션 구성 (사이드 바와 같은 것)
pg = st.navigation({
    "메인" : [home],
    "분석" : [sensors, power]
})

# 사이드바 추가
st.sidebar.write("같이 사이드바 형태입니다")

# 선택 된 폐이지를 실행
pg.run()