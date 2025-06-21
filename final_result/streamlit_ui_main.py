import streamlit as st
import requests
from streamlit_ui_function import (
    page_fire, page_share, page_map,
    page_recommend, page_navigation, page_not_fire, 
     page_detail, page_cctv, page_lock, page_main, page_main_nonfire,
     page_map_nonfire, page_report 
)
from fire_situation import page_map_detail
from fire_image_detection import detect_fire 


# 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "lock"
if "selected_contact" not in st.session_state:
    st.session_state.selected_contact = None
if "selected_message" not in st.session_state:
    st.session_state.selected_message = "실시간 대피 경로 보내기"

# 화재 감지 API 호출 함수 + 이미지
def check_fire():
    try:
        #음성
        response = requests.post(
            "http://localhost:5001/predict_path",
            json={"audio_path": "C:/Users/USER/sm.opensource/전체/voice/tts_1.wav"}
        )
        result = response.json()
        print("API 응답:", result)
        api_fire = result.get("situation") == "fire"

        #이미지 화재/비화재 구분
        image_path = "images/test_img_2.jpg"
        is_fire_detected = detect_fire(image_path)

        #OR로 음성과 이미지 연결
        if api_fire or is_fire_detected:
            print("경고: 화재 또는 연기 발생!")
            st.session_state.page = "lock"
        else:
            st.session_state.page = "not_fire_main"

    except Exception as e:
        print("API 호출 오류:", e)
        st.session_state.page = "not_fire"

# 메인 라우팅
if st.session_state.page == "start":
    st.title("화재 감지 테스트")
    if st.button("화재 감지 시작"):
        check_fire()
elif st.session_state.page == "lock":
    page_lock()
elif st.session_state.page == "main_logo":
    page_main()
elif st.session_state.page == "map_detail":
    page_map_detail()
elif st.session_state.page == "detail_page":
    page_detail()
elif st.session_state.page == "cctv_page":
    page_cctv()
elif st.session_state.page == "fire":
    page_fire()
elif st.session_state.page == "share":
    page_share()
elif st.session_state.page == "map":
    page_map()
elif st.session_state.page == "recommend":
    page_recommend()
elif st.session_state.page == "navigation":
    page_navigation()

elif st.session_state.page == "not_fire_main":
    page_main_nonfire()
elif st.session_state.page == "not_fire_detail":
    page_map_nonfire()
elif st.session_state.page == "report":
    page_report()
else:
    st.write("정상 상황입니다.")