#write the mockup code for timespace eyelink project

# 1.select 3 folders randomly out of 16 folders
# 2.16 folders, each folder has 16 video files i.e.a total of 256 video files
# 3.when the first folder performs randomization same type of files should be deleted in the remaining folders
# 4.repeat step 3, until all the folders performs randomisation
# 5.transfer the respective files to respective folders such as encoding 1, encoding 2, encoding 3 and test
# 6.perform randomisation among these three files
# 7.delete all files from all folders as a step for resetting
# 8.reset the files in all folders( factors to be considered is no duplicate files ),
   # this is equivalent to the copy of all files from dummy folders


# this step performs playing of video file from a folder
import random
import os
import cv2
import time
import shutil

#dummy variable to avoid duplication for 16 folders : this is assigned later
B1A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B1A"
B1H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B1H"
B2A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B2A"
B2H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B2H"
B3A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B3A"
B3H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B3H"
B4A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B4A"
B4H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\B4H"
G1A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G1A"
G1H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G1H"
G2A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G2A"
G2H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G2H"
G3A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G3A"
G3H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G3H"
G4A = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G4A"
G4H = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\G4H"

folder = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial"
print(folder)
encoding_lista = random.choice(os.listdir(folder))
encoding_listb = random.choice(os.listdir(folder))
encoding_listc = random.choice(os.listdir(folder))
print(encoding_lista)
print(encoding_listb)
print(encoding_listc)
#perform concatenation here
encoding_list1 = folder + '\\' + encoding_lista
encoding_list2 = folder + '\\' + encoding_listb
encoding_list3 = folder + '\\' + encoding_listc

print(encoding_list1)
print(encoding_list2)
print(encoding_list3)

encoding_list1_CA = random.choice(os.listdir(encoding_list1))
print(encoding_list1_CA)

encoding_list1_final = encoding_list1 + '\\' + encoding_list1_CA
print(encoding_list1_final)

cap = cv2.VideoCapture(encoding_list1_final)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
#timer
time.sleep(5)
# copy the files from one folder to another folder before deleting the duplicating files, equivalent to saving of files
if encoding_list1_CA == encoding_list1_CA:
    source = encoding_list1_final
    destination= r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\encoding_list1"
    new_path = shutil.copy(source,destination)
    print(new_path)

# avoid duplication : this step is where same type of files can not be repeated or played again
RM_B1A = B1A + '\\' + encoding_list1_CA
RM_B1H = B1H + '\\' + encoding_list1_CA
RM_B2A = B2A + '\\' + encoding_list1_CA
RM_B2H = B2H + '\\' + encoding_list1_CA
RM_B3A = B3A + '\\' + encoding_list1_CA
RM_B3H = B3H + '\\' + encoding_list1_CA
RM_B4A = B4A + '\\' + encoding_list1_CA
RM_B4H = B4H + '\\' + encoding_list1_CA
RM_G1A = G1A + '\\' + encoding_list1_CA
RM_G1H = G1H + '\\' + encoding_list1_CA
RM_G2A = G2A + '\\' + encoding_list1_CA
RM_G2H = G2H + '\\' + encoding_list1_CA
RM_G3A = G3A + '\\' + encoding_list1_CA
RM_G3H = G3H + '\\' + encoding_list1_CA
RM_G4A = G4A + '\\' + encoding_list1_CA
RM_G4H = G4H + '\\' + encoding_list1_CA

os.remove(RM_B1A)
os.remove(RM_B1H)
os.remove(RM_B2A)
os.remove(RM_B2H)
os.remove(RM_B3A)
os.remove(RM_B3H)
os.remove(RM_B4A)
os.remove(RM_B4H)
os.remove(RM_G1A)
os.remove(RM_G1H)
os.remove(RM_G2A)
os.remove(RM_G2H)
os.remove(RM_G3A)
os.remove(RM_G3H)
os.remove(RM_G4A)
os.remove(RM_G4H)

#opens the file for second randomisation i.e. encoding_list2
encoding_list2_CB = random.choice(os.listdir(encoding_list2))
print(encoding_list2_CB)
encoding_list2_final = encoding_list2 + '\\' + encoding_list2_CB
print(encoding_list2_final)
cap1 = cv2.VideoCapture(encoding_list2_final)
while(cap1.isOpened()):
    ret1, frame1 = cap1.read()

    if ret1==True:
        cv2.imshow('frame', frame1)

        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
cap1.release()
cv2.destroyAllWindows()

if encoding_list2_CB == encoding_list2_CB:
    source = encoding_list2_final
    destination= r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\Trial\encoding_list2"
    new_path = shutil.copy(source,destination)
    print(new_path)

# avoid duplication : this step is where same type of files can not be repeated or played again
RM1_B1A = B1A + '\\' + encoding_list2_CB
RM1_B1H = B1H + '\\' + encoding_list2_CB
RM1_B2A = B2A + '\\' + encoding_list2_CB
RM1_B2H = B2H + '\\' + encoding_list2_CB
RM1_B3A = B3A + '\\' + encoding_list2_CB
RM1_B3H = B3H + '\\' + encoding_list2_CB
RM1_B4A = B4A + '\\' + encoding_list2_CB
RM1_B4H = B4H + '\\' + encoding_list2_CB
RM1_G1A = G1A + '\\' + encoding_list2_CB
RM1_G1H = G1H + '\\' + encoding_list2_CB
RM1_G2A = G2A + '\\' + encoding_list2_CB
RM1_G2H = G2H + '\\' + encoding_list2_CB
RM1_G3A = G3A + '\\' + encoding_list2_CB
RM1_G3H = G3H + '\\' + encoding_list2_CB
RM1_G4A = G4A + '\\' + encoding_list2_CB
RM1_G4H = G4H + '\\' + encoding_list2_CB

os.remove(RM1_B1A)
os.remove(RM1_B1H)
os.remove(RM1_B2A)
os.remove(RM1_B2H)
os.remove(RM1_B3A)
os.remove(RM1_B3H)
os.remove(RM1_B4A)
os.remove(RM1_B4H)
os.remove(RM1_G1A)
os.remove(RM1_G1H)
os.remove(RM1_G2A)
os.remove(RM1_G2H)
os.remove(RM1_G3A)
os.remove(RM1_G3H)
os.remove(RM1_G4A)
os.remove(RM1_G4H)
