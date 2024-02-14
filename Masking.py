import cv2 as cv
import numpy as np

#Masking Techniques in OpenCV
img = cv.imread('photos/hills.jpg')
cv.imshow("Original Image", img)

blank = np.zeros(img.shape[0:2], dtype= 'uint8')
cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Masking", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked Image", masked)

cv.waitKey(0)
