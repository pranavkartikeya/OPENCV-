import cv2
import mediapipe as mp
import pyfirmata2
import time
import math

board = pyfirmata2.Arduino("COM6")
ledpin = board.get_pin("d:6:p")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)
while True:

    success,frame = cap.read()
    if success:
        RGB_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            handLandmarks = result.multi_hand_landmarks[0]
            thumbTip = handLandmarks.landmark[4]
            indexTip = handLandmarks.landmark[5]
            distance = math.sqrt((thumbTip.x - indexTip.x)**2 + (thumbTip.y - indexTip.y)**2)
            print(distance)
            if distance > 0.2555:

                ledpin.write(distance)
            else:
                ledpin.write(0)

            cv2.imshow("capture image",frame)
            if  cv2.waitKey(1) & 0xFF == ord('q'):
                break
