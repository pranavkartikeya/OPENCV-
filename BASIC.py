import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
detector = FaceDetector()
cap=cv2.VideoCapture(0)
arduino = SerialObject("COM6")
while True:
    success,frame=cap.read()
    frame,bboxs = detector.findFaces(frame)
    if bboxs:
         arduino.sendData([1])
    else :
         arduino.sendData([0])
    cv2.imshow('frame',frame)
    cv2.waitKey(1)