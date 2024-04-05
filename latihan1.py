# vilda azizah wiguna
# 1217070085
# Split RGB channel & Merge different channel

import cv2 
import numpy as np 
image = cv2.imread("kucing.jpeg")
b,g,r = cv2.split(image)
#buat matriks seukuran dengan citra 
matriks0 = np.zeros(image.shape[:2], image.dtype)
m = matriks0
#merge matrks dengan matriks citra channel merah 
merah = cv2.merge([m,m,r])
cv2.imshow('Citra red channel', merah)
cv2.waitKey(0)