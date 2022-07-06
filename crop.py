# IMAGE CROPPING

import cv2

# Read an input image
img = cv2.imread('baboon.jpg')
# Check the type of read image
print(type(img))

# Get the image dimension
h, w, c = img.shape
print(img.shape)
print('Image height and width =', h,'x', w)
print('Number of color channel =', c,'color channels')

# Crop image with [rows, columns]
crop = img[50:180, 100:300]

#Display the image
cv2.imshow('Original image', img)
cv2.imshow('Cropped image', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
