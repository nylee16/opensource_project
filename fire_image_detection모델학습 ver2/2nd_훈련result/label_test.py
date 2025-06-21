from ultralytics import YOLO

model = YOLO('best.pt')
print(model.names)  # 클래스 목록 출력