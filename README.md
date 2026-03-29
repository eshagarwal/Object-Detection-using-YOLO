## 🎯 Real-Time Object Detection with YOLOv8

A real-time object detection application using YOLOv8 and OpenCV to detect and visualize objects through a webcam feed.

## 📌 Overview

This project uses the Ultralytics YOLOv8 model to perform real-time object detection on live video captured from your system’s webcam. Detected objects are highlighted with bounding boxes and labels in an interactive window.

## 🛠️ Technologies Used
- Python
- YOLOv8 (Ultralytics)
- OpenCV (cv2)

## ⚙️ Installation
1️⃣ Clone the repository
```
git clone <your-repo-url>
cd object-detection-yolo
```

2️⃣ Install dependencies
```
pip install ultralytics opencv-python
```

▶️ How to Run
```
python objdet.py
```
- A webcam window will open
- Detected objects will be highlighted in real-time
- Press q to exit

## 🧠 How It Works

- Loads pre-trained YOLOv8 model
- Captures video frames from webcam
- Runs object detection on each frame
- Draws bounding boxes and labels
- Displays annotated frames in real-time
