#Question - 1) Read the image and change RGB in order of BGR on image.png

import cv2 as cv

img = cv.imread(r"C:\Users\ARJITA\Downloads\image.png")
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('original image of lizard', img)
cv.imshow('RGB IMAGE OF LIZARD', img_rgb)

cv.waitKey(0)
