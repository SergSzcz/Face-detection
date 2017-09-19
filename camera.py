import cv2, pandas
from datetime import datetime


vc = cv2.VideoCapture(0)
first_frame = None # cv2.imread("background.png",0)
status_list = [None,None]
times = []
df = pandas.DataFrame(columns=["Start","End"])

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

a=0
while rval:
    a=a+1
    if a < 100:
        rval, frame = vc.read()
        continue

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    status = 0

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame,30,225,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=5)

    (_,cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 7000:
            continue
        status = 1

        (x,y,w,h)= cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2]  == 0:
        times.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2]  == 1:
        times.append(datetime.now())

    cv2.imshow("camera", gray)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("thresh", thresh_delta)
    cv2.imshow("frame",frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        if status == 1:
            times.append(datetime.now())
        break

print (status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
vc.release()
cv2.destroyAllWindows
