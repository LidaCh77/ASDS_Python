'''
Open the image pic3.jpg and display it with the name pic3. Find the edges of the image using Canny edge detector and then try to find its contours with parameters of your choice. Then convert the original image to grayscale and try to find the contours on a blurred version of the grayscale of the original image. Display the 2 results in separate windows to compare.
'''

import cv2 as cv
import numpy as np


#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic3.jpg')


#show it
cv.imshow('Girl', img) 



#trying contours with canny

canny = cv.Canny(img, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
blank = np.zeros(img.shape, dtype = 'uint8')


cv.drawContours(blank, contours, -1, (0, 0, 255), 1) #image to draw over, contours list, contour index (-1 - all contours), color, thickness

cv.imshow('contours drawn (canny)', blank)





#trying on the blur

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

contours1, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(len(contours1))
blank1 = np.zeros(img.shape, dtype = 'uint8')


#drawing contours on the blank image

cv.drawContours(blank, contours1, -1, (0, 0, 255), 1) #image to draw over, contours list, contour index (-1 - all contours), color, thickness

cv.imshow('contours drawn (blur)', blank1)
print(len(contours1))












cv.waitKey(0)













