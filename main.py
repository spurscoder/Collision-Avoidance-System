import numpy as np
import cv2
from utils import *

def image():
    path = "/home/harish/Documents/Okulo Aerosapce/Collision-Avoidance-System/Dataset/Images/1.png"
    img = cv2.imread(path)
    img = cv2.resize(img, (700, 400))

    left, right = get_Horizon(img)
    border = get_border(left, right, img.shape[0:2])
    C = CMO(img)
    C = cv2.cvtColor(C, cv2.COLOR_BGR2GRAY)
    C = np.where(C <= 50, C, 255)
    C = find_grp(C, border)
    cv2.line(C, left, right, 255, 2)

    # cv2.imwrite('/home/harish/Pictures/Input.png', img)
    # cv2.imwrite('/home/harish/Pictures/CMO.png', im2)

    cv2.imshow("Input", img)
    cv2.imshow("CMO", C)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video():
    path = "/home/harish/Documents/Okulo Aerosapce/Collision-Avoidance-System/Dataset/Videos/Clip_1.mov"
    cap = cv2.VideoCapture(path)
    while True:
        ret, img = cap.read()
        if ret is False:
            break

        img = cv2.resize(img, (700, 400))

        left, right = get_Horizon(img)
        border = get_border(left, right, img.shape[0:2])
        C = CMO(img)
        C = cv2.cvtColor(C, cv2.COLOR_BGR2GRAY).reshape(400, 700, 1)
        C = np.where(C <= 50, C, 255)   
        cv2.line(C, left, right, 255, 2)

        cv2.imshow('Input', img)
        cv2.imshow("CMO", C)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    image()