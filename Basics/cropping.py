# Cropping images


import cv2 as cv


img = cv.imread('../images/car.jpg')
print(img.shape)
img_cropped = img[100:500, 300:1000]
cv.imshow('image', img)
cv.imshow('image cropped', img_cropped)
cv.waitKey(0)
cv.destroyAllWindows()