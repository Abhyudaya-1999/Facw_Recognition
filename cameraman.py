import cv2
import numpy as np

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("harrcascade_frontalface_alt.xml")

skip=0
face_data=[]
dataset_path = './data/'
file_name=input("Enter the name of the person : ")

while True:
    ret,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2_GRAY)


    if ret==False:
        continue

    faces=faces_cascade.detectMultiScale(gray_frame,1,3,5)
    print(faces)

    cv2.imshow("Video Frame",frame)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    key_pressed=cv2.waitkey(1) & 0xFF

    if key_pressed==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
