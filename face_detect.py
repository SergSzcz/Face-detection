import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("news.jpg")
gr_im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gr_im,
scaleFactor=1.01,
minNeighbors=5)

for x, y, w, h in face:
    image = cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),3)

print(type(face))
print(face)

cv2.imshow("twarz",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
