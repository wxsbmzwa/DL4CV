import cv2
import os


def cutimage(inputpath, outputpath, file_name, h1, h2, w1, w2):
    try:
        img = cv2.imread(inputpath+file_name, cv2.IMREAD_GRAYSCALE)
        img = img[h1:h2, w1:w2]
        cv2.imwrite(outputpath+file_name, img)
    except:
        print(inputpath+file_name+'cut error!')


path1 = 'c:/data/20210106infrared/'
path2 = 'c:/data/20210106infraredcut/'
file_list = os.listdir(path1)
for i in file_list:
    cutimage(path1, path2, i, 50, 570, 15, 721)
