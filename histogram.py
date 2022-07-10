# HISTOGRAM
# https://medium.com/@rndayala/image-histograms-in-opencv-40ee5969a3b7

# Histogram is a very important tool in image processing. It is a graphical representation of the distribution of data.
# An image histogram gives a graphical representation of the distribution of pixel intensities in a digital image.
# ---
# Calculatinv histogram
# cv2.calcHist(image, channels, mask, bins, ranges)
# images = the image we want to calculate the histogram of wrapped as a list
# channels = is the the index of the channels to consider wrapped as a list.
#   ([0] for gray-scale images as there's only one channel and [0],
#   [1] or [2] for color images if we want to consider the channel green, blue or red respectively),
# mask = is a mask to be applied on the image if we want to consider only a specific region (we're gonna ignore this in this post),
# bins = is a list containing the number of bins to use for each channel.
# ranges = is the range of the possible pixel values which is [0,256] in case of RGB color space (where 256 is not inclusive).

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('baboon.png')

# GRAY-SCALE HISTOGRAM
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist1 = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist1, color = 'k')    # k = black
plt.show()

# COLOR HISTOGRAM
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

# HISTOGRAM EQUALIZATION
# HE process is an image processing method to adjust the contrast of an image by modifying the image's histogram.
# HE stretches the peak across the whole range of values leading to an improvement in the global contrast of an image.

channels = cv2.split(img)
eq_channels = []
for ch, color in zip (channels, ['B', 'G', 'R']):
    eq_channels.append(cv2.equalizeHist(ch))

eq_img = cv2.merge(eq_channels)

cv2.namedWindow("Original image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Equalized image", cv2.WINDOW_AUTOSIZE)

cv2.imshow("Original image", img)
cv2.imshow("Equalized image", eq_img)

cv2.waitKey()
cv2.destroyAllWindows()

# Plot histogram for equalized image
# Show histogram
channels = ('b', 'g', 'r')

# We now separate the colors and plot each in the histogram
for i, color in enumerate (channels):
    hist2 = cv2.calcHist([eq_img], [i], None, [256], [0, 256])
    plt.plot(hist2, color = color)
    plt.xlim([0, 256])
plt.show()
