from ultralytics import YOLO

# 1. 모델 로드 (모듈 로딩 시 1회만 실행)
model = YOLO('best.pt')  # ⚠️ 실제 모델 경로로 변경

def detect_fire(image_path):
    """
    이미지에서 화재 또는 연기 감지 시 True, 아니면 False 반환

    Args:
        image_path (str): 분석할 이미지 파일 경로

    Returns:
        bool: 화재 또는 연기 감지 시 True, 미감지 시 False
    """
    results = model(image_path, conf=0.25)

    for result in results:
        names = result.names  # 클래스 이름 매핑
        for box in result.boxes:
            cls_id = int(box.cls.item())
            label = names[cls_id]
            if label == 'fire':   # ⚠️ 모델의 클래스명에 맞게 수정
                print(f"🚨 화재 감지! 신뢰도: {box.conf.item():.2f}")
                return True
            if label == 'smoke':  # ⚠️ 모델의 클래스명에 맞게 수정
                print(f"🚨 연기 감지! 신뢰도: {box.conf.item():.2f}")
                return True

    print("✅ 화재 미감지: 안전한 이미지")
    return False

# 직접 실행 테스트 (모듈로 쓸 때는 무시됨)
if __name__ == "__main__":
    test_image = "images/test_img_1.jpg"
    print("화재 감지 결과:", detect_fire(test_image))
