# Resizing images and video feed.

import cv2 as cv


img = cv.imread('../images/car.jpg')
print(img.shape)
img_resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)  # (X , Y)f
print(img_resized.shape)
cv.imshow('image', img)
cv.imshow('resized image', img_resized)
cv.waitKey(0)
cv.destroyAllWindows()