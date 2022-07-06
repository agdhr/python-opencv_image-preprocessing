# cv2 is used for OpenCV library
import cv2
import numpy as np

# IMPORT AN IMAGE
image = cv2.imread('apple.png')

# Convert the RGB image to CMYK
img = image.astype(np.float64)/255
K = 1 - np.max(img, axis=2)
C = (1-img[...,2] - K)/(1-K)
M = (1-img[...,1] - K)/(1-K)
Y = (1-img[...,0] - K)/(1-K)
cmyk_image = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

# Convert the BGR image to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the BGR image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert the BGR image to HLS
hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# Convert the BGR image to YCrCb
yCrCb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Convert the BGR image to YCrCb
Lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# Convert the BGR image to YCrCb
Luv_image = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)

cv2.imshow('BGR', rgb_image)
cv2.imshow('CMYK', cmyk_image)
cv2.imshow('HSV', hsv_image)
cv2.imshow('HLS', hls_image)
cv2.imshow('YCrCb', yCrCb_image)
cv2.imshow('CIELab', Lab_image)
cv2.imshow('CIELuv', Luv_image)
cv2.waitKey(0)

# Print a specific color information
b, g, r = image[128,130]
print("B =", b)
print("G =", g)
print("R =", r)
print("B =", image[128, 130, 0])
print("G =", image[128, 130, 1])
print("R =", image[128, 130, 2])

c,m,y,k = cmyk_image[128, 130]
print("C =", c)
print("M =", m)
print("Y =", y)
print("K =", k)

h, s, v = hsv_image[128, 130]
print("H =", h)
print("S =", s)
print("V =", v)

h, l, s1 = hls_image[128, 130]
print("H =", h)
print("L =", l)
print("S =", s1)

Y, Cr, Cb = yCrCb_image[128, 130]
print("Y =", Y)
print("Cr =", Cr)
print("Cb =", Cb)

L, a, b = Lab_image[128, 130]
print("L =", L)
print("a =", a)
print("b =", b)

CIEL, CIEu, CIEv = Luv_image[128, 130]
print("L =", CIEL)
print("u =", CIEu)
print("v =", CIEv)