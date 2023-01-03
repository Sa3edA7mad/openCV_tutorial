import cv2 as cv
import numpy as np

img = cv.imread('../images/car.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found ')

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank,contours,10,(255,0,0),1)
cv.imshow('contours drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()