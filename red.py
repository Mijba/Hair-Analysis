import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

img= cv2.imread(file_path)
image = cv2.imread(file_path)
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([155,25,0])
upper = np.array([179,255,255])
mask = cv2.inRange(image, lower, upper)
print(mask)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('result', result)
#cv2.imshow('result', image)

cv2.waitKey()
"""
img1=cv2.imread(file_path,1)

#img1=cv2.imread('bald_o.jpg',1)

hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

#lower red
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])


#upper red
lower_red2 = np.array([170,50,50])
upper_red2 = np.array([180,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img1,img1, mask= mask)


mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
res2 = cv2.bitwise_and(img1,img1, mask= mask2)

img3 = res+res2
img4 = cv2.add(res,res2)
img5 = cv2.addWeighted(res,0.5,res2,0.5,0)


kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(res,-1,kernel)
smoothed2 = cv2.filter2D(img3,-1,kernel)




cv2.rectangle
cv2.imshow('Original',img1)
#cv2.imshow('Averaging',smoothed)
#cv2.imshow('mask',mask)
#cv2.imshow('res',res)
#cv2.imshow('mask2',mask2)
#cv2.imshow('res2',res2)
cv2.imshow('res3',img3)
cv2.imshow('res4',img4)
#cv2.imshow('res5',img5)
#cv2.imshow('smooth2',smoothed2)




cv2.waitKey(0)
cv2.destroyAllWindows()"""


