
import Hand_Tracking as htm
import cv2
import time
import math
import socket

# Re-maps a number from one range to another.
#That is, a value of fromLow would get mapped to toLow, a value of fromHigh to toHigh,
#values in-between to values in-between, etc.
def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min




host = '192.168.xx.xx' #replace this with your servers' host ip
port = 8888             #replace this with your servers' host port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    width, height = 640, 480

    cap = cv2.VideoCapture(1)  ## 640 x 480 resolution
    cap.set(3, width)
    cap.set(4, height)
    pTime = 0  # previous time
    cTime = 0  # current time
    detector = htm.handDetectors(maxHands=1, detectionCon=0.8)
    pwm = 0
    while 1:
        ret, img = cap.read()
        img = cv2.flip(img, 1)

        # s.send(str.encode(str(pwm)))

        img = detector.findHands(img, draw=False)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            # print(lmList[4])
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
            image = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            length = math.hypot(x2 - x1, y2 - y1)
            # print(length)
            if length < 25:
                cv2.circle(img, (cx, cy), 5, (0, 0, 0), cv2.FILLED)
            else:
                pwm = int(remap(length, 25, 210, 0, 255))
            print(pwm)
            cv2.putText(img, f'{int(pwm)}', (cx, cy-20), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 0), 2)
            s.sendall(str.encode(str(pwm) + ' '))
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 2)
        cv2.imshow('frame', img)

        if cv2.waitKey(10) == ord(' '):
            break

    cv2.destroyAllWindows()
    cap.release()
s.close()
