'''
In this lesson we will learn how to:
Read images
Read videos
Get Camera Feed
'''

import cv2 as cv  # Importing openCV

# Reading image
# img = cv.imread('../images/car.jpg')
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#######################################

# Reading videos
# capture = cv.VideoCapture('../videos/video_1.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#
#     if isTrue:
#         cv.imshow('Video', frame)
#         if cv.waitKey(20) & 0xFF == ord('x'):
#             break
#     else:
#         break
#
# capture.release()
# cv.destroyAllWindows()

#######################################

# Capturing Camera feed

vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()

    cv.imshow('Camera', frame)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

vid.release()
cv.destroyAllWindows()



