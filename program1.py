print ('"""""""""""""""""""""""""""""""""""""""""""""""""""')
print ('"========== PROGRAM 1 =========="')
print ('"Nama	: Agustina Susanti"')
print ('"NIM	: 311810736"')
print ('"Kelas	: TI.18.A.1"')
print ('""""""""""""""""""""""""""""""""""""""""""""""""""')
print ("")
print ('note:')
print ('bulan pertama dan kedua = 0%')
print ('pada bulan ke 3 = 1%')
print ('pada bulan ke 5 = 5%')
print ('pada bulan ke 8 = 2%')
print ("")

a = 100000000
for x in range(1,9):
	if(x>=1 and x<=2):
		b=a*0
		print("Laba Bulan Ke-",x," :",b)
	if(x>=3 and x<=4):
		c=a*0.1
		print("Laba Bulan Ke-",x," :",c)
	if(x>=5 and x<=7):
		d=a*0.5
		print("Laba Bulan Ke-",x," :",d)
	if(x==8):
		e=a*0.2
		print("Laba Bulan Ke-",x," :",e)
total = b+b+c+c+d+d+d+e
print("\nTotal : ", total)