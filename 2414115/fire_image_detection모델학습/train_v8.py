from ultralytics import YOLO
import torch

if __name__ == '__main__':
    # 모델 로드
    model = YOLO('yolov8s.pt')
    
    # 학습 설정
    results = model.train(
        data='firedetection-6/data.yaml',
        epochs=100,
        batch=16,
        imgsz=640,
        device=0,
        name='firedetection_v8',
        workers=0  # 멀티프로세싱 비활성화 (문제 지속 시)
    )