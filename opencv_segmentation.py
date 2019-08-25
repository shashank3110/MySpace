
import cv2
import numpy as np
import cv2
from matplotlib import pyplot as plt


#Approach1 watershed + thresh+contours 
img = cv2.imread('img.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #bright bckg images
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#black bckg images
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imwrite("sure_fg.png",sure_fg)
cv2.imwrite("unkown.png",unknown)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_cont=cv2.drawContours(img,contours,-1,255,1)
cv2.imwrite("img_contour_pre_water.png",img_cont)     
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
#cv2.imwrite("img_water.png",img_water)
cv2.imwrite("img_water.png",img)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imwrite("img_contour.png",contours)                                         
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_cont=cv2.drawContours(img,contours,-1,255,1)
cv2.imwrite("img_contour.png",img_cont)  #post watershed                                       

cv2.imwrite("thres.png",thresh)
print(contours)
print("#####################")
print(contours[0])
print(len(contours[0]))
#x,y,w,h = cv2.boundingRect(contours[0])
#print(x,y,w,h)
# x1 = x+w/4
# y1 = y+h/4
# x2 = x1 + w/2
# y2 = y1 + h/2
#print(type(x1),type(y1),type(x2),type(y2))
img_rect = cv2.rectangle(img_cont,(128,96),(512,388),(0,255,0),2)
#img_rect = cv2.rectangle(img_cont,(x,y),(x + w,y + h),(0,255,0),2)

#img_rect = cv2.rectangle(img_cont,(x1,y1),(x2,y2),(0,255,0),2)
################################################## Approach2 find rgb contour,crop rectangle, threshold
cv2.imwrite("img_rect_thresh_cont.png",img_rect)
#img_cont=cv2.drawContours(thresh,contours,-1,255)
img_crop = img_rect[96:388,128:512]
cv2.imwrite("img_rect_crop.png",img_crop)
gray = cv2.cvtColor(img_crop,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #bright bckg images
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #black bckg images
cv2.imwrite("img_contour_thres_crop.png",thresh_crop)
############################ Approach3 using background subtraction
img_cont=cv2.drawContours(thresh,contours,-1,255,1)
cv2.imwrite("img_contour_thres.png",img_cont)

# img_convex = cv2.convexHull(contours[0])
# cv2.imwrite("img_cnvx_hull.png",img_convex)
contours, hierarchy = cv2.findContours(unknown, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_cont=cv2.drawContours(unknown,contours,-1,255,1)                           
cv2.imwrite("img_contour_thres_unk.png",img_cont)

