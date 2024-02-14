import cv2 as cv
import numpy as np

img = cv.imread('photos/hills.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#split and merge etc
b, g, r = cv.split (img)

blue = cv.merge([b, blank, blank])
grn = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', grn)
cv.imshow('Red', red)
# cv.imshow('Blue', b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)

print (img.shape)
print(b.shape)
print (g.shape)
print (r.shape)



cv.waitKey()
