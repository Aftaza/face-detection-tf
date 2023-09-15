import cv2
import time
import handTrackingModule as htm

widthCam, heightCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, widthCam)
cap.set(4, heightCam)
# cap = cv2.resize(cap, (widthCam, heightCam))
pTime = 0
detector = htm.handDetector(detectionCon=0.6)

def getState(finger):
    state = {
        "11111" : "follow",
        "11000" : "flip"
    }

while True:
    succes, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    tipId=[4,8,12,16,20]
    if(len(lmList)!=0):
        fingers=[]
        #thumb
        if(lmList[tipId[0]][1]>lmList[tipId[0]-1][1]):
                fingers.append(1)
        else :
                fingers.append(0)
        #4 fingers
        for id in range(1,len(tipId)):
            
            if(lmList[tipId[id]][2]<lmList[tipId[id]-2][2]):
                fingers.append(1)
            
            else :
                fingers.append(0)
        # print(fingers)
        a=""
        for i in fingers:
            a+=str(i)
        print(a)
           
        # cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)   
        # cv2.putText(img,str(getState(a)),(45,375),cv2.FONT_HERSHEY_PLAIN,
        #                              10,(255,0,0),20)  
        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),3)
    cv2.imshow("image",img)
    
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break

cap.release()
cv2.destroyAllWindows()