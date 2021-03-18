import cv2
import numpy as np
import os


def saveImage(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


def getImage(path, name, output_path, freq):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    videoCapture = cv2.VideoCapture(os.path.join(path,name))
    rate = videoCapture.get(7)
    times = 0 
    while True:
        res, image = videoCapture.read()
        if res:
            image = image[50:550]
            # image = cv2.flip(image, 0)
            if not res:
                print("image not found")
                break
            if times % freq == 0:
                cv2.imwrite(output_path + "\\ir" + name[:-4] +'_' + str(times) + '.jpg', image)
                print("get " + output_path + "\\ir" + name[:-4] +'_' + str(times) + '.jpg' + " success")
        times += 50
        if times > rate:
            break
    videoCapture.release()
    return 0


path = "C:\\data\\data_ship\\data_ship\\avi"
file_list = os.listdir(path)
output_path = "C:\\data\\data_ship\\ir"
for name in file_list:
    getImage(path, name, output_path, 50)
