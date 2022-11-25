import cv2 as cv
import numpy as np

empty = np.zeros((600, 600, 3), dtype='uint8')
cv.imshow('Empty', empty)

'''
    In OpenCV the color channels aren't set in order of RGB (Red, Green, Blue)
    But They are reversed so the are BGR (Blue, Green, Red)
'''

# Paint the image or part of it with a certain color
empty[200:300, 300:400] = 150, 200, 150
cv.imshow('colored', empty)

# Draw a Rectangle
cv.rectangle(empty, (0, 0), (empty.shape[1] // 2, empty.shape[0] // 2), (0, 255, 255), thickness=-1)
cv.imshow('Rectangle', empty)

# Draw a line
cv.line(empty, (0, 0), (empty.shape[1] // 2, empty.shape[0] // 2), (255, 255, 255), 3)
cv.imshow('Line', empty)

# Draw a circle
cv.circle(empty, (500, 500), 50, (255, 0, 255), thickness=2)
cv.imshow('circle', empty)

# Write a text
cv.putText(empty, 'Hi, this is a text!!!', (100, 400), cv.FONT_HERSHEY_DUPLEX, 1.0, (65, 14, 255), thickness=2)
cv.imshow('text', empty)

cv.waitKey(0)
cv.destroyAllWindows()
