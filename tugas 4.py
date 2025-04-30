jumlah_data = int(input('Masukkan jumlah data: '))
total_nilai = 0
for i in range (jumlah_data) :
    nilai = float(input(f'Masukkan nilai ke-{i+1}: '))
    total_nilai += nilai
average = total_nilai / jumlah_data
print('Rata-rata adalah: ', average)
    