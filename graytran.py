import cv2
import os


input_path = "C:/DICM/vis/"
output_path = "C:/DICM/vis_gray/"


def tranImage(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_list = os.listdir(input_path)

    for file in file_list:
        tem = cv2.imread(input_path+file, cv2.IMREAD_GRAYSCALE)
        # image = cv2.flip(image, 0)
        cv2.imwrite(output_path + 'gray' + file, tem)
        print("get " + 'gray' + file + " success")


tranImage(input_path, output_path)
