'''
Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and display in a separate window to compare with the original image.
'''


import cv2 as cv


#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic1.jpg')

#displaying the image as a new window, passing the window name and the matrix of pixels to display

cv.imshow('Lamb', img) 
#turn to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

#a keyboard binding function, waits for a specific delay for a key to be pressed

cv.waitKey(0) #waits for an infinite amount of time for a keyboard key to be pressed




