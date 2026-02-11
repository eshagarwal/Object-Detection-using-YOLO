from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame)[0]
    annoted = results.plot()
    cv2.imshow('YOLOv8', annoted)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()