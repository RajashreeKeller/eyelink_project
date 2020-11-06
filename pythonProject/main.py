# this is mock code for eyelink which shows deletes same file from images,images2 folder after the first randomisation is complete
#import os
#import random
#import time

#folder=r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\images"
#folder1=r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\images2"

#first randomisation
#a=random.choice(os.listdir(folder))
#print(a)

#os.open(a, os.O_RDWR)
#from PIL import Image
#file = folder+'\\'+a
#file3 = folder1+'\\' +a
#Image.open(file).show()

import cv2
import os
import random
import time

#folder1 = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\B1A\1.mp4"
#folder2 = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\B1A\2.mp4"

a=random.choice(os.listdir(cap))
print(a)


cap = cv2.VideoCapture(r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\B1A\1.mp4")
cap1 = cv2.VideoCapture(r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\B1A\2.mp4")

file = cap+'\\'+a
file3 = cap1+'\\' +a

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()

#timer
time.sleep(5)
# file comparison
if (file == file) and (file3 != file):
    os.remove(file)
    os.remove(file3)

b=random.choice(os.listdir(folder1))
print(b)

#os.open(a, os.O_RDWR)

file1 = folder1+'\\'+b
Image.open(file1).show()


