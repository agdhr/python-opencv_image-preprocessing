# ROG - Region of Interest
# https://learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/

import cv2
import numpy as np

if __name__ == '__main__':
    # Read image
    img = cv2.imread('daun.jpg')
    # Select Region of Interest
    # if you want to drag rectangle from top left to bottom right
    showCrosshair = False
    fromCenter = False
    rect = []  # this to specify a vector of rectangles (ROI)
    r = cv2.selectROI(img, fromCenter)
    # ---
    # Versi biasa saja
    # r = cv2.selectROI(img)
    # specify the window name
    # r = cv2.selectROI("Image", im)
    # if you want to drag rectangle from top left to bottom right
    # r = cv2.selectROI(img, fromCenter)
    # if you don’t want to show crosshair
    # r = cv2.selectROI(img, fromCenter, showCrosshair)
    # ---
    # Crop image
    imgCrop = img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
    # Display cropped image
    cv2.imshow("Image", imgCrop)
    cv2.waitKey(0)
    cv2.imwrite('daun-cropped.jpg', imgCrop)
    cv2.waitKey(0)

