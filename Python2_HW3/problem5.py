import cv2 as cv
import numpy as np


blank = np.zeros((400, 400, 3), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (128, 128, 128), -1)
rectangle2 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (127, 0, 255), -1)
circle1 = cv.circle(blank.copy(),  (200, 200), 200, (179, 50, 255), -1)
circle2 = cv.circle(blank.copy(), (200, 200), 200, (255, 153, 255),-1)
bitwise_xor = cv.bitwise_xor(rectangle, circle1)
bitwise_or1 = cv.bitwise_or(rectangle, circle1)
bitwise_xor2 = cv.bitwise_xor(rectangle2, circle2)
cv.imshow('bitwise_xor', bitwise_xor)
cv.imshow('bitwise_or1', bitwise_or1)
cv.imshow('bitwise_or2', bitwise_xor2)



cv.waitKey(0)
