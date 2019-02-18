print ('""""""""""""""""""""""""""""""""""""""""""""')
print ('"PROGRAM UNTUK MENENTUKAN BILANGAN TERBESAR DAN BERHENTI DI ANGKA 0"')
print ('"Nama	: Agustina Susanti"')
print ('"NIM	: 311810736"')
print ('"Kelas	: TI.18.A.1"')
print ('""""""""""""""""""""""""""""""""""""""""""""')

print("\nMenentukan Bilangan Terbesar")
print("\n")

max=0
while True:
	a=int(input("Masukan Bilangan :"))
	if max < a:
		max = a
	if a==0:
		break
print("Bilangan Terbesar = ", max)