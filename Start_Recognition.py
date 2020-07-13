import os
import cv2
import numpy as np
from PIL import Image
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer\\trainingData.yml')
def face_detector(img, size=0.5):
    global roi
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    if faces is():
        return img,[]
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi=img[y:y+h,x:x+w]
        roi=cv2.resize(roi,(200,200))

    return img,roi

video_capture = cv2.VideoCapture(0)
while True:

     ret,frame=video_capture.read()

     image,face=face_detector(frame)

     try:
         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
         result = rec.predict(face)

         if result[1]<500:
             confidence=int(100*(1-(result[1])/300))
             display_string = str(confidence)+'% Confidence it is user'
             cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255) )
             if(confidence>75):
                  cv2.putText(image,"Unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                  cv2.imshow('Face Cropper',image)
             else:
              cv2.putText(image, "locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),2)
              cv2.imshow('Face Cropper', image)
     except:
           cv2.putText(image,"Face not found",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
           cv2.imshow('Face Cropper',image)
           pass

     if cv2.waitKey(1)==13:
             break


video_capture.release()
cv2.destroyAllWindows()