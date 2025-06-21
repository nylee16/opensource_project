import streamlit as st
from streamlit_folium import st_folium
import folium
import os

def page_map_detail():
    st.set_page_config(initial_sidebar_state="collapsed")

    # 1. 상단 색상바 이미지 (가운데 정렬)
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image("images/risk_level.png", width=450)

        st.markdown("""
        <style>
        .stButton > button {
            width: 440px !important;
            max-width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

        # 지도 바로 밑에 페이지 이동 버튼 2개만 남김
        if st.button("화재 상황 자세히 알아보기", use_container_width=True):
            st.session_state.page = "detail_page"
        if st.button("대피소 찾기", use_container_width=True):
            st.session_state.page = "shelter_search"
        
    with col2:
        # folium 지도 생성 및 요소 추가
        thunder_mountain = [36.6685, 128.9346]
        user_location = [36.6700, 128.9320]
        m = folium.Map(location=thunder_mountain, zoom_start=15, control_scale=True)

        folium.Circle(
            location=thunder_mountain,
            radius=180,
            color="#fa6c6c",
            fill=True,
            fill_opacity=0.35,
            popup="산불 발생지점"
        ).add_to(m)

        fire_icon_path = os.path.abspath("images/fire_icon.png")
        folium.Marker(
            location=thunder_mountain,
            icon=folium.CustomIcon(fire_icon_path, icon_size=(38, 38)),
            tooltip="산불"
        ).add_to(m)

        folium.CircleMarker(
            location=user_location,
            radius=10,
            color="#3ba9f4",
            fill=True,
            fill_color="#3ba9f4",
            fill_opacity=1
        ).add_to(m)

        folium.PolyLine(
            locations=[user_location, thunder_mountain],
            color="#fa6c6c",
            weight=18,
            opacity=0.18
        ).add_to(m)

        mid_point = [
            (user_location[0] + thunder_mountain[0]) / 2,
            (user_location[1] + thunder_mountain[1]) / 2
        ]
        fire_icon_small_path = os.path.abspath("images/fire_icon_small.png")
        folium.Marker(
            location=mid_point,
            icon=folium.CustomIcon(fire_icon_small_path, icon_size=(28, 28)),
            tooltip="산불 경로"
        ).add_to(m)

        # folium 지도 표시 (가운데 정렬)
        st_folium(m, width=440, height=700)

    

