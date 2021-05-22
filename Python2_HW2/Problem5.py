'''
Open the image pic2.jpg and display it with the name pic2. Translate the image to go down by 200 pixels and to the right by 50 pixels. Then rotate the image around its center by 50 degrees. Then flip the resulting image both vertically and horizontally. Display the result after each action in a separate window.
'''

import cv2 as cv
import numpy as np

#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('pic2.jpg')


#show it
cv.imshow('Bird', img) 



#translation


def translate(img, x, y): #image, # of pixels you want to shift in x and y axes
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix
    dimentions = (img.shape[1], img.shape[0]) #(width, height)
    
    return cv.warpAffine(img, transMat, dimentions)

#-x --> left
#-y --> up
#x --> right
#y --> down


translated = translate(img, 50, 200) #left and down by 100 pixels
    
cv.imshow('Translated', translated)



#Rotating the result

def rotate(img, angle, rotPoint = None): #assume that None - rotating around the center
    
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 - scale
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)


rotated = rotate(translated, 50)

cv.imshow('Translated then rotated', rotated)


#flipping the result

flip = cv.flip(img, -1) #

cv.imshow('Translated then rotated then flipped', flip) #what we initially expected




cv.waitKey(0) 






