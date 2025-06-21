"""
from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/firedetection_v8/weights/best.pt')
results = model('test_image.jpg')

#결과 시각화
cv2.imshow('Detection', results[0].plot())
cv2.waitKey(0)
"""
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
"""
# 수정된 코드2
from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO('runs/detect/firedetection_v8/weights/best.pt')

# 이미지 예측
results = model.predict('test_image.jpg')

# 결과 시각화 및 표시
img = results.plot()  # results[0].plot() 대신 results.plot() 사용 (단일 이미지일 때)
cv2.imshow('Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
