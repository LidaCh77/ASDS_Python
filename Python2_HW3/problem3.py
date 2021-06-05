import cv2 as cv
import numpy as np

picture2 = cv.imread('pic2.jpg') 

cv.imshow('picture2', picture2)


mean = cv.blur(picture2, (5,5)) 

cv.imshow('mean', mean)


bilateral1 = cv.bilateralFilter(picture2,15, 100, 50) # in this case we must use large values in order to see difference
cv.imshow('bilateral', bilateral1)


cv.waitKey(0)






















