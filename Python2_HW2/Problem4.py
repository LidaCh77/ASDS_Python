'''
Open the image pic2.jpg and display it with the name pic2. Resize the image to have 2 times bigger width and the same height as the original image, use INTER_AREA interpolation. Then resize the original image to have 2 times smaller height and the same width as the original image, use INTER_CUBIC interpolation. Display both versions in separate windows.
'''

import cv2 as cv

#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic2.jpg')


#show it
cv.imshow('Bird', img) 

resize_wider = cv.resize(img, (2*img.shape[1], img.shape[0]), interpolation = cv.INTER_AREA) 
cv.imshow('Resize wider', resize_wider)


resize_higher = cv.resize(img, (img.shape[1], img.shape[0]//2), interpolation = cv.INTER_CUBIC) 
cv.imshow('Resize shorter', resize_higher)

cv.waitKey(0) 






