# vilda azizah wiguna
# 1217070085
# Operasi Geometri

#operasi flipping citra
import cv2
import numpy as np 
image = cv2.imread('kucing.jpeg')
#flipping horizontal
flip_hor = cv2.flip(image,1)
#flipping vertical
flip_ver = cv2.flip(image,0)
#flipping vertical - horizontal
flip_verhor = cv2.flip(image, -1)

cv2.imshow('citra', image)
cv2.imshow('citra flip horizontal', flip_hor)
cv2.imshow('citra flip vertical', flip_ver)
cv2.imshow('citra vertical - horizontal', flip_verhor)
cv2.waitKey(0)