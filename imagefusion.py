from cv2  import cv2
 
img1=cv2.imread("C:\\InoImageFusion\\ino_multipledeposit\\INO_MulitpleDeposit\\RGB\\1932.jpg")  #读取图片1
img2=cv2.imread("C:\\InoImageFusion\\ino_multipledeposit\\INO_MulitpleDeposit\\T\\1932.jpg")   #读取图片2
 
cv2.imshow("RGB",img1)
cv2.imshow("T",img2)

def weightedAverage(img1, img2, weights):
    #  进行加权融合处理，图片1占比weights，图片2占比1-weights
    return cv2.addWeighted(img1, weights, img2, 1 - weights, 0)


image_75percents = weightedAverage(img1, img2, 0.75)
cv2.imshow("image_75%", image_75percents)
cv2.waitKey(0)
cv2.destroyAllWindows()

