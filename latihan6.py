# vilda azizah wiguna
# 1217070085
# Operasi Boolean

#operasi boolean operator and 
import cv2 
import numpy as np 
#membuat matriks untuk menggambar persegi 
persegi = np.zeros((400,400), dtype="uint8")
#sintaks method rectangle (var,(titik awal),(lebar, tinggi),warna, thickness)
#jika thickness diisi -1 maka objek akan diisi warna pernuh
cv2.rectangle(persegi,(60,60),(340,340),255,-1)
#membuat matriks untuk menggambar lingkaran
lingkaran = np.zeros((400,400),dtype="uint8")
#sintaks method circle (var,(titik pusat),radius (r)/jari-jari, warna, thickness)
cv2.circle(lingkaran,(200,200),150,255,-1)
#penggunaan operator AND
operasiAND = cv2.bitwise_and(persegi,lingkaran)
cv2.imshow("persegi", persegi)
cv2.imshow("lingkaran", lingkaran)
cv2.imshow("operasi AND", operasiAND)
cv2.waitKey(0)