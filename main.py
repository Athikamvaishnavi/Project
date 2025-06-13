import cvzone
import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)

        if fingers == [1, 0, 0, 0, 0]:
            print("Move Left")
            pyautogui.press('left')

        elif fingers == [0, 0, 0, 0, 1]:
            print("Move Right")
            pyautogui.press('right')

        elif fingers == [1, 1, 1, 1, 1]:
            print("Jump")
            pyautogui.press('up')

        elif fingers == [0, 0, 0, 0, 0]:
            print("Skid")
            pyautogui.press('down')

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
