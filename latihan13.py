# vilda azizah wiguna
# 1217070085
# Operasi Penskalaan Citra (Image Zooming)

import cv2

image = cv2.imread('kucing.jpeg')
#faktor skala
zoom_factor = 1.5 #penambahan untuk zoom in 

#mendapatkan dimensi gambar 
height, width = image.shape[:2]

#hitung dimensi gambar 
new_height = int(height * zoom_factor)
new_width = int(width * zoom_factor)

#resize gambar 
scaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow('original image', image)
cv2.imshow('image zooming', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()