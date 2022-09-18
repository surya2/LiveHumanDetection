import cv2
import uuid
import os
import time

labels = ['face']
num_imgs = 20

imgs_Path = os.path.join('"Live Human Detection"', 'Workspace', 'Images', 'camImages')
path = '.\Workspace\Images\camImages'
print(path)

person = input("Name of person: ")

for label in labels:
    cap = cv2.VideoCapture(0)
    print("Capture for {}".format(label))
    label_path = path+"\\"+label
    print(label_path)
    if not os.path.exists(label_path):
        os.mkdir(label_path)
    time.sleep(5)
    for num in range(num_imgs):
        print("Collecting {}".format(num))
        ret, frame = cap.read()
        #name = os.path.join(imgs_Path,label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        file_name = label_path+"\\"+label+'_'+person+str(num)+'.jpg'
        print(file_name)
        cv2.imwrite(file_name,frame)
        cv2.imshow("Frame", frame)

        if cv2.waitKey() & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()



