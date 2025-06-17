"""
from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/firedetection_v8/weights/best.pt')
results = model('test_image.jpg')

#결과 시각화
cv2.imshow('Detection', results[0].plot())
cv2.waitKey(0)
"""
# 수정된 코드
from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/firedetection_v8/weights/best.pt')
results = model.predict('test_image.jpg')

# 결과 이미지 추출 및 표시
if len(results) > 0:
    plotted_img = results[0].plot()  # NumPy 배열 반환
    cv2.imshow('Detection', plotted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
