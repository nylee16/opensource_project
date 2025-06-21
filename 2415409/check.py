import base64
import streamlit as st

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
    /* Streamlit 버튼 위치 조정 */
    [data-testid="stVerticalBlock"] > div:nth-of-type(1) {{
        position: absolute;
        top: 48px;
        left: 50%;
        transform: translateX(-50%);
        width: 190vw;
        max-width: 340px;
        z-index: 20;
    }}
    /* 버튼 스타일 */
    [data-testid="stVerticalBlock"] > div:nth-of-type(1) button {{
        width: 100%;
        height: 48px;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 50%, #FF8E53 100%);
        border-radius: 18px;
        font-weight: 600;
        font-size: 18px;
        color: white;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to_report():
    st.session_state.page = "report"

def go_to_main():
    st.session_state.page = "main"

if st.session_state.page == "main":
    set_background("11.png")  # 배경 이미지

    # Streamlit 버튼(화재 신고하기) 위치 조정을 위해 컨테이너 사용
    st.container().button(
        "화재 신고하기",
        key="fire_report_btn",
        use_container_width=True,
        help="119 신고 화면으로 이동"
    )
    if st.session_state.get("fire_report_btn"):
        go_to_report()

elif st.session_state.page == "report":
    # 119 신고 화면 구성
    st.markdown("""
    <style>
    .report-container {
        max-width: 400px;
        margin: 60px auto 0 auto;
        padding: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
    }
    .phone-display {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
        letter-spacing: 10px;
        border: 2px solid #ff3b30;
        border-radius: 12px;
        padding: 10px 0;
        color: #ff3b30;
        user-select: none;
    }
    .keypad {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-bottom: 20px;
    }
    .keypad button {
        font-size: 24px;
        padding: 20px 0;
        border-radius: 12px;
        border: 2px solid #ff3b30;
        background: white;
        color: #ff3b30;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .keypad button:hover {
        background-color: #ff3b30;
        color: white;
    }
    .call-button {
        width: 100%;
        padding: 15px 0;
        background-color: #ff3b30;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border: none;
        border-radius: 18px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .call-button:hover {
        background-color: #cc2a24;
    }
    .back-button {
        margin-top: 15px;
        background: #6c757d;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 15px;
        font-size: 14px;
        cursor: pointer;
    }
    </style>
    <div class="report-container">
        <div class="phone-display">119</div>
        <div class="keypad">
            <button>1</button>
            <button>2</button>
            <button>3</button>
            <button>4</button>
            <button>5</button>
            <button>6</button>
            <button>7</button>
            <button>8</button>
            <button>9</button>
            <button>*</button>
            <button>0</button>
            <button>#</button>
        </div>
        <button class="call-button">119로 전화신고하기</button>
        <button class="back-button" id="back_btn">← 뒤로가기</button>
    </div>
    """, unsafe_allow_html=True)

    # 뒤로가기 버튼 클릭 감지
    if st.button("뒤로가기", key="back_to_main"):
        go_to_main()
    
    # 자바스크립트로 HTML 뒤로가기 버튼 연결
    st.markdown(
        """
        <script>
        const backBtn = document.getElementById('back_btn');
        if(backBtn) {
            backBtn.addEventListener('click', () => {
                window.parent.document.querySelector('button[key="back_to_main"]').click();
            });
        }
        </script>
        """,
        unsafe_allow_html=True
    )


