
import cv2
import mediapipe as mp

count_fing = 0
Hand = "None"
Finger1 = "Thumb:Fold"
Finger2 = "Index Finger:Fold"
Finger3 = "Middle Finger:Fold"
Finger4 = "Ring Finger:Fold"
Finger5 = "Little Finger:Fold"
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 5:
                    id5 = int(id)
                    cx5 =cx
                if id == 9:
                    id9 = int(id)
                    cx9 =cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 =cy
            if cx5 > cx9:
                Hand="Right Hand"
                if cx4 > cx3:Finger1 = "Thumb:Thumbs up"
                else:Finger1 = "Thumb:Fold"
                if cy6 > cy8:Finger2 = "Index Finger:Thumbs up"
                else:Finger2 = "Index Finger:Fold"
                if cy10 > cy12:Finger3 = "Middle Finger:Thumbs up"
                else:Finger3 = "Middle Finger:Fold"
                if cy14 > cy16:Finger4 = "Ring Finger:Thumbs up"
                else:Finger4 = "Ring Finger:Fold"
                if cy18 > cy20:Finger5 = "Little Finger:Thumbs up"
                else:Finger5 = "Little Finger:Fold"
            else:
                Hand="Left Hand"
                if cx4 < cx3:Finger1 = "Thumb:Thumbs up"
                else:Finger1 = "Thumb:Fold"
                if cy6 > cy8:Finger2 = "Index Finger:Thumbs up"
                else:Finger2 = "Index Finger:Fold"
                if cy10 > cy12:Finger3 = "Middle Finger:Thumbs up"
                else:Finger3 = "Middle Finger:Fold"
                if cy14 > cy16:Finger4 = "Ring Finger:Thumbs up"
                else:Finger4 = "Ring Finger:Fold"
                if cy18 > cy20:Finger5 = "Little Finger:Thumbs up"
                else:Finger5 = "Little Finger:Fold"

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.putText(img, str(Hand), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(img, str(Finger1), (10, 100), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)
    cv2.putText(img, str(Finger2), (10, 130), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)
    cv2.putText(img, str(Finger3), (10, 160), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)
    cv2.putText(img, str(Finger4), (10, 190), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)
    cv2.putText(img, str(Finger5), (10, 220), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
