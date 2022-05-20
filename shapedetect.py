import cv2
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
#src = cv2.imread("D:\\DigitalHairRemoval-master\\inputImages\\sample1.jpg")
src = cv2.imread(file_path)
print( src.shape )
cv2.imshow("original sample" , src )

filename_w_ext = cv2.os.path.basename(file_path)
#filename = os.path.splitext((filename_w_ext)[0])
print(filename_w_ext)



#im = cv2.imread('E:\\DigitalHairRemoval-master\\Images\\c-type.jpg')
imgray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
im_gauss = cv2.GaussianBlur(imgray, (5, 5), 0)
ret, thresh = cv2.threshold(im_gauss, 127, 255, 0)
# get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_area = []
# calculate area and filter into new array
for con in contours:
    area = cv2.contourArea(con)
    if 1000 < area < 10000:
        contours_area.append(con)

cv2.imshow('detected Shape',thresh)
cv2.imwrite('D:\\DigitalHairRemoval-master\\\outputImages\\hairtype\\detected shape'+filename_w_ext, thresh, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.waitKey(0)
cv2.destroyAllWindows()
