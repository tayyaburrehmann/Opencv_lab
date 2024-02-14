import cv2 as cv
import numpy as np

img = cv.imread('photos/hills.jpg')
cv.imshow('Óriginal Image', img)

#Averaging
avg = cv.blur(img, (3,3))
cv.imshow('Avg', avg)

#Gaussian
gau = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian", gau)

#median blur
medb = cv.medianBlur(img, 3)
cv.imshow('Median Blur', medb)


cv.waitKey()
