import cv2
import numpy as np

'''cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''

import cv2
import time

#print("Before URL")
url = 'http://admin:admin@123@192.168.1.34/1'
cap = cv2.VideoCapture(0)
print(cap)
#print("After URL")

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
body_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_upperbody.xml')

breakSteps = 0
while (True):
    # print("Collecting images for {}".format(label))
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    #time.sleep(5)
    breakSteps += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()