import cv2 as cv

img = cv.imread('photos/group 2.jpg') #Change this to try different images
#cv.imshow("Sample", img)d



#convert image to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar = cv.CascadeClassifier("haar.xml")
face_rect = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 2)

print (f'No of faces found =  {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+ h), (0, 255, 0), thickness = 2)
cv.imshow("Detected Face", img)



cv.waitKey(0)
