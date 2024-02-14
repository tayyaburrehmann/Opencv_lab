import cv2 as cv
import numpy as np

#Essentials Functions in Open CV (Built In)


#convert into grayscale

img = cv.imread('photos/hills.jpg')
#cv.imshow("Photo", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Greyscale', gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)
#edge cascade (edge detection)
canny = cv.Canny(blur, 124, 175 )
#cv.imshow('canny', canny)

#Dialated
dial = cv.dilate(canny, (3,3), iterations = 3)
cv.imshow('Dialated' , dial)

#eroading
erod = cv.erode(dial, (3,3), iterations= 1)
cv.imshow('Eroding', dial )

#resizing of image
resize = cv.resize(img, (400, 300))
cv.imshow('Re', resize)

#cropping

cropped = img[50:200, 255:355]
cv.imshow('Cropped', cropped)


cv.waitKey(0)


