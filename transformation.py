import cv2 as cv
import numpy as np

# Immage Tranfromation etc
img = cv.imread('photos/hills.jpg')
cv.imshow("Read", img)


# Translation
def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)


tran = translate(img, 100, 120)
#cv.imshow('translated', tran)

#Rotation of Image
def rotate (img, angle, rotp = None):
    (height, width) = img.shape[:2]

    if rotp is None:
        rotp = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D( rotp, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rot = rotate (img, 180)
#cv.imshow('Rotation', rot)

#Resizing of the image
res = cv.resize(img, (400, 400), interpolation= cv.INTER_CUBIC)
cv.imshow('Resizing of the Image', res)

#Flipping of the image
flip = cv.flip(img, 0)
cv.imshow('flip V', flip )

#Cropping of the image
crop = img[200:400, 200:400]
cv.imshow("Cropped", crop)


cv.waitKey(0)
