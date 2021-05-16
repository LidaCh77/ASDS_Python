'''
Draw an orange rectangle with thickness 2 on the image pic2.jpg. Use appropriate measures for the rectangle so that the whole rectangle is visible. Display the original image and the changed one in separate windows.
'''


import numpy as np
import cv2 as cv



img = cv.imread('Python2_HW1/pic2.jpg')
cv.imshow('Dog', img)



#3. Drawing a red circle

drawn = cv.rectangle(img, (40,40), (img.shape[1]//2, img.shape[0]//2), (0, 165, 255), thickness = 2)
cv.imshow('Rectangle',drawn)




cv.waitKey(20)





