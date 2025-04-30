stuffs = {
    1 : {'kode' : '1', 'nama' : 'Bayam', 'harga' : 5000},
    2 :  {'kode' : '2', 'nama' : 'Terong', 'harga' : 4500},
    3 :  {'kode' : '3', 'nama' : 'Kubis', 'harga' : 6000}
}

harga =[]
barang = []
total_harga = []

print(36*'=')
print('SELAMAT DATANG DI KASIR'.center(36, ' '))
print(36*'=')
print('Kode''   |   ''Nama Barang''   |   ''Harga')
print(36*'=')
print("""   1   |   Bayam         |   5000 \n  2    |   Terong        |   4500 \n  3    |   Kubis         |   6000 """ )
print(36*'=')

jumlah_barang = int(input('Berapa jenis barang yang akan dibeli?'))
jumlah_barang-=1
for _ in range (jumlah_barang) :
    while True:
        kode_barang = int(input('Masukkan kode barang: '))
        while jumlah_barang !=0: 
            while kode_barang >3 :
            #belanjaan = int(input('Masukkan kode barang: '))
        #belanjaan-=1
                print('Kode barang tidak valid, silakan masukkan ulang.')
                break
            else :
                if kode_barang ==1 :
                    kode_barang-=1
                    jumlah = int(input('Berapa banyak bayam yang ingin dibeli?'))
                    jumlah*=[harga]
                    break
                elif kode_barang ==2 :
                    #belanjaan-=1
                    jumlah = int(input('Berapa banyak terong yang ingin dibeli?'))
                    break
                elif kode_barang ==3 :
                    #belanjaan-=1
                    jumlah = int(input('Berapa banyak kubis yang ingin dibeli?'))
                    break
        break
        
        
    

    #nama_barang, harga_barang = stuffs [kode]


    

#while True :

#print(36 * '=')
#total_harga =
#print('Total harga: Rp', total_harga)
#diskon = 0
#if total_harga <20000 :
   # print('Tidak ada diskon')
#elif total_harga >20.000 >50.000 :
#print ('Diskon 10%: ', total_harga *= 10%)
##elif total_harga >50000 <100000 :
   # print('Diskon 15%: ', total_harga *= 15%)
##elif total_harga >200000 :
    #print('Diskon 20%', total_harga *= 20%)
#total_dibayar = total_harga - diskon
#print('Total harga yang harus dibayar: Rp',total_dibayar )
#print()
#print('Terimakasih sudah berbelanja!')