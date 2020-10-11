import cv2
import numpy as np
import time
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
time.sleep(3)
for i in range(50):
    check,background=video.read()
background=np.flip(background,axis=1)

while True:
    check,img=video.read()
    if check==False:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_r=np.array([0,120,50])
    upper_r=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_r,upper_r)
    lower_r=np.array([170,120,70])
    upper_r=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_r,upper_r)
    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    result1= cv2.bitwise_and(img,img,mask=mask2)
    result2=cv2.bitwise_and(background,background,mask=mask1)

    final=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("final",final)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()


