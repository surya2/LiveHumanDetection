# Test script for video capture from DVR box
import cv2
import cvui
import numpy as np

rtsp_username = 'username'
rtsp_pass = 'password'
pi_ipAddress = '---'  #Raspberry Pi's ip address e.g. 192.168.11.118:554
camera_no = 0 #What camera number/channel do we want to look at e.g. front cam, back cam, etc.

width = 800
height = 400

'''Human detection cascades: '''
face_cascade = cv2.CascadeClassifier('cascades/data/harrcascade_frontalface_alt2.xml')
body_cascade = cv2.CascadeClassifier('cascades/data/harrcascade_upperbody.xml')

def create_virtual_cam(channel):
    rtsp = "rtsp://"+rtsp_username+":"+rtsp_pass+"@"+pi_ipAddress+"Streaming/channels/"+channel+"02"   #Creating rtsp protocol link
    capture = cv2.VideoCapture()
    capture.open(rtsp)
    capture.set(3, 640)   #Set width (id of 3) to 640 pixels
    capture.set(4, 480)   #Set height (id of 4) to 480 pixels
    capture.set(10, 100)  #Set brightness (++id of 10) to 100
    return capture

#camera = create_virtual_cam(str(camera_no))
cvui.init("Screen Display")

camera = cv2.VideoCapture(0)

while True:
    success, current_cam = camera.read()   #current_cam indicates which camera we are reading from
    gray = cv2.cvtColor(current_cam, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    dim = (width, height)
    frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA);  #Interpolating missing pixels when adjusting to computer screen
    cv2.namedWindow("Camera "+camera_no, cv2.WINDOW_NORMAL);
    cv2.setWindowProperty("Camera "+camera_no, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    for (x,y,w,h) in faces:
        print(x, y, w, h)
    '''
    if (cvui.button(frame, width - 100, height - 40, "Next") and cvui.mouse(cvui.CLICK)):  #Geting another camera's footage using next and prev arrows
        print("Next Button Pressed")
        cvui.init('screen')
        cam_no = cam_no + 1
        if (cam_no > 4):
            cam_no = 1
        del cam
        cam = create_virtual_cam(str(cam_no))
    if (cvui.button(frame, width - 200, height - 40, "Previous") and cvui.mouse(cvui.CLICK)):
        print("Previous Button Pressed")
        cvui.init('screen')
        cam_no = cam_no - 1
        if (cam_no < 1):
            cam_no = 4
        del cam
        cam = create_virtual_cam(str(cam_no))
    '''

    cv2.imshow('Camera Footage', current_cam)     #Showing continuous footage (while True loop)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #Exit upon 'q' key click
        break
camera.release()
cv2.destroyAllWindows()