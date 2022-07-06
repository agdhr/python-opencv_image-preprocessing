import cv2

# Load an image
image = cv2.imread('infectedleaf2.jpg')
# Get the image dimension
h,w,c = image.shape
print(h,"px", w, "px")

# CASE 1 – Resize and Preserve Aspect Ratio
# Downscale the image using new  width and height
down_width = 300
down_height = 200
down_dimension = (down_width, down_height)
resized_down = cv2.resize(image, down_dimension, interpolation= cv2.INTER_LINEAR)

# Upscale the image using new width and height with percent of image size
scale_percent = 200
up_width = int(image.shape[1] * scale_percent / 100)
up_height = int(image.shape[0] * scale_percent / 100)
up_dimension = (up_width, up_height)
resized_up = cv2.resize(image, up_dimension, interpolation= cv2.INTER_AREA)

# CASE 2 - Resize and Do not Preserve Aspect Ratio
# Resize only width
a_width = 700
a_height = image.shape[0]
dim_width = (a_width, a_height)
# Resize only height
b_width = image.shape[1]
b_height = 500
dim_height = (b_width, b_height)
resized_width = cv2.resize(image,dim_width, interpolation = cv2.INTER_NEAREST)
resized_height = cv2.resize(image,dim_height, interpolation = cv2.INTER_NEAREST)

#Display the image
cv2.imshow('Original image', image)
cv2.imshow('Down resized image', resized_down)
cv2.imshow('Up resized image', resized_up)
cv2.imshow('Resized image only width', resized_width)
cv2.imshow('Resized image only height', resized_height)
cv2.waitKey(0)
cv2.destroyAllWindows()