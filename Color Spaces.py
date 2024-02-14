import cv2 as cv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Color Spaces

img = cv.imread('photos/hills.jpg')
cv.imshow('Original Image', img)

# plt.imshow(img)
# plt.show()

#RGB to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#bgr to lab formate
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)



cv.waitKey()
