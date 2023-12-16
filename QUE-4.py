#Question-4)- Binarization the image image.png (threshold = 124)

import cv2 as cv

img = cv.imread(r"C:\Users\ARJITA\Downloads\image.png")
cv.imshow('original image of lizard', img)

#graying the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image of lizard', gray)
#BINARIZING THE IMAGE

threshold, thresh = cv.threshold(img, 124, 255, cv.THRESH_BINARY)
threshold, thresh1 = cv.threshold(gray, 124, 255, cv.THRESH_BINARY)
cv.imshow('lizard image after binarizing directly from original', thresh)

cv.imshow('lizard image after binarizing from gray image', thresh1)

cv.waitKey(0)
