from cv2 import cv2
import numpy as np
import os


def getbody(img_path, thresh, width):
    img = cv2.imread(img_path)
    img1 = img[50:550,0:800]
    ret, thresh4 = cv2.threshold(img1, thresh, 255, cv2.THRESH_TOZERO)  # 高于阈值时像素设置为255，低于阈值时不作处理 看起来可以
    if not ret:
        print('error!')
        print(img_path)
    tem = []
    for i in range(thresh4.shape[1]):
        tem.append(sum(thresh4[:, i].flatten()))
    tem = tem[150:651]
    a = tem.index(max(tem))
    return thresh4[:, int(a + 150 - width/2):int(a + 150 + width/2)]


def main():
    path = 'C:\\DICM\\aa\\'
    save_path = 'C:\\DICM\\result\\'
    os.chdir(path)
    file_list = os.listdir(path)
    for i in range( len(file_list)):
        img_tem = getbody(path + file_list[i], 90, 300)
        cv2.imwrite(save_path + file_list[i][:-4] + "bmp", img_tem)


if __name__ == '__main__':
    main()


# for i in range(thresh4.shape[0]):
#     for j in range(thresh4.shape[1]):
#         if thresh4[thresh4.shape[0] - i][j] != 0:
#             print(i, j)

# for i in range(thresh4.shape[0]):
#     for j in range(thresh4.shape[1]):
#         if thresh4[i][thresh4.shape[0] - j] != 0:
#             print(i, j)

# for i in range(thresh4.shape[0]):
#     for j in range(thresh4.shape[1]):
#         if thresh4[thresh4.shape[0] - i][thresh4.shape[0] - j] != 0:
#             print(i, j)

# # ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # binary （黑白二值）
# # ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # （黑白二值反转）
# # ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 得到的图像为多像素值
# ret, thresh4 = cv2.threshold(img, 90, 255, cv2.THRESH_TOZERO)  # 高于阈值时像素设置为255，低于阈值时不作处理 看起来可以
# # ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 低于阈值时设置为255，高于阈值时不作处理
 
# print(ret)
 
# # cv2.imshow('thresh1', thresh1)
# # cv2.imshow('thresh2', thresh2)
# # cv2.imshow('thresh3', thresh3)
# cv2.imshow('thresh4', thresh4)
# # cv2.imshow('thresh5', thresh5)
# cv2.imshow('grey-map', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

