# vilda azizah wiguna
# 1217070085
# Operasi Geometri

#operasi translasi
import cv2 
import numpy as np 
image = cv2.imread('kucing.jpeg')
height, width = image.shape[:2]
#membuat matriks M dengan contoh Tx = 100 & Ty = 50
M = np.float32([[1,0,100],[0,1,50]])
image_translation = cv2.warpAffine(image, M, (height, width))

cv2.imshow('citra', image)
cv2.imshow('citra hasil translation', image_translation)
cv2.waitKey(0)