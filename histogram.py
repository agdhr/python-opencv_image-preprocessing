# Buat Histogram

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('baboon.png')
color = ('b', 'r', 'g')
for i, clr in enumerate(color):
    histbgr = cv2.calcHist([img],[i], None, [256], [0, 256])
    plt.plot(histbgr, color=clr)
    plt.xlim([0,256])
plt.show()

# OR TO PLOT SEPARATELY
# histB = cv2.calcHist([img],[0], None, [256], [0, 256])
# histG = cv2.calcHist([img],[1], None, [256], [0, 256])
# histR = cv2.calcHist([img],[2], None, [256], [0, 256])
# plt.plot(histB)
# plt.plot(histG)
# plt.plot(histR)
# plt.show()

# Histogram in BAR PLOT
x = plt.hist(img[:,:,0].ravel(), 256, [0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
