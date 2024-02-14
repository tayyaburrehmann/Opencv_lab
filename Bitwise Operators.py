import cv2 as cv
import numpy as np

#Bitwise Operations in OpenCV
#And, OR, NOT, and XOR

blank = np.zeros((400, 400), dtype = 'uint8')

restangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow("Rectangle", restangle)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow("Circle", circle)

#Bitwise And
band = cv.bitwise_and(restangle, circle)
cv.imshow("And", band)

#Bitwise Or
bor = cv.bitwise_or(restangle, circle)
cv.imshow('OR', bor)

#Bitwise XOR --> Non intersecting
bxor = cv.bitwise_xor(restangle, circle)
cv.imshow('xor', bxor)

#Bitwise not
bnot = cv.bitwise_not(restangle, circle)
cv.imshow("NOT", bnot)

cv.waitKey()

