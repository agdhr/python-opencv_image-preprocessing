import numpy as np
import cv2
from matplotlib import pyplot as plt

imgbgr = cv2.imread('sea.jpg', 1)
imggray = cv2.imread('sea.jpg', 0)

denoise_gray = cv2.fastNlMeansDenoising(imggray,None,20,7,21)
# (input image, output dimension, strength of the filter, templateWindowSize, searchWindowSize)

denoise_rgb = cv2.fastNlMeansDenoisingColored(imgbgr,None,20,20,7,21)
# (input image, output dimension, strength of the filter, ColorComponents, templateWindowSize, searchWindowSize)

titles = ['Original Image(colored)','Image after removing the noise (colored)', 'Original Image (grayscale)','Image after removing the noise (grayscale)']
images = [imgbgr, denoise_rgb, imggray, denoise_gray]
plt.figure(figsize=(13,5))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()