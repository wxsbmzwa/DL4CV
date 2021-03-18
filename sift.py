# import cv2

# import matplotlib.pyplot as plt

# # matplotlib inline

# # reading image

# img1 = cv2.imread('C:\\data\\test.jpg')

# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# # keypoints

# sift = cv2.xfeatures2d.SIFT_create()

# keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)

# img_1 = cv2.drawKeypoints(gray1, keypoints_1, img1)

# cv2.imwrite('C:\\data\\1.jpg', img_1)
# cv2.imshow(img_1)
# cv2.waitKey()
# cv2.destroyAllWindows()


from PIL import Image
from pylab import *
import sys
from PCV.localdescriptors import sift


if len(sys.argv) >= 3:
    im1f, im2f = sys.argv[1], sys.argv[2]
else:
    im1f = 'C:\\data\\1.jpg'
    im2f = '../pic/12.jpg'
#  im1f = '../data/crans_1_small.jpg'
#  im2f = '../data/crans_2_small.jpg'
#  im1f = '../data/climbing_1_small.jpg'
#  im2f = '../data/climbing_2_small.jpg'
im1 = array(Image.open(im1f))
im2 = array(Image.open(im2f))


sift.process_image(im1f, 'out_sift_1.txt')
l1, d1 = sift.read_features_from_file('out_sift_1.txt')
figure()
gray()
subplot(121)
suptitle("SIFT feature points")
sift.plot_features(im1, l1, circle=False)

sift.process_image(im2f, 'out_sift_2.txt')
l2, d2 = sift.read_features_from_file('out_sift_2.txt')
subplot(122)
sift.plot_features(im2, l2, circle=False)

matches = sift.match(d1, d2)
matches = sift.match_twosided(d1, d2)
print '{} matches'.format(len(matches.nonzero()[0]))

figure()
gray()
sift.plot_matches(im1, im2, l1, l2, matches, show_below=True)
suptitle("SIFT matching")
show()
