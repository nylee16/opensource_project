import streamlit as st
import base64

st.set_page_config(initial_sidebar_state="collapsed")

# 로컬 이미지 파일 base64 인코딩 함수
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 이미지 파일명 (실제 파일명으로 변경)
img_path = "images/detail_image.png"  # 실제 경로와 파일명

img_base64 = img_to_base64(img_path)

st.set_page_config(layout="centered")

# HTML/CSS로 배경 이미지와 컨테이너 겹치기 (크기 키움)
st.markdown(f"""
<style>
.bg-wrap {{
    position: relative;
    width: 450px;
    height: 800px;
    margin: 0 auto;
    border-radius: 32px;
    overflow: hidden;
    box-shadow: 0 2px 16px rgba(0,0,0,0.10);
    background: #f5f5f5;
}}
.bg-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}}
.info-container {{
    position: absolute;
    left: 50%;
    bottom: 20px;
    transform: translateX(-50%);
    width: 92%;
    background: white;
    border-radius: 24px 24px 0 0;
    box-shadow: 0 -2px 16px rgba(0,0,0,0.10);
    padding: 32px 24px 24px 24px;
    z-index: 2;
}}
.info-title {{
    font-weight: bold;
    font-size: 24px;
    margin-bottom: 6px;
}}
.info-sub {{
    color: #5A8DFF;
    font-size: 17px;
    margin-bottom: 18px;
}}
.info-row {{
    background: #F6F6F8;
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 10px;
    font-size: 17px;
}}
.close-btn {{
    position: absolute;
    top: 24px;
    right: 24px;
    font-size: 28px;
    color: #bbb;
    cursor: pointer;
    z-index: 3;
}}
.stButton > button {{
    width: 100% !important;
    font-size: 17px;
    padding: 13px 0;
    border-radius: 13px;
    background: #F6F6F8;
    color: #5A8DFF;
    font-weight: 700;
    border: none;
}}

.stButton > button:active {{
    background: #e0e8fa;
}}
</style>
<div class="bg-wrap">
    <img src="data:image/png;base64,{img_base64}" class="bg-img"/>
    <div class="info-container">
        <span class="close-btn">&times;</span>
        <div class="info-title">경북 의성군 안평면 괴산리 산 61</div>
        <div class="info-sub">567m</div>
        <div class="info-row">
            <div style="color:#888; font-size:14px;">발생 일시</div>
            <div>2025-03-22 09:10</div>
        </div>
        <div class="info-row">
            <div style="color:#888; font-size:14px;">대피 방향</div>
            <div>남쪽 / 남동쪽으로 대피하세요</div>
        </div>
        <div class="info-row">
            <div style="color:#888; font-size:14px;">주의할 것</div>
            <div>현장 지휘관의 공식 안내를 우선시하세요</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 이미지 아래에 페이지 이동 버튼 추가
st.markdown("<br>", unsafe_allow_html=True)  # 여백 주기

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    if st.button("자세히 알아보기", use_container_width=True):
        st.switch_page("more_detail_page.py")  
    if st.button("홈으로 돌아가기", use_container_width=True):
        st.switch_page("fire_situation.py")  # 메인 파일명에 맞게 수정



