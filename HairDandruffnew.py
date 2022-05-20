import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
#src = cv2.imread("D:\\DigitalHairRemoval-master\\inputImages\\sample1.jpg")
src = cv2.imread(file_path)
print( src.shape )

cv2.imshow("original sample" , src )

filename_w_ext = os.path.basename(file_path)
#filename = os.path.splitext((filename_w_ext)[0])
print(filename_w_ext)
img = cv2.imread(file_path,0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,15,
        param1=35,param2=12,minRadius=0,maxRadius=5)
p=0
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    p=p+1

## findcontours
cnts = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


## filter by area
s1= 3
s2 = 20

xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)
if p<10:
 print("Normal")
else:print("hair dandruff")
#print("\nDots number: {}".format(len(circles)))
print("\nthreshed value: {}".format(p))



cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


