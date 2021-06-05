import cv2 as cv
import numpy as np

picture2 = cv.imread('pic2.jpg') 
cv.imshow('picture2', picture2)

blank = np.zeros(picture2.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (picture2.shape[1]//2, picture2.shape[0]//2), 50, 255, -1)

mask_pic = cv.bitwise_and(picture2,picture2, mask=mask)

cv.imshow('result', mask_pic)

 
cv.waitKey(0)