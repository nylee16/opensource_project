import streamlit as st
import requests
from PIL import Image
import os
import base64
from streamlit_folium import st_folium
import folium

# 이미지 경로
IMG1 = "images/map1.png"
IMG3 = "images/map3.png"
IMG_TEST="images/test_img_1.jpg"

# 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "start"
if "selected_contact" not in st.session_state:
    st.session_state.selected_contact = None
if "selected_message" not in st.session_state:
    st.session_state.selected_message = "실시간 대피 경로 보내기"


# 1. 화재 감지 API 호출 (실제 연동) => main으로 옮김


# 2. 첫 번째 화면 (지도 + 버튼)
def page_fire():
    img_path = IMG1
    img_width = 300  # 원하는 가로폭(px)으로 조절
    img_height = 400

    cols = st.columns([1,2,1])
    with cols[1]:
        st.image(img_path, width=img_width)
        st.markdown(
            f"""
            <style>
            div.stButton > button {{
                width: {img_width}px !important;
                height: 48px !important;
                font-size: 1.2em;
                background: #115399 !important;
                color: #fff !important;
                border-radius: 12px !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        if st.button("현 위치와 대피 경로 공유하기"):
            st.session_state.page = "share"

# 3. 두 번째 화면 (연락처/메시지 선택)
def page_share():
    st.markdown('<h2><b>현 위치와 대피 경로 공유하기</b></h2>', unsafe_allow_html=True)
    st.write("수신자")
    contacts = [("우리 딸", "images/contact1.png"), ("손자", "images/contact2.png")]
    for name, img in contacts:
        cols = st.columns([1,2,1])
        with cols[1]:
            st.image(img, width=300)
            if st.button(name):
                st.session_state.selected_contact = name
    # 연락처 선택 시 안내 문구 표시
    if st.session_state.selected_contact:
        st.markdown(f"""
        <div style="background-color:#fff3cd; color:#856404; padding:16px; border-radius:8px; font-weight:bold; font-size:1.1em; margin-bottom:10px; text-align:center;">
            {st.session_state.selected_contact}에게 대피 경로를 공유합니다.
        </div>
        """, unsafe_allow_html=True)
    st.write("메시지")
    msg_cols = st.columns([1,2,1])
    with msg_cols[1]:
        msg1 = st.button("메시지 수정하기")
        msg2 = st.button("실시간 대피 경로 보내기")
        if msg1:
            st.session_state.selected_message = "메시지 수정하기"
        if msg2:
            st.session_state.selected_message = "실시간 대피 경로 보내기"
        st.markdown(f"""
        <div style="background-color:#fff3cd; color:#856404; padding:12px; border-radius:8px; font-weight:bold; font-size:1.05em; margin-bottom:10px; text-align:center;">
            선택된 메시지: {st.session_state.selected_message}
        </div>
        """, unsafe_allow_html=True)
        if st.button("보내기"):
            st.session_state.page = "map"

# 4. 세 번째 화면 (대피 경로 지도)
def page_map():
    st.markdown('''
        <div style="background-color:#fff3cd; color:#856404; padding:16px; border-radius:8px; font-weight:bold; font-size:1.1em; margin-bottom:18px; text-align:center;">
            대피 경로가 공유되었습니다!
        </div>
    ''', unsafe_allow_html=True)
    if st.button("위치 기반 대피소 추천 보기"):
        st.session_state.page = "recommend"

# 네 번째 페이지: 위치 기반 추천

def page_recommend():
    st.markdown('<b style="font-size:1.1em;">위치 기반 추천</b>', unsafe_allow_html=True)
    shelters = [
        {"name": "안평면사무소", "desc": "면행정복지센터", "time": "38분", "distance": "2.2Km", "address": "경북 의성군 안평면 안평의성로 36"},
        {"name": "신동마을회관", "desc": "", "time": "1시간 47분", "distance": "6.9km", "address": "경북 의성군 안평면 신동길 12"}
    ]
    selected = st.session_state.get('selected_shelter')
    btn_css = '''
        <style>
        div.stButton > button {
            width: 100% !important;
            height: 48px !important;
            background: #115399 !important;
            color: #fff !important;
            font-weight: bold !important;
            font-size: 1.1em !important;
            border: none !important;
            border-radius: 12px !important;
            margin-top: 8px;
            margin-bottom: 8px;
            cursor: pointer;
        }
        </style>
    '''
    st.markdown(btn_css, unsafe_allow_html=True)
    if not selected:
        for shelter in shelters:
            cols = st.columns([1,6,1])
            with cols[1]:
                st.markdown(f"""
                    <div style='background:#fff; border-radius:16px; box-shadow:0 1px 4px rgba(0,0,0,0.04); padding:18px 0 10px 0; margin-bottom:12px; width:100%; text-align:left;'>
                        <div style='font-size:1.2em; font-weight:bold; color:#222; display:inline;'>{shelter['name']}</div>
                        <span style='color:#888; font-size:1em; margin-left:8px;'>{shelter['desc']}</span><br>
                        <span style='color:#1976d2; font-weight:bold; font-size:1em;'>{shelter['time']}</span>
                        <span style='color:#888; font-size:0.95em; margin-left:8px;'>{shelter['distance']}</span>
                        <span style='color:#888; font-size:0.95em; margin-left:16px;'>{shelter['address']}</span>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("선택", key=f"select_{shelter['name']}"):
                    st.session_state.selected_shelter = shelter['name']
    else:
        # 선택된 대피소 상세 정보만 카드로 출력
        shelter = next(s for s in shelters if s['name'] == selected)
        cols = st.columns([1,6,1])
        with cols[1]:
            st.markdown(f"""
                <div style='background:#fff; border-radius:16px; box-shadow:0 1px 4px rgba(0,0,0,0.04); padding:18px 0 18px 0; margin-bottom:18px; width:100%; text-align:left;'>
                    <div style='font-size:1.2em; font-weight:bold; color:#222; display:inline;'>{shelter['name']}</div>
                    <span style='color:#888; font-size:1em; margin-left:8px;'>{shelter['desc']}</span><br>
                    <span style='color:#1976d2; font-weight:bold; font-size:1em;'>{shelter['time']}</span>
                    <span style='color:#888; font-size:0.95em; margin-left:8px;'>{shelter['distance']}</span>
                    <span style='color:#888; font-size:0.95em; margin-left:16px;'>{shelter['address']}</span>
                </div>
            """, unsafe_allow_html=True)
            if st.button("길 찾기 시작", key="start_route"):
                st.session_state.page = "navigation"

# 마지막 페이지: 길찾기 진행

def page_navigation():
    btn_css = '''
        <style>
        div.stButton > button {
            width: 300px !important;
            height: 48px !important;
            background: #115399 !important;
            color: #fff !important;
            font-weight: bold !important;
            font-size: 1.1em !important;
            border: none !important;
            border-radius: 12px !important;
            margin-top: 8px;
            margin-bottom: 8px;
            cursor: pointer;
        }
        </style>
    '''
    st.markdown(btn_css, unsafe_allow_html=True)
    img_width = 300
    cols = st.columns([1,2,1])
    with cols[1]:
        st.image("images/map4.png", width=img_width)
        st.button("길찾기 종료", key="end_route")



#화재상황
def page_detail():
    def img_to_base64(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img_path = "images/detail_image.png"
    img_base64 = img_to_base64(img_path)

    st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

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

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        if st.button("자세히 알아보기", use_container_width=True):
            st.session_state.page = "cctv_page"  # 변경
        if st.button("홈으로 돌아가기", use_container_width=True):
            st.session_state.page = "map_detail"  # 변경
#세부사항
def page_cctv():
    def img_to_base64(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    cctv_img_path = "images/cctv_img.jpg"
    cctv_img_base64 = img_to_base64(cctv_img_path)

    st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

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

    with st.container():
        st.markdown('<div class="button-box">', unsafe_allow_html=True)
        if st.button("근방 1km에 공유하기"):
            st.success("반경 1km내 해당 앱을 이용 중인 사람들에게 공유되었습니다")
        if st.button("공유 메뉴"):
            st.session_state.page = "fire"  # 변경
        st.markdown('</div>', unsafe_allow_html=True)

def set_background(image_path, size="contain"):
    with open(image_path, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: {size};
        background-position: center top;
        background-repeat: no-repeat;
        background-color: white;
        min-height: 100vh;
    }}
    .fixed-bottom-btn {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100vw;
        background:transparent;
        color: white;
        text-align: center;
        padding-bottom: 32px;
        z-index: 1000;
    }}
    .fixed-bottom-btn button {{
        width: 320px;
        height: 56px;
        border-radius: 16px;
        background-color: transparent;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin: 0 auto;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def page_lock():
    set_background("images/lock_bg.png", "contain")
    st.markdown('<div class="fixed-bottom-btn">', unsafe_allow_html=True)
    if st.button("알림 확인", key="noti_btn"):
        st.session_state.page = "main_logo"
    st.markdown('</div>', unsafe_allow_html=True)

def page_main():
    set_background("images/main_bg.png", "contain")
    st.markdown('<div class="fixed-bottom-btn">', unsafe_allow_html=True)
    if st.button("다음", key="main_next_btn"):
        st.session_state.page = "map_detail"
    st.markdown('</div>', unsafe_allow_html=True)

def page_main_nonfire():
    set_background("images/main_bg.png", "contain")
    st.markdown('<div class="fixed-bottom-btn">', unsafe_allow_html=True)
    if st.button("다음", key="main_next_btn"):
        st.session_state.page = "not_fire_detail"
    st.markdown('</div>', unsafe_allow_html=True)

# 비화재상황 관련 함수
# 화재 상황 아님 안내 페이지
def page_not_fire():
    st.markdown('<div style="text-align:center; font-size:1.3em; font-weight:bold; color:#1976d2; margin-top:60px;">화재 상황이 아닙니다.</div>', unsafe_allow_html=True)

def page_map_nonfire():
    # 상단 안내/버튼
    st.markdown("""
        <div style='
            width: 100%%;
            max-width: 400px;
            margin: 0 auto 10px auto;
            padding: 12px 0 8px 0;
            background: linear-gradient(90deg, #FFED8B 0%, #FFB88C 100%);
            border-radius: 16px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            color: #444;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        '>
            화재 신고하기<br>
            <span style='font-size:15px; font-weight:normal;'>비화재 상황 지도/메인 페이지입니다.</span>
        </div>
    """, unsafe_allow_html=True)

    # 지도 이미지 중앙 정렬
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/11.png", use_container_width=True)
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # 버튼 중앙 정렬
        if st.button("화재 신고하기", key="fire_report_btn", use_container_width=True):
            st.session_state.page = "report"

        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("대피소 찾기", key="shelter_btn", use_container_width=True):
            st.success("대피소 찾기 기능이 실행됩니다.")
            st.session_state.page = "recommend"

        st.image(IMG_TEST, use_container_width=True)
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        

def page_report():
    keypad_buttons = "".join([
        f'<button disabled style="font-size:24px;padding:15px 0;border-radius:12px;border:2px solid #ff3b30;background:white;color:#ff3b30;font-weight:bold;cursor:pointer;">{x}</button>' 
        for x in ["1","2","3","4","5","6","7","8","9","*","0","#"]
    ])
    
    st.markdown(f"""
    <div style="display: flex; justify-content: center;">
      <div style="
        max-width: 400px;
        width: 100%%;  <!-- %%로 변경 -->
        margin: 60px auto 0 auto;
        padding: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;">
        <div style="font-size: 48px; font-weight: bold; margin-bottom: 20px; letter-spacing: 10px; border: 2px solid #ff3b30; border-radius: 12px; padding: 10px 0; color: #ff3b30; user-select: none;">119</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 20px;">
            {keypad_buttons}  <!-- f-string으로 직접 삽입 -->
        </div>
        <button style="width: 100%%; padding: 15px 0; background-color: #ff3b30; color: white; font-size: 24px; font-weight: bold; border: none; border-radius: 18px; cursor: pointer; margin-bottom: 10px;" disabled>
            119로 전화신고하기
        </button>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 뒤로가기 버튼 (Streamlit으로 구현)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← 뒤로가기", key="back_to_main", use_container_width=True):
            st.session_state.page = "not_fire_detail"