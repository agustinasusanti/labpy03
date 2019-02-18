print ('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print ('"PROGRAM UNTUK MENENTUKAN BILANGAN ACAK YANG LEBIH KECIL DARI 0,5"')
print ('"Nama	: Agustina Susanti"')
print ('"NIM	: 311810736"')
print ('"Kelas	: TI.18.A1"')
print ('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

import random
jumlah = int(input("Masukkan Jumlah N:"))

for i in range(jumlah):
	i=random.uniform(0.0,0.5)
	print("Data ke: =>",i)

print("Selesai")