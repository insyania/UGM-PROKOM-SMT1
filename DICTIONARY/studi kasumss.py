print(36*'=')
print('SELAMAT DATANG DI KASIR'.center(36, ' '))
print(36*'=')
print('Kode''   |   ''Nama Barang''   |   ''Harga'.center(36, ' '))
print(36*'=')

stuffs = {
    1 :  {'nama' : 'Bayam', 'harga' : 5000},
    2 :  {'nama' : 'Tomat', 'harga' : 4500},
    3 :  {'nama' : 'Kubis', 'harga' : 6000}
}

def menentukan_kode (kode):
    return kode in stuffs

for kode_barang, info in stuffs.items() :
    print(f'{kode_barang}       |   {info['nama']}         |   Rp{info['harga']}'.center(36," "))
print(36 *'=')

total_harga = 0
subtotal = 0
diskon = 0
struk = []

jumlah_barang = int(input('Berapa jenis barang yang ingin dibeli?'))
for i in range (jumlah_barang) :
    while True:
        kode = int(input('Masukkan kode barang: '))
        if kode in stuffs :
            break
        else :
            print('Kode barang tidak valid, silakan masukkan ulang')
    
    sayur = int(input(f'Berapa banyak {stuffs[kode]['nama']} yang ingin dibeli? '))
    subtotal =  stuffs[kode]['harga'] * sayur
    total_harga+= subtotal
    struk.append((stuffs[kode]['nama'], sayur, subtotal))


print('STRUK BELANJA'.center(36, '=')) 
for i, items in enumerate (struk, 1):
    print(f'Barang {i} : {items[0]} * {items[1]} = Rp {items[2]}')
print(36 *'=')  
 
print('Total harga : Rp ', total_harga)
if total_harga > 100000 :
    diskon = total_harga * 0.2
elif total_harga >=50000 :
    diskon = total_harga * 0.15
elif total_harga >=20000 :
    diskon = total_harga * 0.1
else :
    diskon = total_harga * 0

print('Diskon      : Rp ', diskon )
total_bayar = total_harga - diskon
print('Total yang harus dibayar: ', total_bayar)
print()
print('Terimakasih telah berbelanja!')

