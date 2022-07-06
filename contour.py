# Steps for Detecting and Drawing Contours in OpenCV
# https://learnopencv.com/contour-detection-using-opencv-python-c/
import cv2
import numpy as np
# Step 1 - Read the image and convert it to Grayscale format
image = cv2.imread('daun.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2 - Apply Binary Thresholding
# now use the threshold() function to apply a binary threshold to the image.
# any pixel with a value greater than 150 will be set to a value of 255.
# all remaining pixels in the resulting image will be set to 0 (BLACK).
# the thresehold value of 150 is a TUNABLE parameter, so you can experiment with it.
ret, biner = cv2.threshold(gray, 35, 255, cv2.THRESH_BINARY)
# untuk membentuk semua citra berwarna yang ada 3 kanal menjadi 0 (warna hitam)
# pada citra inilah kontur hendak digambar dan memungkinkan kontur untuk diwarnai
numRow = biner.shape[0]   # memperoleh jumlah baris berwarna hitam
numCol = biner.shape[1]   # memperoleh jumlah baris berwarna putih
citraKontur = np.zeros((numRow, numCol, 3), np.uint8)

# Step 3 - Find and Draw the Contours

# Contour in binary
contour1, hierarchy1 = cv2.findContours(biner, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(citraKontur, contour1, -1, (255, 255, 255), 1)
# -1 menyatakan bahwa semua kontur diberi warna sama
# (255, 255, 255) menyatakan warna dari kontur - putih
# 1 menyatakan ketebalan kontur sebesar 1 pixel
# ---
# apabila ingin menjukkan warna yang berbeda
# warna = [(255, 255, 255), (230, 216, 187), (255, 255, 0), (255, 0, 255),(0, 255, 255)]
# for index in range (len(kontur)):
#   cv2.drawContours(citraKontur, kontur, index, warna[index %5], 1)
# index %5 untuk memastikan index pada warna selalu dalam jangkauan 0 hingga 4
# ---
citraRGB = cv2.merge((biner, biner, biner))
# Script di atas digunakan untuk membentuk citra berwarna dari citra berskala abu-abu atau biner)
# Hal ini dilakukan agar dapat digabungkan dengan citraKontur yang merupakan citra berwarna
hasil = np.hstack((citraRGB, citraKontur))
cv2.imshow('Hasil', hasil)
cv2.waitKey()

# Kontur dengan Warna
contour2, hierarchy2 = cv2.findContours(image = biner, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_NONE)
img = image.copy()
cv2.drawContours(image = img, contours = contour2, contourIdx = -1, color=(0,255,00), thickness = 1, lineType = cv2.LINE_AA)
cv2.imshow('N', img)
cv2.waitKey()
