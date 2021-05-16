'''
Rescale the image pic1.jpg by 0.5 and display the original image and the rescaled one in separate windows.
'''



import cv2 as cv

def rescale(frame, scale):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #will talk more about this later

img = cv.imread('Python2_HW1/pic1.jpg')

img_rescaled = rescale(img, scale = 0.5)

cv.imshow('Dog', img)
cv.imshow('Dog_rescaled', img_rescaled)


cv.waitKey(20)



    






