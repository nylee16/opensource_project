# opensource_project
2414115 이나연 2415485 양서연 2415409 윤소윤 2572307 이은진 / 오픈소스프로그래밍 프로젝트

# Project Name
##재난 취약계층인 노인을 위한 음성·이미지 기반 화재 감지 및 대피 안내 서비스
(Voice and Image-based Fire Detection and Evacuation Guidance Service for Disaster-Vulnerable Elderly)

팀원 : 
•이나연(2414115, nylee16) 
•양서연(2415485, bigfish951)
•윤소윤(2415409, Sso1002) 
•이은진(2572307, xxnjxn)

소속 : 
숙명여자대학교 (Sookmyung Women's University) 인공지능공학부 (Department of Artificial Intelligence Engineering)
오픈소스프로그래밍 과목 기말 프로젝트 (Final Project for the Open-Source Programming Course)


## Project Overview (프로젝트 개요)
본 프로젝트는 Hugging Face의 Whisper 음성 인식 모델과 YOLOv8 이미지 인식 모델을 결합하여 음성 및 이미지 데이터를 동시에 분석하는 화재 감지 시스템. 두 모델의 결과를 융합하여 정확한 화재 감지를 목표로 함.
This project is a fire detection system that combines Hugging Face’s Whisper speech recognition model and the YOLOv8 image recognition model to simultaneously analyze audio and image data. The results of the two models are fused to achieve accurate fire detection.

프로젝트 배경 :
산불 등 화재 발생 시, 고령층과 장애인, 어린이 등 재난 취약계층의 피해가 집중되고 있음. 2020년부터 2024년 6월까지 전체 화재 사상자의 36.4%가 취약계층임. 실제로 2025년 3월 경북 산불에서는 사망자의 대부분이 60~80대 노인이었고, 일부는 대피 안내 방송을 듣지 못하거나 이동이 어려워 제때 피하지 못함. 따라서 우리는 거동이 불편한 고령층이 신속하고 안전하게 대피할 수 있도록, 화재 감지와 빠른 알림을 제공하는 전용 앱을 개발하기로 함.
During wildfires and other fire incidents, vulnerable groups such as the elderly, disabled, and children suffer disproportionately. Therefore, we developed a dedicated app to provide fire detection and rapid alerts, enabling elderly individuals with limited mobility to evacuate quickly and safely.


## Installation & How to Run (설치 및 실행 방법)
저장소 클론 (Repository clone)
git clone https://github.com/nylee16/opensource_project.git) 
cd opensource_project
파이썬 / conda 가상환경 생성 및 활성화 (creating and activating a Python / conda Virtual Environment)
종속성 설치(streamlit, torch, transformers (Whisper), YOLOv8)

## Features / Usage (주요 기능 및 사용법)
• 음성 기반 화재 감지 (Voice-based Fire Detection)
Whisper 모델이 음성 파일에서 화재 관련 음성(예: "불이야", 경보음 등)을 인식함.
The Whisper model recognizes fire-related sounds from audio files.

• 이미지 기반 화재 감지 (Image-based Fire Detection)
YOLOv8 모델이 이미지에서 불꽃, 연기 등 화재 징후를 감지함.
The YOLOv8 model detects signs of fire, such as flames and smoke, in images.

→ 음성과 이미지 두 데이터를 동시에 분석하여, 한 쪽에서 놓칠 수 있는 상황도 보완함. 두 신호를 결합해 오경보를 줄이고 실제 화재만 빠르게 인식하게 함.

• UI 활용
음성과 이미지 기반 화재감지를 통해 상황에 맞는 UI 서비스 제공

• 대피 안내
화재 발생 시 UI 화면에 맞춤형 대피 경로 안내 및 행동 요령 메시지 제공

• 발전 가능성
외부 장치와 연동하여 데이터 수집 및 분석 가능
실시간 데이터 기반 예측 자동화 기능 확장 가능

## Examples(Screenshots)
UI 디자인 노션 링크:
https://www.notion.so/UI-21ac6b602efe8016b686db2182a901ca?source=copy_link

화재/비화재 이미지 분류 결과
모델은 학습된 딥러닝 알고리즘(YOLOv8)을 활용해 입력된 이미지를 화재와 비화재로 구분함. 
1,2 : 화재 / 3,4 : 비화재

![image](https://github.com/user-attachments/assets/b005813c-2ad6-489a-ba3f-3bb6dc935b94) ![result_1750434153](https://github.com/user-attachments/assets/00c47a3a-ea96-41df-b06c-c638956d6267)
![image](https://github.com/user-attachments/assets/43c4fc12-738b-4b2c-af7a-fcfb190388a9) ![image](https://github.com/user-attachments/assets/a045e1d5-f785-45df-a601-14af168e2e3a)

• 화재
불꽃의 색상, 연기, 밝기 변화 등 시각적 패턴을 인식하여 화재로 판단함.

• 비화재
색상은 유사할 수 있으나, 불꽃이나 연기 특유의 패턴이 없으면 비화재로 분류함.


