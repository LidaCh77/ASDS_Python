'''
Open the image pic2.jpg and display it with the name pic2. Try to detect the image edges using Canny edge detector and display the result in a separate window. Then run the edge detector on a blurred version of an image (use a window size of your choice) and display the result in a different window to compare.

'''


import cv2 as cv

#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic2.jpg')


#show it
cv.imshow('Bird', img) 

canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)
#we can reduce the number of edges by using bluring
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges_blured', canny)


cv.waitKey(0) 



