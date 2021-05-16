'''
Draw a line starting from the left lower corner and ending in the right upper corner of the image pic1.jpg. Display the original image and the changed one in separate windows.
'''



import numpy as np
import cv2 as cv



img = cv.imread('Python2_HW1/pic1.jpg')
cv.imshow('Dog', img)


#7 Drawing a line
#cv.line(img, point1, point2, color, thickness)


line = cv.line(img, (0,img.shape[0]), (img.shape[1],0), (0, 255, 0), thickness = 3)
cv.imshow('Line', line)



cv.waitKey(20)

