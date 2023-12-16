#IMPLEMENT THE SOBEL FILTER(3*3) ON IMAGE.PNG

import cv2 as cv

img = cv.imread(r"C:\Users\ARJITA\Downloads\image.png")
cv.imshow('original image of lizard', img)

#APPLYING SOBEL EFFECT
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 0)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)

cv.imshow('combined sobel effect image of lizard', combined_sobel)


cv.waitKey(0)

