
import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
from PIL import Image
path='dataSet'
onlyfiles =[f for f in listdir(path) if isfile(join(path,f))]

Training_Data,Labels =[],[]

for i,files in enumerate(onlyfiles):
     image_path=path+onlyfiles[i]
     images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

     Facenp=np.array(images,'uint8')
     Training_Data.append(Facenp)

     Labels.append(i)

Labels = np.array(Labels,dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data),np.asarray(Labels))

print("Model Training Complete")

cv2.destroyAllWindows()