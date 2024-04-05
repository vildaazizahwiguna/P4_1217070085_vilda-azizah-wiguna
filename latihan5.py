# vilda azizah wiguna
# 1217070085
# Operasi Penjumlahan secara manual 

import cv2

# membaca dua gambar 
gambar1 = cv2.imread('kucing.jpeg')
gambar2 = cv2.imread('test_image.jpg')

# pastikan kedua gambar memiliki dimensi yang sama
tinggi, lebar, _ = gambar1.shape
gambar2 = cv2.resize(gambar2, (lebar, tinggi))

# membuat gambar hasil penjumlahan 
hasil_penjumlahan = gambar1.copy()

# melakukan penjumlahan manual untuk setiap piksel
for y in range(tinggi):
    for x in range(lebar):
        for c in range(3): #loop untuk masing-masing channel (BGR)
            nilai_baru = gambar1[y, x, c] + gambar2[y, x, c]
            hasil_penjumlahan[y, x, c] = min(nilai_baru, 255) #batasi nilai maksimal menjadi 255

# menampilkan dan menyimpan gambar hasil penjumlahan 
cv2.imshow('hasil penjumlahan', hasil_penjumlahan)
cv2.waitKey(0)
cv2.destroyAllWindows()

# opsional : menyimpan hasil penjumlahan
cv2.imwrite('hasil_penjumlahan_manual_rumus.jpg', hasil_penjumlahan)