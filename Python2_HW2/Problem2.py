'''
Open the image pic1.jpg and display it with the name pic1. Blur the image using Gaussian blur using 2 different windows sizes: (3, 3) and (11, 11) and display both versions in separate windows to compare with the original image.
'''
import cv2 as cv


#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic1.jpg')


#show it
cv.imshow('Lamb', img) 



#blurring

blur1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) # blur
cv.imshow('Blur1', blur1)


blur2 = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT) #more blur
cv.imshow('Blur2', blur2)


#a keyboard binding function, waits for a specific delay for a key to be pressed

cv.waitKey(0) #waits for an infinite amount of time for a keyboard key to be pressed



