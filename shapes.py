import cv2 as cv
import numpy as np

#Writing on Images

#Making Blank Image
blank = np.zeros((500, 500,3), dtype = 'uint8')
cv.imshow('blank', blank)


img = cv.imread ('photos/hills.jpg')
cv.imshow('hills', img)
#Color
#blank[200:300, 300:400] = 0, 255, 0
#cv.imshow('green', blank)

#Draw Rectangle
cv.rectangle(blank, (0,0),(250, 250),  (0, 255,0), thickness = cv.FILLED)


#Circle
cv.circle(blank, (255,255),50, (0, 0, 255), thickness = 3  )
cv.imshow('rectangle', blank)

#line
cv.line(blank, (0, 0), (255, 255 ), (255,255,255), thickness = 3)
cv.imshow('line', blank)

#write Test on image
cv.putText(blank, 'hello World', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255, 255))
cv.imshow('text', blank)

cv.waitKey(0)




