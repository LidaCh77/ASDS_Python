"""
Open the video vid1.mp4 and display it frame by frame in a window named vid1.
"""


import cv2 as cv





capture = cv.VideoCapture('Python2_HW1/vid1.mp4')

#using a loop to read the video frame by frame

while True:
    isTrue, frame = capture.read() #returns the frames and a boolean indicating if it was successfully read
    
    if isTrue:
        cv.imshow('vid1', frame)
    else:
        print('empty frame')
        exit()
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() #distroying all windows since we don't need them anymore
    
cv.waitKey(0)