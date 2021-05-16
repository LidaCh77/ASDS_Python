"""
Open images pic1.jpg, pic2.jpg and pic3.jpg and display in separate windows
with the names pic1, pic2 and pic3 correspondingly.
"""
import cv2 as cv


pic1 = cv.imread('Python2_HW1/pic1.jpg')
pic2 = cv.imread('Python2_HW1/pic2.jpg')
pic3 = cv.imread('Python2_HW1/pic3.jpg')
cv.imshow('pic1', pic1)
cv.imshow('pic2', pic2)
cv.imshow('pic3', pic3)



cv.waitKey(10)

