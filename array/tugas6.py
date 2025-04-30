data = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
print(data) 

jumlah_genap =  0
jumlah_ganjil = 0
genap = []
ganjil = []

for c in data:
    if c % 2 == 0:
        genap.append(c)
    if c % 2 == 0:
        jumlah_genap += 1
    if c % 2 == 1:
        ganjil.append(c)
    if c % 2 == 1:
        jumlah_ganjil += 1
        

print('Anggota bilangan genap adalah: ', list(genap))
print('Jumlah bilangan genap adalah: ', jumlah_genap, 'angka')
print('Anggota bilangan ganjil adalah: ', list(ganjil))
print('Jumlah bilangan ganjil adalah: ', jumlah_ganjil, 'angka')


