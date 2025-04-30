masukkan_jumlah = (int(input('Masukkan jumlah elemen dalam array: ')))
data = list(range(1, masukkan_jumlah + 1))
print('Data array: ', data)
kelipatan = (int(input('Masukkan sebuah bilangan bulat untuk mencari kelipatan: ')))
kelipatan_data = [bil for bil in data if bil % kelipatan ==0]
print('Elemen yang merupakan kelipatan dari', kelipatan, ':')

if kelipatan in data:
    print(kelipatan_data)

else:
    print('Tidak ada hasil yang cocok dengan data')




