from ultralytics import YOLO
import cv2
import time

# 1. 훈련된 모델 로드 (사용자 모델 경로 지정)
model = YOLO('best.pt')  # 사용자의 best.pt 경로로 변경

# 2. 이미지 추론 함수
def classify_fire(image_path):
    # 이미지 로드 및 추론
    results = model(image_path, conf=0.25)  # conf: 최소 신뢰도
    
    # 결과 시각화 (선택사항)
    annotated_img = results[0].plot()

    #결과 화면 표시=> 주석처리. 
    #cv2.imshow('Detection', annotated_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # 이미지 저장 (화면 표시 대체)
    output_path = f"result_{int(time.time())}.jpg"  # 타임스탬프 추가
    cv2.imwrite(output_path, annotated_img)
    print(f"결과 이미지 저장됨: {output_path}")
    
    # 3. 화재 감지 로직
    for result in results:
        names = result.names  # 클래스 이름 매핑
        for box in result.boxes:
            cls_id = int(box.cls.item())  # 클래스 ID
            conf = box.conf.item()  # 신뢰도
            
            # 클래스 이름이 'fire'인 경우 (모델 훈련 시 클래스명에 따라 변경)
            if names[cls_id] == 'fire':  # ⚠️ 사용자 모델의 클래스명 확인
                print(f"🚨 화재 감지! 신뢰도: {conf:.2f}")
                return True
            # 클래스 이름이 'smoke'인 경우 (모델 훈련 시 클래스명에 따라 변경)
            if names[cls_id] == 'smoke':  # ⚠️ 사용자 모델의 클래스명 확인
                print(f"🚨 화재 경고! 연기가 감지되었습니다! 신뢰도: {conf:.2f}")
                return True
    
    
    print("✅ 화재 미감지: 안전한 이미지")
    return False

# 4. 실행 예시
image_path = "test9.jpg"  # 테스트 이미지 경로
is_fire = classify_fire(image_path)

# 5. 추가 처리
if is_fire:
    # 화재 감지 시 추가 작업 (알림 전송 등)
    print("경고: 화재 발생 가능성!")