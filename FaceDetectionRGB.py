import cv2
from cvzone.FaceDetectionModule import  FaceDetector
from cvzone.SerialModule import SerialObject
cap = cv2.VideoCapture(0)
arduino = SerialObject("COM3")
detector = FaceDetector(minDetectionCon=0.5) #if 1 the only when 100% it will detect the faces

while True:
    success, img = cap.read()
    img,bboxs = detector.findFaces(img)

    if bboxs:
          arduino.sendData([0,1,0])
    else :
        arduino.sendData([1,0,0])

    cv2.imshow("Image",img)
    cv2.waitKey(1)

