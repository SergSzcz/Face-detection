import cv2

vc = cv2.VideoCapture(0)
first_frame = None

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

    cv2.imwrite("background.png",gray)
    break
# import cv2, time
#
# video = cv2.VideoCapture(0)
#
#
# if video.isOpened(): # try to get the first frame
#     check, frame = video.read()
# else:
#     check = False







# print(check)
# print(frame)
#
# time.sleep(3)
# cv2.imshow("capturing",frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# video.release()
