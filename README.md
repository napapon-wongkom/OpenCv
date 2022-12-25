#  OpenCv & Mediapipe FingerCheck
###### การทำงาน: เมื่อเริ่มต้นจะแสดงค่ามือเป็น none และนิ้วทั้งหมดจะแสดงเป็น fold คือหุบอยู่ และเมื่อพบมือบนกล้องจะแสดงว่ามือเป็นมือข้างไหนที่อยู่ในกล้อง และแสดงว่านิ้วไหนกำลังชูอยู่บ้าง โดยถ้าชูอยู่ให้แสดงเป็น Thumbs up แต่ถ้าหุบอยู่ให้แสดงเป็น Fold
###### ข้อจำกัด: จะจับภาพมือได้เฉพาะมือตั้งตรงเท่านั้น เนื่องจากเมื่อหมุนมือจะทำให้แกนที่ใช้ในการจำแนกนิ้วเปลี่ยนตาม และหากพลิกจากฝ่ามือไปเป็นหลังมือจะทำให้showเป็นมืออีกข้างแทน เนื่องจากเมื่อพลิกฝ่ามือskeletonที่trackบนมือจะเหมือนskeletonของอีกข้างหนึ่ง

```bash
# นำเข้าlibrary opencv & mediapipe
import cv2
import mediapipe as mp

#กำหนดตัวแปร
Hand = "None" #ตัวแปรแสดงมือ
Finger1 = "Thumb:Fold" #ตัวแปรนิ้วโป้ง
Finger2 = "Index Finger:Fold" #ตัวแปรนิ้วชี้
Finger3 = "Middle Finger:Fold"  #ตัวแปรนิ้วกลาง
Finger4 = "Ring Finger:Fold"  #ตัวแปรนิ้วนาง
Finger5 = "Little Finger:Fold" #ตัวแปรนิ้วก้อย
cap = cv2.VideoCapture(0) #ตัวแปรรับวิดีโอจากกล้อง

#ตัวแปรรับการแสดงมือของmediapipe
mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#loopใช้สำหรับตรวจจับมือและแสดงผล
while True: 
    success, img = cap.read() #ตัวแปรimgรับภาพจากตัวแปรcap
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #แปลงภาพBGRเป็นRGB
    results = hands.process(imgRGB) #รับค่าจากภาพRGBที่trackมือแล้ว

    if results.multi_hand_landmarks: #ให้ทำตามคำสั่งเมื่อตรวจพบมือ
        for handLms in results.multi_hand_landmarks: #ให้handLmsเป็นจุดต่างๆบนมือ
            for id, lm in enumerate(handLms.landmark): #ให้idเป็นค่าของจุดต่างๆบนมือ
                h, w, c = img.shape #กำหนดตัวแปรเก็บขนาดภาพ
                cx, cy = int(lm.x * w), int(lm.y * h)  #นำภาพมาแปลงเป็นพิกัดX,Y
                
                #กำหนดค่าตัวแปรแต่ละจุดบนนิ้วที่จะใช้ว่าให้ใช้ค่าจากแกนXหรือY
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
                    
            #กำหนดเขื่อนไขให้ทำเมื่อค่าแกนXของจุดที่5มากกว่าค่าแกนXของจุดที่9
            #ใช้จำแนกนิ้วมือ
            if cx5 > cx9:
                Hand="Right Hand" #ให้Handเป็นมือขวาเมื่อcx5>cx9(จำแนกมือ)
                
                #ส่วนจำแนกนิ้ว
                if cx4 > cx3:Finger1 = "Thumb:Thumbs up" #ถ้าcx4>cx3ให้แสดงว่านิ้วโป้งชูอยู่
                else:Finger1 = "Thumb:Fold" #ถ้าไม่ให้แสดงว่าหุบอยู่
                if cy6 > cy8:Finger2 = "Index Finger:Thumbs up" #ถ้าcy6>cy8ให้แสดงว่านิ้วชี้ชูอยู่
                else:Finger2 = "Index Finger:Fold" #ถ้าไม่ให้แสดงว่าหุบอยู่
                if cy10 > cy12:Finger3 = "Middle Finger:Thumbs up" #ถ้าcy10>cy12ให้แสดงว่านิ้วกลางชูอยู่
                else:Finger3 = "Middle Finger:Fold" #ถ้าไม่ให้แสดงว่าหุบอยู่
                if cy14 > cy16:Finger4 = "Ring Finger:Thumbs up" #ถ้าcy14>cy16ให้แสดงว่านิ้วนางชูอยู่
                else:Finger4 = "Ring Finger:Fold" #ถ้าไม่ให้แสดงว่าหุบอยู่
                if cy18 > cy20:Finger5 = "Little Finger:Thumbs up" #ถ้าcy18>cy20ให้แสดงว่านิ้วก้อยชูอยู่
                else:Finger5 = "Little Finger:Fold" #ถ้าไม่ให้แสดงว่าหุบอยู่
                
            #เหมือนมือขวาแต่เป็นข้างซ้าย
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
                
            #วาดเส้นtrackมือ           
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    #show text บนจอแสดงผล        
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
    cv2.imshow("Image", img) #showจอแสดงผล
    
    #ถ้ากดปุ่ม e ให้ปิดจอ
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
```