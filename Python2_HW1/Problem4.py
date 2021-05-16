'''
Rescale the video vid1.jpg by 0.5 and display the original video and the rescaled one in separate windows.

'''


import cv2 as cv

def rescale(frame, scale):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 


capture = cv.VideoCapture('Python2_HW1/vid1.mp4')


while True:
    isTrue, frame = capture.read()
    
    
    if isTrue: 
        frame_rescaled = rescale(frame, scale = 0.5)
        cv.imshow('Video', frame)
        cv.imshow('Video_rescaled', frame_rescaled)
    else:
        print('empty frame')
        exit(1)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
    
cv.waitKey(0)