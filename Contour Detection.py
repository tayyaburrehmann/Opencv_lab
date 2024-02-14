import cv2 as cv
import numpy as np
import pandas as pd


img = cv.imread('photos/hills.jpg')
cv.imshow("REAL IMAGE", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)


#Boundries of Object.....used in recognitions etc

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow ("Gray", gray )

# opetional..
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) #bluring image for contoure, her, etc
# cv.imshow("Blured", blur) #... and it will reduce the no. of contours
#
# canny = cv.Canny(blur, 125, 125)
# cv.imshow ('Canny', canny )

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print (f'{len(contours)} contour(s) found!' )


cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Red Contour", blank)











cv.waitKey(0)
