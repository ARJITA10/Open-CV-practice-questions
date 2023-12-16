#ques-2) Implement the gaussian filter(3*3, standard deviation 1.3) and remove the noise of noise.png.

import cv2 as cv


img = cv.imread(r"C:\Users\ARJITA\Downloads\noise.png")
cv.imshow('noise image of lizard', img)

#implementing gaussian filter
gauss = cv.GaussianBlur(img, (3,3), 1.3)
cv.imshow('clear image of lizard', gauss)
median = cv.medianBlur(img, 3)
cv.imshow('clear image of lizard1', median)





cv.waitKey(0)
cv.destroyAllWindows

