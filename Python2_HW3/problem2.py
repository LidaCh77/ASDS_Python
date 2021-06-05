import cv2 as cv
import numpy as np

picture1 = cv.imread('pic1.jpg') 

cv.imshow('picture1', pic1) 

blue, green, red = cv.split(pic1)


cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)















cv.waitKey(0)
