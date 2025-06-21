import streamlit as st
import base64

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# CCTV 이미지 base64 변환 함수
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# CCTV 이미지 경로 (사용자 파일명으로 변경)
cctv_img_path = "images/cctv_img.png"  # 예시 파일명
cctv_img_base64 = img_to_base64(cctv_img_path)

# 스타일 및 레이아웃
st.markdown("""
<style>
.outer-box {
    max-width: 390px;
    margin: 0 auto;
    background: #F6F6F8;
    border-radius: 18px;
    padding: 24px 14px 18px 14px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
}
.header-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 2px;
    letter-spacing: -0.5px;
}
.header-sub {
    color: #5A8DFF;
    font-size: 15px;
    margin-bottom: 10px;
}
.info-box {
    background: #fff;
    border-radius: 12px;
    padding: 13px 16px 7px 16px;
    margin-bottom: 8px;
    text-align: left;
}
.info-label {
    color: #888;
    font-size: 13px;
    margin-bottom: 2px;
}
.info-value {
    font-size: 16px;
    font-weight: 600;
}
.cctv-img-wrap {
    width: 100%;
    background: #222;
    border-radius: 14px;
    margin: 12px 0 10px 0;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}
.cctv-img {
    width: 100%;
    max-width: 360px;
    display: block;
}
.desc {
    font-size: 15px;
    color: #222;
    margin: 10px 0 0 0;
    padding: 0 2px;
}
.button-box {
    margin-top: 22px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.stButton > button {
    width: 100% !important;
    font-size: 17px;
    padding: 13px 0;
    border-radius: 13px;
    background: #F6F6F8;
    color: #5A8DFF;
    font-weight: 700;
    border: none;
}
.stButton > button:active {
    background: #e0e8fa;
}
</style>
""", unsafe_allow_html=True)

# 본문 UI
st.markdown(f"""
<div class="outer-box">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <div class="header-title">경북 의성군 안평면 괴산리 산 61</div>
            <div class="header-sub">567m</div>
        </div>
        <div style="font-size:24px; color:#bbb; font-weight:700; cursor:pointer;">×</div>
    </div>
    <div class="info-box">
        <div class="info-label">발생 일시</div>
        <div class="info-value">2025-06-22 09:10</div>
    </div>
    <div class="info-box">
        <div class="info-label">방향</div>
        <div class="info-value">163°S</div>
    </div>
    <div class="info-box">
        <div class="info-label">순간 최대 풍속</div>
        <div class="info-value">35m/s</div>
    </div>
    <div class="cctv-img-wrap">
        <img src="data:image/jpg;base64,{cctv_img_base64}" class="cctv-img" alt="CCTV 이미지"/>
    </div>
    <div class="desc">
        안평면 괴산리 산 61 산불 확산. 인근 주민과 등산객은 안전한 곳으로 대피 바람.
    </div>
</div>
""", unsafe_allow_html=True)

# 버튼 영역
with st.container():
    st.markdown(
        '<div class="button-box">',
        unsafe_allow_html=True
    )
    if st.button("근방 1km에 공유하기"):
        st.success("반경 1km내 해당 앱을 이용 중인 사람들에게 공유되었습니다")
    if st.button("홈으로 돌아가기"):
        st.switch_page("fire_situation.py")  # 메인 페이지 파일명에 맞게 수정
    st.markdown('</div>', unsafe_allow_html=True)
