# vilda azizah wiguna
# 1217070085
# Operasi Penjumlahan & Pengurangan 

import cv2
import numpy as np 

image = cv2.imread("kucing.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2], image.dtype)*100

#operasi penjumlahan
citraPenjumlahan = cv2.add(gray, MatriksSatu)
cv2.imshow('citra', gray)
cv2.imshow('citra penjumlahan', citraPenjumlahan)
cv2.waitKey(0)

#operasi penambahan dapat meningkatkan dari sebuah citra dan operasi dan operasi pengurangan dapat menurunkan kecerahan sebuah citra