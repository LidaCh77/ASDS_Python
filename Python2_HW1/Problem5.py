'''
Draw a red filled circle in the middle of the image pic2.jpg. Use an appropriate radius value so that the whole circle is visible. Display the original image and the changed one in separate windows.
'''

import numpy as np
import cv2 as cv



img = cv.imread('pic2.jpg')
cv.imshow('Dog', img)



#3. Drawing a red circle

drawn = cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 100, (0, 0, 255), thickness = -1)
cv.imshow('Circle',drawn)




#cv.rectangle(blank, (20,20), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)



# #6. Filling in the circle
# #cv.circle(img, center, radius, color, thickness)




# """
# cv.circle(blank, (200, 200), 50, (0, 255, 0), thickness = -1)
# cv.imshow('Circle', blank)
# """



cv.waitKey(20)

