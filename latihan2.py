# vilda azizah wiguna
# 1217070085
# Operasi Negative

import cv2
import numpy as np

image = cv2.imread('kucing.jpeg')

#maksimum pixel 
max_pixel_value = 255
#rumus citra negative 244 - f(x,y)
inverted_image = max_pixel_value - image 

cv2.imshow('original image', image)
cv2.imshow('citra negative', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()