import streamlit as st

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
        st.image("11.png", use_container_width=True)
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # 버튼 중앙 정렬
        if st.button("화재 신고하기", key="fire_report_btn", use_container_width=True):
            st.session_state.page = "report"

        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("대피소 찾기", key="shelter_btn", use_container_width=True):
            st.success("대피소 찾기 기능이 실행됩니다.")

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
            st.session_state.page = "main"


# 메인 라우팅
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    page_map_nonfire()
elif st.session_state.page == "report":
    page_report()
else:
    st.write("정상 상황입니다.")

