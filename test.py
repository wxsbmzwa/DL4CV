import cv2
import os
import numpy as np

file_path = 'c:/data/20210119bench'
file_name = os.listdir(file_path)

for name in file_name:
    tem = cv2.imread(os.path.join(file_path, name))
    name = name[:-4]+'.bmp'
    tem = np.array(tem)
    cv2.imwrite(os.path.join(file_path, name), tem)
