#computing histogram
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('photos/hills.jpg')
cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of Pixels")
plt.plot(gray_hist)
plt.xlim(0, 256)
plt.show()


cv.waitKey(0)
