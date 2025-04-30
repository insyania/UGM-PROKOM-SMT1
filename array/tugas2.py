nilai=[]

for i in range (1,6):
    angka = (float(input(f"Masukkan angka ke-{i}: ")))
    nilai.append(angka)
    print(nilai)

operasi = (input('Operasi apa yang ingin dilakukan? '))
jumlah = (sum(nilai))
rata_rata = (jumlah/len(nilai))

if operasi == 'jumlah':
    print('Hasil dari penjumlahan nilai adalah: ', jumlah)

elif operasi == 'rata-rata':
    print('Rata-rata dari nilai adalah: ', rata_rata)

else:
    print('Hanya bisa memilih jumlah atau rata-rata!')
