import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsreader = cvzone.FPS()

listimg = os.listdir("BGImages")
print(listimg)
imgList = []
for imgPath in listimg:
    img = cv2.imread(f'BGImages/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0
thresImg = 0.75
BGC = imgList[indexImg]
blue = 0
green = 0
red = 0
#bgColor = (blue,green,red)

while True:
    success, img = cap.read()
    #cv2.putText(img, indexImg, (5,5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    imgOut = segmentor.removeBG(img, BGC, threshold=thresImg)

    imgStacked = cvzone.stackImages([imgOut],1,2)
    _, img = fpsreader.update(imgStacked, color= (0,255,0))

    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('f'):
        thresImg = 0.75
        print("defaultsq")
    elif key == ord('s'):
        if thresImg > 0:
            thresImg -=0.05
            print(thresImg)
    elif key == ord('w'):
        if thresImg < 1:
            thresImg +=0.05
            print(thresImg)
    elif key == ord('v'):
        BGC = imgList[indexImg]
        print("BG-Picture")
    elif key == ord('c'):
        BGC = (blue,green,red)
        print("BG-Color")
    elif key == ord('z'):
        thresImg =1
        print("invisible")
    elif key == ord('x'):
        thresImg =0.049999999999999906-0.05
        print("no BG")
    elif key == ord('a'):
        if indexImg>0:
            indexImg -=1
            BGC = imgList[indexImg]
            print(indexImg)
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg +=1
            BGC = imgList[indexImg]
            print(indexImg)
    elif key == ord('j'):
        if blue > 0:
            blue -=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('u'):
        if blue < 255:
            blue +=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('k'):
        if green > 0:
            green -=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('i'):
        if green < 255:
            green +=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('l'):
        if red > 0:
            red -=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('o'):
        if red < 255:
            red +=1
            BGC = (blue, green, red)
            print((blue,green,red))
    elif key == ord('e'):
        print("--------------------")
        print("Threshold: ",thresImg)
        print("Index",indexImg)
        print("Blue",blue)
        print("Green",green)
        print("Red",red)
        print("--------------------")
    elif key == ord('q'):
        break