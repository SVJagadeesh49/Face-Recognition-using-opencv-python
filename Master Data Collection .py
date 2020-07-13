import cv2
import numpy as np
import sqlite3
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    if faces is ():
        return None
    for (x, y, w, h) in faces:
        cropped_face=img[y:y+h, x:x+w]

    return cropped_face


def insertOrupdate(id,Name):
    conn=sqlite3.connect("Face database.db")
    cmd="select * from People where ID="+str(id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" Where ID="+str(id)
    else:
        cmd="INSERT INTO People(ID,Name) Values ("+str(id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
id =input('enter user id')
name=input('enter user name')
insertOrupdate(id,name)
video_capture = cv2.VideoCapture(0)
sampleNum=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if face_extractor(frame) is not None:
        sampleNum = sampleNum + 1
        face = cv2.resize(face_extractor(frame),(400,400))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", face)
        cv2.putText(face,str(sampleNum),(60,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow("Face Cropper",face)
    else:
        print("Face Not Found")
        pass
    if(cv2.waitKey(1)==13 or sampleNum>100):
        break


video_capture.release()
cv2.destroyAllWindows()