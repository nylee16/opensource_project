# Project Name

### 재난 취약계층인 노인을 위한 음성·이미지 기반 화재 감지 및 대피 안내 서비스
### (Voice and Image-based Fire Detection and Evacuation Guidance Service for Disaster-Vulnerable Elderly)


팀원 : <br>
•이나연(2414115, nylee16) <br>
•양서연(2415485, bigfish951)<br>
•윤소윤(2415409, Sso1002) <br>
•이은진(2572307, xxnjxn)<br>

소속 : 
숙명여자대학교 (Sookmyung Women's University) 인공지능공학부 (Department of Artificial Intelligence Engineering)<br>
오픈소스프로그래밍 과목 기말 프로젝트 (Final Project for the Open-Source Programming Course)


## Project Overview (프로젝트 개요)
본 프로젝트는 Hugging Face의 Whisper 음성 인식 모델과 YOLOv8 이미지 인식 모델을 결합하여 음성 및 이미지 데이터를 동시에 분석하는 화재 감지 시스템. 두 모델의 결과를 융합하여 정확한 화재 감지를 목표로 함.
This project is a fire detection system that combines Hugging Face’s Whisper speech recognition model and the YOLOv8 image recognition model to simultaneously analyze audio and image data. The results of the two models are fused to achieve accurate fire detection.

프로젝트 배경 :
산불 등 화재 발생 시, 고령층과 장애인, 어린이 등 재난 취약계층의 피해가 집중되고 있음. 2020년부터 2024년 6월까지 전체 화재 사상자의 36.4%가 취약계층임. 실제로 2025년 3월 경북 산불에서는 사망자의 대부분이 60~80대 노인이었고, 일부는 대피 안내 방송을 듣지 못하거나 이동이 어려워 제때 피하지 못함. 따라서 우리는 거동이 불편한 고령층이 신속하고 안전하게 대피할 수 있도록, 화재 감지와 빠른 알림을 제공하는 전용 앱을 개발하기로 함.
During wildfires and other fire incidents, vulnerable groups such as the elderly, disabled, and children suffer disproportionately. Therefore, we developed a dedicated app to provide fire detection and rapid alerts, enabling elderly individuals with limited mobility to evacuate quickly and safely.<br>

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

---
1,2 : 화재 / 3,4 : 비화재

![image](https://github.com/user-attachments/assets/b005813c-2ad6-489a-ba3f-3bb6dc935b94) ![result_1750434153](https://github.com/user-attachments/assets/00c47a3a-ea96-41df-b06c-c638956d6267) <br>
![image](https://github.com/user-attachments/assets/43c4fc12-738b-4b2c-af7a-fcfb190388a9) ![image](https://github.com/user-attachments/assets/0a75899a-8053-45ee-af7d-c9716338a3f5)


---

• 화재
불꽃의 색상, 연기, 밝기 변화 등 시각적 패턴을 인식하여 화재로 판단함.<br>
• 비화재
색상은 유사할 수 있으나, 불꽃이나 연기 특유의 패턴이 없으면 비화재로 분류함.

---

화재/비화재 음성 분류 결과
모델은 파인튜닝된 Whisper 모델(SungBeom/whisper-small-ko)을 활용해 입력된 음성을 
화재와 비화재로 구분함.
(위: 화재, 아래: 비화재)

---

![image](https://github.com/user-attachments/assets/5cde1f12-3f12-413c-ac8c-324ff9c86eaa) 
![image](https://github.com/user-attachments/assets/bb6d30ce-b294-4b1d-8c1b-df7cf771ad54)


---

• 화재
음성 파일에서 화재 키워드(‘불’, ‘비상’, ‘대피’ 등) 또는 화재 관련 음성(경보음 등)이 인식되면 화재 상황으로 판단함. <br>
• 비화재
음성 파일에서 화재 키워드(‘불’, ‘비상’, ‘대피’ 등) 또는 화재 관련 음성(경보음 등)이 인식되지 않으면 비화재 상황으로 판단함.

##Folder Structure (폴더 구조)
Opensource_project/<br>
├── 2414115/<br>
│   ├── fire_image_detection모델학습<br>
│   └── fire_image_detection모델학습 ver2<br>
├── 2415409/<br>
├── 2415485/<br>
│   ├── backup-test<br>
│   └── images<br>
├── 2572307/<br>
├── final_result/<br>
│   ├── images<br>
│   ├── pages <br>
│   └── voice<br>
├── raw_video/<br>
├── .gitattributes<br>
├── LICENSE<br>
├── README.md<br>
├── Untitled1.ipynb<br>
├── fire_case_sampling.ipynb<br>
├── firedetection.v6i.yolov8.zip<br>
├── opensource_project_plan(2...<br>
├── wav2vec2,9_raw.ipynb<br>

---

## Test Instructions (테스트 방법)

• 이미지 모델 활용 방법 (How to utilize the image-based fire detection model)<br>
=> opensource_project/2414115/fire_image_detection모델학습 ver2/2nd_훈련result 기반 설명<br>
1. 제공된 모델 파일(best.pt)과 원하는 이미지를 지정된 경로에 저장하세요. Save the provided model file (best.pt) and your desired image to the specified directory<br>

2. 필수 패키지를 설치해주세요.<br>
pip install -r requirements.txt<br>

3. 코드 내 경로 설정. test.py에서 각 파일의 경로를 원하는 이미지 파일 경로에 맞춰 수정하세요. Set the file paths in the code.<br>
#test.py<br>
image_path = "test1.jpg"  # 테스트 이미지 로컬 경로

4. 터미널을 하나 열어주세요. Open a terminal.<br>
• 터미널(terminal) : test.py 실행

5. 동작 방식<br>
• best.pt 경로에서 YOLOv8 화재 감지 모델을 불러옵니다. Load the YOLOv8 fire detection model from the best.pt path.<br>
• 원하는 이미지에서 fire 또는 smoke 탐지를 수행합니다. (신뢰도 ≥ 0.25 감지시 성공) Perform fire or smoke detection on your desired image.<br>
• 감지 성공 (detection sucess) : True 반환(return) + 경고 메시지 (+ 결과 이미지 제시 또는 저장) (warning message)<br>
• 감지 실패 (detection failure) : False 반환(return) + 안전 메시지 (safety message)

---

• 음성 모델 활용 방법 (How to utilize the voice-based fire detection model)<br>
=>  opensource_project/2415485/ 기반 설명<br>
1. 원하는 음성 데이터와 레이블을 준비하거나, 제공된 학습용 파일을 지정된 경로에 저장하세요. Prepare your own audio files and transcripts, or use the provided training files by placing them in the designated directories.

2. 필수 패키지를 설치해주세요.<br>
	pip install -r requirements.txt

3. Hugging Face 로그인 토큰을 입력하세요. Enter your Hugging Face access token in the script.

4. 학습 스크립트를 실행하세요. Run the training script.<br>
python 3rd_upload.py

5. 동작 방식<br>
• labels.csv의 내용을 기반으로, 오디오 파일 경로를 사용하여 학습용 데이터셋을 생성합니다. labels.csv is parsed to generate a training dataset using valid local audio paths.<br>
• Whisper processor를 통해 음성과 텍스트를 전처리합니다. Audio and transcript data are preprocessed using the Whisper processor.<br>
• Hugging Face에서 SungBeom/whisper-small-ko 모델을 불러와 fine-tuning을 진행합니다. The model SungBeom/whisper-small-ko from Hugging Face is fine-tuned using the dataset.<br>
• 학습이 완료되면 ./whisper-output 폴더에 체크포인트가 저장됩니다. After training, checkpoints are saved in the ./whisper-output directory.

---

• UI 적용 방법 / 음성, 이미지 동시 활용 (How to implement the UI with combined voice and image detection)<br>
=> opensource_project/final_result directory 기반 설명<br>
1. 제공된 모델 파일을 지정된 경로에 저장하세요. Save the provided model file (best.pt) and your desired image to the specified directory

2. 필수 패키지를 설치해주세요.<br>
pip install -r requirements.txt

3. 코드 내 경로 설정. streamlit_ui_main.py의 check_fire 함수에서 테스트할 음성 및 이미지 파일 경로에 맞춰 수정하세요. Set the file paths in the code.<br>
#streamlit_ui_main.py<br>
#테스트 음성, 이미지 로컬 경로<br>
json={"audio_path": "C:/Users/USER/sm.opensource/전체/voice/tts_1.wav"}<br>
image_path = "images/test_img_2.jpg"

4. VScode에서 터미널을 두 개 열어주세요. Open two terminals in VS Code.<br>
• 첫 번째 터미널(1st) : python fire_detection_api.py 실행 (음성 감지 실행)<br>
• 두 번째 터미널(2nd) : streamlit run streamlit_ui_main.py 실행 

5. 동작 방식<br>
• fire_detection_api.py : 음성 모델을 실시간으로 감지 (The voice model performs real-time monitoring)<br>
• fire_image_detection.py : 이미지 모델 결과(true/flase) 값을 반환합니다. (Returns a true/false value indicating fire detection)<br>
• streamlit_ui_main : 두 모델 결과 통합 / streamlit 사이트에서 화재 감지 시작 버튼을 누르면 화재 감지가 시작되고 상황에 맞는 UI 서비스가 구현됩니다.
(Pressing the 화재 감지 시작 button on the Streamlit site initiates detection and launches a context-aware UI service)


## Contribution Guide (기여방법) 
1. 이슈 등록
버그, 개선사항, 새로운 기능 제안 등은 Issues에  등록해 주세요.
이슈 작성 시 발생 환경/재현 방법/스크린샷 등 상세한 설명을 부탁드립니다.

2. 포크 및 브랜치 생성
저장소를 본인 계정으로 Fork합니다.
새로운 기능/수정 사항은 반드시 별도의 브랜치에서 작업해 주세요. (예: git checkout -b feature/기능명)

3. 코드 작성 및 커밋
PEP8 가이드에 맞춰 코드를 작성해주세요.
함수/클래스에는 간단한 주석과 docstring을 추가해 주세요.
커밋 메시지는 명확하게 작성해 주세요.

4. Pull Request(PR 생성)
작업이 끝나면 원본 저장소에 Pull Request를 생성해 주세요.
PR 설명란에 변경 내용, 목적, 테스트 결과 등을 구체적으로 작성해 주세요.


## License (라이선스)
MIT License

Copyright (c) 2025 이나연(2414115, nylee16), 윤소윤(2415409, Sso1002), 
양서연(2415485, bigfish951), 이은진(2572307, xxnjxn), 숙명여자대학교 Sookmyung Women's University

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact (문의, 작성자 정보)
숙명여자대학교 (Sookmyung Women's University)

Name : 이나연 (Nayeon Lee)
Email : nylee16@sookmyung.ac.kr

Name : 양서연
Email : 2415485@sookmyung.ac.kr

Name : 윤소윤
Email : ysy2415409@sookmyung.ac.kr

Name : 이은진
Email : ejlee917@seoultech.ac.kr

