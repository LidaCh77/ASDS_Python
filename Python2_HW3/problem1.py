import cv2 as cv
import numpy as np

picture1 = cv.imread('pic1.jpg') 
cv.imshow('picture1', picture1)


rgb = cv.cvtColor(picture1, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

lab = cv.cvtColor(picture1, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 


gray = cv.cvtColor(picture1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


hsv = cv.cvtColor(picture1, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)






cv.waitKey(0)