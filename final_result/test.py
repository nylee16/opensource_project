import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: contain;
        background-position: center top;
        background-repeat: no-repeat;
        background-color: white;
        min-height: 100vh;
    }}
    /* Streamlit 버튼 컨테이너 위치 조정 */
    [data-testid="stVerticalBlock"] > div:nth-of-type(1) {{
        position: absolute;
        top: 560px; /* 배경 이미지의 버튼 위치에 맞게 조정 */
        left: 50%;
        transform: translateX(-50%);
        width: 357px;
        z-index: 10;
    }}
    /* 버튼 스타일 (완전 투명, 테두리 없음) */
    [data-testid="stVerticalBlock"] > div:nth-of-type(1) button {{
        width: 100%;
        height: 56px;
        border-radius: 16px;
        background-color: transparent;
        border: none;
        color: transparent;
        cursor: pointer;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "lock"

def go_to_main():
    st.session_state.page = "main"

if st.session_state.page == "lock":
    set_background("images/lock_bg.png")  # 배경 이미지

    # Streamlit 버튼 (완전 투명, 알림창 위치에 맞춤)
    if st.container().button(" ", key="noti_btn", use_container_width=True):
        go_to_main()

elif st.session_state.page == "main":
    set_background("images/main_bg.png")  # 메인화면 배경 이미지
    # 아무 내용도 출력하지 않음
